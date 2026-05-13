---
agent: ask
description: Translate provided Polish text to English in formal and informal variants.
model: Auto (copilot)
---

When the user runs `/toEN`, do the following:

1. Use Auto model behavior (lightweight/default model routing).
2. Translate the Polish text currently provided in chat/editor context into English.
3. Return exactly two versions:
    - Formal English
    - Informal English
4. Preserve original meaning, key terms, names, numbers, and formatting.
5. If source text is ambiguous, choose the most natural translation and keep both variants semantically aligned.
6. Do not add explanations unless the user explicitly asks for them.

Output format:

Formal (EN):
<translated formal text>

Informal (EN):
<translated informal text>