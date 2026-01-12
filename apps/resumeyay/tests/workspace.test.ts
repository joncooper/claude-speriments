import { describe, test, expect, beforeEach } from 'bun:test';
import {
  createSampleResume,
  createWorkspace,
  createDefaultVariant,
} from '../src/store';
import type { Resume, ResumeWorkspace, ResumeVariant, JobDescription } from '../src/types';

describe('Workspace Functions', () => {
  let sampleResume: Resume;

  beforeEach(() => {
    sampleResume = createSampleResume();
  });

  test('createDefaultVariant creates a variant with all entries included', () => {
    const variant = createDefaultVariant(sampleResume);

    expect(variant.id).toBeDefined();
    expect(variant.name).toBe('Master Resume');
    expect(variant.isDefault).toBe(true);
    expect(variant.snapshots).toHaveLength(0);

    // Should include all entry IDs
    let expectedEntryCount = 0;
    for (const section of sampleResume.sections) {
      expectedEntryCount += section.entries.length;
    }
    expect(variant.includedEntryIds.length).toBe(expectedEntryCount);
  });

  test('createWorkspace creates workspace with content pool and default variant', () => {
    const workspace = createWorkspace(sampleResume);

    expect(workspace.id).toBeDefined();
    expect(workspace.contentPool).toBeDefined();
    expect(workspace.contentPool.header.name).toBe('Jon Cooper');
    expect(workspace.variants).toHaveLength(1);
    expect(workspace.variants[0].isDefault).toBe(true);
    expect(workspace.activeVariantId).toBe(workspace.variants[0].id);
    expect(workspace.jobDescriptions).toHaveLength(0);
    expect(workspace.analyses).toHaveLength(0);
  });
});

describe('Variant Types', () => {
  test('ResumeVariant has required fields', () => {
    const variant: ResumeVariant = {
      id: 'test-variant',
      name: 'Test Variant',
      targetRole: 'Engineering Manager',
      targetCompany: 'Tech Corp',
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      includedEntryIds: ['entry-1', 'entry-2'],
      includedBulletIds: ['bullet-1', 'bullet-2', 'bullet-3'],
      snapshots: [],
    };

    expect(variant.id).toBe('test-variant');
    expect(variant.name).toBe('Test Variant');
    expect(variant.targetRole).toBe('Engineering Manager');
    expect(variant.targetCompany).toBe('Tech Corp');
    expect(variant.includedEntryIds).toHaveLength(2);
    expect(variant.includedBulletIds).toHaveLength(3);
  });

  test('JobDescription has required fields', () => {
    const job: JobDescription = {
      id: 'test-job',
      title: 'Senior Software Engineer',
      company: 'ACME Inc',
      description: 'We are looking for a talented engineer...',
      requirements: ['5+ years experience', 'Python', 'AWS'],
      keywords: ['python', 'aws', 'docker', 'kubernetes'],
      url: 'https://example.com/jobs/123',
      createdAt: new Date().toISOString(),
    };

    expect(job.id).toBe('test-job');
    expect(job.title).toBe('Senior Software Engineer');
    expect(job.company).toBe('ACME Inc');
    expect(job.requirements).toHaveLength(3);
    expect(job.keywords).toHaveLength(4);
  });
});

describe('Resume DNA Architecture', () => {
  test('workspace separates content pool from variants', () => {
    const resume = createSampleResume();
    const workspace = createWorkspace(resume);

    // Content pool is the full resume
    expect(workspace.contentPool.header.name).toBe('Jon Cooper');
    expect(workspace.contentPool.sections.length).toBeGreaterThan(0);

    // Variants reference content by ID, not copy
    const variant = workspace.variants[0];
    expect(variant.includedEntryIds.length).toBeGreaterThan(0);

    // IDs in variant should match IDs in content pool
    const firstEntryId = variant.includedEntryIds[0];
    const foundInPool = workspace.contentPool.sections.some(
      section => section.entries.some(entry => entry.id === firstEntryId)
    );
    expect(foundInPool).toBe(true);
  });

  test('multiple variants can coexist with different selections', () => {
    const resume = createSampleResume();
    const workspace = createWorkspace(resume);

    // Add a second variant manually (simulating what WorkspaceStore.createVariant would do)
    const secondVariant: ResumeVariant = {
      id: 'variant-2',
      name: 'Tech Focus',
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      includedEntryIds: workspace.variants[0].includedEntryIds.slice(0, 2), // Only first 2 entries
      includedBulletIds: workspace.variants[0].includedBulletIds.slice(0, 5), // Only first 5 bullets
      snapshots: [],
    };

    workspace.variants.push(secondVariant);

    expect(workspace.variants).toHaveLength(2);
    expect(workspace.variants[0].includedEntryIds.length).toBeGreaterThan(
      workspace.variants[1].includedEntryIds.length
    );
  });

  test('snapshots preserve variant state at a point in time', () => {
    const resume = createSampleResume();
    const variant = createDefaultVariant(resume);

    // Create a snapshot
    const snapshot = {
      id: 'snapshot-1',
      name: 'Initial Version',
      createdAt: new Date().toISOString(),
      includedEntryIds: [...variant.includedEntryIds],
      includedBulletIds: [...variant.includedBulletIds],
    };

    variant.snapshots.push(snapshot);

    // Modify the variant
    variant.includedEntryIds = variant.includedEntryIds.slice(0, 1);

    // Snapshot should preserve original state
    expect(variant.includedEntryIds.length).toBe(1);
    expect(snapshot.includedEntryIds.length).toBeGreaterThan(1);
  });
});

describe('Keyword Extraction', () => {
  test('job description keywords can be manually specified', () => {
    const job: JobDescription = {
      id: 'test-job',
      title: 'Tech Lead',
      company: 'Startup Inc',
      description: 'Looking for a technical leader',
      requirements: [],
      keywords: ['leadership', 'python', 'aws', 'team management'],
      createdAt: new Date().toISOString(),
    };

    expect(job.keywords).toContain('leadership');
    expect(job.keywords).toContain('python');
    expect(job.keywords).toContain('aws');
  });
});

describe('Analysis Types', () => {
  test('ResumeAnalysis structure for job matching', () => {
    const analysis = {
      id: 'analysis-1',
      variantId: 'variant-1',
      jobDescriptionId: 'job-1',
      createdAt: new Date().toISOString(),
      overallScore: 75,
      keywordMatches: [
        { keyword: 'python', found: true, inEntryIds: ['entry-1'], importance: 'high' as const },
        { keyword: 'java', found: false, inEntryIds: [], importance: 'medium' as const },
      ],
      suggestions: [
        {
          id: 'suggestion-1',
          type: 'add' as const,
          reason: 'Consider adding Java experience',
          priority: 'medium' as const,
        },
      ],
      missingSkills: ['java'],
      strongPoints: ['Strong Python background'],
    };

    expect(analysis.overallScore).toBe(75);
    expect(analysis.keywordMatches).toHaveLength(2);
    expect(analysis.keywordMatches[0].found).toBe(true);
    expect(analysis.keywordMatches[1].found).toBe(false);
    expect(analysis.suggestions).toHaveLength(1);
    expect(analysis.missingSkills).toContain('java');
  });

  test('suggestions have actionable types', () => {
    const suggestionTypes: Array<'add' | 'modify' | 'remove' | 'reorder'> = ['add', 'modify', 'remove', 'reorder'];

    suggestionTypes.forEach(type => {
      const suggestion = {
        id: `suggestion-${type}`,
        type,
        reason: `Test ${type} suggestion`,
        priority: 'high' as const,
      };
      expect(suggestion.type).toBe(type);
    });
  });
});
