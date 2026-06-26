# Requirements, Architecture, And Change Control

## What matters

This role strongly emphasizes requirements work. You should be ready to explain how you elicit, refine, negotiate, document, review, trace, and update requirements.

## A good requirement should be

- Clear
- Unambiguous
- Necessary
- Feasible
- Verifiable
- Traceable
- Consistent with related requirements

Bad requirement example:

The inverter shall respond quickly.

Better requirement example:

The inverter shall achieve commanded torque response within the specified response-time window under defined operating conditions listed in the system performance specification.

## Elicitation to verification flow

1. Collect stakeholder needs and constraints.
2. Clarify operating scenarios, failure scenarios, and interfaces.
3. Write system requirements.
4. Review them with cross-functional teams.
5. Allocate them to hardware, software, controls, and test.
6. Link each important requirement to verification evidence.

## Negotiating requirements

In an interview, show that you understand that requirements are often negotiated, not simply received.

Useful negotiation questions:

- What customer problem is this requirement solving?
- Is this a true need or a preferred implementation?
- What is the acceptance criterion?
- What operating range, timing, and fault conditions apply?
- What happens if this requirement conflicts with cost, thermal, or safety limits?

## Architecture proposals

When you discuss architecture, show structured reasoning:

1. State the system goal.
2. Name the key functions.
3. Define major interfaces.
4. Describe constraints.
5. Explain why one allocation is better than another.

## Change request handling

The offer explicitly mentions change requests and issue investigations. A strong answer should include impact analysis.

Good change-control flow:

1. Understand the change trigger.
2. Identify impacted requirements, interfaces, components, and tests.
3. Assess risk, cost, timing, and verification impact.
4. Review with stakeholders.
5. Approve, reject, or defer with rationale.
6. Update traceability and verification plan.

## Tools you should be able to discuss

- Polarion or DOORS for requirements management
- SysML for system structure and behavior modeling
- Simulink for control-oriented modeling and simulation

You do not need to pretend expert depth if you do not have it. It is better to say how you would use a tool in a process than to fake tool-specific details.

## Senior-level insight

Weak engineers treat requirement changes as document edits. Strong engineers treat them as system-impact events that affect architecture, test coverage, safety analysis, and delivery risk.

## Practice task

Take one imaginary requirement change: tighter torque response time. Write a 6-step impact analysis for software, hardware, and testing.