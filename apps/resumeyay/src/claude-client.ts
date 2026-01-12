/**
 * Claude Client for Fit Coach
 *
 * Handles:
 * 1. Job description parsing into structured requirements
 * 2. Fit coaching conversations
 * 3. Keyword extraction and matching
 */

import type {
  JDRequirement,
  FitCoachMessage,
  ParsedJobDescription,
  JobDescription,
  Resume,
  ResumeVariant,
  ContentNode,
} from './types';
import { v4 as uuid } from 'uuid';

// Claude API types
interface ClaudeResponse {
  content: Array<{
    type: string;
    text: string;
  }>;
}

// Configuration
const CLAUDE_API_URL = 'https://api.anthropic.com/v1/messages';
const CLAUDE_MODEL = 'claude-sonnet-4-20250514';
const ANTHROPIC_VERSION = '2023-06-01';

/**
 * Parse a job description into structured requirements using Claude.
 */
export async function parseJobDescription(
  jobDescription: JobDescription,
  apiKey: string
): Promise<ParsedJobDescription> {
  const prompt = `Analyze this job description and extract requirements.

JOB TITLE: ${jobDescription.title}
COMPANY: ${jobDescription.company}

JOB DESCRIPTION:
${jobDescription.description}

Extract ALL requirements and categorize them. Return ONLY valid JSON in this exact format:
{
  "requirements": [
    {
      "text": "requirement description",
      "category": "required" | "preferred" | "nice-to-have",
      "keywords": ["keyword1", "keyword2"]
    }
  ]
}

Important:
- "required" = must-have, hard requirements
- "preferred" = strongly desired, important
- "nice-to-have" = bonus, would be nice
- Extract specific skills, technologies, years of experience, qualifications
- Include soft skills and cultural fit items
- Keywords should be searchable terms to find in a resume`;

  try {
    const response = await fetch(CLAUDE_API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': apiKey,
        'anthropic-version': ANTHROPIC_VERSION,
      },
      body: JSON.stringify({
        model: CLAUDE_MODEL,
        max_tokens: 4096,
        messages: [{ role: 'user', content: prompt }],
      }),
    });

    if (!response.ok) {
      throw new Error(`Claude API error: ${response.status}`);
    }

    const data: ClaudeResponse = await response.json();
    const text = data.content[0]?.text || '{}';

    // Extract JSON from response (might have markdown code blocks)
    const jsonMatch = text.match(/\{[\s\S]*\}/);
    const parsed = JSON.parse(jsonMatch?.[0] || '{"requirements":[]}');

    const requirements: JDRequirement[] = parsed.requirements.map((req: {
      text: string;
      category: string;
      keywords: string[];
    }) => ({
      id: uuid(),
      text: req.text,
      category: req.category as 'required' | 'preferred' | 'nice-to-have',
      keywords: req.keywords || [],
      matchedBulletIds: [],
      matchedEntryIds: [],
      coverageStatus: 'missing' as const,
    }));

    return {
      id: uuid(),
      originalJobDescriptionId: jobDescription.id,
      title: jobDescription.title,
      company: jobDescription.company,
      requirements,
      parsedAt: new Date().toISOString(),
      rawText: jobDescription.description,
    };
  } catch (error) {
    console.error('Failed to parse job description:', error);
    // Return mock parse on failure
    return mockParseJobDescription(jobDescription);
  }
}

/**
 * Mock job description parser for testing and when API is unavailable.
 */
export function mockParseJobDescription(jobDescription: JobDescription): ParsedJobDescription {
  // Extract requirements from the already-extracted requirements field
  const requirements: JDRequirement[] = jobDescription.requirements.map((req, index) => ({
    id: uuid(),
    text: req,
    category: index < 3 ? 'required' : index < 6 ? 'preferred' : 'nice-to-have',
    keywords: extractKeywordsFromText(req),
    matchedBulletIds: [],
    matchedEntryIds: [],
    coverageStatus: 'missing' as const,
  }));

  // Also parse keywords from the job description
  const additionalKeywords = jobDescription.keywords.filter(
    kw => !requirements.some(r => r.keywords.includes(kw.toLowerCase()))
  );

  // Add any additional keywords as separate requirements
  if (additionalKeywords.length > 0) {
    requirements.push({
      id: uuid(),
      text: `Skills: ${additionalKeywords.join(', ')}`,
      category: 'preferred',
      keywords: additionalKeywords.map(k => k.toLowerCase()),
      matchedBulletIds: [],
      matchedEntryIds: [],
      coverageStatus: 'missing' as const,
    });
  }

  return {
    id: uuid(),
    originalJobDescriptionId: jobDescription.id,
    title: jobDescription.title,
    company: jobDescription.company,
    requirements,
    parsedAt: new Date().toISOString(),
    rawText: jobDescription.description,
  };
}

/**
 * Generate a coaching message based on current state.
 */
export async function generateCoachingMessage(
  requirement: JDRequirement,
  resume: Resume,
  variant: ResumeVariant,
  conversationHistory: FitCoachMessage[],
  apiKey: string
): Promise<FitCoachMessage> {
  // Get relevant resume content
  const relevantBullets = getRelevantBullets(resume, variant, requirement);

  const systemPrompt = `You are a resume Fit Coach helping someone improve their resume for a specific job. Your role is to guide and coach, never to write content for them.

Guidelines:
- Be encouraging but honest
- Ask ONE focused question at a time
- Help the user recall specific accomplishments, metrics, technologies used
- NEVER write bullets for them - coach them to write their own
- Suggest what TYPE of content would help, not the exact words
- Keep responses to 2-3 sentences`;

  const userPrompt = `REQUIREMENT TO ADDRESS:
"${requirement.text}"
Category: ${requirement.category}
Keywords to include: ${requirement.keywords.join(', ')}
Current status: ${requirement.coverageStatus}

RELEVANT RESUME CONTENT:
${relevantBullets.map(b => `- ${b}`).join('\n') || 'None found'}

CONVERSATION HISTORY:
${conversationHistory.slice(-6).map(m => `${m.role}: ${m.content}`).join('\n')}

Based on the above, provide coaching guidance. If the resume already covers this well, acknowledge it. If partially covered, ask probing questions. If missing, help them think of relevant experiences.`;

  try {
    const response = await fetch(CLAUDE_API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': apiKey,
        'anthropic-version': ANTHROPIC_VERSION,
      },
      body: JSON.stringify({
        model: CLAUDE_MODEL,
        max_tokens: 500,
        system: systemPrompt,
        messages: [{ role: 'user', content: userPrompt }],
      }),
    });

    if (!response.ok) {
      throw new Error(`Claude API error: ${response.status}`);
    }

    const data: ClaudeResponse = await response.json();
    const text = data.content[0]?.text || '';

    return {
      id: uuid(),
      role: 'coach',
      content: text.trim(),
      timestamp: new Date().toISOString(),
      relatedRequirementId: requirement.id,
    };
  } catch (error) {
    console.error('Failed to generate coaching message:', error);
    return mockGenerateCoachingMessage(requirement, relevantBullets);
  }
}

/**
 * Mock coaching message generator.
 */
export function mockGenerateCoachingMessage(
  requirement: JDRequirement,
  relevantBullets: string[]
): FitCoachMessage {
  let content: string;

  if (requirement.coverageStatus === 'strong') {
    content = `Great news! Your resume already addresses "${requirement.text}" well. The keywords ${requirement.keywords.slice(0, 2).join(' and ')} appear in your experience. Consider if you have any quantifiable metrics to strengthen this further.`;
  } else if (requirement.coverageStatus === 'partial') {
    content = `I see you have some experience related to "${requirement.text}". Can you tell me about a specific project where you used ${requirement.keywords[0] || 'this skill'}? What was the outcome or impact?`;
  } else if (relevantBullets.length > 0) {
    content = `I found some potentially relevant experience in your resume. Looking at "${relevantBullets[0].slice(0, 50)}...", could this be expanded to highlight ${requirement.keywords[0] || 'this requirement'}? What specific results did you achieve?`;
  } else {
    content = `The requirement "${requirement.text}" isn't clearly addressed yet. Have you had any experience with ${requirement.keywords.slice(0, 2).join(' or ')}? Even projects from a different context might be relevant.`;
  }

  return {
    id: uuid(),
    role: 'coach',
    content,
    timestamp: new Date().toISOString(),
    relatedRequirementId: requirement.id,
  };
}

/**
 * Analyze coverage of requirements against resume.
 */
export function analyzeCoverage(
  parsedJD: ParsedJobDescription,
  resume: Resume,
  variant: ResumeVariant
): ParsedJobDescription {
  const updatedRequirements = parsedJD.requirements.map(req => {
    const { matchedBulletIds, matchedEntryIds, strength } = findMatches(
      req,
      resume,
      variant
    );

    let coverageStatus: 'strong' | 'partial' | 'missing' | 'not-me' = 'missing';
    if (req.coverageStatus === 'not-me') {
      coverageStatus = 'not-me';
    } else if (strength >= 0.7) {
      coverageStatus = 'strong';
    } else if (strength >= 0.3) {
      coverageStatus = 'partial';
    }

    return {
      ...req,
      matchedBulletIds,
      matchedEntryIds,
      coverageStatus,
    };
  });

  return {
    ...parsedJD,
    requirements: updatedRequirements,
  };
}

/**
 * Calculate overall fit score from requirements.
 */
export function calculateFitScore(requirements: JDRequirement[]): {
  score: number;
  breakdown: { strong: number; partial: number; missing: number; notMe: number };
} {
  const breakdown = {
    strong: 0,
    partial: 0,
    missing: 0,
    notMe: 0,
  };

  // Weight by category
  const weights = {
    required: 3,
    preferred: 2,
    'nice-to-have': 1,
  };

  let totalWeight = 0;
  let earnedPoints = 0;

  for (const req of requirements) {
    const weight = weights[req.category];
    totalWeight += weight;

    switch (req.coverageStatus) {
      case 'strong':
        earnedPoints += weight;
        breakdown.strong++;
        break;
      case 'partial':
        earnedPoints += weight * 0.5;
        breakdown.partial++;
        break;
      case 'not-me':
        // Not counted against, but not for either
        totalWeight -= weight;
        breakdown.notMe++;
        break;
      default:
        breakdown.missing++;
    }
  }

  const score = totalWeight > 0 ? Math.round((earnedPoints / totalWeight) * 100) : 0;

  return { score, breakdown };
}

// Helper functions

function extractKeywordsFromText(text: string): string[] {
  // Common tech keywords to look for
  const techTerms = [
    'javascript', 'typescript', 'python', 'java', 'c++', 'go', 'rust', 'ruby',
    'react', 'vue', 'angular', 'node', 'express', 'django', 'flask', 'spring',
    'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'terraform',
    'sql', 'nosql', 'postgresql', 'mysql', 'mongodb', 'redis',
    'agile', 'scrum', 'ci/cd', 'devops', 'microservices',
    'machine learning', 'ml', 'ai', 'data science',
    'leadership', 'management', 'mentoring', 'communication',
  ];

  const lowerText = text.toLowerCase();
  const foundTerms = techTerms.filter(term => lowerText.includes(term));

  // Also extract years of experience patterns
  const yearsMatch = text.match(/(\d+)\+?\s*years?/i);
  if (yearsMatch) {
    foundTerms.push(`${yearsMatch[1]}+ years`);
  }

  return foundTerms;
}

function getRelevantBullets(resume: Resume, variant: ResumeVariant, requirement: JDRequirement): string[] {
  const bullets: string[] = [];

  for (const section of resume.sections) {
    for (const entry of section.entries) {
      if (!variant.includedEntryIds.includes(entry.id)) continue;

      const collectBullets = (nodes: ContentNode[]) => {
        for (const node of nodes) {
          if (variant.includedBulletIds.includes(node.id)) {
            // Check if any keyword matches
            const lowerText = node.text.toLowerCase();
            if (requirement.keywords.some(kw => lowerText.includes(kw.toLowerCase()))) {
              bullets.push(node.text);
            }
          }
          if (node.children) {
            collectBullets(node.children);
          }
        }
      };

      collectBullets(entry.content);
    }
  }

  return bullets;
}

function findMatches(
  requirement: JDRequirement,
  resume: Resume,
  variant: ResumeVariant
): { matchedBulletIds: string[]; matchedEntryIds: string[]; strength: number } {
  const matchedBulletIds: string[] = [];
  const matchedEntryIds: Set<string> = new Set();
  let totalKeywords = requirement.keywords.length;
  let matchedKeywords = 0;

  if (totalKeywords === 0) {
    totalKeywords = 1; // Avoid division by zero
  }

  for (const section of resume.sections) {
    for (const entry of section.entries) {
      if (!variant.includedEntryIds.includes(entry.id)) continue;

      const searchInNodes = (nodes: ContentNode[]) => {
        for (const node of nodes) {
          if (!variant.includedBulletIds.includes(node.id)) continue;

          const lowerText = node.text.toLowerCase();
          let hasMatch = false;

          for (const keyword of requirement.keywords) {
            if (lowerText.includes(keyword.toLowerCase())) {
              hasMatch = true;
              matchedKeywords++;
            }
          }

          if (hasMatch) {
            matchedBulletIds.push(node.id);
            matchedEntryIds.add(entry.id);
          }

          if (node.children) {
            searchInNodes(node.children);
          }
        }
      };

      // Also search in entry metadata
      const entryText = `${entry.organization} ${entry.role}`.toLowerCase();
      for (const keyword of requirement.keywords) {
        if (entryText.includes(keyword.toLowerCase())) {
          matchedEntryIds.add(entry.id);
          matchedKeywords++;
        }
      }

      searchInNodes(entry.content);
    }
  }

  const strength = Math.min(1, matchedKeywords / totalKeywords);

  return {
    matchedBulletIds,
    matchedEntryIds: Array.from(matchedEntryIds),
    strength,
  };
}

/**
 * Check if Claude API key is configured.
 */
export function hasApiKey(): boolean {
  return !!getApiKey();
}

/**
 * Get API key from localStorage.
 */
export function getApiKey(): string | null {
  return localStorage.getItem('claude-api-key');
}

/**
 * Set API key in localStorage.
 */
export function setApiKey(key: string): void {
  localStorage.setItem('claude-api-key', key);
}
