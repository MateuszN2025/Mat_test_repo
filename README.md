# QA Automation Mentor Setup

This repository contains a minimal custom Copilot setup for learning toward a senior QA automation engineer role.

## What Is Included

- `.github/skills/qa-automation-mentor/SKILL.md`
- `.github/agents/qa-automation-mentor.agent.md`
- `.github/prompts/qa-automation-mentor.prompt.md`

## What Each File Does

- `SKILL.md` creates a reusable slash skill for guided QA automation learning.
- `qa-automation-mentor.agent.md` creates a selectable custom agent persona.
- `qa-automation-mentor.prompt.md` creates a slash command that opens a mentoring session with the custom agent.

## Topics Covered

- Python
- pytest
- Linux
- bash
- CI and debugging
- test design and flaky test analysis

## Example Prompts

- `/qa-automation-mentor Give me a 7-day pytest study plan.`
- `Use qa-automation-mentor to give me a 7-day pytest study plan.`
- `Teach me Linux commands every QA automation engineer should know.`
- `Review this pytest fixture setup like a senior automation engineer.`
- `Give me 5 senior-level Python plus pytest interview questions.`

## Notes

- Skills are discovered when placed under a supported `.github/skills/<name>/` path.
- Agents are discovered when placed under `.github/agents/`.
- Prompts are discovered when placed under `.github/prompts/`.
- Open `Mat_test_repo` as the workspace folder so Copilot can discover the root `.github` customizations.
- If the new prompt or agent does not appear immediately, run `Developer: Reload Window` in VS Code.