---
agent: ask
description: Translate provided text to Polish in formal and informal variants.
model: Auto (copilot)
---

When the user runs `/toPL`, do the following:

1. Use Auto model behavior (lightweight/default model routing).
2. Translate the text currently provided in chat/editor context into Polish.
3. Return exactly two versions:
    - Formal Polish
    - Informal Polish
4. Preserve original meaning, key terms, names, numbers, and formatting.
5. If source text is ambiguous, choose the most natural translation and keep both variants semantically aligned.
6. Do not add explanations unless the user explicitly asks for them.

Output format:

Formal (PL):
<translated formal text>

Informal (PL):
<translated informal text>