# Tools, Tradeoffs, And Interview Questions

## What matters

This file helps you convert theory into spoken interview answers.

## Tool awareness you should show

### Polarion or DOORS

Use them to organize requirements, trace links, baselines, changes, and review evidence.

### SysML

Use it to describe structure, interfaces, behavior, and system relationships at a level that supports discussion and alignment.

### Simulink

Use it when control logic, dynamic behavior, or simulation-based reasoning helps de-risk design before full implementation.

The important point is not the tool name itself. The important point is what engineering problem the tool helps solve.

## Tradeoffs to practice

You should be able to discuss tradeoffs like these:

- performance versus thermal margin
- efficiency versus cost
- feature ambition versus delivery risk
- early architectural flexibility versus implementation simplicity
- broad test scope versus fast feedback

## Interview questions to rehearse

1. How do you derive system requirements from a customer feature request?
2. How do you make sure requirements are testable?
3. How would you handle a late change request on a safety-relevant feature?
4. What is the difference between verification and validation?
5. How would you coordinate software, hardware, and test teams for one system feature?
6. What would you look for in an FMEA review?
7. How would you explain inverter-related system risk to a non-specialist stakeholder?
8. How do you decide whether a requirement belongs at system level or subsystem level?

## Answer framework for behavioral-technical questions

When a question asks what you would do, use this sequence:

1. Clarify the goal.
2. Identify risks and constraints.
3. Explain your engineering approach.
4. Show collaboration points.
5. End with verification and change control.

## Example answer skeleton

Question: How would you handle a late change request on an inverter feature?

Short answer skeleton:

I would first clarify the business and technical reason for the change, then identify impacted requirements, interfaces, safety analyses, and tests. After that I would run a cross-functional impact review with software, hardware, and test stakeholders. I would make the tradeoffs visible, especially on timing, risk, and verification effort. Finally, I would update traceability and ensure the revised acceptance criteria are explicit.

## Practice task

Pick any three questions from this list and answer each one in 6 to 8 lines out loud. If any answer sounds vague, rewrite it using stronger engineering language.