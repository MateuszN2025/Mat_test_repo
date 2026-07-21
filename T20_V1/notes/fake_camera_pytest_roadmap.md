# Roadmap: Fake Camera to Pytest Runner

## Goal

Prepare a small learning path for an embedded QA-style workflow:

1. Create a fake camera model that can represent several cameras.
2. Connect to a camera instance and retrieve logs.
3. Prepare a Bash entrypoint that runs pytest tests.

This document is intentionally a roadmap only. It does not include implementation details or code.

## Scope

- Focus on structure, sequence, and acceptance checkpoints.
- Keep the first version simple and test-oriented.
- Treat this as a stepping stone toward camera-device automation for interview practice.

## Phase 1: Fake Camera Model

### Objective

Define a camera abstraction that can be instantiated multiple times and behaves predictably in tests.

### Planning points

- Decide what makes one fake camera different from another.
- Define the minimum camera attributes needed for testing.
- Define basic camera states such as available, offline, or busy.
- Decide how each camera should expose status and logs.
- Decide whether logs are static, generated, or state-based.

### Deliverable

- A clear fake-camera concept that supports creating a few independent camera instances.

### Exit criteria

- It is clear how to create multiple camera objects.
- Each camera has a stable identity.
- Each camera has predictable behavior for later test scenarios.
- The camera model is simple enough to support smoke-style tests.

## Phase 2: Camera Connection and Log Retrieval

### Objective

Define how a test or helper layer interacts with a camera instance and gathers logs.

### Planning points

- Decide what "connect" means for the fake camera.
- Define the expected success path for connection.
- Define failure paths such as timeout, unavailable camera, or bad state.
- Decide when logs are fetched: before, during, or after a test action.
- Define the format and minimum content of collected logs.
- Decide how to separate connection problems from camera-behavior problems.

### Deliverable

- A documented interaction flow for connect, inspect, and collect logs.

### Exit criteria

- The connection flow is explicit and repeatable.
- Log retrieval has a defined trigger and expected output.
- Failure cases are named and distinguishable.
- The artifact path for logs is clear enough for later pytest use.

## Phase 3: Pytest Test Layer

### Objective

Define the first tests that validate fake-camera behavior and log collection.

### Planning points

- Decide the smallest smoke scenarios worth automating first.
- Separate happy-path checks from negative checks.
- Decide what setup should be reusable across tests.
- Decide how camera instances will be selected by tests.
- Define what a useful test failure message should communicate.

### Suggested first test themes

- Camera can be created with expected identity.
- Multiple cameras can exist without interfering with each other.
- Connection succeeds for a healthy camera.
- Connection fails clearly for an unavailable camera.
- Log retrieval returns expected data for a known scenario.

### Exit criteria

- There is a small, high-signal smoke suite.
- Test intent is easy to read.
- The first tests can support later extension to more realistic device behavior.

## Phase 4: Bash Script to Run Pytest

### Objective

Prepare a Bash entrypoint that runs the pytest suite in a consistent way.

### Planning points

- Define how the environment should be prepared before test execution.
- Decide whether the script runs all tests or a selected subset.
- Define how test results should be displayed.
- Define how exit codes should be passed through.
- Decide where logs or reports should be stored.
- Keep the script narrow: one job, clear output, predictable failure behavior.

### Deliverable

- A documented Bash runner concept for executing pytest tests locally.

### Exit criteria

- The test command path is clear.
- The script behavior is deterministic.
- Failures are visible from the shell return status.
- The script is simple enough to reuse in CI later.

## Recommended Order of Work

1. Define the fake camera shape and minimum states.
2. Decide how connection and log collection should behave.
3. Write the first smoke-oriented pytest scenarios on top of that model.
4. Add the Bash wrapper only after the test entrypoint is clear.
5. Refine naming, artifacts, and failure reporting once the flow is stable.

## Decisions to Make Early

- What is the minimum realistic behavior needed from the fake camera.
- Whether logs are generated dynamically or returned from prepared samples.
- Whether connection is modeled as a direct method call or as a transport-like layer.
- Which failures belong to the device model and which belong to the test harness.

## Risks to Watch

- Making the fake camera too complex before the first tests exist.
- Mixing camera behavior with test-runner concerns too early.
- Collecting logs without defining how they help diagnose failures.
- Writing a Bash wrapper before the pytest entrypoint is stable.

## Practical Definition of Done

- A few fake cameras can be represented consistently.
- A test flow can connect to a chosen camera and request logs.
- A small pytest suite validates the core behavior.
- A Bash script can run the tests repeatably from the command line.

## Natural Next Step After This Roadmap

Start with the smallest possible fake-camera behavior that is enough to support one positive connection scenario and one log-retrieval scenario.