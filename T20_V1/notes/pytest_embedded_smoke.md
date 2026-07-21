# Pytest for Embedded Smoke Checks

## What matters

Pytest is strong for embedded QA because it makes test intent readable, failures explicit, and setup reusable with fixtures.

## Why use fixtures

- They define a known starting state
- They reduce duplicated setup code
- They make state changes in each test easier to reason about

## Why use parametrization

In smoke testing, you often want to prove that each critical signal can fail the overall readiness gate. Parametrization helps do that without copying the same test structure three times.

## What to learn from the example

- The fixture models a healthy device
- The parametrized test flips one critical field at a time
- The assertion message explains the operational meaning of the failure

## Senior-level insight

The best pytest suites for hardware-adjacent systems separate state modeling from transport details. Test behavior in Python first, then integrate with real device calls one layer higher.

## Practice task

Add a field for `disk_space_ok` to the fake device model and extend the smoke readiness logic and tests.