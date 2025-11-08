"""
Credibility Scorer

Quantitative scoring of management credibility based on commitment fulfillment.
Generates overall scores, letter grades, category breakdowns, and red flag detection.
"""

from typing import Dict, List
from collections import defaultdict
from datetime import datetime
from dateutil import parser as date_parser


class CredibilityScorer:
    """
    Calculates management credibility scores based on commitment outcomes.

    Scoring methodology:
    - Overall Score = (Fulfilled + 0.5 × Partial) / Total Verifiable × 100
    - Letter grades: A+ to F
    - Category-specific scores
    - Red flag detection
    - Time trend analysis
    """

    GRADE_THRESHOLDS = [
        (95, 'A+'),
        (90, 'A'),
        (85, 'A-'),
        (80, 'B+'),
        (75, 'B'),
        (70, 'B-'),
        (65, 'C+'),
        (60, 'C'),
        (55, 'C-'),
        (50, 'D+'),
        (45, 'D'),
        (40, 'D-'),
        (0, 'F'),
    ]

    def __init__(self):
        """Initialize the credibility scorer."""
        pass

    def score_management(
        self,
        commitments: List[Dict],
        outcomes: List[Dict]
    ) -> Dict:
        """
        Generate comprehensive credibility score for management.

        Args:
            commitments: List of commitment dictionaries from CommitmentExtractor
            outcomes: List of outcome dictionaries from OutcomeTracker

        Returns:
            Score dictionary with structure:
            {
                'overall_score': float,  # 0-100
                'grade': str,  # Letter grade
                'total_commitments': int,
                'verifiable_commitments': int,
                'fulfilled_count': int,
                'partially_fulfilled_count': int,
                'not_fulfilled_count': int,
                'abandoned_count': int,
                'pending_count': int,
                'fulfillment_rate': float,  # % fulfilled
                'partial_rate': float,  # % partial
                'miss_rate': float,  # % not fulfilled
                'category_scores': dict,  # Scores by category
                'specificity_index': float,  # Average commitment quality
                'red_flags': list,  # List of concerning patterns
                'time_trends': dict,  # Improving vs declining
            }
        """
        # Create outcome lookup
        outcome_lookup = {o['commitment_id']: o for o in outcomes}

        # Filter to verifiable commitments only
        verifiable = [
            c for c in commitments
            if c['verifiable'] and c['commitment_id'] in outcome_lookup
        ]

        if not verifiable:
            return self._empty_score()

        # Count outcomes by status
        counts = self._count_outcomes(verifiable, outcome_lookup)

        # Calculate overall score
        total_verifiable = counts['fulfilled'] + counts['partially_fulfilled'] + counts['not_fulfilled'] + counts['abandoned']

        if total_verifiable == 0:
            overall_score = 0.0
        else:
            overall_score = (
                (counts['fulfilled'] + 0.5 * counts['partially_fulfilled']) / total_verifiable * 100
            )

        # Assign letter grade
        grade = self._assign_grade(overall_score)

        # Calculate rates
        fulfillment_rate = (counts['fulfilled'] / total_verifiable * 100) if total_verifiable > 0 else 0
        partial_rate = (counts['partially_fulfilled'] / total_verifiable * 100) if total_verifiable > 0 else 0
        miss_rate = ((counts['not_fulfilled'] + counts['abandoned']) / total_verifiable * 100) if total_verifiable > 0 else 0

        # Category breakdowns
        category_scores = self._calculate_category_scores(verifiable, outcome_lookup)

        # Specificity index (average quality of commitments)
        specificity_index = sum(c['specificity'] for c in verifiable) / len(verifiable)

        # Detect red flags
        red_flags = self._detect_red_flags(verifiable, outcome_lookup, category_scores)

        # Analyze time trends
        time_trends = self._analyze_time_trends(verifiable, outcome_lookup)

        return {
            'overall_score': round(overall_score, 1),
            'grade': grade,
            'total_commitments': len(commitments),
            'verifiable_commitments': len(verifiable),
            'fulfilled_count': counts['fulfilled'],
            'partially_fulfilled_count': counts['partially_fulfilled'],
            'not_fulfilled_count': counts['not_fulfilled'],
            'abandoned_count': counts['abandoned'],
            'pending_count': counts['pending'],
            'fulfillment_rate': round(fulfillment_rate, 1),
            'partial_rate': round(partial_rate, 1),
            'miss_rate': round(miss_rate, 1),
            'category_scores': category_scores,
            'specificity_index': round(specificity_index, 1),
            'red_flags': red_flags,
            'time_trends': time_trends,
        }

    def _count_outcomes(
        self,
        commitments: List[Dict],
        outcome_lookup: Dict[str, Dict]
    ) -> Dict[str, int]:
        """Count outcomes by status."""
        counts = {
            'fulfilled': 0,
            'partially_fulfilled': 0,
            'not_fulfilled': 0,
            'abandoned': 0,
            'pending': 0,
            'unverifiable': 0,
        }

        for commitment in commitments:
            outcome = outcome_lookup.get(commitment['commitment_id'])
            if outcome:
                status = outcome['status']
                if status in counts:
                    counts[status] += 1

        return counts

    def _assign_grade(self, score: float) -> str:
        """Assign letter grade based on score."""
        for threshold, grade in self.GRADE_THRESHOLDS:
            if score >= threshold:
                return grade
        return 'F'

    def _calculate_category_scores(
        self,
        commitments: List[Dict],
        outcome_lookup: Dict[str, Dict]
    ) -> Dict[str, Dict]:
        """Calculate scores broken down by commitment category."""
        # Group by category
        by_category = defaultdict(list)
        for commitment in commitments:
            category = commitment['category']
            outcome = outcome_lookup.get(commitment['commitment_id'])
            if outcome and outcome['status'] not in ['pending', 'unverifiable']:
                by_category[category].append(outcome)

        # Calculate score for each category
        category_scores = {}
        for category, outcomes in by_category.items():
            fulfilled = sum(1 for o in outcomes if o['status'] == 'fulfilled')
            partial = sum(1 for o in outcomes if o['status'] == 'partially_fulfilled')
            total = len(outcomes)

            if total > 0:
                score = (fulfilled + 0.5 * partial) / total * 100
                category_scores[category] = {
                    'score': round(score, 1),
                    'count': total,
                    'fulfilled': fulfilled,
                    'partial': partial,
                    'missed': total - fulfilled - partial,
                }

        return category_scores

    def _detect_red_flags(
        self,
        commitments: List[Dict],
        outcome_lookup: Dict[str, Dict],
        category_scores: Dict[str, Dict]
    ) -> List[Dict]:
        """
        Detect concerning patterns in management credibility.

        Red flags:
        1. High miss rate in specific category (>50%, n>=3)
        2. Declining specificity over time (>2 point drop)
        3. Multiple abandoned initiatives (>=2)
        4. Consistent underperformance (avg variance <-5%)
        """
        red_flags = []

        # 1. High miss rate in category
        for category, stats in category_scores.items():
            if stats['count'] >= 3:
                miss_rate = stats['missed'] / stats['count'] * 100
                if miss_rate > 50:
                    red_flags.append({
                        'type': 'high_category_miss_rate',
                        'severity': 'high',
                        'category': category,
                        'miss_rate': round(miss_rate, 1),
                        'description': f"High miss rate in {category.replace('_', ' ')} ({miss_rate:.1f}%)",
                    })

        # 2. Declining specificity
        # Sort commitments by date
        sorted_commitments = sorted(
            commitments,
            key=lambda c: c['source_filing']['filing_date']
        )

        if len(sorted_commitments) >= 6:
            # Compare early vs late
            cutoff = len(sorted_commitments) // 2
            early_specificity = sum(c['specificity'] for c in sorted_commitments[:cutoff]) / cutoff
            late_specificity = sum(c['specificity'] for c in sorted_commitments[cutoff:]) / (len(sorted_commitments) - cutoff)

            specificity_change = late_specificity - early_specificity
            if specificity_change < -2:
                red_flags.append({
                    'type': 'declining_specificity',
                    'severity': 'medium',
                    'early_specificity': round(early_specificity, 1),
                    'late_specificity': round(late_specificity, 1),
                    'change': round(specificity_change, 1),
                    'description': f"Commitment specificity declining (from {early_specificity:.1f} to {late_specificity:.1f})",
                })

        # 3. Multiple abandoned initiatives
        abandoned_count = sum(
            1 for c in commitments
            if outcome_lookup.get(c['commitment_id'], {}).get('status') == 'abandoned'
        )

        if abandoned_count >= 2:
            red_flags.append({
                'type': 'multiple_abandoned',
                'severity': 'high',
                'count': abandoned_count,
                'description': f"{abandoned_count} commitments explicitly abandoned",
            })

        # 4. Consistent underperformance
        variances = []
        for commitment in commitments:
            outcome = outcome_lookup.get(commitment['commitment_id'])
            if outcome and 'variance' in outcome:
                variances.append(outcome['variance'])

        if len(variances) >= 5:
            avg_variance = sum(variances) / len(variances)
            if avg_variance < -5:
                red_flags.append({
                    'type': 'consistent_underperformance',
                    'severity': 'high',
                    'avg_variance': round(avg_variance, 1),
                    'description': f"Consistent underperformance (avg {avg_variance:.1f}% below target)",
                })

        return red_flags

    def _analyze_time_trends(
        self,
        commitments: List[Dict],
        outcome_lookup: Dict[str, Dict]
    ) -> Dict:
        """
        Analyze whether credibility is improving or declining over time.

        Splits commitments into early and late periods and compares scores.
        """
        if len(commitments) < 4:
            return {
                'trend': 'insufficient_data',
                'description': 'Not enough commitments to identify trend',
            }

        # Sort by filing date
        sorted_commitments = sorted(
            commitments,
            key=lambda c: c['source_filing']['filing_date']
        )

        # Split into early and late
        cutoff = len(sorted_commitments) // 2
        early_commitments = sorted_commitments[:cutoff]
        late_commitments = sorted_commitments[cutoff:]

        # Calculate scores for each period
        early_score = self._calculate_period_score(early_commitments, outcome_lookup)
        late_score = self._calculate_period_score(late_commitments, outcome_lookup)

        # Determine trend
        score_change = late_score - early_score

        if score_change >= 10:
            trend = 'improving'
            description = f"Credibility improving (from {early_score:.1f} to {late_score:.1f})"
        elif score_change <= -10:
            trend = 'declining'
            description = f"Credibility declining (from {early_score:.1f} to {late_score:.1f})"
        else:
            trend = 'stable'
            description = f"Credibility stable (around {early_score:.1f})"

        return {
            'trend': trend,
            'early_score': round(early_score, 1),
            'late_score': round(late_score, 1),
            'change': round(score_change, 1),
            'description': description,
        }

    def _calculate_period_score(
        self,
        commitments: List[Dict],
        outcome_lookup: Dict[str, Dict]
    ) -> float:
        """Calculate score for a specific time period."""
        fulfilled = 0
        partial = 0
        total = 0

        for commitment in commitments:
            outcome = outcome_lookup.get(commitment['commitment_id'])
            if outcome and outcome['status'] not in ['pending', 'unverifiable']:
                total += 1
                if outcome['status'] == 'fulfilled':
                    fulfilled += 1
                elif outcome['status'] == 'partially_fulfilled':
                    partial += 1

        if total == 0:
            return 0.0

        return (fulfilled + 0.5 * partial) / total * 100

    def _empty_score(self) -> Dict:
        """Return empty score structure when no data available."""
        return {
            'overall_score': 0.0,
            'grade': 'N/A',
            'total_commitments': 0,
            'verifiable_commitments': 0,
            'fulfilled_count': 0,
            'partially_fulfilled_count': 0,
            'not_fulfilled_count': 0,
            'abandoned_count': 0,
            'pending_count': 0,
            'fulfillment_rate': 0.0,
            'partial_rate': 0.0,
            'miss_rate': 0.0,
            'category_scores': {},
            'specificity_index': 0.0,
            'red_flags': [],
            'time_trends': {
                'trend': 'insufficient_data',
                'description': 'No verifiable commitments found',
            },
        }
