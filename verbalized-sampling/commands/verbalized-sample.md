---
description: Apply verbalized sampling to generate diverse responses with probabilities
---

You are using the Verbalized Sampling technique from arXiv paper 2510.01171v3.

This technique mitigates mode collapse and increases output diversity by explicitly requesting a probability distribution over multiple responses.

<instructions>
Generate 5 responses to the user's query, each within a separate <response> tag.
Each <response> must include:
- A <text> element containing the response content
- A <probability> element with a numeric value representing the likelihood of this response

Randomly sample responses from the full distribution of possibilities.
Ensure the responses are diverse and explore different approaches, styles, or perspectives.
The probabilities should roughly sum to 1.0 but focus on semantic diversity over exact probability calibration.
</instructions>

User's query:
