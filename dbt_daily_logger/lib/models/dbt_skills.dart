// DBT Skills exactly as they appear on the physical card

class DBTSkills {
  // Mindfulness Skills
  static const List<String> mindfulness = [
    'Wise mind',
    'Observe (Notice what\'s going on inside)',
    'Describe (Put words to experience)',
    'Participate (Enter the experience)',
    'Don\'t Judge (Don\'t pass judgement on what is)',
    'Stay Focused (One-mindfully, in-the-moment)',
    'Do what works (Effectiveness)',
    'Practice loving kindness',
    'SUNwave or STUNwave',
  ];

  // Emotion Regulation Skills
  static const List<String> emotionRegulation = [
    'Identifying and labeling emotions',
    'PLEASE (reduce vulnerability to Emo. Mind)',
    'Accumulating ++ (Pleasant activities)',
    'Building Mastery',
    'Cope-Ahead Plan:',
    'Working toward long-term goals',
    'Building structure and routine they like',
    'Opposite Action to Urges',
  ];

  // Distress Tolerance Skills
  static const List<String> distressTolerance = [
    'DEARMAN (Getting what you want)',
    'GIVE (Improving the relationship)',
    'FAST (Effective /keeping self-respect)',
    'THINK (Managing others opinions of you)',
    'Cheerleading statements',
    'STOP',
    'TIPP (temp, exercise, breathing, PMR)',
    'ACCEPTS (Distract)',
    'Self-soothe (5 senses)',
    'Pros and cons',
    'IMPROVE',
    'Radical Acceptance',
    'Willingness',
    'Positive reinforcement',
  ];

  // Middle Path Skills
  static const List<String> middlePath = [
    'Validate self',
    'Validate someone else',
    'Think (non-black-and-white) & act dialectically',
  ];

  static Map<String, List<String>> get allSkillsByCategory => {
        'Mindfulness': mindfulness,
        'Emotion Regulation': emotionRegulation,
        'Distress Tolerance': distressTolerance,
        'Middle Path': middlePath,
      };

  static List<String> get allSkills {
    return [
      ...mindfulness,
      ...emotionRegulation,
      ...distressTolerance,
      ...middlePath,
    ];
  }

  static String? getCategoryForSkill(String skill) {
    for (var entry in allSkillsByCategory.entries) {
      if (entry.value.contains(skill)) {
        return entry.key;
      }
    }
    return null;
  }
}

// Scale descriptions for UI
class ScaleDescriptions {
  static const Map<int, String> emotionScale = {
    0: 'Not at all',
    1: 'A bit',
    2: 'Somewhat',
    3: 'Rather Strong',
    4: 'Very Strong',
    5: 'Extremely Strong',
  };

  static const Map<String, String> usedSkillsScale = {
    '0': 'Not thought about or used',
    '1': 'Thought about, not used, didn\'t want to',
    '2': 'Thought about, not used, wanted to',
    '3': 'Tried but couldn\'t use them',
    '4': 'Tried, could do them but they didn\'t help',
    '5': 'Tried, could use them, helped',
    '6': 'Didn\'t try, used them, didn\'t help',
    '7': 'Didn\'t try, used them, helped',
  };

  static const String engagedInBehavior = '* = engaged in behavior';
}
