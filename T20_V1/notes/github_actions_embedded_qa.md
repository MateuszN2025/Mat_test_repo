# GitHub Actions for Embedded QA

## What matters

Even when hardware tests run outside GitHub-hosted runners, GitHub Actions can orchestrate validation, packaging, reporting, and safe promotion.

## Typical pipeline stages

1. Lint and unit test Python code
2. Build artifacts or test packages
3. Run smoke tests
4. Publish reports
5. Gate promotion or release

## Embedded-specific concerns

- Hardware is limited, so jobs must queue cleanly
- Devices need cleanup after failures
- Logs, screenshots, and serial output should be archived
- Retry policy must be controlled so real issues are not hidden

## Good interview talking points

- Separate fast checks from hardware-dependent checks
- Keep hardware lab resources visible and schedulable
- Capture enough context so a failed job is diagnosable without rerunning
- Use clear pass or fail gates for promotion

## Practice task

Explain when you would run HIL tests on every pull request and when you would move them to scheduled nightly runs.