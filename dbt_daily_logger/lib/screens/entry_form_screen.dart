import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:provider/provider.dart';
import '../models/diary_entry.dart';
import '../models/dbt_constants.dart';
import '../services/diary_service.dart';
import '../widgets/emotion_tracker.dart';
import '../widgets/skills_selector.dart';
import '../widgets/urge_tracker.dart';
import '../widgets/behavior_selector.dart';

class EntryFormScreen extends StatefulWidget {
  final DateTime date;
  final DiaryEntry? existingEntry;

  const EntryFormScreen({
    super.key,
    required this.date,
    this.existingEntry,
  });

  @override
  State<EntryFormScreen> createState() => _EntryFormScreenState();
}

class _EntryFormScreenState extends State<EntryFormScreen> {
  late DateTime _selectedDate;
  final Map<String, int> _emotions = {};
  final Map<String, int> _urges = {};
  final List<String> _skillsUsed = [];
  final List<String> _targetBehaviors = [];
  final TextEditingController _notesController = TextEditingController();
  int? _sleepHours;
  bool? _tookMedication;

  @override
  void initState() {
    super.initState();
    _selectedDate = widget.date;

    if (widget.existingEntry != null) {
      _loadExistingEntry(widget.existingEntry!);
    }
  }

  void _loadExistingEntry(DiaryEntry entry) {
    _emotions.addAll(entry.emotions);
    _urges.addAll(entry.urges);
    _skillsUsed.addAll(entry.skillsUsed);
    _targetBehaviors.addAll(entry.targetBehaviors);
    _notesController.text = entry.notes;
    _sleepHours = entry.sleepHours;
    _tookMedication = entry.tookMedication;
  }

  @override
  void dispose() {
    _notesController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final dateFormat = DateFormat('EEEE, MMMM d, y');

    return Scaffold(
      appBar: AppBar(
        title: Text(widget.existingEntry == null ? 'New Entry' : 'Edit Entry'),
        actions: [
          TextButton(
            onPressed: _saveEntry,
            child: const Text('Save'),
          ),
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          // Date selection
          Card(
            child: ListTile(
              leading: const Icon(Icons.calendar_today),
              title: const Text('Date'),
              subtitle: Text(dateFormat.format(_selectedDate)),
              trailing: const Icon(Icons.chevron_right),
              onTap: _selectDate,
            ),
          ),
          const SizedBox(height: 16),

          // Sleep and medication
          Card(
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Daily Basics',
                    style: Theme.of(context).textTheme.titleMedium?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                  ),
                  const SizedBox(height: 16),
                  Row(
                    children: [
                      Expanded(
                        child: DropdownButtonFormField<int>(
                          decoration: const InputDecoration(
                            labelText: 'Hours of sleep',
                            prefixIcon: Icon(Icons.bedtime),
                          ),
                          value: _sleepHours,
                          items: List.generate(
                            25,
                            (index) => DropdownMenuItem(
                              value: index,
                              child: Text('$index hours'),
                            ),
                          ),
                          onChanged: (value) {
                            setState(() {
                              _sleepHours = value;
                            });
                          },
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 16),
                  CheckboxListTile(
                    title: const Text('Took medication as prescribed'),
                    value: _tookMedication ?? false,
                    onChanged: (value) {
                      setState(() {
                        _tookMedication = value;
                      });
                    },
                    contentPadding: EdgeInsets.zero,
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(height: 16),

          // Emotions section
          _buildSectionCard(
            title: 'Emotions',
            icon: Icons.mood,
            child: EmotionTracker(
              emotions: _emotions,
              onChanged: (emotions) {
                setState(() {
                  _emotions.clear();
                  _emotions.addAll(emotions);
                });
              },
            ),
          ),
          const SizedBox(height: 16),

          // Urges section
          _buildSectionCard(
            title: 'Urges',
            icon: Icons.warning_amber_rounded,
            child: UrgeTracker(
              urges: _urges,
              onChanged: (urges) {
                setState(() {
                  _urges.clear();
                  _urges.addAll(urges);
                });
              },
            ),
          ),
          const SizedBox(height: 16),

          // Target behaviors
          _buildSectionCard(
            title: 'Target Behaviors',
            icon: Icons.flag,
            child: BehaviorSelector(
              selectedBehaviors: _targetBehaviors,
              onChanged: (behaviors) {
                setState(() {
                  _targetBehaviors.clear();
                  _targetBehaviors.addAll(behaviors);
                });
              },
            ),
          ),
          const SizedBox(height: 16),

          // Skills used
          _buildSectionCard(
            title: 'DBT Skills Used',
            icon: Icons.psychology,
            child: SkillsSelector(
              selectedSkills: _skillsUsed,
              onChanged: (skills) {
                setState(() {
                  _skillsUsed.clear();
                  _skillsUsed.addAll(skills);
                });
              },
            ),
          ),
          const SizedBox(height: 16),

          // Notes section
          _buildSectionCard(
            title: 'Notes',
            icon: Icons.note,
            child: TextField(
              controller: _notesController,
              maxLines: 5,
              decoration: const InputDecoration(
                hintText: 'Add any additional notes here...',
                border: OutlineInputBorder(),
              ),
            ),
          ),
          const SizedBox(height: 32),
        ],
      ),
    );
  }

  Widget _buildSectionCard({
    required String title,
    required IconData icon,
    required Widget child,
  }) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(icon, size: 20),
                const SizedBox(width: 8),
                Text(
                  title,
                  style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                ),
              ],
            ),
            const SizedBox(height: 16),
            child,
          ],
        ),
      ),
    );
  }

  Future<void> _selectDate() async {
    final picked = await showDatePicker(
      context: context,
      initialDate: _selectedDate,
      firstDate: DateTime(2020),
      lastDate: DateTime.now(),
    );

    if (picked != null) {
      setState(() {
        _selectedDate = picked;
      });
    }
  }

  Future<void> _saveEntry() async {
    final diaryService = Provider.of<DiaryService>(context, listen: false);

    final entry = DiaryEntry(
      date: _selectedDate,
      emotions: Map.from(_emotions),
      urges: Map.from(_urges),
      targetBehaviors: List.from(_targetBehaviors),
      skillsUsed: List.from(_skillsUsed),
      notes: _notesController.text,
      sleepHours: _sleepHours,
      tookMedication: _tookMedication,
    );

    await diaryService.saveEntry(entry);

    if (mounted) {
      Navigator.pop(context, true);
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Entry saved')),
      );
    }
  }
}
