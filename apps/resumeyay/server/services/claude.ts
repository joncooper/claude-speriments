/**
 * Claude Service
 *
 * Server-side Claude API integration for:
 * - Job description parsing
 * - Fit coaching conversations
 * - Coverage analysis
 */

import type {
  JDRequirement,
  FitCoachMessage,
  ParsedJobDescription,
  JobDescription,
  Resume,
  ResumeVariant,
  ContentNode,
} from '../../src/types';
import { v4 as uuid } from 'uuid';

// Configuration
const CLAUDE_API_URL = 'https://api.anthropic.com/v1/messages';
const CLAUDE_MODEL = 'claude-sonnet-4-20250514';
const ANTHROPIC_VERSION = '2023-06-01';

// Get API key from environment
function getApiKey(): string {
  const key = process.env.ANTHROPIC_API_KEY;
  if (!key) {
    throw new Error('ANTHROPIC_API_KEY not configured');
  }
  return key;
}

interface ClaudeResponse {
  content: Array<{
    type: string;
    text: string;
  }>;
}

/**
 * Parse a job description into structured requirements
 */
export async function parseJobDescription(
  jobDescription: JobDescription
): Promise<ParsedJobDescription> {
  const apiKey = getApiKey();

  const prompt = `Analyze this job description and extract ALL requirements.

JOB TITLE: ${jobDescription.title}
COMPANY: ${jobDescription.company}

JOB DESCRIPTION:
${jobDescription.description}

Extract every requirement, qualification, skill, and experience mentioned. Categorize them and extract searchable keywords.

Return ONLY valid JSON in this exact format:
{
  "requirements": [
    {
      "text": "Full requirement description as stated or implied",
      "category": "required" | "preferred" | "nice-to-have",
      "keywords": ["searchable", "keywords", "for", "matching"]
    }
  ]
}

Guidelines:
- "required" = explicitly required, must-have, mandatory
- "preferred" = strongly desired, preferred, should have
- "nice-to-have" = bonus, plus, would be nice
- Extract EVERY requirement, even implied ones
- Include years of experience as requirements
- Include soft skills and leadership qualities
- Keywords should be specific and searchable (e.g., "React", "5+ years", "team lead")`;

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
      const error = await response.text();
      throw new Error(`Claude API error: ${response.status} ${error}`);
    }

    const data: ClaudeResponse = await response.json();
    const text = data.content[0]?.text || '{}';

    // Extract JSON from response
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
    // Fall back to basic parsing
    return basicParseJobDescription(jobDescription);
  }
}

/**
 * Basic job description parser (fallback when API fails)
 */
function basicParseJobDescription(jobDescription: JobDescription): ParsedJobDescription {
  const requirements: JDRequirement[] = jobDescription.requirements.map((req, index) => ({
    id: uuid(),
    text: req,
    category: index < 3 ? 'required' : index < 6 ? 'preferred' : 'nice-to-have',
    keywords: extractKeywordsFromText(req),
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
}

/**
 * Generate a coaching message for a specific requirement
 */
export async function generateCoachingMessage(
  requirement: JDRequirement,
  resume: Resume,
  variant: ResumeVariant,
  conversationHistory: FitCoachMessage[]
): Promise<FitCoachMessage> {
  const apiKey = getApiKey();
  const relevantBullets = getRelevantBullets(resume, variant, requirement);

  const systemPrompt = `You are a resume Fit Coach helping someone improve their resume for a specific job. Your role is to guide and coach, never to write content for them.

Guidelines:
- Be encouraging but honest
- Ask ONE focused question at a time
- Help the user recall specific accomplishments, metrics, technologies used
- NEVER write bullets for them - coach them to write their own
- Suggest what TYPE of content would help, not the exact words
- Keep responses to 2-3 sentences
- If they mention an experience, ask follow-up questions about impact, scale, technologies`;

  const userPrompt = `REQUIREMENT TO ADDRESS:
"${requirement.text}"
Category: ${requirement.category}
Keywords to include: ${requirement.keywords.join(', ')}
Current coverage status: ${requirement.coverageStatus}

RELEVANT RESUME CONTENT FOUND:
${relevantBullets.length > 0 ? relevantBullets.map(b => `- ${b}`).join('\n') : 'None found - this is a gap'}

CONVERSATION HISTORY:
${conversationHistory.slice(-6).map(m => `${m.role === 'coach' ? 'Coach' : 'User'}: ${m.content}`).join('\n')}

Provide coaching guidance. If the resume already covers this well, acknowledge it and suggest refinements. If partially covered, ask probing questions. If missing, help them think of relevant experiences they might have forgotten.`;

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
    return generateFallbackCoachingMessage(requirement, relevantBullets);
  }
}

/**
 * Fallback coaching message when API fails
 */
function generateFallbackCoachingMessage(
  requirement: JDRequirement,
  relevantBullets: string[]
): FitCoachMessage {
  let content: string;

  if (requirement.coverageStatus === 'strong') {
    content = `Your resume addresses "${requirement.text}" well. Consider adding specific metrics or outcomes to make it even stronger.`;
  } else if (requirement.coverageStatus === 'partial') {
    content = `You have some experience related to "${requirement.text}". Can you tell me about a specific project where you demonstrated ${requirement.keywords[0] || 'this skill'}? What was the impact?`;
  } else if (relevantBullets.length > 0) {
    content = `I found some potentially relevant experience. Could "${relevantBullets[0].slice(0, 60)}..." be expanded to address ${requirement.keywords[0] || 'this requirement'}?`;
  } else {
    content = `The requirement "${requirement.text}" isn't clearly addressed. Have you had any experience with ${requirement.keywords.slice(0, 2).join(' or ')}? Even from side projects or different contexts?`;
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
 * Clean and structure a messy job description
 */
export async function cleanJobDescription(rawText: string): Promise<{
  title: string;
  company: string;
  description: string;
  requirements: string[];
  keywords: string[];
}> {
  const apiKey = getApiKey();

  const prompt = `Clean and structure this job posting. Extract the key information.

RAW JOB POSTING:
${rawText}

Return ONLY valid JSON:
{
  "title": "Job title",
  "company": "Company name",
  "description": "Clean description of the role and responsibilities",
  "requirements": ["requirement 1", "requirement 2", ...],
  "keywords": ["skill1", "skill2", "technology1", ...]
}

Guidelines:
- Extract the actual job title (not internal codes)
- Identify the company name
- Clean up the description (remove HTML, weird formatting)
- List each requirement as a separate item
- Extract all mentioned technologies, skills, qualifications as keywords`;

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
        max_tokens: 2048,
        messages: [{ role: 'user', content: prompt }],
      }),
    });

    if (!response.ok) {
      throw new Error(`Claude API error: ${response.status}`);
    }

    const data: ClaudeResponse = await response.json();
    const text = data.content[0]?.text || '{}';

    const jsonMatch = text.match(/\{[\s\S]*\}/);
    return JSON.parse(jsonMatch?.[0] || '{}');
  } catch (error) {
    console.error('Failed to clean job description:', error);
    // Return basic structure
    return {
      title: 'Untitled Position',
      company: 'Unknown Company',
      description: rawText,
      requirements: [],
      keywords: [],
    };
  }
}

// ============================================================================
// HELPER FUNCTIONS
// ============================================================================

function extractKeywordsFromText(text: string): string[] {
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

  const yearsMatch = text.match(/(\d+)\+?\s*years?/i);
  if (yearsMatch) {
    foundTerms.push(`${yearsMatch[1]}+ years`);
  }

  return foundTerms;
}

function getRelevantBullets(
  resume: Resume,
  variant: ResumeVariant,
  requirement: JDRequirement
): string[] {
  const bullets: string[] = [];

  for (const section of resume.sections) {
    for (const entry of section.entries) {
      if (!variant.includedEntryIds.includes(entry.id)) continue;

      const collectBullets = (nodes: ContentNode[]) => {
        for (const node of nodes) {
          if (variant.includedBulletIds.includes(node.id)) {
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

/**
 * Analyze coverage of requirements against resume
 */
export function analyzeCoverage(
  parsedJD: ParsedJobDescription,
  resume: Resume,
  variant: ResumeVariant
): ParsedJobDescription {
  const updatedRequirements = parsedJD.requirements.map(req => {
    const { matchedBulletIds, matchedEntryIds, strength } = findMatches(req, resume, variant);

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

function findMatches(
  requirement: JDRequirement,
  resume: Resume,
  variant: ResumeVariant
): { matchedBulletIds: string[]; matchedEntryIds: string[]; strength: number } {
  const matchedBulletIds: string[] = [];
  const matchedEntryIds: Set<string> = new Set();
  let totalKeywords = requirement.keywords.length || 1;
  let matchedKeywords = 0;

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

  return {
    matchedBulletIds,
    matchedEntryIds: Array.from(matchedEntryIds),
    strength: Math.min(1, matchedKeywords / totalKeywords),
  };
}

/**
 * Calculate fit score from requirements
 */
export function calculateFitScore(requirements: JDRequirement[]): {
  score: number;
  breakdown: { strong: number; partial: number; missing: number; notMe: number };
} {
  const breakdown = { strong: 0, partial: 0, missing: 0, notMe: 0 };
  const weights = { required: 3, preferred: 2, 'nice-to-have': 1 };

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
