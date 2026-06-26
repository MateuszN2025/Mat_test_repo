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
6. Run `tests/test_embedded_smoke_pytest.py` with pytest
7. Read `notes/pytest_embedded_smoke.md`
8. Read `notes/github_actions_embedded_qa.md`
9. Read `notes/bdd_gherkin_basics.md`
10. Read `notes/hil_and_lab_mindset.md`
11. Read `notes/interview_questions_embedded_qa.md`

## Why files are separated

Each topic is isolated so you can study one skill at a time. For example, `subprocess` usage is in its own Python file instead of being mixed into a bigger script.

## Quick commands

```bash
python3 T20_V/python/01_subprocess_learning.py
python3 T20_V/python/02_embedded_smoke_check.py
python3 T20_V/python/03_log_parser_learning.py
python3 -m pytest -q T20_V/tests/test_embedded_smoke_pytest.py
bash T20_V/bash/01_bash_strict_mode.sh
bash T20_V/bash/02_device_smoke_runner.sh 127.0.0.1
bash T20_V/run_learning_checks.sh
```

## Senior-level insight

In embedded QA, the hard part is usually not writing one test. The hard part is designing a test system that gives fast signal, survives flaky hardware, and makes failure diagnosis cheap.