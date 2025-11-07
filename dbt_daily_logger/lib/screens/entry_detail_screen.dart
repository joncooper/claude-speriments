import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import '../models/diary_entry.dart';
import '../models/dbt_constants.dart';
import 'entry_form_screen.dart';

class EntryDetailScreen extends StatelessWidget {
  final DiaryEntry entry;

  const EntryDetailScreen({
    super.key,
    required this.entry,
  });

  @override
  Widget build(BuildContext context) {
    final dateFormat = DateFormat('EEEE, MMMM d, y');

    return Scaffold(
      appBar: AppBar(
        title: const Text('Entry Details'),
        actions: [
          IconButton(
            icon: const Icon(Icons.edit),
            onPressed: () => _editEntry(context),
          ),
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          // Date
          Card(
            child: ListTile(
              leading: const Icon(Icons.calendar_today),
              title: const Text('Date'),
              subtitle: Text(dateFormat.format(entry.date)),
            ),
          ),
          const SizedBox(height: 16),

          // Daily basics
          if (entry.sleepHours != null || entry.tookMedication != null) ...[
            Card(
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'Daily Basics',
                      style:
                          Theme.of(context).textTheme.titleMedium?.copyWith(
                                fontWeight: FontWeight.bold,
                              ),
                    ),
                    const SizedBox(height: 12),
                    if (entry.sleepHours != null) ...[
                      _buildInfoRow(
                        Icons.bedtime,
                        'Sleep',
                        '${entry.sleepHours} hours',
                      ),
                    ],
                    if (entry.tookMedication != null) ...[
                      const SizedBox(height: 8),
                      _buildInfoRow(
                        Icons.medication,
                        'Medication',
                        entry.tookMedication! ? 'Taken' : 'Not taken',
                      ),
                    ],
                  ],
                ),
              ),
            ),
            const SizedBox(height: 16),
          ],

          // Emotions
          if (entry.emotions.isNotEmpty) ...[
            _buildDetailCard(
              context,
              'Emotions',
              Icons.mood,
              Colors.blue,
              Column(
                children: entry.emotions.entries
                    .map((e) => _buildIntensityRow(e.key, e.value))
                    .toList(),
              ),
            ),
            const SizedBox(height: 16),
          ],

          // Urges
          if (entry.urges.isNotEmpty) ...[
            _buildDetailCard(
              context,
              'Urges',
              Icons.warning_amber_rounded,
              Colors.orange,
              Column(
                children: entry.urges.entries
                    .map((e) => _buildIntensityRow(e.key, e.value))
                    .toList(),
              ),
            ),
            const SizedBox(height: 16),
          ],

          // Target behaviors
          if (entry.targetBehaviors.isNotEmpty) ...[
            _buildDetailCard(
              context,
              'Target Behaviors',
              Icons.flag,
              Colors.red,
              Wrap(
                spacing: 8,
                runSpacing: 8,
                children: entry.targetBehaviors
                    .map((behavior) => Chip(
                          label: Text(behavior),
                          backgroundColor: Colors.red[50],
                        ))
                    .toList(),
              ),
            ),
            const SizedBox(height: 16),
          ],

          // Skills used
          if (entry.skillsUsed.isNotEmpty) ...[
            _buildDetailCard(
              context,
              'DBT Skills Used',
              Icons.psychology,
              Colors.green,
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: _buildSkillsByModule(),
              ),
            ),
            const SizedBox(height: 16),
          ],

          // Notes
          if (entry.notes.isNotEmpty) ...[
            _buildDetailCard(
              context,
              'Notes',
              Icons.note,
              Colors.purple,
              Text(
                entry.notes,
                style: const TextStyle(fontSize: 16),
              ),
            ),
          ],
        ],
      ),
    );
  }

  Widget _buildDetailCard(
    BuildContext context,
    String title,
    IconData icon,
    Color color,
    Widget content,
  ) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(icon, color: color, size: 20),
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
            content,
          ],
        ),
      ),
    );
  }

  Widget _buildIntensityRow(String label, int intensity) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: Row(
        children: [
          Expanded(
            flex: 2,
            child: Text(label, style: const TextStyle(fontSize: 16)),
          ),
          Expanded(
            flex: 3,
            child: Row(
              children: [
                Expanded(
                  child: LinearProgressIndicator(
                    value: intensity / 10,
                    backgroundColor: Colors.grey[200],
                    minHeight: 8,
                  ),
                ),
                const SizedBox(width: 8),
                SizedBox(
                  width: 30,
                  child: Text(
                    '$intensity',
                    style: const TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 16,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildInfoRow(IconData icon, String label, String value) {
    return Row(
      children: [
        Icon(icon, size: 20),
        const SizedBox(width: 12),
        Text(
          '$label: ',
          style: const TextStyle(fontWeight: FontWeight.bold),
        ),
        Text(value),
      ],
    );
  }

  List<Widget> _buildSkillsByModule() {
    final skillsByModule = <String, List<String>>{};

    for (var skill in entry.skillsUsed) {
      final module = DBTSkills.getModuleForSkill(skill) ?? 'Other';
      skillsByModule.putIfAbsent(module, () => []).add(skill);
    }

    final widgets = <Widget>[];
    for (var moduleEntry in skillsByModule.entries) {
      widgets.add(
        Padding(
          padding: const EdgeInsets.only(bottom: 8),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                moduleEntry.key,
                style: const TextStyle(
                  fontWeight: FontWeight.bold,
                  fontSize: 14,
                ),
              ),
              const SizedBox(height: 4),
              Wrap(
                spacing: 8,
                runSpacing: 8,
                children: moduleEntry.value
                    .map((skill) => Chip(
                          label: Text(skill, style: const TextStyle(fontSize: 12)),
                          backgroundColor: Colors.green[50],
                          visualDensity: VisualDensity.compact,
                        ))
                    .toList(),
              ),
            ],
          ),
        ),
      );
    }

    return widgets;
  }

  Future<void> _editEntry(BuildContext context) async {
    final result = await Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => EntryFormScreen(
          date: entry.date,
          existingEntry: entry,
        ),
      ),
    );

    if (result == true && context.mounted) {
      Navigator.pop(context, true);
    }
  }
}
