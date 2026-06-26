# Embedded QA Interview Questions

## What matters

These are short prompts you should be able to answer clearly, with examples and tradeoffs.

## Questions to practice

1. How would you design a smoke suite for a newly deployed embedded device?
2. What should run on every commit versus nightly in a hardware-dependent test lab?
3. How would you reduce flaky failures in HIL testing?
4. What logs and artifacts would you collect when a device update fails?
5. When would you keep logic in Bash and when would you move it to Python?
6. How would you structure CI when hardware resources are limited?
7. How would you prove a failed test is a product bug rather than a lab issue?

## Strong answer pattern

- Start with risk and goal
- Explain the fastest trustworthy signal first
- Mention observability and artifacts
- Mention cleanup or rollback
- Mention one tradeoff

## Example short answer skeleton

For a smoke suite, I would keep the checks small and release-oriented: boot, reachability, critical service health, firmware version, and one core functional path. I would optimize for speed and trust, because a noisy smoke suite slows every team down and gets ignored.

## Practice task

Answer question 3 in 6 to 8 lines using one concrete lab example.