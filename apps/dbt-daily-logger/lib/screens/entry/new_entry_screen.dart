import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:intl/intl.dart';
import '../../models/diary_entry.dart';
import '../../models/dbt_skills.dart';
import '../../providers/auth_provider.dart';
import '../../providers/entries_provider.dart';
import '../../widgets/emotion_slider.dart';
import '../../widgets/behavior_selector.dart';
import '../../widgets/skills_selector.dart';
import '../../widgets/sleep_tracker.dart';

/// Screen for creating a new diary entry
class NewEntryScreen extends StatefulWidget {
  final DateTime? initialDate;

  const NewEntryScreen({super.key, this.initialDate});

  @override
  State<NewEntryScreen> createState() => _NewEntryScreenState();
}

class _NewEntryScreenState extends State<NewEntryScreen> {
  late DateTime _selectedDate;
  final Map<String, int> _emotions = {};
  final Map<String, int> _urges = {};
  final Map<String, int> _behaviors = {};
  final Set<String> _skillsUsed = {};
  double? _sleepHours;
  int? _sleepQuality;
  bool _exercised = false;
  bool _tookMedication = false;
  final TextEditingController _notesController = TextEditingController();
  bool _isSaving = false;

  @override
  void initState() {
    super.initState();
    _selectedDate = widget.initialDate ?? DateTime.now();
  }

  @override
  void dispose() {
    _notesController.dispose();
    super.dispose();
  }

  Future<void> _selectDate(BuildContext context) async {
    final DateTime? picked = await showDatePicker(
      context: context,
      initialDate: _selectedDate,
      firstDate: DateTime.now().subtract(const Duration(days: 365)),
      lastDate: DateTime.now(),
    );
    if (picked != null && picked != _selectedDate) {
      setState(() {
        _selectedDate = picked;
      });
    }
  }

  Future<void> _saveEntry() async {
    final authProvider = Provider.of<AuthProvider>(context, listen: false);
    final entriesProvider = Provider.of<EntriesProvider>(context, listen: false);

    if (authProvider.user == null) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('You must be logged in to save entries')),
        );
      }
      return;
    }

    setState(() {
      _isSaving = true;
    });

    try {
      final entry = DiaryEntry.empty(
        userId: authProvider.user!.uid,
        date: _selectedDate,
      ).copyWith(
        emotions: _emotions,
        urges: _urges,
        behaviors: _behaviors,
        skillsUsed: _skillsUsed.toList(),
        sleepHours: _sleepHours,
        sleepQuality: _sleepQuality,
        exercised: _exercised,
        tookMedication: _tookMedication,
        notes: _notesController.text.isEmpty ? null : _notesController.text,
      );

      await entriesProvider.createEntry(entry);

      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('Entry saved successfully!')),
        );
        Navigator.of(context).pop();
      }
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Failed to save entry: $e')),
        );
      }
    } finally {
      if (mounted) {
        setState(() {
          _isSaving = false;
        });
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final dateFormat = DateFormat('EEEE, MMMM d, yyyy');

    return Scaffold(
      appBar: AppBar(
        title: const Text('New Entry'),
        actions: [
          TextButton(
            onPressed: _isSaving ? null : _saveEntry,
            child: _isSaving
                ? const SizedBox(
                    width: 20,
                    height: 20,
                    child: CircularProgressIndicator(strokeWidth: 2),
                  )
                : const Text('Save'),
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Date selector
            Card(
              child: ListTile(
                leading: const Icon(Icons.calendar_today),
                title: const Text('Entry Date'),
                subtitle: Text(dateFormat.format(_selectedDate)),
                trailing: const Icon(Icons.edit),
                onTap: () => _selectDate(context),
              ),
            ),
            const SizedBox(height: 24),

            // Emotions Section
            _buildSectionHeader('How are you feeling?', Icons.sentiment_satisfied),
            const SizedBox(height: 12),
            EmotionSlider(
              emotions: _emotions,
              onChanged: (emotions) {
                setState(() {
                  _emotions.clear();
                  _emotions.addAll(emotions);
                });
              },
            ),
            const SizedBox(height: 24),

            // Urges Section
            _buildSectionHeader('Urges', Icons.warning_amber),
            const SizedBox(height: 12),
            EmotionSlider(
              emotions: _urges,
              onChanged: (urges) {
                setState(() {
                  _urges.clear();
                  _urges.addAll(urges);
                });
              },
              customLabels: const ['Self-harm', 'Substance use', 'Avoid'],
            ),
            const SizedBox(height: 24),

            // Behaviors Section
            _buildSectionHeader('Target Behaviors', Icons.track_changes),
            const SizedBox(height: 12),
            BehaviorSelector(
              behaviors: _behaviors,
              onChanged: (behaviors) {
                setState(() {
                  _behaviors.clear();
                  _behaviors.addAll(behaviors);
                });
              },
            ),
            const SizedBox(height: 24),

            // DBT Skills Section
            _buildSectionHeader('DBT Skills Used', Icons.psychology),
            const SizedBox(height: 12),
            SkillsSelector(
              selectedSkills: _skillsUsed,
              onChanged: (skills) {
                setState(() {
                  _skillsUsed.clear();
                  _skillsUsed.addAll(skills);
                });
              },
            ),
            const SizedBox(height: 24),

            // Sleep & Self-Care Section
            _buildSectionHeader('Sleep & Self-Care', Icons.bedtime),
            const SizedBox(height: 12),
            SleepTracker(
              sleepHours: _sleepHours,
              sleepQuality: _sleepQuality,
              exercised: _exercised,
              onSleepHoursChanged: (hours) {
                setState(() {
                  _sleepHours = hours;
                });
              },
              onSleepQualityChanged: (quality) {
                setState(() {
                  _sleepQuality = quality;
                });
              },
              onExercisedChanged: (value) {
                setState(() {
                  _exercised = value;
                });
              },
            ),
            const SizedBox(height: 16),

            // Medication
            Card(
              child: CheckboxListTile(
                title: const Text('Took medication'),
                value: _tookMedication,
                onChanged: (value) {
                  setState(() {
                    _tookMedication = value ?? false;
                  });
                },
                secondary: const Icon(Icons.medication),
              ),
            ),
            const SizedBox(height: 24),

            // Notes Section
            _buildSectionHeader('Notes', Icons.note),
            const SizedBox(height: 12),
            Card(
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: TextField(
                  controller: _notesController,
                  maxLines: 5,
                  decoration: const InputDecoration(
                    hintText: 'Add any additional notes here...',
                    border: OutlineInputBorder(),
                  ),
                ),
              ),
            ),
            const SizedBox(height: 32),

            // Save Button (bottom)
            SizedBox(
              width: double.infinity,
              child: FilledButton.icon(
                onPressed: _isSaving ? null : _saveEntry,
                icon: _isSaving
                    ? const SizedBox(
                        width: 20,
                        height: 20,
                        child: CircularProgressIndicator(
                          strokeWidth: 2,
                          color: Colors.white,
                        ),
                      )
                    : const Icon(Icons.save),
                label: Text(_isSaving ? 'Saving...' : 'Save Entry'),
                style: FilledButton.styleFrom(
                  padding: const EdgeInsets.symmetric(vertical: 16),
                ),
              ),
            ),
            const SizedBox(height: 16),
          ],
        ),
      ),
    );
  }

  Widget _buildSectionHeader(String title, IconData icon) {
    return Row(
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
    );
  }
}
