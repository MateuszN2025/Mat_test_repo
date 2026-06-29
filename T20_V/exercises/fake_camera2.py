from __future__ import annotations

import argparse
from dataclasses import dataclass
import importlib
import logging
from pathlib import Path
import sys
from typing import Any


def load_module(module_name: str) -> Any:
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None


requests = load_module("requests")
paramiko = load_module("paramiko")


def setup_logger(log_file: str | None = None) -> logging.Logger:
    logger = logging.getLogger("fake_camera")
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


LOGGER = setup_logger(log_file=str(Path("/tmp/fake_camera.log")))


@dataclass
class CameraConfig:
    name: str
    host: str
    api_base_url: str
    ssh_user: str
    ssh_port: int = 22
    ssh_password: str | None = None
    ssh_key_path: str | None = None
    api_timeout: int = 5
    ssh_timeout: int = 5


def require_dependency(module_ref: Any, module_name: str, install_hint: str) -> Any:
    if module_ref is None:
        raise RuntimeError(f"{module_name} is required. Install it with: {install_hint}")
    return module_ref


class RemoteFakeCamera:
    def __init__(self, config: CameraConfig) -> None:
        self.config = config

    def get_data(self) -> dict[str, str | int]:
        camera_data = {
            "name": self.config.name,
            "host": self.config.host,
            "api_base_url": self.config.api_base_url,
            "ssh_user": self.config.ssh_user,
            "ssh_port": self.config.ssh_port,
        }
        LOGGER.info("camera inventory configured name=%s host=%s", self.config.name, self.config.host)
        return camera_data

    def log_warning(self, message: str) -> None:
        LOGGER.warning("camera=%s host=%s %s", self.config.name, self.config.host, message)

    def log_error(self, message: str) -> None:
        LOGGER.error("camera=%s host=%s %s", self.config.name, self.config.host, message)

    def build_session(self) -> Any:
        requests_module = require_dependency(requests, "requests", "python3 -m pip install requests")
        return requests_module.Session()

    def check_api_health(self, session: Any) -> bool:
        health_url = f"{self.config.api_base_url}/health"
        LOGGER.info("camera=%s api_check start url=%s", self.config.name, health_url)

        try:
            response = session.get(health_url, timeout=self.config.api_timeout)
            payload = response.json()
        except Exception as exc:
            self.log_error(f"api health request failed error={exc}")
            return False

        if response.status_code != 200:
            self.log_error(f"api health returned status_code={response.status_code}")
            return False
        if payload.get("status") != "healthy":
            self.log_warning(f"api health payload is degraded payload={payload}")
            return False

        LOGGER.info("camera=%s api_check ok payload=%s", self.config.name, payload)
        return True

    def fetch_api_logs(self, session: Any, tail: int = 20) -> bool:
        logs_url = f"{self.config.api_base_url}/logs"
        LOGGER.info("camera=%s api_logs start url=%s tail=%s", self.config.name, logs_url, tail)

        try:
            response = session.get(logs_url, params={"tail": tail}, timeout=self.config.api_timeout)
            payload = response.json()
        except Exception as exc:
            self.log_error(f"api logs request failed error={exc}")
            return False

        if response.status_code != 200:
            self.log_error(f"api logs returned status_code={response.status_code}")
            return False

        LOGGER.info("camera=%s api_logs ok payload=%s", self.config.name, payload)
        return True

    def build_ssh_client(self) -> Any:
        paramiko_module = require_dependency(paramiko, "paramiko", "python3 -m pip install paramiko")
        ssh_client = paramiko_module.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko_module.AutoAddPolicy())
        connect_kwargs = {
            "hostname": self.config.host,
            "port": self.config.ssh_port,
            "username": self.config.ssh_user,
            "timeout": self.config.ssh_timeout,
        }

        if self.config.ssh_key_path:
            connect_kwargs["key_filename"] = self.config.ssh_key_path
        if self.config.ssh_password:
            connect_kwargs["password"] = self.config.ssh_password

        ssh_client.connect(**connect_kwargs)
        return ssh_client

    def run_ssh_check(self, ssh_client: Any, command: str, expected_text: str) -> bool:
        LOGGER.info("camera=%s ssh_check start command=%s", self.config.name, command)

        try:
            _, stdout_stream, stderr_stream = ssh_client.exec_command(command)
            output = stdout_stream.read().decode().strip()
            error_output = stderr_stream.read().decode().strip()
        except Exception as exc:
            self.log_error(f"ssh check failed command={command} error={exc}")
            return False

        merged_output = "\n".join(part for part in [output, error_output] if part)

        if expected_text not in merged_output:
            self.log_error(f"ssh check failed command={command} output={merged_output}")
            return False

        LOGGER.info("camera=%s ssh_check ok command=%s output=%s", self.config.name, command, merged_output)
        return True


def parse_args() -> CameraConfig:
    parser = argparse.ArgumentParser(description="Probe a fake camera API and Linux host over HTTP and SSH.")
    parser.add_argument("--name", default="logi1000")
    parser.add_argument("--host", required=True, help="Linux VM or target host reachable over SSH")
    parser.add_argument("--api-base-url", required=True, help="Base URL for the fake camera API, for example http://192.168.1.10:8080")
    parser.add_argument("--ssh-user", required=True)
    parser.add_argument("--ssh-port", type=int, default=22)
    parser.add_argument("--ssh-password")
    parser.add_argument("--ssh-key-path")
    args = parser.parse_args()
    return CameraConfig(
        name=args.name,
        host=args.host,
        api_base_url=args.api_base_url,
        ssh_user=args.ssh_user,
        ssh_port=args.ssh_port,
        ssh_password=args.ssh_password,
        ssh_key_path=args.ssh_key_path,
    )


def main() -> int:
    print(f"{'➖'*20}\n")
    config = parse_args()
    camera = RemoteFakeCamera(config)
    print(camera.get_data())

    try:
        session = camera.build_session()
        ssh_client = camera.build_ssh_client()
    except RuntimeError as exc:
        LOGGER.error("startup failed error=%s", exc)
        return 2
    except Exception as exc:
        LOGGER.error("connection setup failed error=%s", exc)
        return 3

    api_ok = camera.check_api_health(session)
    api_logs_ok = camera.fetch_api_logs(session)
    ssh_service_ok = camera.run_ssh_check(ssh_client, "systemctl is-active ssh", "active")
    ssh_uname_ok = camera.run_ssh_check(ssh_client, "uname -a", "Linux")
    ssh_client.close()

    if not api_ok or not api_logs_ok or not ssh_service_ok or not ssh_uname_ok:
        LOGGER.error("camera=%s smoke check failed", config.name)
        print(f"\n{'➖'*20}")
        return 1

    LOGGER.info("camera=%s smoke check passed", config.name)
    print(f"\n{'➖'*20}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())