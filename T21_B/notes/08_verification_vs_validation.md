# Verification Vs Validation

## Short answer

- Verification asks: did we build the system right?
- Validation asks: did we build the right system?

## What matters

These two terms are often confused in interviews and project discussions, but they answer different questions.

- Verification checks whether the implementation matches specified requirements.
- Validation checks whether the final system satisfies the real stakeholder, customer, or user need.

## Simple difference

### Verification

- Compares the product against requirements, design, or specification.
- Usually happens at component, software, hardware, and subsystem levels.
- Focuses on correctness against defined expectations.

Typical question:

Did this feature behave exactly as the requirement said?

### Validation

- Compares the final system behavior against intended use and customer value.
- Usually happens at integrated system level, sometimes in realistic or vehicle-level scenarios.
- Focuses on fitness for purpose.

Typical question:

Does this solution actually solve the real customer problem in the intended context?

## In the V-cycle

- Verification is mostly on the right side of the V when checking lower-level and mid-level outputs against allocated requirements.
- Validation is near the top-right of the V when checking the full system against stakeholder intent.

## Practical example: traction inverter

Customer need:

The vehicle should deliver stable torque response during normal driving and safe behavior during faults.

System requirement:

The inverter shall disable torque output within 100 ms after overtemperature fault detection.

### Verification example

You run a test and measure the time from overtemperature detection to torque disable.

- Requirement says: within 100 ms.
- Measured result: 82 ms.
- Conclusion: requirement is met.

This is verification because you checked the implementation against a defined requirement.

### Validation example

You test the complete vehicle behavior in a realistic scenario and confirm that fault handling is safe, understandable, and acceptable from the vehicle and customer perspective.

- The driver does not experience dangerous unintended behavior.
- The system enters a safe state.
- The behavior supports the intended use case.

This is validation because you checked whether the complete solution fulfills the real need.

## A useful rule

- Verification can pass while validation fails.
- Validation can reveal that the original requirement was incomplete or wrong.

Example:

If the inverter always disables torque within 100 ms, verification may pass. But if the strategy creates unsafe or unacceptable behavior in a real driving situation, validation may fail.

## Common mistake

A common junior mistake is treating validation as just another functional test. A senior engineer understands that validation is broader: it checks whether the chosen requirements and architecture actually solved the right problem.

## Good interview answer

Verification is about conformance to requirements. Validation is about suitability for real use. In simple words, verification checks whether we built the system right, while validation checks whether we built the right system. In an inverter project, timing a fault response against a requirement is verification, but confirming the complete vehicle-level behavior meets customer and safety intent is validation.

## Senior-level insight

Strong engineers do not wait until the end of the project to think about validation. They challenge assumptions early, because a perfectly verified system can still be the wrong solution.

## Practice task

Write two short examples from your own experience:

1. One case that was mostly verification.
2. One case that was true validation.

Keep each example under 5 lines.