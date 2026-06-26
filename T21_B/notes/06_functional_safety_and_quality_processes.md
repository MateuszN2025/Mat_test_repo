# Functional Safety And Quality Processes

## What matters

The job offer explicitly names FMEA, FTA, ASPICE, and ISO 26262. You should be ready to explain the purpose of each one and how they support development quality.

## FMEA in simple language

Failure Mode and Effects Analysis is a structured way to ask:

- How can this item fail?
- What happens if it fails?
- How severe is that effect?
- How likely is the cause?
- How likely are we to detect it?
- What should we change to reduce risk?

Good interview point:

FMEA is useful early because it forces teams to think beyond nominal behavior and design verification around realistic failures.

## FTA in simple language

Fault Tree Analysis starts from an unwanted top event and works backward through possible contributing faults and combinations.

Good interview point:

FTA is especially useful when you need to understand how multiple lower-level failures can combine into a system-level hazard.

## ASPICE

ASPICE is a process assessment framework used heavily in automotive development. In interview terms, focus on what it changes in behavior:

- clearer engineering processes
- better work-product discipline
- stronger traceability
- more consistent reviews and verification

You do not need to recite process area names unless the interviewer goes deep.

### ASPICE in practical language

ASPICE matters because it pushes teams to work in a controlled, reviewable way instead of relying on informal knowledge.

In day-to-day engineering, that usually means:

- requirements are reviewed and version-controlled
- architecture decisions are documented
- test cases are linked to requirements
- changes are impact-checked before implementation
- defects, reviews, and verification evidence are recorded

If an interviewer asks what ASPICE means in real work, a good answer is:

ASPICE improves engineering discipline. It helps the team prove that requirements were understood, design decisions were reviewed, tests were planned, and changes were controlled.

### ASPICE example in a car project

Example: regenerative braking coordination feature.

- System requirement defines when regen braking is allowed and when friction braking must take over.
- Software and hardware teams receive allocated requirements.
- Interfaces between brake controller, inverter, and diagnostics are documented.
- Test team creates verification cases for normal braking, low battery, cold temperature, and fault fallback.
- If a requirement changes, the team performs impact analysis and updates design, tests, and traceability.

That is the kind of engineering behavior ASPICE is trying to enforce.

## ISO 26262

ISO 26262 is the automotive functional safety standard. At interview depth, you should understand:

- hazards must be identified and assessed
- safety goals must be defined
- requirements and architecture must support safe behavior
- verification must include safety-relevant cases
- the process must produce objective evidence

## Functional safety in practical language

Functional safety is about reducing unreasonable risk caused by malfunctioning behavior of electrical or electronic systems.

It is not only about whether the feature works in nominal conditions. It is about what happens when something goes wrong.

Typical functional safety thinking:

- What dangerous behavior could happen?
- What could cause it?
- How do we detect it?
- How do we move the system to a safe state?
- How do we prove that the safety mechanism works?

## Practical car functionalities with functional safety relevance

### 1. Torque control in an electric vehicle

Risk:

The inverter may command unintended acceleration or fail to remove torque.

Possible safety mechanisms:

- plausibility check between pedal input and torque request
- monitoring of motor current and torque feedback
- watchdog supervision of control software
- safe torque off on severe fault

Verification examples:

- inject invalid torque request
- simulate sensor disagreement
- confirm torque is limited or removed within required timing

### 2. Brake-by-wire or brake assist

Risk:

The braking request may be too low, too high, or delayed.

Possible safety mechanisms:

- redundant sensing of pedal position or pressure
- plausibility checks between requested and measured brake response
- fallback to hydraulic braking path where applicable
- diagnostic fault reporting to the vehicle controller

Verification examples:

- simulate stuck sensor value
- simulate communication loss between brake controller and actuator
- confirm system enters degraded but safe mode

### 3. Steering assist

Risk:

The vehicle may apply unintended steering torque or lose required assist.

Possible safety mechanisms:

- steering angle sensor plausibility checks
- torque command monitoring
- redundant channels for key signals
- controlled shutdown of assist with driver warning

Verification examples:

- inject steering angle mismatch
- simulate internal controller fault
- confirm no hazardous unintended steering command is produced

### 4. Battery management system

Risk:

Battery cells may overcharge, overdischarge, or overheat.

Possible safety mechanisms:

- voltage and temperature monitoring
- contactor opening on severe fault
- cell balancing control with diagnostics
- communication of limits to the powertrain controller

Verification examples:

- simulate overtemperature sensor reading
- simulate cell voltage outside safe range
- confirm charging or discharging is blocked when required

### 5. ADAS camera or radar support functions

Risk:

The system may fail to detect an object or may trigger a false intervention.

Possible safety mechanisms:

- sensor health monitoring
- degraded mode handling
- driver handover or warning strategy
- cross-checking between multiple sensors where applicable

Verification examples:

- simulate blocked camera
- simulate corrupted radar input
- confirm safe degradation and correct driver notification

## How to explain functional safety in interview practice

Use this pattern:

1. Name the function.
2. Name the hazardous malfunction.
3. Describe detection or monitoring.
4. Describe the safe state or fallback behavior.
5. Mention how you would verify it.

Example:

For inverter torque control, the key hazard is unintended torque. I would expect monitoring of torque request plausibility, current feedback, and fault timing. On severe mismatch, the system should move to a safe torque-off or torque-limited state. Then I would verify both fault detection and reaction timing in realistic scenarios.

## How these topics connect

- Requirements define intended behavior.
- Safety analysis challenges that behavior under fault conditions.
- Process frameworks ensure the work is repeatable and auditable.
- Verification proves both function and protection.

- ASPICE helps ensure the work products, reviews, and traceability exist.
- ISO 26262 helps ensure that safety-relevant risks are identified and controlled.

## Strong answer pattern

I see FMEA and FTA as risk-analysis tools that feed system requirements, diagnostics, and verification scope. ASPICE and ISO 26262 then shape how rigorously those activities are performed, reviewed, and evidenced.

## Senior-level insight

The value of process is not bureaucracy by itself. The value is that it reduces the chance of hidden assumptions, missing evidence, and late discovery of safety-relevant defects.

Another senior point: strong engineers connect process and safety to technical decisions. They do not treat ASPICE as paperwork or functional safety as a separate team problem. They use both to improve architecture, diagnostics, and verification scope early.

## Practice task

Prepare a 5-line answer to this question: Why is FMEA not just a documentation exercise?