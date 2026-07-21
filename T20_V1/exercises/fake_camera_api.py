from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import json
import logging
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse


def setup_logger(log_file: str | None = None) -> logging.Logger:
    logger = logging.getLogger("fake_camera_api")
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


LOGGER = setup_logger(log_file=str(Path("/tmp/fake_camera_api.log")))


@dataclass
class CameraState:
    name: str
    host: str
    status: str = "healthy"
    stream: str = "up"
    firmware: str = "1.2.3"
    logs: list[str] = field(default_factory=list)

    def add_log(self, level: str, message: str) -> None:
        timestamp = datetime.now(timezone.utc).isoformat()
        entry = f"{timestamp} {level.upper()} {message}"
        self.logs.append(entry)
        LOGGER.info("camera=%s %s", self.name, entry)


def build_handler(camera_state: CameraState) -> type[BaseHTTPRequestHandler]:
    class FakeCameraHandler(BaseHTTPRequestHandler):
        def _write_json(self, payload: dict, status_code: int = 200) -> None:
            body = json.dumps(payload).encode()
            self.send_response(status_code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _read_json(self) -> dict:
            content_length = int(self.headers.get("Content-Length", "0"))
            if content_length == 0:
                return {}
            raw_body = self.rfile.read(content_length)
            return json.loads(raw_body.decode())

        def log_message(self, format: str, *args: object) -> None:
            LOGGER.info("http %s", format % args)

        def do_GET(self) -> None:
            parsed_url = urlparse(self.path)

            if parsed_url.path == "/health":
                self._write_json(
                    {
                        "status": camera_state.status,
                        "stream": camera_state.stream,
                        "camera": camera_state.name,
                        "firmware": camera_state.firmware,
                    }
                )
                return

            if parsed_url.path == "/camera":
                self._write_json(asdict(camera_state))
                return

            if parsed_url.path == "/logs":
                query = parse_qs(parsed_url.query)
                tail = int(query.get("tail", ["20"])[0])
                self._write_json({"logs": camera_state.logs[-tail:], "count": len(camera_state.logs)})
                return

            self._write_json({"error": "not found"}, status_code=404)

        def do_POST(self) -> None:
            parsed_url = urlparse(self.path)
            payload = self._read_json()

            if parsed_url.path == "/status":
                status_value = payload.get("status")
                stream_value = payload.get("stream")

                if status_value:
                    camera_state.status = str(status_value)
                if stream_value:
                    camera_state.stream = str(stream_value)

                camera_state.add_log("INFO", f"state updated status={camera_state.status} stream={camera_state.stream}")
                self._write_json({"ok": True, "status": camera_state.status, "stream": camera_state.stream})
                return

            if parsed_url.path == "/logs":
                level = str(payload.get("level", "INFO"))
                message = str(payload.get("message", "manual log"))
                camera_state.add_log(level, message)
                self._write_json({"ok": True, "last_log": camera_state.logs[-1]})
                return

            self._write_json({"error": "not found"}, status_code=404)

    return FakeCameraHandler


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a fake camera HTTP API on a Linux VM.")
    parser.add_argument("--bind-host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument("--camera-name", default="logi1000")
    parser.add_argument("--camera-host", default="127.0.0.1")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    camera_state = CameraState(name=args.camera_name, host=args.camera_host)
    camera_state.add_log("INFO", "fake camera API started")
    server = ThreadingHTTPServer((args.bind_host, args.port), build_handler(camera_state))
    LOGGER.info("serving fake camera api on http://%s:%s", args.bind_host, args.port)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        LOGGER.info("shutdown requested")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())