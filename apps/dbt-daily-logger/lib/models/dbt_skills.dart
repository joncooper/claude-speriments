/// DBT Skills organized by module
/// Matches the physical DBT diary card structure
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
      'TIP',
      'ACCEPTS',
      'Self-Soothe',
      'IMPROVE',
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
      'Building/Ending Relationships',
    ],
  };

  /// Get all skills as a flat list
  static List<String> get allSkills {
    return skillsByModule.values.expand((skills) => skills).toList();
  }

  /// Get the module for a given skill
  static String? getModuleForSkill(String skill) {
    for (final entry in skillsByModule.entries) {
      if (entry.value.contains(skill)) {
        return entry.key;
      }
    }
    return null;
  }

  /// Get all module names
  static List<String> get modules => skillsByModule.keys.toList();
}
