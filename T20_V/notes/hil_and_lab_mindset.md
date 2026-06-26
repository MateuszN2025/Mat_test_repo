# HIL and Lab Mindset

## What matters

Hardware-in-the-loop testing is where many embedded QA problems become real: timing, boot issues, flaky power, device recovery, and environmental instability.

## Good HIL habits

- Reset the device to a known state before the test
- Record firmware version and configuration before execution
- Capture logs, timestamps, and external observations
- Design cleanup steps for both pass and fail cases
- Separate product failure from lab failure

## Common failure sources

- Loose cables or unstable power
- Shared lab devices used by multiple jobs
- Timing assumptions that are too optimistic
- Incomplete cleanup after a previous test

## Interview angle

If asked about HIL, explain how you reduce false failures: stable setup, clear reset steps, observability, and artifact collection.

## Practice task

Write a short pre-test checklist for a camera or access control device before running an automated smoke suite.