import 'package:flutter/material.dart';
import '../models/dbt_skills.dart';

class SkillsReferenceScreen extends StatelessWidget {
  const SkillsReferenceScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('DBT Skills Reference'),
        centerTitle: true,
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          const Text(
            '✨ Your DBT Skills Toolkit',
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 8),
          Text(
            'Tap any skill to learn more about it',
            style: TextStyle(color: Colors.grey[600], fontSize: 16),
          ),
          const SizedBox(height: 24),

          // Build categories
          ...DBTSkills.allSkillsByCategory.entries.map((category) {
            return _CategorySection(
              categoryName: category.key,
              skills: category.value,
            );
          }),
        ],
      ),
    );
  }
}

class _CategorySection extends StatelessWidget {
  final String categoryName;
  final List<String> skills;

  const _CategorySection({
    required this.categoryName,
    required this.skills,
  });

  Color _getCategoryColor() {
    switch (categoryName) {
      case 'Mindfulness':
        return Colors.purple;
      case 'Emotion Regulation':
        return Colors.blue;
      case 'Distress Tolerance':
        return Colors.orange;
      case 'Middle Path':
        return Colors.teal;
      default:
        return Colors.grey;
    }
  }

  String _getCategoryEmoji() {
    switch (categoryName) {
      case 'Mindfulness':
        return '🧘';
      case 'Emotion Regulation':
        return '💙';
      case 'Distress Tolerance':
        return '🛡️';
      case 'Middle Path':
        return '⚖️';
      default:
        return '✨';
    }
  }

  @override
  Widget build(BuildContext context) {
    final color = _getCategoryColor();
    final emoji = _getCategoryEmoji();

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
          decoration: BoxDecoration(
            color: color.withOpacity(0.1),
            borderRadius: BorderRadius.circular(12),
          ),
          child: Row(
            children: [
              Text(emoji, style: const TextStyle(fontSize: 24)),
              const SizedBox(width: 12),
              Text(
                categoryName,
                style: TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                  color: color,
                ),
              ),
            ],
          ),
        ),
        const SizedBox(height: 12),

        ...skills.map((skill) => Padding(
          padding: const EdgeInsets.only(bottom: 8),
          child: _SkillCard(skill: skill, color: color),
        )),

        const SizedBox(height: 24),
      ],
    );
  }
}

class _SkillCard extends StatelessWidget {
  final String skill;
  final Color color;

  const _SkillCard({
    required this.skill,
    required this.color,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      child: InkWell(
        onTap: () {
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => SkillDetailScreen(
                skillName: skill,
                categoryColor: color,
              ),
            ),
          );
        },
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Row(
            children: [
              Expanded(
                child: Text(
                  skill,
                  style: const TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.w500,
                  ),
                ),
              ),
              Icon(Icons.arrow_forward_ios, size: 16, color: color),
            ],
          ),
        ),
      ),
    );
  }
}

class SkillDetailScreen extends StatefulWidget {
  final String skillName;
  final Color categoryColor;

  const SkillDetailScreen({
    super.key,
    required this.skillName,
    required this.categoryColor,
  });

  @override
  State<SkillDetailScreen> createState() => _SkillDetailScreenState();
}

class _SkillDetailScreenState extends State<SkillDetailScreen> {
  bool _isExpanded = false;

  @override
  Widget build(BuildContext context) {
    final category = DBTSkills.getCategoryForSkill(widget.skillName);
    final description = _getSkillDescription(widget.skillName);
    final howToUse = _getHowToUse(widget.skillName);
    final whenToUse = _getWhenToUse(widget.skillName);

    return Scaffold(
      appBar: AppBar(
        title: Text(
          widget.skillName,
          style: const TextStyle(fontSize: 16),
        ),
        centerTitle: true,
        backgroundColor: widget.categoryColor,
      ),
      body: Stack(
        children: [
          SingleChildScrollView(
            padding: const EdgeInsets.all(20),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Category badge
                if (category != null)
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                    decoration: BoxDecoration(
                      color: widget.categoryColor.withOpacity(0.2),
                      borderRadius: BorderRadius.circular(20),
                    ),
                    child: Text(
                      category,
                      style: TextStyle(
                        color: widget.categoryColor,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                const SizedBox(height: 24),

                // Skill name
                Text(
                  widget.skillName,
                  style: const TextStyle(
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 16),

                // Description
                const Text(
                  'What is it?',
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                    color: Colors.teal,
                  ),
                ),
                const SizedBox(height: 8),
                Text(
                  description,
                  style: const TextStyle(fontSize: 16, height: 1.5),
                ),
                const SizedBox(height: 24),

                // When to use
                const Text(
                  'When to use it?',
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                    color: Colors.teal,
                  ),
                ),
                const SizedBox(height: 8),
                Text(
                  whenToUse,
                  style: const TextStyle(fontSize: 16, height: 1.5),
                ),
                const SizedBox(height: 24),

                // How to use
                const Text(
                  'How to use it?',
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                    color: Colors.teal,
                  ),
                ),
                const SizedBox(height: 8),
                Text(
                  howToUse,
                  style: const TextStyle(fontSize: 16, height: 1.5),
                ),
                const SizedBox(height: 100), // Space for expand button
              ],
            ),
          ),

          // Expand indicator at bottom
          if (!_isExpanded)
            Positioned(
              bottom: 0,
              left: 0,
              right: 0,
              child: Container(
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    begin: Alignment.topCenter,
                    end: Alignment.bottomCenter,
                    colors: [
                      Colors.white.withOpacity(0),
                      Colors.white,
                    ],
                  ),
                ),
                child: Center(
                  child: IconButton(
                    icon: const Icon(Icons.keyboard_arrow_down),
                    onPressed: () {
                      setState(() {
                        _isExpanded = true;
                      });
                    },
                  ),
                ),
              ),
            ),
        ],
      ),
    );
  }

  String _getSkillDescription(String skill) {
    // Comprehensive descriptions for each skill
    final descriptions = {
      'Wise mind': 'Wise Mind is the balance between your emotional mind and your logical mind. It\'s that inner knowing that helps you make decisions that honor both your feelings and your reason.',

      'Observe (Notice what\'s going on inside)': 'This skill involves paying attention to what\'s happening inside you (thoughts, feelings, sensations) and outside you (sights, sounds) without getting caught up in it.',

      'Describe (Put words to experience)': 'Putting words to your experience helps you understand and communicate what\'s happening. Like putting a label on what you\'re feeling or thinking.',

      'Participate (Enter the experience)': 'Being fully present in the moment, throwing yourself completely into what you\'re doing without self-consciousness.',

      'Don\'t Judge (Don\'t pass judgement on what is)': 'Noticing when you\'re adding judgments like "good" or "bad" to your experiences, and practicing just seeing things as they are.',

      'Stay Focused (One-mindfully, in-the-moment)': 'Doing one thing at a time with your full attention, rather than multitasking or getting distracted.',

      'Do what works (Effectiveness)': 'Focusing on what actually works to meet your goals, rather than being "right" or proving a point.',

      'Practice loving kindness': 'Intentionally sending kind thoughts to yourself and others, even when it\'s hard.',

      'SUNwave or STUNwave': 'Acronyms to help you remember mindfulness practices. SUNwave: Smile, Unclench, Notice, Wave (of breath). STUNwave: Stop, Take a breath, Unclench, Notice, Wave (of breath).',

      'Identifying and labeling emotions': 'Recognizing what emotion you\'re feeling and giving it a name. This is the first step in managing emotions.',

      'PLEASE (reduce vulnerability to Emo. Mind)': 'Taking care of your body to reduce emotional vulnerability. Treat PhysicaL illness, balanced Eating, Avoid mood-altering substances, balanced Sleep, Exercise.',

      'Accumulating ++ (Pleasant activities)': 'Building positive experiences in your life by doing things you enjoy. Creates emotional resilience.',

      'Building Mastery': 'Doing things that make you feel capable and accomplished. Helps build confidence and positive emotions.',

      'Cope-Ahead Plan:': 'Planning ahead for difficult situations by imagining them and practicing coping skills before they happen.',

      'Working toward long-term goals': 'Setting and taking steps toward goals that matter to you, which builds meaning and positive emotions over time.',

      'Building structure and routine they like': 'Creating daily routines and structures that support your well-being and reduce chaos.',

      'Opposite Action to Urges': 'Acting opposite to your emotional urge when the emotion doesn\'t fit the facts. Like approaching when you want to avoid, or being gentle when you want to attack.',

      'DEARMAN (Getting what you want)': 'Describe the situation, Express your feelings, Assert yourself, Reinforce, stay Mindful, Appear confident, Negotiate. For asking for what you need.',

      'GIVE (Improving the relationship)': 'Be Gentle, act Interested, Validate, use an Easy manner. For maintaining relationships.',

      'FAST (Effective /keeping self-respect)': 'Be Fair, no Apologies (for having needs), Stick to values, be Truthful. For maintaining self-respect.',

      'THINK (Managing others opinions of you)': 'Think about whether you care about this person\'s opinion, Have empathy, Interpret kindly, Notice positives, Keep perspective.',

      'Cheerleading statements': 'Positive, encouraging self-talk to motivate yourself through difficult moments.',

      'STOP': 'Stop, Take a step back, Observe, Proceed mindfully. For crisis moments.',

      'TIPP (temp, exercise, breathing, PMR)': 'Temperature (cold water on face), Intense exercise, Paced breathing, Progressive muscle relaxation. For reducing intense arousal quickly.',

      'ACCEPTS (Distract)': 'Activities, Contributing, Comparisons, Emotions (opposite), Pushing away, Thoughts (other), Sensations. Ways to distract from overwhelming emotions.',

      'Self-soothe (5 senses)': 'Using your five senses (sight, sound, smell, taste, touch) to comfort and calm yourself.',

      'Pros and cons': 'Looking at the positive and negative consequences of both tolerating and not tolerating distress.',

      'IMPROVE': 'Imagery, Meaning, Prayer, Relaxation, One thing in the moment, Vacation (brief), Encouragement. Ways to improve the moment.',

      'Radical Acceptance': 'Completely accepting reality as it is, without fighting it. Doesn\'t mean approval, just acknowledgment.',

      'Willingness': 'Being willing to do what\'s needed in the moment, rather than being willful or refusing.',

      'Positive reinforcement': 'Rewarding yourself for positive behaviors to make them more likely to happen again.',

      'Validate self': 'Acknowledging and accepting your own thoughts, feelings, and experiences as valid.',

      'Validate someone else': 'Acknowledging and accepting another person\'s thoughts, feelings, and experiences as valid.',

      'Think (non-black-and-white) & act dialectically': 'Seeing the grays instead of just black and white. Recognizing that two things that seem opposite can both be true.',
    };

    return descriptions[skill] ?? 'A valuable DBT skill for managing emotions and difficult situations.';
  }

  String _getWhenToUse(String skill) {
    final whenToUse = {
      'Wise mind': 'When you need to make an important decision and want to balance emotions and logic.',
      'Observe (Notice what\'s going on inside)': 'When you\'re feeling overwhelmed and need to step back from your thoughts and feelings.',
      'Describe (Put words to experience)': 'When you\'re confused about what you\'re feeling or need to communicate it to others.',
      'Participate (Enter the experience)': 'When you want to fully enjoy an activity or connect with others.',
      'Don\'t Judge (Don\'t pass judgement on what is)': 'When you notice you\'re being hard on yourself or others.',
      'Stay Focused (One-mindfully, in-the-moment)': 'When you\'re scattered or distracted and need to focus.',
      'Do what works (Effectiveness)': 'When you\'re more focused on being right than on getting what you need.',
      'Practice loving kindness': 'When you\'re feeling judgmental, angry, or disconnected from yourself or others.',
      'SUNwave or STUNwave': 'When you need a quick mindfulness reset during stress.',
      'Identifying and labeling emotions': 'When you\'re experiencing strong feelings but aren\'t sure what they are.',
      'PLEASE (reduce vulnerability to Emo. Mind)': 'Daily practice to prevent emotional vulnerability.',
      'Accumulating ++ (Pleasant activities)': 'When you\'re feeling down or want to build emotional resilience.',
      'Building Mastery': 'When you need a confidence boost or want to feel accomplished.',
      'Cope-Ahead Plan:': 'When you know a difficult situation is coming up.',
      'Working toward long-term goals': 'When you want to build meaning and purpose in your life.',
      'Building structure and routine they like': 'When life feels chaotic or you\'re struggling with consistency.',
      'Opposite Action to Urges': 'When your emotion doesn\'t fit the facts or acting on it would make things worse.',
      'DEARMAN (Getting what you want)': 'When you need to ask for something or set a boundary.',
      'GIVE (Improving the relationship)': 'When you want to strengthen a relationship or resolve conflict.',
      'FAST (Effective /keeping self-respect)': 'When you need to maintain your self-respect in an interaction.',
      'THINK (Managing others opinions of you)': 'When you\'re worried about what someone thinks of you.',
      'Cheerleading statements': 'When you\'re struggling and need encouragement.',
      'STOP': 'In crisis moments when you need to pause before acting.',
      'TIPP (temp, exercise, breathing, PMR)': 'When you\'re in extreme distress and need to calm down quickly.',
      'ACCEPTS (Distract)': 'When emotions are too intense to address directly.',
      'Self-soothe (5 senses)': 'When you need comfort and are feeling upset.',
      'Pros and cons': 'When deciding whether to tolerate a difficult situation.',
      'IMPROVE': 'When you\'re in a painful moment and want to make it more bearable.',
      'Radical Acceptance': 'When fighting reality is causing you suffering.',
      'Willingness': 'When you notice yourself being stubborn or refusing what needs to be done.',
      'Positive reinforcement': 'After you do something positive to encourage yourself.',
      'Validate self': 'When you\'re being hard on yourself or doubting your feelings.',
      'Validate someone else': 'When someone shares their feelings with you.',
      'Think (non-black-and-white) & act dialectically': 'When you\'re stuck in all-or-nothing thinking or conflict.',
    };

    return whenToUse[skill] ?? 'In situations where you need support managing difficult emotions or situations.';
  }

  String _getHowToUse(String skill) {
    final howToUse = {
      'Wise mind': '1. Notice your emotional response\n2. Notice your logical thoughts\n3. Ask yourself what feels right deep down\n4. Trust your inner wisdom',

      'Observe (Notice what\'s going on inside)': '1. Step back mentally\n2. Notice thoughts like clouds passing\n3. Notice body sensations\n4. Notice without reacting',

      'Describe (Put words to experience)': '1. Notice what you\'re experiencing\n2. Put a label on it ("I\'m feeling anxious")\n3. Describe just the facts, not judgments\n4. Share with someone if needed',

      'Participate (Enter the experience)': '1. Let go of self-consciousness\n2. Throw yourself into the activity\n3. Become one with what you\'re doing\n4. Don\'t worry about how you look',

      'Don\'t Judge (Don\'t pass judgement on what is)': '1. Notice when you use words like "good," "bad," "should"\n2. Replace with neutral descriptions\n3. See things as they are, not as good or bad\n4. Let go of evaluation',

      'Stay Focused (One-mindfully, in-the-moment)': '1. Choose one thing to focus on\n2. When your mind wanders, gently bring it back\n3. Do one thing at a time\n4. Be here now',

      'Do what works (Effectiveness)': '1. Identify your goal\n2. Ask "What will help me reach my goal?"\n3. Let go of being right\n4. Do what works, not what you feel like',

      'Practice loving kindness': '1. Think kind thoughts toward yourself\n2. Extend those thoughts to loved ones\n3. Extend to neutral people\n4. Practice regularly',

      'SUNwave or STUNwave': '1. Smile (even slightly)\n2. Unclench your jaw and fists\n3. Notice your breath\n4. Ride the wave of your breath',

      'Identifying and labeling emotions': '1. Notice you\'re feeling something\n2. Ask "What am I feeling?"\n3. Give it a specific name (angry, sad, anxious)\n4. Notice where you feel it in your body',

      'PLEASE (reduce vulnerability to Emo. Mind)': '1. Treat physical illness promptly\n2. Eat balanced meals\n3. Avoid mood-altering substances\n4. Get enough sleep\n5. Exercise regularly',

      'Accumulating ++ (Pleasant activities)': '1. Make a list of things you enjoy\n2. Schedule one pleasant activity daily\n3. Do it mindfully\n4. Notice positive feelings',

      'Building Mastery': '1. Choose something slightly challenging\n2. Do it step by step\n3. Notice your accomplishment\n4. Celebrate your success',

      'Cope-Ahead Plan:': '1. Imagine the difficult situation\n2. Decide which skills to use\n3. Practice using them in imagination\n4. Review your plan',

      'Working toward long-term goals': '1. Identify what matters to you\n2. Set a specific goal\n3. Break it into small steps\n4. Take one step at a time',

      'Building structure and routine they like': '1. Create a daily schedule\n2. Include self-care activities\n3. Start small and build up\n4. Be flexible but consistent',

      'Opposite Action to Urges': '1. Identify the emotion and urge\n2. Check if the emotion fits the facts\n3. If not, do the opposite of your urge\n4. Do it completely and wholeheartedly',

      'DEARMAN (Getting what you want)': '1. Describe the situation\n2. Express your feelings\n3. Assert what you want\n4. Reinforce (explain benefits)\n5. Stay mindful of your goal\n6. Appear confident\n7. Be willing to negotiate',

      'GIVE (Improving the relationship)': '1. Be gentle (no attacks)\n2. Act interested (listen)\n3. Validate their perspective\n4. Use an easy manner (smile, be calm)',

      'FAST (Effective /keeping self-respect)': '1. Be fair to yourself and others\n2. No unnecessary apologies\n3. Stick to your values\n4. Be truthful',

      'THINK (Managing others opinions of you)': '1. Do I care about this person\'s opinion?\n2. Have empathy for them\n3. Interpret their behavior kindly\n4. Notice the positives\n5. Keep perspective',

      'Cheerleading statements': '1. Prepare some statements ("I can do this")\n2. Say them when struggling\n3. Make them personal and believable\n4. Repeat as needed',

      'STOP': '1. Stop - freeze\n2. Take a step back - physically or mentally\n3. Observe - notice what\'s happening\n4. Proceed mindfully - choose your action',

      'TIPP (temp, exercise, breathing, PMR)': '1. Use cold water on your face OR\n2. Do intense exercise OR\n3. Practice paced breathing OR\n4. Do progressive muscle relaxation',

      'ACCEPTS (Distract)': '1. Choose a distraction method\n2. Fully engage in it\n3. Use until emotions are less intense\n4. Return to problem-solving when ready',

      'Self-soothe (5 senses)': '1. Choose a sense to focus on\n2. Find something pleasant for that sense\n3. Fully experience it\n4. Notice the comfort it brings',

      'Pros and cons': '1. List pros of tolerating distress\n2. List cons of tolerating distress\n3. List pros of not tolerating\n4. List cons of not tolerating\n5. Review and decide',

      'IMPROVE': '1. Choose one or more methods\n2. Use imagery, find meaning, pray, relax\n3. Focus on one thing, take a break, or encourage yourself\n4. Stay with it until the moment improves',

      'Radical Acceptance': '1. Notice you\'re fighting reality\n2. Remind yourself "It is what it is"\n3. Relax your body\n4. Accept with your whole self',

      'Willingness': '1. Notice willfulness (refusing, giving up)\n2. Ask "What\'s needed here?"\n3. Do it willingly, even if you don\'t feel like it\n4. Half-smile and be gentle',

      'Positive reinforcement': '1. Notice positive behavior\n2. Give yourself a reward\n3. Make it immediate and meaningful\n4. Do it consistently',

      'Validate self': '1. Notice your feelings\n2. Say "It makes sense that I feel this way"\n3. Don\'t judge yourself for feeling\n4. Treat yourself with kindness',

      'Validate someone else': '1. Listen without judgment\n2. Acknowledge their feelings\n3. Say it makes sense given the situation\n4. Show you understand',

      'Think (non-black-and-white) & act dialectically': '1. Notice extreme thinking ("always," "never")\n2. Look for the middle ground\n3. Find what\'s true on both sides\n4. Hold multiple truths at once',
    };

    return howToUse[skill] ?? '1. Notice when you need this skill\n2. Practice it step by step\n3. Be patient with yourself\n4. Use it regularly to build the habit';
  }
}
