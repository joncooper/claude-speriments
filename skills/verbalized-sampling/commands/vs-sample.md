---
description: Generate diverse responses and randomly sample one based on verbalized probabilities
---

You are using Verbalized Sampling with weighted random selection.

This technique first generates a diverse distribution of responses, then samples from it to return a single response.

<instructions>
STEP 1: Generate 5 responses to the user's query, each within a <response> tag.
Each <response> must include:
- A <text> element containing the response content
- A <probability> element with a numeric value

Ensure the responses are diverse and explore different approaches.

STEP 2: After generating all 5 responses, randomly select ONE based on the probabilities.
Think through your sampling decision:
- Normalize the probabilities if needed
- Consider each response's probability weight
- Make a random selection (don't just pick the highest probability)
- Explain which response you selected and why

STEP 3: Present the selected response to the user along with a brief note about the sampling process.

This two-step process maintains diversity while providing a single actionable response.
</instructions>

User's query:
