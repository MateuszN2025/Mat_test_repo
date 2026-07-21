# End-to-End Embedded QA Scenario

## Interview question shape

How would you design an automated test that power-cycles a camera, waits for Linux to boot, logs in over SSH, checks logs, and verifies that the main service came back healthy?

## Strong answer structure

1. Reset the device through a controllable power source or relay.
2. Start artifact collection immediately: timestamps, serial logs, and power actions.
3. Wait for the boot signal with a timeout, usually from serial output or a health probe.
4. Log in over SSH only after reachability is confirmed.
5. Verify a few release-critical checks first: firmware version, service state, and one simple functional path.
6. Parse logs for hard failures such as kernel panic, watchdog reset, or repeated service crashes.
7. Return a clear pass or fail exit code and attach artifacts for debugging.

## Pseudocode flow

```text
power_off()
power_on()
wait_for_serial_text("boot completed", timeout=90)
wait_for_ping(timeout=30)
ssh_run("systemctl is-active camera-service")
ssh_run("journalctl -u camera-service --since test-start")
assert no critical log signatures
assert service is active
```

## Tradeoffs to mention

- Serial is better than SSH for early boot visibility.
- Smoke checks should be fast and deterministic, not exhaustive.
- Retries belong on unstable transport edges, not around every assertion.
- The framework should separate lab failures from product failures.

## Quick notes

- HIL means real hardware is part of the loop, so resets, cabling, and power control matter.
- Yocto is commonly used to build custom embedded Linux images, so it is worth knowing at a high level.