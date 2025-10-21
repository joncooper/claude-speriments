# Cialdini Persuasion Techniques - Test Plan

## Executive Summary

This document outlines a rigorous, deterministic testing methodology to validate whether Cialdini's persuasion techniques actually improve AI agent instruction adherence. The plan focuses on objective, reproducible metrics with automated validation wherever possible.

**Key Question:** Do these techniques measurably improve agent behavior, or are they just prompting theater?

---

## Testing Principles

### 1. Deterministic Validation
- Use automated checks (tests, linters, parsers) over subjective evaluation
- Define clear pass/fail criteria before running experiments
- Minimize human judgment in scoring

### 2. Control for Variability
- Use temperature=0 or run multiple trials (N=10+) per condition
- Compare identical tasks with/without techniques
- Control for prompt length (techniques add tokens - is it just verbosity?)

### 3. Measure What Matters
- **Instruction adherence:** Did the agent follow ALL instructions?
- **Completeness:** Did the agent skip any required steps?
- **Consistency:** Did the agent maintain prior commitments?
- **Error rate:** How often did attempts fail validation?

---

## Test Methodology

### A/B Testing Framework

Each test consists of:
- **Control group:** Standard prompt without techniques
- **Treatment group:** Same prompt enhanced with 1-2 Cialdini techniques
- **Validation:** Automated check of output quality/correctness

**Structure:**
```
Task X, Control:     "Do Y"
Task X, Treatment:   "/cialdini-commitment Do Y" (or manual application)
```

### Experimental Controls

1. **Length control:** Ensure treatment prompts aren't just longer
   - Create verbose control prompts matched for token count
   - Test if verbosity alone explains any improvements

2. **Randomness control:**
   - Use temperature=0 for deterministic results, OR
   - Run N=20 trials per condition and compare success rates

3. **Task difficulty:** Include easy, medium, and hard tasks
   - Easy tasks: High baseline success (test for ceiling effects)
   - Medium tasks: Moderate baseline success (ideal for detecting improvements)
   - Hard tasks: Low baseline success (test if techniques help with difficult instructions)

---

## Benchmark Task Suite

### Category 1: Multi-Step Instruction Adherence

**Goal:** Test if agents complete ALL steps, not just some.

**Task 1.1: Code Generation with Constraints**
```
Prompt (Control):
"Write a Python function to calculate factorial. Include type hints,
docstring, error handling for negative numbers, and unit tests."

Prompt (Treatment - Commitment):
"/cialdini-commitment Write a Python function to calculate factorial.
First, list all requirements you'll implement: type hints, docstring,
error handling for negative numbers, and unit tests. Then implement them all."
```

**Validation Criteria (Automated):**
- [ ] Function exists and runs
- [ ] Has type hints (parse AST for annotations)
- [ ] Has docstring (check `__doc__` exists)
- [ ] Handles negative numbers (run test: factorial(-1) should error)
- [ ] Includes unit tests (check for test functions/assertions)

**Success Metric:** Percentage of criteria met (0-100%)

---

**Task 1.2: File Modifications with Style Requirements**
```
Prompt (Control):
"Add error handling to user_service.py. Use try/except blocks,
log all errors, follow PEP 8, and don't change the function signatures."

Prompt (Treatment - Commitment + Authority):
"/cialdini-commitment According to PEP 8 style guidelines, add error
handling to user_service.py. First outline which functions you'll modify
and confirm you'll preserve signatures. Then implement with try/except,
logging, and PEP 8 compliance."
```

**Validation Criteria (Automated):**
- [ ] Error handling added (grep for try/except)
- [ ] Logging present (grep for log statements)
- [ ] Passes PEP 8 (run `flake8` or `pylint`)
- [ ] Function signatures unchanged (parse and compare signatures)
- [ ] Code still runs (execute tests)

**Success Metric:** Percentage of criteria met (0-100%)

---

### Category 2: Consistency Maintenance

**Goal:** Test if agents maintain earlier commitments throughout execution.

**Task 2.1: Variable Naming Consistency**
```
Prompt (Control):
"Refactor this code to use consistent variable naming. Use snake_case
throughout and make names descriptive."

Prompt (Treatment - Commitment):
"/cialdini-commitment Refactor this code. First, state your naming
convention (e.g., 'I will use snake_case for all variables'). Then
apply it consistently throughout the entire file."
```

**Validation Criteria (Automated):**
- [ ] No camelCase variables remain (regex check)
- [ ] All variables use snake_case (regex validation)
- [ ] Variable names > 3 characters (descriptiveness check)
- [ ] 100% consistency (no mixed conventions)

**Success Metric:** Consistency score (% of variables following stated convention)

---

**Task 2.2: Code Style Consistency**
```
Prompt (Control):
"Update these 5 functions to use async/await. Maintain the same
return types and error handling approach across all functions."

Prompt (Treatment - Commitment):
"/cialdini-commitment Update these 5 functions to use async/await.
First, describe the pattern you'll use (return types, error handling).
Then apply it identically to all 5 functions."
```

**Validation Criteria (Automated):**
- [ ] All 5 functions are async (AST parsing)
- [ ] All use same error handling pattern (AST pattern matching)
- [ ] All have same return type structure (type hint analysis)
- [ ] No inconsistencies in implementation approach

**Success Metric:** Pattern consistency score (0-100%)

---

### Category 3: Edge Case Coverage

**Goal:** Test if agents handle all specified edge cases, not just happy paths.

**Task 3.1: Input Validation**
```
Prompt (Control):
"Write a function to parse user input. Handle empty strings, None,
whitespace-only input, and strings exceeding 1000 characters."

Prompt (Treatment - Reciprocity):
"/cialdini-reciprocity I've identified all edge cases for you: empty
strings, None, whitespace-only, and 1000+ characters. Now write a parser
that handles each of these cases I've specified."
```

**Validation Criteria (Automated):**
- [ ] Handles empty string ("") - run test
- [ ] Handles None - run test
- [ ] Handles whitespace (" ", "\n", "\t") - run test
- [ ] Handles 1000+ chars - run test
- [ ] All tests pass

**Success Metric:** Edge case coverage (% of cases handled)

---

**Task 3.2: Error Conditions**
```
Prompt (Control):
"Implement file upload. Handle: file too large, wrong type,
missing file, corrupted file, network timeout."

Prompt (Treatment - Social Proof):
"/cialdini-social-proof Industry best practices for file upload
require handling: file too large, wrong type, missing file,
corrupted file, network timeout. Implement all of these error cases."
```

**Validation Criteria (Automated):**
- [ ] Large file check (grep for size validation)
- [ ] Type checking (grep for MIME type validation)
- [ ] Missing file handling (grep for existence check)
- [ ] Corruption handling (grep for validation/checksum)
- [ ] Timeout handling (grep for timeout or retry logic)

**Success Metric:** Error condition coverage (0-100%)

---

### Category 4: Avoiding Premature Completion

**Goal:** Test if agents complete full tasks vs. stopping early with "TODO" comments.

**Task 4.1: Full Implementation vs. Stubs**
```
Prompt (Control):
"Implement a caching layer with get, set, delete, clear, and TTL support."

Prompt (Treatment - Scarcity):
"/cialdini-scarcity This is the only chance to implement this caching
layer correctly - there's no time for iteration. Implement get, set,
delete, clear, and TTL support completely, not as stubs or TODOs."
```

**Validation Criteria (Automated):**
- [ ] No TODO comments (grep for "TODO", "FIXME", "XXX")
- [ ] No placeholder/stub functions (check for `pass` or `raise NotImplementedError`)
- [ ] All 5 operations fully implemented (AST verification)
- [ ] Implementation has real logic (LOC > 5 per function)

**Success Metric:** Completion rate (% fully implemented vs. stubbed)

---

**Task 4.2: Test Coverage**
```
Prompt (Control):
"Write comprehensive tests for this authentication module."

Prompt (Treatment - Authority):
"/cialdini-authority According to the testing standards document,
write comprehensive tests covering: happy path, invalid credentials,
expired tokens, rate limiting, and concurrent logins."
```

**Validation Criteria (Automated):**
- [ ] Happy path test exists (grep/AST)
- [ ] Invalid credentials test exists
- [ ] Expired token test exists
- [ ] Rate limiting test exists
- [ ] Concurrent login test exists
- [ ] All tests run and pass

**Success Metric:** Test scenario coverage (0-100%)

---

### Category 5: Following Constraints

**Goal:** Test if agents respect hard constraints (don't modify X, stay under Y lines, etc.).

**Task 5.1: No-Change Constraints**
```
Prompt (Control):
"Optimize the database queries in this file. Don't change the API
interface or the function signatures."

Prompt (Treatment - Commitment):
"/cialdini-commitment Optimize the database queries in this file.
First, confirm you understand you cannot change the API interface
or function signatures. Then proceed with optimization."
```

**Validation Criteria (Automated):**
- [ ] Function signatures unchanged (compare before/after AST)
- [ ] Public API unchanged (compare exported functions)
- [ ] Performance improved (run benchmark before/after)

**Success Metric:** Constraint violation count (0 = success)

---

**Task 5.2: Size Constraints**
```
Prompt (Control):
"Refactor this function to be more readable. Keep it under 50 lines."

Prompt (Treatment - Scarcity):
"/cialdini-scarcity You have a strict limit of 50 lines for this
function - not a line more. Refactor for readability while staying
within this hard constraint."
```

**Validation Criteria (Automated):**
- [ ] Function is < 50 lines (count LOC)
- [ ] Code still works (run tests)
- [ ] Readability improved (check cyclomatic complexity)

**Success Metric:** Constraint adherence (binary: within limit or not)

---

## Metrics & Scoring

### Primary Metrics

1. **Instruction Adherence Rate (IAR)**
   ```
   IAR = (Instructions Followed / Total Instructions) × 100%
   ```
   - Measured per task
   - Averaged across task suite

2. **First-Try Success Rate (FTSR)**
   ```
   FTSR = (Tasks Passing All Criteria / Total Tasks) × 100%
   ```
   - Binary: did it pass all checks on first attempt?
   - Key metric for user experience

3. **Completeness Score (CS)**
   ```
   CS = (Fully Implemented Features / Required Features) × 100%
   ```
   - Detects partial implementations and TODOs

4. **Constraint Violation Rate (CVR)**
   ```
   CVR = (Constraints Violated / Total Constraints)
   ```
   - Lower is better
   - Critical for production use cases

### Secondary Metrics

5. **Iteration Count**
   - How many user corrections needed to pass all criteria?
   - Lower is better

6. **Edge Case Coverage**
   - Percentage of specified edge cases handled

7. **Consistency Score**
   - For tasks requiring pattern repetition

---

## Experimental Design

### Experiment 1: Individual Technique Efficacy

**Hypothesis:** Each Cialdini technique improves instruction adherence for specific task types.

**Method:**
- Run all 10 benchmark tasks (control)
- Run all 10 benchmark tasks (each with appropriate technique)
- Compare metrics

**Sample Size:**
- N=10 tasks × 2 conditions = 20 runs (if temp=0)
- N=10 tasks × 2 conditions × 10 trials = 200 runs (if temp>0)

**Analysis:**
- Paired t-test on IAR scores
- Chi-square test on FTSR (pass/fail counts)
- Effect size calculation (Cohen's d)

**Success Criteria:**
- Statistically significant improvement (p < 0.05)
- Practically significant effect size (Cohen's d > 0.5)
- Improvement on at least 70% of tasks

---

### Experiment 2: Technique Matching

**Hypothesis:** Different techniques work better for different task types.

**Method:**
- Match techniques to task categories based on theory
- Test matched vs. mismatched combinations

**Expected Matches:**
- Commitment → Multi-step tasks, consistency tasks
- Reciprocity → Edge case coverage (you gave me cases, I handle them)
- Scarcity → Avoiding premature completion
- Authority → Following constraints/standards
- Social Proof → Best practices adherence

**Analysis:**
- Compare matched vs. mismatched technique performance
- Identify which techniques work best for which tasks

---

### Experiment 3: Verbosity Control

**Hypothesis:** Improvements (if any) come from the technique content, not just longer prompts.

**Method:**
- Control: Standard prompt
- Treatment 1: Cialdini technique (adds N tokens)
- Treatment 2: Verbose prompt (adds N tokens with filler)

**Example:**
```
Control: "Write a function with error handling."
Treatment 1 (Commitment): "/cialdini-commitment Write a function.
First outline your approach to error handling, then implement it."
Treatment 2 (Verbose): "Write a function. This function should have
error handling. Error handling is important. Make sure to include it."
```

**Analysis:**
- If Treatment 1 > Treatment 2, technique content matters
- If Treatment 1 ≈ Treatment 2, it's just verbosity
- If Treatment 2 > Control, verbosity alone helps

---

### Experiment 4: Combined Techniques

**Hypothesis:** Combining 2-3 techniques amplifies effects.

**Method:**
- Test individual techniques
- Test pairwise combinations
- Test `/cialdini-all` (all 7)

**Analysis:**
- Is there a superadditive effect?
- What's the optimal combination?
- Does `/cialdini-all` help or create prompt bloat?

---

## Automation & Tooling

### Test Harness

Create a test runner that:

```bash
# Run full benchmark suite
./run_cialdini_tests.sh --suite full --trials 10

# Run specific category
./run_cialdini_tests.sh --category multi-step --technique commitment

# Compare control vs treatment
./run_cialdini_tests.sh --compare control,commitment
```

**Output:**
```
=== Cialdini Technique Test Results ===

Task 1.1: Multi-Step Code Generation
  Control:    60% IAR (3/5 criteria met)
  Commitment: 100% IAR (5/5 criteria met)
  Improvement: +40% ✓

Task 1.2: File Modifications
  Control:    80% IAR (4/5 criteria met)
  Commitment: 100% IAR (5/5 criteria met)
  Improvement: +20% ✓

...

=== Summary ===
Overall IAR: Control=68%, Treatment=89% (+21%, p=0.003)
FTSR: Control=30%, Treatment=70% (+40%, p=0.001)
Effect Size: Cohen's d = 1.2 (large effect)
```

### Validation Scripts

Create automated validators:

```python
# validators/code_quality.py
def validate_task_1_1(code: str) -> dict:
    """Validate factorial function meets all criteria."""
    return {
        "has_function": check_function_exists(code, "factorial"),
        "has_type_hints": check_type_hints(code),
        "has_docstring": check_docstring(code),
        "handles_negatives": check_error_handling(code, -1),
        "has_tests": check_unit_tests(code),
        "iar": calculate_iar(...),
    }
```

### Statistical Analysis

```python
# analysis/stats.py
def analyze_results(control_scores, treatment_scores):
    """Statistical analysis of A/B test results."""
    return {
        "mean_diff": np.mean(treatment) - np.mean(control),
        "t_statistic": scipy.stats.ttest_rel(...),
        "p_value": ...,
        "cohens_d": calculate_effect_size(...),
        "confidence_interval": ...,
    }
```

---

## Success Criteria for Validation

For the techniques to be considered **validated and effective**:

### Minimum Thresholds

1. **Statistical Significance**
   - p-value < 0.05 on primary metrics
   - Replicable across multiple runs

2. **Practical Significance**
   - IAR improvement ≥ 15% over control
   - FTSR improvement ≥ 20% over control
   - Effect size (Cohen's d) ≥ 0.5

3. **Consistency**
   - Improvements on ≥ 70% of benchmark tasks
   - No significant degradation on any task category
   - Results hold across different task difficulties

4. **Specificity**
   - Technique content matters (not just verbosity)
   - Different techniques show different effectiveness profiles
   - Matched techniques outperform mismatched ones

### Failure Criteria

The techniques would be considered **ineffective** if:

- No statistically significant improvement (p ≥ 0.05)
- Improvement < 10% and not practically meaningful
- Results are inconsistent (high variance across trials)
- Verbose control performs equally well (it's just prompt length)
- Improvements only on easy tasks (ceiling effects)

---

## Implementation Timeline

### Phase 1: Infrastructure (Week 1)
- [ ] Create benchmark task suite (10 tasks)
- [ ] Write automated validation scripts
- [ ] Build test harness/runner
- [ ] Setup results tracking

### Phase 2: Baseline Testing (Week 2)
- [ ] Run control group (baseline metrics)
- [ ] Verify automation works correctly
- [ ] Establish baseline variability (if temp>0)

### Phase 3: Treatment Testing (Week 3-4)
- [ ] Run Experiment 1 (individual techniques)
- [ ] Run Experiment 2 (technique matching)
- [ ] Run Experiment 3 (verbosity control)

### Phase 4: Analysis (Week 5)
- [ ] Statistical analysis
- [ ] Effect size calculations
- [ ] Generate reports and visualizations

### Phase 5: Advanced Testing (Week 6)
- [ ] Run Experiment 4 (combinations)
- [ ] Test `/cialdini-all` effectiveness
- [ ] Identify optimal technique pairings

---

## Reporting

### Test Report Format

For each experiment, generate:

1. **Executive Summary**
   - Key findings (1-2 sentences)
   - Statistical significance
   - Recommendation (use technique or not)

2. **Detailed Metrics**
   - Table of all metric comparisons
   - Statistical test results
   - Effect sizes

3. **Visualizations**
   - Bar charts: Control vs. Treatment performance
   - Heatmap: Technique × Task Category effectiveness
   - Box plots: Distribution of scores

4. **Task-Level Analysis**
   - Which tasks improved most?
   - Which tasks showed no effect?
   - Any degradation?

5. **Recommendations**
   - Which techniques to implement
   - Which task types benefit most
   - Suggested command usage patterns

---

## Open Questions

1. **Temperature Setting**
   - Should we use temp=0 for determinism or temp>0 with multiple trials?
   - Trade-off: determinism vs. statistical power

2. **Prompt Engineering Confounds**
   - Are we comparing techniques or comparing prompt quality?
   - Should we have expert-crafted controls?

3. **Task Representativeness**
   - Do our 10 benchmark tasks cover real-world usage?
   - Should we add user-submitted tasks?

4. **Secondary Model Evaluation**
   - Use another AI to score instruction adherence?
   - Trade-off: objectivity vs. "teaching to the test"

5. **Human Validation**
   - Should subset of results be human-validated?
   - Inter-rater reliability?

---

## Conclusion

This test plan provides a rigorous, automated framework for validating whether Cialdini's persuasion techniques actually improve AI agent instruction adherence. By using:

- **Objective metrics** (automated validation)
- **Controlled experiments** (A/B testing with controls)
- **Statistical rigor** (significance tests, effect sizes)
- **Reproducible methodology** (documented, automated)

We can definitively answer: **Do these techniques work, or are they prompting theater?**

If validated, we'll have evidence-based guidance for when and how to use each technique. If not validated, we'll have saved users from adopting ineffective practices.

---

*Generated: 2025-10-21*
