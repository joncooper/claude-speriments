import 'dart:math';
import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import '../services/simple_storage.dart';
import '../widgets/emoji_rating_scale.dart';
import '../models/dbt_skills.dart';

class NewDailyEntryScreen extends StatefulWidget {
  final DateTime date;

  NewDailyEntryScreen({super.key, DateTime? date})
      : date = date ?? DateTime.now();

  @override
  State<NewDailyEntryScreen> createState() => _NewDailyEntryScreenState();
}

// Behavior definitions from physical card
class BehaviorDefinition {
  final String key;
  final String label;
  final Color color;
  final List<String> emojis;

  const BehaviorDefinition({
    required this.key,
    required this.label,
    required this.color,
    this.emojis = const ['😌', '🙂', '😐', '😟', '😰', '😱'],
  });
}

// Emotion definitions from physical card
class EmotionDefinition {
  final String key;
  final String label;
  final Color color;
  final List<String> emojis;

  const EmotionDefinition({
    required this.key,
    required this.label,
    required this.color,
    required this.emojis,
  });
}

class _NewDailyEntryScreenState extends State<NewDailyEntryScreen> {
  late DailyEntryData entry;
  final PageController _pageController = PageController();
  int _currentPage = 0;

  // All behaviors from physical card
  static const List<BehaviorDefinition> _allBehaviors = [
    BehaviorDefinition(
      key: 'si',
      label: 'SI',
      color: Colors.red,
      emojis: ['😌', '🤔', '😐', '😟', '😰', '😱'],
    ),
    BehaviorDefinition(
      key: 'nssi',
      label: 'NSSI',
      color: Colors.deepOrange,
      emojis: ['😌', '🤔', '😐', '😟', '😰', '😱'],
    ),
    BehaviorDefinition(
      key: 'familyConflict',
      label: 'Family conflict',
      color: Colors.orange,
    ),
    BehaviorDefinition(
      key: 'isolate',
      label: 'Isolate',
      color: Colors.blue,
    ),
    BehaviorDefinition(
      key: 'avoidProcrast',
      label: 'Avoid/Procrast',
      color: Colors.purple,
    ),
    BehaviorDefinition(
      key: 'withhold',
      label: 'Withhold',
      color: Colors.indigo,
    ),
    BehaviorDefinition(
      key: 'substUse',
      label: 'Subst. Use',
      color: Colors.brown,
    ),
  ];

  // All emotions from physical card
  static const List<EmotionDefinition> _allEmotions = [
    EmotionDefinition(
      key: 'anger',
      label: 'Anger',
      color: Colors.red,
      emojis: ['😌', '😠', '😤', '😡', '🤬', '💢'],
    ),
    EmotionDefinition(
      key: 'fearAnxiety',
      label: 'Fear/Anxiety',
      color: Colors.purple,
      emojis: ['😌', '😕', '😟', '😨', '😰', '😱'],
    ),
    EmotionDefinition(
      key: 'joy',
      label: 'Joy',
      color: Color(0xFFFBC02D), // yellow.shade700
      emojis: ['😐', '🙂', '😊', '😄', '😁', '🤩'],
    ),
    EmotionDefinition(
      key: 'sadness',
      label: 'Sadness',
      color: Colors.blue,
      emojis: ['😌', '🙁', '😔', '😢', '😭', '💔'],
    ),
    EmotionDefinition(
      key: 'guilt',
      label: 'Guilt',
      color: Colors.teal,
      emojis: ['😌', '😕', '😟', '😣', '😖', '😞'],
    ),
    EmotionDefinition(
      key: 'shame',
      label: 'Shame',
      color: Colors.pink,
      emojis: ['😌', '😳', '😔', '😣', '😖', '🫣'],
    ),
  ];

  late List<BehaviorDefinition> _randomizedBehaviors;
  late List<EmotionDefinition> _randomizedEmotions;

  @override
  void initState() {
    super.initState();

    // Randomize order to avoid sequencing bias
    final random = Random();
    _randomizedBehaviors = List.from(_allBehaviors)..shuffle(random);
    _randomizedEmotions = List.from(_allEmotions)..shuffle(random);

    entry = DailyEntryData(date: widget.date);
    _loadEntry();
  }

  Future<void> _loadEntry() async {
    final existing = await SimpleStorage.getEntryForDate(widget.date);
    if (existing != null && mounted) {
      setState(() {
        entry = existing;
      });
    }
  }

  Future<void> _saveEntry() async {
    await SimpleStorage.saveEntry(entry);
    if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('✨ Entry saved!'),
          backgroundColor: Colors.teal,
          duration: Duration(seconds: 2),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final pages = _buildPages();

    return Scaffold(
      appBar: AppBar(
        title: Column(
          children: [
            const Text('Daily Check-In', style: TextStyle(fontSize: 18)),
            Text(
              DateFormat('EEEE, MMM d').format(widget.date),
              style: const TextStyle(fontSize: 14, fontWeight: FontWeight.w400),
            ),
          ],
        ),
        centerTitle: true,
        actions: [
          TextButton.icon(
            onPressed: _saveEntry,
            icon: const Icon(Icons.check, color: Colors.white),
            label: const Text('Save', style: TextStyle(color: Colors.white)),
          ),
        ],
      ),
      body: Column(
        children: [
          // Progress indicator
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
            child: Row(
              children: [
                Expanded(
                  child: LinearProgressIndicator(
                    value: (_currentPage + 1) / pages.length,
                    backgroundColor: Colors.grey[200],
                    valueColor: const AlwaysStoppedAnimation<Color>(Colors.teal),
                    minHeight: 8,
                    borderRadius: BorderRadius.circular(4),
                  ),
                ),
                const SizedBox(width: 12),
                Text(
                  '${_currentPage + 1}/${pages.length}',
                  style: const TextStyle(fontWeight: FontWeight.bold),
                ),
              ],
            ),
          ),

          // Swipeable pages
          Expanded(
            child: PageView(
              controller: _pageController,
              onPageChanged: (index) {
                setState(() {
                  _currentPage = index;
                });
              },
              children: pages,
            ),
          ),

          // Navigation buttons
          Container(
            padding: const EdgeInsets.all(16),
            child: Row(
              children: [
                if (_currentPage > 0)
                  Expanded(
                    child: OutlinedButton.icon(
                      onPressed: () {
                        _pageController.previousPage(
                          duration: const Duration(milliseconds: 300),
                          curve: Curves.easeInOut,
                        );
                      },
                      icon: const Icon(Icons.arrow_back),
                      label: const Text('Back'),
                    ),
                  ),
                if (_currentPage > 0) const SizedBox(width: 12),
                Expanded(
                  child: ElevatedButton.icon(
                    onPressed: () async {
                      if (_currentPage < pages.length - 1) {
                        _pageController.nextPage(
                          duration: const Duration(milliseconds: 300),
                          curve: Curves.easeInOut,
                        );
                      } else {
                        await _saveEntry();
                        if (mounted) {
                          Navigator.pop(context);
                        }
                      }
                    },
                    icon: Icon(_currentPage < pages.length - 1
                        ? Icons.arrow_forward
                        : Icons.check),
                    label: Text(_currentPage < pages.length - 1 ? 'Next' : 'Done'),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  List<Widget> _buildPages() {
    return [
      _buildBehaviorsPage(),
      _buildEmotionsPage(),
      _buildSleepAndMedsPage(),
      _buildSkillsPage(),
      _buildNotesPage(),
    ];
  }

  Widget _buildBehaviorsPage() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            '💭 How did today go?',
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 8),
          Text(
            'Rate these behaviors (0 = not at all, 5 = a lot)',
            style: TextStyle(color: Colors.grey[600]),
          ),
          const SizedBox(height: 24),

          // Generate rating scales from randomized behaviors
          ..._randomizedBehaviors.expand((behavior) => [
            EmojiRatingScale(
              label: behavior.label,
              value: entry.behaviors[behavior.key],
              onChanged: (val) => setState(() => entry.behaviors[behavior.key] = val),
              color: behavior.color,
              emojis: behavior.emojis,
            ),
            const SizedBox(height: 20),
          ]),
        ],
      ),
    );
  }

  Widget _buildEmotionsPage() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            '💖 How are you feeling?',
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 24),

          // Generate rating scales from randomized emotions
          ..._randomizedEmotions.expand((emotion) => [
            EmojiRatingScale(
              label: emotion.label,
              value: entry.emotions[emotion.key],
              onChanged: (val) => setState(() => entry.emotions[emotion.key] = val),
              color: emotion.color,
              emojis: emotion.emojis,
            ),
            const SizedBox(height: 20),
          ]),
        ],
      ),
    );
  }

  Widget _buildSleepAndMedsPage() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            '😴 Sleep & Self-Care',
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 24),

          // Hours of Sleep
          Card(
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      const Text(
                        '🛌 Hours of sleep',
                        style: TextStyle(fontSize: 16, fontWeight: FontWeight.w500),
                      ),
                      Text(
                        entry.hoursOfSleep != null
                            ? '${entry.hoursOfSleep!.toStringAsFixed(1)} hours'
                            : 'Not set',
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                          color: Colors.teal,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 8),
                  Slider(
                    value: entry.hoursOfSleep ?? 7.0,
                    min: 0,
                    max: 12,
                    divisions: 24,
                    label: entry.hoursOfSleep?.toStringAsFixed(1) ?? '7.0',
                    onChanged: (val) => setState(() => entry.hoursOfSleep = val),
                    activeColor: Colors.teal,
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(height: 16),

          // Sleep Quality
          EmojiRatingScale(
            label: 'Sleep quality',
            value: entry.sleepQuality,
            onChanged: (val) => setState(() => entry.sleepQuality = val),
            color: Colors.indigo,
            emojis: const ['😫', '😴', '😐', '🙂', '😊', '🌟'],
          ),
          const SizedBox(height: 16),

          // Exercise
          Card(
            child: SwitchListTile(
              title: const Text('🏃 Exercised today'),
              subtitle: const Text('Any physical activity'),
              value: entry.exercised ?? false,
              onChanged: (val) => setState(() => entry.exercised = val),
              activeColor: Colors.teal,
            ),
          ),
          const SizedBox(height: 16),

          // Medication
          Card(
            child: SwitchListTile(
              title: const Text('💊 Took medication today'),
              subtitle: const Text('As prescribed'),
              value: entry.tookMeds ?? false,
              onChanged: (val) => setState(() => entry.tookMeds = val),
              activeColor: Colors.teal,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSkillsPage() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            '✨ DBT Skills Used Today',
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 8),
          Text(
            'Check off any skills you practiced',
            style: TextStyle(color: Colors.grey[600]),
          ),
          const SizedBox(height: 24),

          // Build skills by category with expandable sections
          ...DBTSkills.allSkillsByCategory.entries.map((category) {
            return Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Padding(
                  padding: const EdgeInsets.only(bottom: 12, top: 8),
                  child: Text(
                    category.key,
                    style: const TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                      color: Colors.teal,
                    ),
                  ),
                ),
                ...category.value.map((skill) {
                  return CheckboxListTile(
                    title: Text(skill),
                    value: entry.skillsUsedToday.contains(skill),
                    onChanged: (val) {
                      setState(() {
                        if (val == true) {
                          entry.skillsUsedToday.add(skill);
                        } else {
                          entry.skillsUsedToday.remove(skill);
                        }
                      });
                    },
                    activeColor: Colors.teal,
                    dense: true,
                    contentPadding: const EdgeInsets.symmetric(horizontal: 8),
                  );
                }),
                const SizedBox(height: 16),
              ],
            );
          }),
        ],
      ),
    );
  }

  Widget _buildNotesPage() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            '📝 Anything else?',
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 8),
          Text(
            'Write down anything you want to remember about today',
            style: TextStyle(color: Colors.grey[600]),
          ),
          const SizedBox(height: 24),

          TextField(
            maxLines: 10,
            decoration: InputDecoration(
              hintText: 'What happened today? How are you feeling? What helped?',
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(12),
              ),
              filled: true,
            ),
            onChanged: (val) => entry.notes = val,
            controller: TextEditingController(text: entry.notes),
          ),
        ],
      ),
    );
  }
}
