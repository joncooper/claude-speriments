/// Detailed descriptions for all DBT skills
class SkillDescriptions {
  static const Map<String, String> descriptions = {
    // Mindfulness
    'Observe': 'Notice and experience what is happening in the present moment without words. Just notice thoughts, feelings, and sensations.',
    'Describe': 'Put words on the experience. Describe what you observe using words, but stick to the facts.',
    'Participate': 'Throw yourself completely into the activity of the moment. Become one with whatever you\'re doing.',
    'One-mindfully': 'Do one thing at a time with full attention. Focus your mind and your awareness on the current activity.',
    'Non-judgmentally': 'See but don\'t evaluate. Take a non-judgmental stance. Just the facts. Let go of judgments.',
    'Effectively': 'Focus on what works. Do what is needed in each situation. Stay focused on your goals.',
    'Wise Mind': 'The middle path between emotion mind and reasonable mind. Integrates both logic and emotion.',

    // Distress Tolerance
    'STOP': 'Stop, Take a step back, Observe, Proceed mindfully. Pause before reacting to intense situations.',
    'Pros and Cons': 'Make a list of the pros and cons of acting on urges versus resisting urges.',
    'TIP': 'Change your body chemistry. Temperature (ice), Intense exercise, Paced breathing.',
    'ACCEPTS': 'Distract with Activities, Contributing, Comparisons, Emotions, Pushing away, Thoughts, Sensations.',
    'Self-Soothe': 'Comfort yourself using your five senses: vision, hearing, smell, taste, touch.',
    'IMPROVE': 'IMPROVE the moment with Imagery, Meaning, Prayer, Relaxation, One thing in the moment, Vacation, Encouragement.',
    'Radical Acceptance': 'Completely accept reality as it is in this moment. Let go of fighting reality.',
    'Willingness': 'Do what is needed, being willing rather than willful. Give up control.',
    'Half-smile': 'Relax your face and half-smile. Adopting a serene facial expression can help change your emotions.',

    // Emotion Regulation
    'Check the Facts': 'Check whether your emotional reactions fit the facts of the situation. Look at the evidence.',
    'Opposite Action': 'Act opposite to your emotion\'s urge when the emotion doesn\'t fit the facts or isn\'t effective.',
    'Problem Solving': 'Change the situation causing the unwanted emotion if the facts justify the emotion.',
    'ABC PLEASE': 'Accumulate positive emotions, Build mastery, Cope ahead. Treat Physical illness, balance Eating, avoid mood-Altering drugs, balance Sleep, get Exercise.',
    'Accumulate Positive Emotions': 'Build positive experiences now. Do pleasant things that are possible now.',
    'Build Mastery': 'Do things that make you feel competent and effective. Build on skills and accomplishments.',
    'Cope Ahead': 'Rehearse a plan for coping with an emotional situation before you\'re in it.',
    'Mindfulness of Current Emotions': 'Experience emotions as waves, coming and going. Observe and describe your emotions.',

    // Interpersonal Effectiveness
    'DEAR MAN': 'Describe, Express, Assert, Reinforce, stay Mindful, Appear confident, Negotiate. For getting what you want.',
    'GIVE': 'Be Gentle, act Interested, Validate, use an Easy manner. For keeping relationships.',
    'FAST': 'Be Fair, no Apologies, Stick to values, be Truthful. For keeping self-respect.',
    'Validation': 'Communicate that you understand and accept another person\'s feelings and thoughts.',
    'Building/Ending Relationships': 'Skills for finding and maintaining healthy relationships, or ending destructive ones.',
  };

  static String getDescription(String skill) {
    return descriptions[skill] ?? 'A valuable DBT skill for managing emotions and relationships.';
  }
}
