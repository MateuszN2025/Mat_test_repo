#!/usr/bin/env bash

set -euo pipefail

# This wrapper keeps the runnable learning examples in one place.
python3 T20_V/python/01_subprocess_learning.py
python3 T20_V/python/02_embedded_smoke_check.py
python3 T20_V/python/03_log_parser_learning.py
python3 -m pytest -q T20_V/tests/test_embedded_smoke_pytest.py
bash T20_V/bash/01_bash_strict_mode.sh
bash T20_V/bash/02_device_smoke_runner.sh 127.0.0.1

echo "All T20_V learning checks finished successfully."