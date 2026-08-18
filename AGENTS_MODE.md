# Agent Working Mode

CURRENT_MODE: ACCEPT_EDITS

Change only the `CURRENT_MODE` value to one of the modes below.

## MANUAL

- Inspect, explain, review, and answer questions.
- Do not modify files.
- Do not run commands that change repository state.
- Show a proposed diff only when requested.

## ACCEPT_EDITS

- Inspect the relevant files and explain the proposed change.
- Show the exact diff before modifying files.
- Wait for explicit user approval.
- After approval, apply only the approved diff and run relevant checks.
- Ask again if the required implementation materially differs from the approved diff.

## PLAN

- Investigate using read-only commands and produce an implementation plan.
- Do not modify files or implement the plan.
- Identify decisions, risks, affected files, and verification steps.

## AUTO

- Make requested, in-scope local edits without asking for approval first.
- Run relevant formatting, tests, and static checks.
- Still request approval for destructive actions, external writes, new authority, or a material expansion of scope.

## General rules

- A direct instruction in the current user message overrides this file for that task.
- Preserve unrelated user changes in every mode.
- Read-only inspection is allowed in all modes.
- If `CURRENT_MODE` is missing or invalid, use `ACCEPT_EDITS`.
- State the active mode briefly before beginning work that may modify files.
