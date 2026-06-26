# BDD and Gherkin Basics

## What matters

BDD is useful when you want readable behavior descriptions shared across QA, developers, and product people.

## Core syntax

- `Feature`: the capability
- `Scenario`: one example of behavior
- `Given`: starting state
- `When`: action
- `Then`: expected outcome

## Good BDD habits

- Describe behavior, not UI click noise
- Keep scenarios small and readable
- Avoid putting implementation details in steps
- Use domain language that stakeholders understand

## Embedded example idea

A camera device boots, connects to the network, and starts streaming within a target time budget.

## Tradeoff

BDD improves readability, but badly written scenarios become another brittle layer. Use it for important behaviors, not every tiny assertion.

## Practice task

Convert one smoke test from `python/02_embedded_smoke_check.py` into a Gherkin scenario.