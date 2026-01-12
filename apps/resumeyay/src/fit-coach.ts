/**
 * Fit Coach Module - Coverage Grid UI and Coaching Flow
 *
 * Provides visual feedback on how well a resume matches a job description,
 * with an interactive coaching conversation to improve coverage.
 */

import type {
  FitSession,
  FitCoachMessage,
  ParsedJobDescription,
  JobDescription,
  HeatMapHighlight,
  Resume,
  ResumeVariant,
} from './types';
import {
  mockParseJobDescription,
  parseJobDescription,
  mockGenerateCoachingMessage,
  generateCoachingMessage,
  analyzeCoverage,
  calculateFitScore,
  getApiKey,
  setApiKey,
} from './claude-client';
import { v4 as uuid } from 'uuid';

// ============================================================================
// FIT COACH STORE
// ============================================================================

interface FitCoachState {
  activeFitSession: FitSession | null;
  parsedJobDescriptions: Map<string, ParsedJobDescription>;
  heatMapHighlights: HeatMapHighlight[];
  showHeatMap: boolean;
  isCoachPanelOpen: boolean;
  isLoading: boolean;
  selectedRequirementId: string | null;
}

type FitCoachListener = () => void;

class FitCoachStore {
  private state: FitCoachState = {
    activeFitSession: null,
    parsedJobDescriptions: new Map(),
    heatMapHighlights: [],
    showHeatMap: true,
    isCoachPanelOpen: false,
    isLoading: false,
    selectedRequirementId: null,
  };

  private listeners: Set<FitCoachListener> = new Set();

  subscribe(listener: FitCoachListener): () => void {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  }

  private notify(): void {
    this.listeners.forEach(l => l());
  }

  getState(): FitCoachState {
    return this.state;
  }

  // Panel visibility
  toggleCoachPanel(): void {
    this.state = {
      ...this.state,
      isCoachPanelOpen: !this.state.isCoachPanelOpen,
    };
    this.notify();
  }

  closeCoachPanel(): void {
    this.state = {
      ...this.state,
      isCoachPanelOpen: false,
    };
    this.notify();
  }

  // Heat map
  toggleHeatMap(): void {
    this.state = {
      ...this.state,
      showHeatMap: !this.state.showHeatMap,
    };
    this.notify();
  }

  setHeatMapHighlights(highlights: HeatMapHighlight[]): void {
    this.state = {
      ...this.state,
      heatMapHighlights: highlights,
    };
    this.notify();
  }

  // Requirement selection
  selectRequirement(requirementId: string | null): void {
    this.state = {
      ...this.state,
      selectedRequirementId: requirementId,
    };
    this.notify();
  }

  // Job description parsing
  async parseJob(jobDescription: JobDescription, resume: Resume, variant: ResumeVariant): Promise<ParsedJobDescription> {
    this.state = { ...this.state, isLoading: true };
    this.notify();

    let parsed: ParsedJobDescription;
    const apiKey = getApiKey();

    if (apiKey) {
      parsed = await parseJobDescription(jobDescription, apiKey);
    } else {
      parsed = mockParseJobDescription(jobDescription);
    }

    // Analyze coverage against resume
    parsed = analyzeCoverage(parsed, resume, variant);

    // Store parsed job
    this.state.parsedJobDescriptions.set(jobDescription.id, parsed);

    // Update heat map highlights
    const highlights = this.generateHeatMapHighlights(parsed, resume, variant);

    this.state = {
      ...this.state,
      heatMapHighlights: highlights,
      isLoading: false,
    };
    this.notify();

    return parsed;
  }

  // Start a new fit session
  async startFitSession(
    jobDescription: JobDescription,
    resume: Resume,
    variant: ResumeVariant
  ): Promise<FitSession> {
    this.state = { ...this.state, isLoading: true };
    this.notify();

    // Parse job if not already parsed
    let parsed = this.state.parsedJobDescriptions.get(jobDescription.id);
    if (!parsed) {
      parsed = await this.parseJob(jobDescription, resume, variant);
    }

    const { score, breakdown } = calculateFitScore(parsed.requirements);

    const session: FitSession = {
      id: uuid(),
      jobDescriptionId: jobDescription.id,
      variantId: variant.id,
      requirements: parsed.requirements,
      conversationHistory: [],
      overallFitScore: score,
      coverageBreakdown: breakdown,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      isActive: true,
    };

    // Generate initial coaching message
    const firstMissing = session.requirements.find(r => r.coverageStatus === 'missing');
    if (firstMissing) {
      const apiKey = getApiKey();
      let coachMessage: FitCoachMessage;

      if (apiKey) {
        coachMessage = await generateCoachingMessage(firstMissing, resume, variant, [], apiKey);
      } else {
        coachMessage = mockGenerateCoachingMessage(firstMissing, []);
      }

      session.conversationHistory.push({
        id: uuid(),
        role: 'coach',
        content: `Welcome to Fit Coach! Let's work together to improve your resume's fit for this role.\n\nYour current score is ${score}% with ${breakdown.strong} strong matches, ${breakdown.partial} partial matches, and ${breakdown.missing} gaps.\n\nLet's start with the first gap...`,
        timestamp: new Date().toISOString(),
      });
      session.conversationHistory.push(coachMessage);
    } else {
      session.conversationHistory.push({
        id: uuid(),
        role: 'coach',
        content: `Great news! Your resume already has strong coverage for this role with a ${score}% match score. You can still review each requirement and refine your wording if needed.`,
        timestamp: new Date().toISOString(),
      });
    }

    this.state = {
      ...this.state,
      activeFitSession: session,
      isLoading: false,
      isCoachPanelOpen: true,
    };
    this.notify();

    return session;
  }

  // Send user message and get coaching response
  async sendMessage(
    message: string,
    resume: Resume,
    variant: ResumeVariant
  ): Promise<void> {
    if (!this.state.activeFitSession) return;

    const session = this.state.activeFitSession;

    // Add user message
    const userMessage: FitCoachMessage = {
      id: uuid(),
      role: 'user',
      content: message,
      timestamp: new Date().toISOString(),
      relatedRequirementId: this.state.selectedRequirementId || undefined,
    };
    session.conversationHistory.push(userMessage);

    this.state = {
      ...this.state,
      activeFitSession: { ...session },
      isLoading: true,
    };
    this.notify();

    // Get coaching response
    const relatedReq = this.state.selectedRequirementId
      ? session.requirements.find(r => r.id === this.state.selectedRequirementId)
      : session.requirements.find(r => r.coverageStatus === 'missing' || r.coverageStatus === 'partial');

    if (relatedReq) {
      const apiKey = getApiKey();
      let coachMessage: FitCoachMessage;

      if (apiKey) {
        coachMessage = await generateCoachingMessage(
          relatedReq,
          resume,
          variant,
          session.conversationHistory,
          apiKey
        );
      } else {
        coachMessage = mockGenerateCoachingMessage(relatedReq, []);
      }

      session.conversationHistory.push(coachMessage);
    }

    this.state = {
      ...this.state,
      activeFitSession: {
        ...session,
        updatedAt: new Date().toISOString(),
      },
      isLoading: false,
    };
    this.notify();
  }

  // Mark requirement as "Not me"
  markNotMe(requirementId: string, reason?: string): void {
    if (!this.state.activeFitSession) return;

    const session = this.state.activeFitSession;
    const req = session.requirements.find(r => r.id === requirementId);
    if (req) {
      req.coverageStatus = 'not-me';
      req.notMeReason = reason;
    }

    // Recalculate score
    const { score, breakdown } = calculateFitScore(session.requirements);

    this.state = {
      ...this.state,
      activeFitSession: {
        ...session,
        overallFitScore: score,
        coverageBreakdown: breakdown,
        updatedAt: new Date().toISOString(),
      },
    };
    this.notify();
  }

  // Update requirement status
  updateRequirementStatus(
    requirementId: string,
    status: 'strong' | 'partial' | 'missing' | 'not-me'
  ): void {
    if (!this.state.activeFitSession) return;

    const session = this.state.activeFitSession;
    const req = session.requirements.find(r => r.id === requirementId);
    if (req) {
      req.coverageStatus = status;
    }

    // Recalculate score
    const { score, breakdown } = calculateFitScore(session.requirements);

    this.state = {
      ...this.state,
      activeFitSession: {
        ...session,
        overallFitScore: score,
        coverageBreakdown: breakdown,
        updatedAt: new Date().toISOString(),
      },
    };
    this.notify();
  }

  // Refresh coverage analysis
  refreshCoverage(resume: Resume, variant: ResumeVariant): void {
    if (!this.state.activeFitSession) return;

    const session = this.state.activeFitSession;
    const parsed = this.state.parsedJobDescriptions.get(session.jobDescriptionId);
    if (!parsed) return;

    // Re-analyze coverage
    const updated = analyzeCoverage(parsed, resume, variant);

    // Preserve "not-me" statuses
    for (const req of updated.requirements) {
      const existing = session.requirements.find(r => r.id === req.id);
      if (existing?.coverageStatus === 'not-me') {
        req.coverageStatus = 'not-me';
        req.notMeReason = existing.notMeReason;
      }
    }

    const { score, breakdown } = calculateFitScore(updated.requirements);
    const highlights = this.generateHeatMapHighlights(updated, resume, variant);

    this.state = {
      ...this.state,
      activeFitSession: {
        ...session,
        requirements: updated.requirements,
        overallFitScore: score,
        coverageBreakdown: breakdown,
        updatedAt: new Date().toISOString(),
      },
      heatMapHighlights: highlights,
    };
    this.notify();
  }

  // Generate heat map highlights from parsed requirements
  private generateHeatMapHighlights(
    parsed: ParsedJobDescription,
    _resume: Resume,
    _variant: ResumeVariant
  ): HeatMapHighlight[] {
    const highlights: HeatMapHighlight[] = [];
    const bulletMap = new Map<string, HeatMapHighlight>();

    for (const req of parsed.requirements) {
      for (const bulletId of req.matchedBulletIds) {
        const existing = bulletMap.get(bulletId);
        if (existing) {
          existing.keywords.push(...req.keywords);
          existing.requirementIds.push(req.id);
          // Upgrade strength if needed
          if (req.category === 'required' && existing.matchStrength !== 'high') {
            existing.matchStrength = 'high';
          }
        } else {
          bulletMap.set(bulletId, {
            bulletId,
            keywords: [...req.keywords],
            matchStrength: req.category === 'required' ? 'high' : req.category === 'preferred' ? 'medium' : 'low',
            requirementIds: [req.id],
          });
        }
      }
    }

    bulletMap.forEach(h => highlights.push(h));
    return highlights;
  }

  // End fit session
  endSession(): void {
    this.state = {
      ...this.state,
      activeFitSession: null,
      heatMapHighlights: [],
      selectedRequirementId: null,
    };
    this.notify();
  }

  // API Key management
  hasApiKey(): boolean {
    return !!getApiKey();
  }

  setApiKey(key: string): void {
    setApiKey(key);
  }
}

// Export singleton
export const fitCoachStore = new FitCoachStore();

// ============================================================================
// RENDER FUNCTIONS
// ============================================================================

function escapeHtml(text: string): string {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

function getCoverageIcon(status: 'strong' | 'partial' | 'missing' | 'not-me'): string {
  switch (status) {
    case 'strong': return '&#10003;'; // ✓
    case 'partial': return '&#9679;'; // ●
    case 'missing': return '&#10007;'; // ✗
    case 'not-me': return '&#8709;'; // ∅
  }
}

function getCoverageClass(status: 'strong' | 'partial' | 'missing' | 'not-me'): string {
  return `coverage-${status}`;
}

export function renderFitCoachPanel(): string {
  const state = fitCoachStore.getState();
  if (!state.isCoachPanelOpen) return '';

  const session = state.activeFitSession;

  if (!session) {
    return `
      <div class="panel-overlay fit-coach-panel-overlay">
        <div class="panel fit-coach-panel">
          <div class="panel-header">
            <h2>Fit Coach</h2>
            <button class="btn-close-panel" data-panel="fit-coach">&times;</button>
          </div>
          <div class="panel-content fit-coach-setup">
            <div class="fit-coach-intro">
              <h3>Welcome to Fit Coach</h3>
              <p>Fit Coach helps you tailor your resume to specific job descriptions by:</p>
              <ul>
                <li>Parsing job requirements automatically</li>
                <li>Showing coverage gaps with a visual grid</li>
                <li>Highlighting matching keywords in your resume</li>
                <li>Coaching you through improvements</li>
              </ul>
            </div>
            <div class="fit-coach-api-key">
              <h4>Claude API Key (optional)</h4>
              <p>For AI-powered job parsing and coaching, enter your Claude API key:</p>
              <input type="password" id="claude-api-key" placeholder="Enter Claude API key..."
                     value="${fitCoachStore.hasApiKey() ? '••••••••••••' : ''}" />
              <button class="btn-secondary btn-save-api-key">Save Key</button>
              <p class="api-note">Without an API key, basic keyword matching will be used.</p>
            </div>
            <div class="fit-coach-start">
              <p>Select a job description from the Jobs panel and click "Start Fit Coach" to begin.</p>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  const { requirements, conversationHistory, overallFitScore, coverageBreakdown } = session;

  return `
    <div class="panel-overlay fit-coach-panel-overlay">
      <div class="panel fit-coach-panel fit-coach-active">
        <div class="panel-header">
          <h2>Fit Coach</h2>
          <div class="fit-coach-score">
            <span class="score-badge score-${getScoreClass(overallFitScore)}">${overallFitScore}%</span>
            <div class="score-breakdown">
              <span class="breakdown-item strong" title="Strong matches">${coverageBreakdown.strong}</span>
              <span class="breakdown-item partial" title="Partial matches">${coverageBreakdown.partial}</span>
              <span class="breakdown-item missing" title="Gaps">${coverageBreakdown.missing}</span>
              <span class="breakdown-item not-me" title="Not applicable">${coverageBreakdown.notMe}</span>
            </div>
          </div>
          <button class="btn-close-panel" data-panel="fit-coach">&times;</button>
        </div>
        <div class="panel-content fit-coach-content">
          <div class="coverage-grid">
            <h3>Coverage Grid</h3>
            <div class="requirements-list">
              ${requirements.map(req => `
                <div class="requirement-item ${getCoverageClass(req.coverageStatus)} ${state.selectedRequirementId === req.id ? 'selected' : ''}"
                     data-requirement-id="${req.id}">
                  <div class="requirement-status">
                    <span class="status-icon">${getCoverageIcon(req.coverageStatus)}</span>
                    <span class="category-badge category-${req.category}">${req.category}</span>
                  </div>
                  <div class="requirement-text">${escapeHtml(req.text)}</div>
                  <div class="requirement-keywords">
                    ${req.keywords.slice(0, 4).map(k => `<span class="keyword-tag small">${escapeHtml(k)}</span>`).join('')}
                    ${req.keywords.length > 4 ? `<span class="keyword-more">+${req.keywords.length - 4}</span>` : ''}
                  </div>
                  <div class="requirement-actions">
                    ${req.coverageStatus !== 'not-me' ? `
                      <button class="btn-icon btn-not-me" data-requirement-id="${req.id}" title="Mark as Not Me">&#8709;</button>
                    ` : `
                      <button class="btn-icon btn-undo-not-me" data-requirement-id="${req.id}" title="Undo Not Me">&#8634;</button>
                    `}
                    <button class="btn-icon btn-focus-req" data-requirement-id="${req.id}" title="Focus on this">&#10140;</button>
                  </div>
                  ${req.notMeReason ? `<div class="not-me-reason">${escapeHtml(req.notMeReason)}</div>` : ''}
                </div>
              `).join('')}
            </div>
          </div>
          <div class="coach-conversation">
            <h3>Coaching Conversation</h3>
            <div class="conversation-messages">
              ${conversationHistory.map(msg => `
                <div class="message message-${msg.role}">
                  <div class="message-avatar">${msg.role === 'coach' ? '🎯' : '👤'}</div>
                  <div class="message-content">${escapeHtml(msg.content)}</div>
                  ${msg.suggestedBullets ? `
                    <div class="suggested-bullets">
                      <p class="suggestion-label">Suggested formats:</p>
                      ${msg.suggestedBullets.map(b => `<p class="suggestion-item">"${escapeHtml(b)}"</p>`).join('')}
                    </div>
                  ` : ''}
                </div>
              `).join('')}
              ${state.isLoading ? `
                <div class="message message-coach loading">
                  <div class="message-avatar">🎯</div>
                  <div class="message-content">Thinking...</div>
                </div>
              ` : ''}
            </div>
            <div class="conversation-input">
              <textarea id="coach-message-input" placeholder="Type your response... (tell me about relevant experience, skills, or ask for guidance)" rows="3"></textarea>
              <button class="btn-primary btn-send-message" ${state.isLoading ? 'disabled' : ''}>Send</button>
            </div>
          </div>
        </div>
        <div class="panel-footer">
          <label class="heatmap-toggle">
            <input type="checkbox" id="show-heatmap" ${state.showHeatMap ? 'checked' : ''} />
            Show heat map in preview
          </label>
          <button class="btn-secondary btn-refresh-coverage">Refresh Coverage</button>
          <button class="btn-secondary btn-end-session">End Session</button>
        </div>
      </div>
    </div>
  `;
}

function getScoreClass(score: number): string {
  if (score >= 80) return 'excellent';
  if (score >= 60) return 'good';
  if (score >= 40) return 'fair';
  return 'poor';
}

// Heat map CSS class generator for preview bullets
export function getHeatMapClass(bulletId: string): string {
  const state = fitCoachStore.getState();
  if (!state.showHeatMap) return '';

  const highlight = state.heatMapHighlights.find(h => h.bulletId === bulletId);
  if (!highlight) return '';

  return `heatmap-${highlight.matchStrength}`;
}

// Check if a bullet is highlighted
export function isBulletHighlighted(bulletId: string): boolean {
  const state = fitCoachStore.getState();
  if (!state.showHeatMap) return false;
  return state.heatMapHighlights.some(h => h.bulletId === bulletId);
}

// Get highlighted keywords for a bullet
export function getHighlightedKeywords(bulletId: string): string[] {
  const state = fitCoachStore.getState();
  const highlight = state.heatMapHighlights.find(h => h.bulletId === bulletId);
  return highlight?.keywords || [];
}
