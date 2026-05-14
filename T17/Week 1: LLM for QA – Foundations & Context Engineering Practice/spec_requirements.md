# Week 1 Spec/Requirements

## Title
LLM for QA - Foundations & Context Engineering Practice

## Purpose
Build baseline capability for QA engineers to use LLMs safely and effectively in daily test automation work.

## Scope
- QA-focused prompt engineering fundamentals
- Context packaging for debugging and test design
- Safe usage patterns for test data, logs, and defects
- Small practical exercises tied to pytest and CI workflows

## Learning Objectives
- Explain what context engineering is and why it matters in QA
- Create clear prompts from bug reports, logs, and failing tests
- Distinguish between strong and weak context payloads
- Produce reproducible issue summaries for LLM-assisted debugging

## Functional Requirements
1. Provide one concise theory section covering:
   - Prompt structure
   - Context windows
   - Hallucination risk in QA workflows
2. Include three hands-on exercises:
   - Convert a failing test trace into a structured prompt
   - Generate test ideas from a requirement paragraph
   - Refine a noisy bug report into an actionable defect summary
3. Include one review checklist for prompt quality:
   - Completeness
   - Reproducibility
   - Precision of expected vs actual behavior
4. Include one mini-evaluation rubric with pass/fail criteria.

## Non-Functional Requirements
- Material must be readable by mid-level QA engineers
- Examples must be deterministic and reproducible
- No production secrets in examples
- All examples must use sanitized IDs and placeholders

## Deliverables
- Session notes (markdown)
- Bug-history export sample (csv)
- CI failure excerpt sample (log)

## Acceptance Criteria
- At least 3 practical tasks completed by learner
- Learner can produce one high-quality debugging prompt from CI logs
- Learner can identify at least 2 hallucination risks in generated output
- Mentor review confirms prompt checklist usage in all exercises

## Test Scenarios From bug_history_export.csv

### Scenario 1 : Incorrect TestClient POST Usage
- Goal: Detect incorrect API client call syntax in tests.
- Input Source: bug_history_export.csv row BUG-001.
- Preconditions:
  - FastAPI app and pytest tests available.
  - A test calls `client.post("/items/3", payload)`.
- Steps:
  - Run the targeted test.
  - Capture the exception and stack trace.
  - Refactor call to use `json=payload`.
  - Re-run the test.
- Expected Result:
  - Initial run fails with a type/signature error.
  - After fix, request is sent correctly and test proceeds to API-level assertions.

### Scenario 2 : POST Status Code Contract Validation
- Goal: Validate API contract alignment between route behavior and test expectation.
- Input Source: bug_history_export.csv row BUG-002.
- Preconditions:
  - Route performs resource creation but does not explicitly set status code.
- Steps:
  - Execute POST test expecting status `201`.
  - Verify observed response status.
  - Update route decorator to return `201` for create flow.
  - Re-run test.
- Expected Result:
  - Before fix: response status is `200`.
  - After fix: response status is `201` and test passes.



### Scenario 4 : Fixture Drift After Refactor
- Goal: Validate that mocks patch active data structures after refactoring.
- Input Source: bug_history_export.csv row BUG-004.
- Preconditions:
  - Application reads from `items_db`.
  - Fixture patches legacy symbol `ITEMS`.
- Steps:
  - Run mock-marked tests.
  - Confirm mock has no effect on current data path.
  - Update fixture to patch the active store or redesign fixture scope.
  - Re-run tests.
- Expected Result:
  - Before fix: mock tests are flaky or fail against real data.
  - After fix: mocked responses are deterministic and isolated.



## Scenario Review Checklist
- Each scenario references one bug row from the CSV.
- Each scenario includes preconditions, steps, and expected results.
- Each scenario has one clear pass/fail signal.
- Scenarios are reproducible on a clean local setup.

## Risks and Mitigations
- Risk: Over-trust in LLM output
  - Mitigation: Require source-grounded validation step in each exercise
- Risk: Poor context quality
  - Mitigation: Enforce fixed prompt template before model usage
- Risk: Leaking sensitive data
  - Mitigation: Mandatory redaction pass before sharing logs

## Week 1 Done Definition
- All three artifacts created and reviewed
- One CI failure converted into a QA-ready incident summary
- One retrospective note added: what context improved answer quality
