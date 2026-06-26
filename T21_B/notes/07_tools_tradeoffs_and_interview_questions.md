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

## Model answers

### 1. How do you derive system requirements from a customer feature request?

I would start by clarifying the real customer intent, operating scenarios, constraints, and failure consequences. Then I would separate the need from any assumed implementation, because customers often describe a solution instead of the underlying goal. After that I would translate the feature into clear system behaviors, interfaces, performance limits, and fault responses. I would review the draft requirements with software, hardware, and test stakeholders to remove ambiguity and expose missing assumptions. Finally, I would define traceability from the original feature request to the system requirements and planned verification.

### 2. How do you make sure requirements are testable?

I make sure each requirement is clear, measurable, and bounded by conditions. A testable requirement should define what the system does, under which input or state, and what measurable result is expected. I avoid vague words like fast, robust, or user-friendly unless they are converted into measurable criteria. I also check whether the requirement has an obvious verification method such as test, analysis, inspection, or demonstration. If the test team cannot derive an acceptance check from the wording, the requirement is not ready.

### 3. How would you handle a late change request on a safety-relevant feature?

I would first clarify why the change is needed and whether it affects safety goals, assumptions, interfaces, or timing behavior. Then I would run an impact analysis covering requirements, architecture, software, hardware, diagnostics, FMEA or FTA inputs, and verification scope. I would bring the cross-functional owners together to review risk, implementation effort, and release impact before agreeing on the path forward. If the change is accepted, I would update traceability, acceptance criteria, and regression scope in a controlled way. For a safety-relevant feature, I would not treat the change as local until the safety and verification impact is explicitly reviewed.

### 4. What is the difference between verification and validation?

Verification checks whether we built the system right against defined requirements. Validation checks whether we built the right system for the real customer or stakeholder need. In practice, verification is often done at component, software, hardware, or subsystem level against allocated requirements. Validation is usually done at integrated system level in realistic use conditions. A system can pass verification and still fail validation if the original requirement set was incomplete or wrong.

### 5. How would you coordinate software, hardware, and test teams for one system feature?

I would align the teams around one shared feature definition: system goal, interfaces, constraints, timing, fault behavior, and acceptance criteria. Then I would allocate responsibilities clearly so each team knows what they own and what they need from others. I would review interfaces early, because integration problems usually come from mismatched assumptions rather than isolated defects. I would also keep regular cross-functional checkpoints focused on risks, open issues, and change impact instead of only status reporting. The main goal is to keep traceability and technical alignment intact from requirement to verification.

### 6. What would you look for in an FMEA review?

I would check whether the team identified realistic failure modes, not only obvious nominal issues. Then I would look at the effect chain: local effect, next higher-level effect, and final system or customer impact. I would examine whether severity, occurrence, and detection thinking is technically credible and whether the planned actions actually reduce risk. I would also check whether diagnostics, safe states, and verification cases were derived from the analysis. A strong FMEA review is useful only if it changes design, monitoring, or test scope in a concrete way.

### 7. How would you explain inverter-related system risk to a non-specialist stakeholder?

I would explain it in terms of vehicle behavior, safety, and business impact rather than internal electronics details. For example, I would say the inverter controls how electrical power becomes motor torque, so a defect there can affect acceleration, drivability, thermal stress, or fault response. The key risk is not only that the feature stops working, but that it behaves incorrectly under certain conditions such as overheating, sensor faults, or communication loss. Then I would explain what protections exist, how we verify them, and what residual risk remains. That keeps the discussion understandable while still technically honest.

### 8. How do you decide whether a requirement belongs at system level or subsystem level?

I decide based on the intent and scope of the behavior being controlled. If the requirement describes what the overall product must achieve from a customer, vehicle, or integrated feature perspective, it belongs at system level. If it describes how one part of the solution must behave to support the higher-level need, it belongs at subsystem or component level. I also check whether the requirement depends on coordination across multiple domains such as software, hardware, sensing, and diagnostics, because that usually indicates system level. A good rule is that system requirements define the what, while lower-level requirements refine the how within allocated boundaries.

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