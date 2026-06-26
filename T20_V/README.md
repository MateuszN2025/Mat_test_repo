# T20_V Learning Pack

This folder is a short learning pack for the Embedded Automated Test & Test System Engineer role described in [job_offer.txt](./job_offer.txt).

## What matters for this role

- Python for automation, reporting, and orchestration
- Bash and Linux for daily device and CI work
- Embedded QA thinking: smoke tests, reliability, observability, rollback
- CI basics for hardware-adjacent systems
- BDD/Gherkin basics for readable test intent

## Suggested order

1. Read `notes/test_strategy_embedded_qa.md`
2. Read `notes/linux_bash_for_qa.md`
3. Run `bash/01_bash_strict_mode.sh`
4. Run `python/01_subprocess_learning.py`
5. Run `python/02_embedded_smoke_check.py`
6. Run `python/03_log_parser_learning.py`
7. Run `python/04_argparse_logging_pathlib_learning.py`
8. Run `python/05_serial_boot_learning.py`
9. Run `python/06_requests_learning.py`
10. Run `python/07_paramiko_ssh_learning.py`
11. Run `python/08_threading_learning.py`
12. Run `python/09_multiprocessing_learning.py`
13. Run `python/10_pytest_fixtures_learning.py` with pytest
14. Run `python/11_pytest_parametrize_scope_learning.py` with pytest
15. Run `python/12_bdd_step_mapping_learning.py`
16. Run `python/13_oop_device_model_learning.py`
17. Run `python/14_decorators_generators_learning.py`
18. Run `python/15_regex_json_csv_learning.py`
19. Run `bash/03_linux_log_toolbox.sh`
20. Run `bash/04_linux_network_device_checks.sh`
21. Run `bash/05_linux_process_permissions.sh`
22. Run `tests/test_embedded_smoke_pytest.py` with pytest
23. Read `notes/pytest_embedded_smoke.md`
24. Read `notes/python_framework_organization.md`
25. Read `notes/end_to_end_camera_recovery.md`
26. Read `notes/github_actions_embedded_qa.md`
27. Read `notes/bdd_gherkin_basics.md`
28. Read `notes/hil_and_lab_mindset.md`
29. Read `notes/interview_questions_embedded_qa.md`

## Why files are separated

Each topic is isolated so you can study one skill at a time. For example, `subprocess` usage is in its own Python file instead of being mixed into a bigger script.

## Quick commands

```bash
python3 T20_V/python/01_subprocess_learning.py
python3 T20_V/python/02_embedded_smoke_check.py
python3 T20_V/python/03_log_parser_learning.py
python3 T20_V/python/04_argparse_logging_pathlib_learning.py --log-file /tmp/device.log
python3 T20_V/python/05_serial_boot_learning.py
python3 T20_V/python/06_requests_learning.py
python3 T20_V/python/07_paramiko_ssh_learning.py
python3 T20_V/python/08_threading_learning.py
python3 T20_V/python/09_multiprocessing_learning.py
python3 -m pytest -q T20_V/python/10_pytest_fixtures_learning.py
python3 -m pytest -q T20_V/python/11_pytest_parametrize_scope_learning.py
python3 T20_V/python/12_bdd_step_mapping_learning.py
python3 T20_V/python/13_oop_device_model_learning.py
python3 T20_V/python/14_decorators_generators_learning.py
python3 T20_V/python/15_regex_json_csv_learning.py
python3 -m pytest -q T20_V/tests/test_embedded_smoke_pytest.py
bash T20_V/bash/01_bash_strict_mode.sh
bash T20_V/bash/02_device_smoke_runner.sh 127.0.0.1
bash T20_V/bash/03_linux_log_toolbox.sh
bash T20_V/bash/04_linux_network_device_checks.sh
bash T20_V/bash/05_linux_process_permissions.sh
bash T20_V/run_learning_checks.sh
```

## Senior-level insight

In embedded QA, the hard part is usually not writing one test. The hard part is designing a test system that gives fast signal, survives flaky hardware, and makes failure diagnosis cheap.