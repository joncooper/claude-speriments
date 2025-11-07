import 'package:flutter/material.dart';
import '../models/dbt_constants.dart';

class SkillsReferenceScreen extends StatefulWidget {
  const SkillsReferenceScreen({super.key});

  @override
  State<SkillsReferenceScreen> createState() => _SkillsReferenceScreenState();
}

class _SkillsReferenceScreenState extends State<SkillsReferenceScreen> {
  String? _selectedModule;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('DBT Skills Reference'),
      ),
      body: Column(
        children: [
          // Module selector
          Container(
            padding: const EdgeInsets.all(16),
            child: DropdownButtonFormField<String>(
              decoration: const InputDecoration(
                labelText: 'Select Module',
                prefixIcon: Icon(Icons.psychology),
              ),
              value: _selectedModule,
              items: DBTSkills.skillsByModule.keys.map((module) {
                return DropdownMenuItem(
                  value: module,
                  child: Text(module),
                );
              }).toList(),
              onChanged: (value) {
                setState(() {
                  _selectedModule = value;
                });
              },
            ),
          ),

          // Skills cards
          Expanded(
            child: _selectedModule == null
                ? Center(
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(
                          Icons.swipe,
                          size: 64,
                          color: Colors.grey[400],
                        ),
                        const SizedBox(height: 16),
                        Text(
                          'Select a module to view skills',
                          style: TextStyle(
                            color: Colors.grey[600],
                            fontSize: 16,
                          ),
                        ),
                      ],
                    ),
                  )
                : _buildSkillsCarousel(),
          ),
        ],
      ),
    );
  }

  Widget _buildSkillsCarousel() {
    final skills = DBTSkills.skillsByModule[_selectedModule]!;

    return PageView.builder(
      itemCount: skills.length,
      itemBuilder: (context, index) {
        final skill = skills[index];
        return _buildSkillCard(skill, _selectedModule!);
      },
    );
  }

  Widget _buildSkillCard(String skill, String module) {
    final explanation = _getSkillExplanation(skill);
    final tips = _getSkillTips(skill);

    return Container(
      margin: const EdgeInsets.all(16),
      child: Card(
        elevation: 4,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20),
        ),
        child: Container(
          decoration: BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
              colors: [
                _getModuleColor(module),
                _getModuleColor(module).withOpacity(0.7),
              ],
            ),
            borderRadius: BorderRadius.circular(20),
          ),
          child: Padding(
            padding: const EdgeInsets.all(24),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Module badge
                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 12,
                    vertical: 6,
                  ),
                  decoration: BoxDecoration(
                    color: Colors.white.withOpacity(0.9),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Text(
                    module,
                    style: TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.bold,
                      color: _getModuleColor(module),
                    ),
                  ),
                ),
                const SizedBox(height: 16),

                // Skill name
                Text(
                  skill,
                  style: const TextStyle(
                    fontSize: 28,
                    fontWeight: FontWeight.bold,
                    color: Colors.white,
                  ),
                ),
                const SizedBox(height: 24),

                // Explanation
                Expanded(
                  child: SingleChildScrollView(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text(
                          'What is it?',
                          style: TextStyle(
                            fontSize: 16,
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                          ),
                        ),
                        const SizedBox(height: 8),
                        Text(
                          explanation,
                          style: const TextStyle(
                            fontSize: 14,
                            color: Colors.white,
                            height: 1.5,
                          ),
                        ),
                        const SizedBox(height: 24),
                        const Text(
                          'How to use it:',
                          style: TextStyle(
                            fontSize: 16,
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                          ),
                        ),
                        const SizedBox(height: 8),
                        ...tips.map((tip) => Padding(
                              padding: const EdgeInsets.only(bottom: 8),
                              child: Row(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  const Text(
                                    '• ',
                                    style: TextStyle(
                                      color: Colors.white,
                                      fontSize: 14,
                                    ),
                                  ),
                                  Expanded(
                                    child: Text(
                                      tip,
                                      style: const TextStyle(
                                        fontSize: 14,
                                        color: Colors.white,
                                        height: 1.5,
                                      ),
                                    ),
                                  ),
                                ],
                              ),
                            )),
                      ],
                    ),
                  ),
                ),

                // Swipe indicator
                const Center(
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(Icons.arrow_back_ios, color: Colors.white70, size: 16),
                      SizedBox(width: 8),
                      Text(
                        'Swipe to explore',
                        style: TextStyle(
                          color: Colors.white70,
                          fontSize: 12,
                        ),
                      ),
                      SizedBox(width: 8),
                      Icon(Icons.arrow_forward_ios, color: Colors.white70, size: 16),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Color _getModuleColor(String module) {
    switch (module) {
      case 'Mindfulness':
        return Colors.purple;
      case 'Distress Tolerance':
        return Colors.orange;
      case 'Emotion Regulation':
        return Colors.blue;
      case 'Interpersonal Effectiveness':
        return Colors.green;
      default:
        return Colors.grey;
    }
  }

  String _getSkillExplanation(String skill) {
    final explanations = {
      'Observe': 'Notice and attend to what is happening without getting caught up in it. Just observe your thoughts, feelings, and sensations.',
      'Describe': 'Put words to your experience. Describe what you observe without judgments or interpretations.',
      'Participate': 'Throw yourself completely into the activity of the moment. Become one with what you are doing.',
      'Wise Mind': 'The integration of emotional mind and reasonable mind. It is knowing something in a centered way.',
      'STOP': 'Stop, Take a step back, Observe, Proceed mindfully. A crisis survival skill to prevent impulsive actions.',
      'Pros and Cons': 'Consider the advantages and disadvantages of tolerating distress versus giving in to urges.',
      'TIP (Temperature, Intense exercise, Paced breathing)': 'Change your body chemistry quickly to reduce intense emotions.',
      'Radical Acceptance': 'Completely accepting reality as it is, without fighting it or judging it.',
      'Opposite Action': 'Act opposite to your emotional urge when the emotion doesn\'t fit the facts.',
      'Check the Facts': 'Examine whether your emotional reaction fits the actual facts of the situation.',
      'ABC PLEASE': 'Build positive experiences and take care of your physical health to increase emotional resilience.',
      'DEAR MAN': 'A skill for asking for what you want effectively: Describe, Express, Assert, Reinforce, Mindful, Appear confident, Negotiate.',
      'GIVE': 'Keep relationships: be Gentle, act Interested, Validate, use an Easy manner.',
      'FAST': 'Maintain self-respect: be Fair, no Apologies, Stick to values, be Truthful.',
    };

    return explanations[skill] ??
        'A valuable DBT skill that helps you manage emotions and improve relationships.';
  }

  List<String> _getSkillTips(String skill) {
    final tips = {
      'Observe': [
        'Notice without reacting',
        'Sense with your eyes, ears, nose, skin, and tongue',
        'Experience without describing or labeling',
      ],
      'Describe': [
        'Use words to represent what you observe',
        'Stick to the facts',
        'Don\'t interpret or judge',
      ],
      'Wise Mind': [
        'Find the middle path between emotion and reason',
        'Listen to your intuition',
        'Trust your inner wisdom',
      ],
      'STOP': [
        'Stop: Freeze! Don\'t react',
        'Take a step back from the situation',
        'Observe what\'s happening',
        'Proceed mindfully',
      ],
      'Opposite Action': [
        'Identify the emotion and its urge',
        'Check if the emotion fits the facts',
        'If not, do the opposite of the urge',
      ],
      'DEAR MAN': [
        'Describe the situation',
        'Express your feelings',
        'Assert yourself',
        'Reinforce the person',
        'Stay mindful',
        'Appear confident',
        'Be willing to negotiate',
      ],
    };

    return tips[skill] ??
        [
          'Practice regularly for best results',
          'Use in real-life situations',
          'Combine with other DBT skills',
        ];
  }
}
