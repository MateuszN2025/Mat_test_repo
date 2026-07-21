# Embedded QA Test Strategy

## What matters

For embedded systems, test strategy is not only about feature coverage. It is also about risk, recovery, field behavior, and update safety.

## A practical pyramid

1. Unit tests: validate small logic quickly.
2. Service or API tests: validate interfaces around the device.
3. HIL tests: validate hardware behavior with real signals or realistic stubs.
4. Smoke tests: prove the build is safe enough for deeper testing.
5. Soak or reliability tests: run longer to expose leaks, hangs, or timing problems.

## What to define early

- Entry criteria for smoke tests
- Exit criteria for release candidates
- Logs and metrics that must be captured on failure
- Rollback path when an update fails
- Flaky test policy

## Useful smoke checks for device fleets

- Device boots and stays reachable
- Critical service is running
- API returns healthy status
- Sensor or camera pipeline starts
- Device can accept config update
- Device reports expected firmware version

## Important tradeoff

A smaller, trusted smoke suite is better than a huge unstable one. In CI, speed and trust are often more valuable than broad but noisy coverage.

## Practice task

Write a 6-point smoke checklist for an access control device and mark which checks should run on every commit versus nightly.