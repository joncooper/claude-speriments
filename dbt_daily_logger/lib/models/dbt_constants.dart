// DBT Skills organized by module
class DBTSkills {
  static const Map<String, List<String>> skillsByModule = {
    'Mindfulness': [
      'Observe',
      'Describe',
      'Participate',
      'One-mindfully',
      'Non-judgmentally',
      'Effectively',
      'Wise Mind',
    ],
    'Distress Tolerance': [
      'STOP',
      'Pros and Cons',
      'TIP (Temperature, Intense exercise, Paced breathing)',
      'ACCEPTS',
      'Self-Soothe (5 senses)',
      'IMPROVE the moment',
      'Radical Acceptance',
      'Willingness',
      'Half-smile',
    ],
    'Emotion Regulation': [
      'Check the Facts',
      'Opposite Action',
      'Problem Solving',
      'ABC PLEASE',
      'Accumulate Positive Emotions',
      'Build Mastery',
      'Cope Ahead',
      'Mindfulness of Current Emotions',
    ],
    'Interpersonal Effectiveness': [
      'DEAR MAN',
      'GIVE',
      'FAST',
      'Validation',
      'Building Relationships',
      'Ending Destructive Relationships',
    ],
  };

  static List<String> get allSkills {
    return skillsByModule.values.expand((skills) => skills).toList();
  }

  static String? getModuleForSkill(String skill) {
    for (var entry in skillsByModule.entries) {
      if (entry.value.contains(skill)) {
        return entry.key;
      }
    }
    return null;
  }
}

// Common emotions
class CommonEmotions {
  static const List<String> emotions = [
    'Sadness',
    'Anger',
    'Fear',
    'Anxiety',
    'Joy',
    'Shame',
    'Guilt',
    'Jealousy',
    'Love',
    'Loneliness',
    'Disgust',
    'Frustration',
    'Contentment',
    'Gratitude',
    'Hope',
  ];
}

// Common urges tracked in DBT
class CommonUrges {
  static const List<String> urges = [
    'Self-harm',
    'Substance use',
    'Binge eating',
    'Restricting food',
    'Suicide',
    'Escape/avoid',
    'Aggression',
    'Excessive spending',
    'Risky behavior',
  ];
}

// Common target behaviors
class CommonTargetBehaviors {
  static const List<String> behaviors = [
    'Self-harm',
    'Substance use',
    'Binge eating',
    'Purging',
    'Restricting',
    'Suicide attempt',
    'Therapy-interfering behavior',
    'Quality of life-interfering behavior',
    'Lying',
    'Aggression/violence',
    'Excessive spending',
  ];
}
