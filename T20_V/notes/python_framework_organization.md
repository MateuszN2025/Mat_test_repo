# Python Interview Topics For Embedded QA

## Why pytest

- `pytest` gives fast feedback with very little boilerplate.
- Fixtures make hardware, API, and SSH setup reusable across many tests.
- Markers let you split smoke, regression, lab-only, and slow suites.
- Parameterization helps reuse the same test flow across multiple device types.
- Reporting, xfail, skip, and plugin support make CI integration much easier than hand-rolled scripts.

## How to organize a large test framework

A practical structure for embedded QA usually separates test intent from device control code.

```text
tests/
    smoke/
    regression/
    performance/
helpers/
    api_client.py
    ssh_client.py
    serial_client.py
    log_parser.py
framework/
    config.py
    reporting.py
    retry.py
    fixtures.py
data/
    sample_logs/
    configs/
```

## Design rules that matter

- Keep device transports behind small wrappers so tests do not know whether they talk over SSH, serial, or HTTP.
- Put retries and timeout logic in helper layers, not repeated inside every test.
- Make logs and artifacts first-class outputs so failures are cheap to debug.
- Separate smoke tests from longer regression suites so CI keeps fast signal.
- Keep test data in files when it changes often, instead of hard-coding everything into test functions.

## Live-coding topics likely to matter

- `subprocess`: execute local commands, inspect return codes, and capture output.
- `pyserial`: wait for boot logs, send a command, and detect timeouts safely.
- `requests`: call device health endpoints and verify structured responses.
- `paramiko`: run Linux checks on remote devices over SSH.
- `logging`: emit clear timestamps and step-level diagnostics.
- `argparse`: turn a script into a CI-friendly command-line tool.
- `pathlib`: handle logs, configs, and artifact paths cleanly.
- `threading`: poll multiple devices at the same time for I/O-bound work.
- `multiprocessing`: parallelize CPU-heavy parsing or data processing when needed.

## Senior-level insight

The test framework should optimize for diagnosability before cleverness. In hardware-adjacent automation, the winning design is usually the one that makes the next failure obvious in two minutes, not the one with the most abstraction.