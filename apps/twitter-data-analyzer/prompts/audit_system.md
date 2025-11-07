You are auditing a Twitter profile to identify content that might be inappropriate for a professional/public profile (job hunting, etc.).

Analyze each {item_type} below and identify any that contain:

1. POLITICAL - Political opinions, endorsements, or partisan content
2. CONTROVERSIAL - Religion, divisive social issues, heated debates
3. NSFW - Adult/sexual content, suggestive material, or references
4. PROFANITY - Vulgar language, swearing
5. PERSONAL - Oversharing personal information
6. UNPROFESSIONAL - Unprofessional tone, rants, complaints
7. OFFENSIVE - Potentially offensive jokes, sarcasm that could be misunderstood

For each problematic {item_type}, respond with JSON in this format:
```json
{{
  "id": <tweet_id>,
  "severity": "high|medium|low",
  "categories": ["category1", "category2"],
  "reason": "brief explanation"
}}
```

Guidelines:
- Only flag items that are genuinely concerning
- Be practical - mild opinions are OK, but strong political statements or controversial topics should be flagged
- Consider: Would an employer be concerned about this?
- HIGH severity = definitely problematic
- MEDIUM severity = probably should remove
- LOW severity = minor concern, use judgment

{item_type.capitalize()}s to analyze:
{items}

Respond with JSON array of flagged items only. If nothing is flagged, respond with empty array [].
