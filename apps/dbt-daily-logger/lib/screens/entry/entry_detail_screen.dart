import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:intl/intl.dart';
import '../../models/diary_entry.dart';
import '../../models/dbt_skills.dart';
import '../../providers/entries_provider.dart';
import '../../providers/auth_provider.dart';
import 'edit_entry_screen.dart';

/// Screen for viewing entry details
class EntryDetailScreen extends StatelessWidget {
  final DiaryEntry entry;

  const EntryDetailScreen({super.key, required this.entry});

  Future<void> _deleteEntry(BuildContext context) async {
    final confirmed = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Delete Entry'),
        content: const Text('Are you sure you want to delete this entry? This cannot be undone.'),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(false),
            child: const Text('Cancel'),
          ),
          FilledButton(
            onPressed: () => Navigator.of(context).pop(true),
            style: FilledButton.styleFrom(
              backgroundColor: Theme.of(context).colorScheme.error,
            ),
            child: const Text('Delete'),
          ),
        ],
      ),
    );

    if (confirmed == true && context.mounted) {
      final authProvider = Provider.of<AuthProvider>(context, listen: false);
      final entriesProvider = Provider.of<EntriesProvider>(context, listen: false);

      try {
        await entriesProvider.deleteEntry(authProvider.user!.uid, entry.id);

        if (context.mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Entry deleted')),
          );
          Navigator.of(context).pop(); // Go back to list
        }
      } catch (e) {
        if (context.mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(content: Text('Failed to delete: $e')),
          );
        }
      }
    }
  }

  void _editEntry(BuildContext context) {
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) => EditEntryScreen(entry: entry),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final dateFormat = DateFormat('EEEE, MMMM d, yyyy');
    final timeFormat = DateFormat('h:mm a');

    return Scaffold(
      appBar: AppBar(
        title: const Text('Entry Details'),
        actions: [
          IconButton(
            icon: const Icon(Icons.edit),
            onPressed: () => _editEntry(context),
            tooltip: 'Edit',
          ),
          IconButton(
            icon: const Icon(Icons.delete),
            onPressed: () => _deleteEntry(context),
            tooltip: 'Delete',
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Date
            Card(
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Row(
                  children: [
                    Icon(Icons.calendar_today, color: theme.colorScheme.primary),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            dateFormat.format(entry.date),
                            style: theme.textTheme.titleMedium?.copyWith(
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          Text(
                            'Logged at ${timeFormat.format(entry.createdAt)}',
                            style: theme.textTheme.bodySmall?.copyWith(
                              color: theme.colorScheme.onSurface.withOpacity(0.6),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 16),

            // Emotions
            if (entry.emotions.isNotEmpty) ...[
              _buildSectionHeader(context, 'Emotions', Icons.sentiment_satisfied),
              const SizedBox(height: 8),
              Card(
                child: Padding(
                  padding: const EdgeInsets.all(16),
                  child: Column(
                    children: entry.emotions.entries.map((e) {
                      return _buildRatingRow(context, e.key, e.value);
                    }).toList(),
                  ),
                ),
              ),
              const SizedBox(height: 16),
            ],

            // Urges
            if (entry.urges.isNotEmpty) ...[
              _buildSectionHeader(context, 'Urges', Icons.warning_amber),
              const SizedBox(height: 8),
              Card(
                child: Padding(
                  padding: const EdgeInsets.all(16),
                  child: Column(
                    children: entry.urges.entries.map((e) {
                      return _buildRatingRow(context, e.key, e.value);
                    }).toList(),
                  ),
                ),
              ),
              const SizedBox(height: 16),
            ],

            // Behaviors
            if (entry.behaviors.isNotEmpty) ...[
              _buildSectionHeader(context, 'Target Behaviors', Icons.track_changes),
              const SizedBox(height: 8),
              Card(
                child: Padding(
                  padding: const EdgeInsets.all(16),
                  child: Column(
                    children: entry.behaviors.entries.map((e) {
                      return _buildCountRow(context, e.key, e.value);
                    }).toList(),
                  ),
                ),
              ),
              const SizedBox(height: 16),
            ],

            // Skills
            if (entry.skillsUsed.isNotEmpty) ...[
              _buildSectionHeader(context, 'DBT Skills Used', Icons.psychology),
              const SizedBox(height: 8),
              Card(
                child: Padding(
                  padding: const EdgeInsets.all(16),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: _buildSkillsGrouped(context),
                  ),
                ),
              ),
              const SizedBox(height: 16),
            ],

            // Sleep & Self-Care
            if (entry.sleepHours != null || entry.sleepQuality != null || entry.exercised != null) ...[
              _buildSectionHeader(context, 'Sleep & Self-Care', Icons.bedtime),
              const SizedBox(height: 8),
              Card(
                child: Padding(
                  padding: const EdgeInsets.all(16),
                  child: Column(
                    children: [
                      if (entry.sleepHours != null)
                        _buildInfoRow(
                          context,
                          'Sleep Hours',
                          '${entry.sleepHours!.toStringAsFixed(1)}h',
                          Icons.bedtime,
                        ),
                      if (entry.sleepQuality != null)
                        _buildInfoRow(
                          context,
                          'Sleep Quality',
                          '${entry.sleepQuality}/5',
                          Icons.star,
                        ),
                      if (entry.exercised == true)
                        _buildInfoRow(
                          context,
                          'Exercise',
                          'Yes',
                          Icons.fitness_center,
                        ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 16),
            ],

            // Medication
            if (entry.tookMedication == true) ...[
              Card(
                child: ListTile(
                  leading: Icon(Icons.medication, color: theme.colorScheme.primary),
                  title: const Text('Took medication'),
                  trailing: const Icon(Icons.check_circle, color: Colors.green),
                ),
              ),
              const SizedBox(height: 16),
            ],

            // Notes
            if (entry.notes != null && entry.notes!.isNotEmpty) ...[
              _buildSectionHeader(context, 'Notes', Icons.note),
              const SizedBox(height: 8),
              Card(
                child: Padding(
                  padding: const EdgeInsets.all(16),
                  child: Text(
                    entry.notes!,
                    style: theme.textTheme.bodyMedium,
                  ),
                ),
              ),
            ],
          ],
        ),
      ),
    );
  }

  Widget _buildSectionHeader(BuildContext context, String title, IconData icon) {
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

  Widget _buildRatingRow(BuildContext context, String label, int value) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(
            label,
            style: Theme.of(context).textTheme.bodyLarge,
          ),
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
            decoration: BoxDecoration(
              color: _getIntensityColor(value),
              borderRadius: BorderRadius.circular(12),
            ),
            child: Text(
              value.toString(),
              style: const TextStyle(
                color: Colors.white,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildCountRow(BuildContext context, String label, int count) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(
            label,
            style: Theme.of(context).textTheme.bodyLarge,
          ),
          Text(
            'x$count',
            style: Theme.of(context).textTheme.titleMedium?.copyWith(
                  fontWeight: FontWeight.bold,
                  color: Theme.of(context).colorScheme.primary,
                ),
          ),
        ],
      ),
    );
  }

  Widget _buildInfoRow(BuildContext context, String label, String value, IconData icon) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Row(
        children: [
          Icon(icon, size: 20),
          const SizedBox(width: 12),
          Expanded(
            child: Text(
              label,
              style: Theme.of(context).textTheme.bodyLarge,
            ),
          ),
          Text(
            value,
            style: Theme.of(context).textTheme.titleSmall?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
          ),
        ],
      ),
    );
  }

  List<Widget> _buildSkillsGrouped(BuildContext context) {
    final skillsByModule = <String, List<String>>{};

    for (final skill in entry.skillsUsed) {
      final module = DBTSkills.getModuleForSkill(skill);
      if (module != null) {
        skillsByModule.putIfAbsent(module, () => []).add(skill);
      }
    }

    final widgets = <Widget>[];

    for (final module in skillsByModule.keys) {
      final skills = skillsByModule[module]!;

      widgets.add(
        Padding(
          padding: const EdgeInsets.only(bottom: 12),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                module,
                style: Theme.of(context).textTheme.titleSmall?.copyWith(
                      fontWeight: FontWeight.bold,
                      color: _getModuleColor(module),
                    ),
              ),
              const SizedBox(height: 4),
              Wrap(
                spacing: 8,
                runSpacing: 8,
                children: skills.map((skill) {
                  return Chip(
                    label: Text(skill),
                    backgroundColor: _getModuleColor(module).withOpacity(0.2),
                    labelStyle: TextStyle(
                      color: _getModuleColor(module),
                      fontWeight: FontWeight.w500,
                    ),
                  );
                }).toList(),
              ),
            ],
          ),
        ),
      );
    }

    return widgets;
  }

  Color _getIntensityColor(int intensity) {
    if (intensity <= 3) {
      return Colors.green;
    } else if (intensity <= 7) {
      return Colors.orange;
    } else {
      return Colors.red;
    }
  }

  Color _getModuleColor(String module) {
    switch (module) {
      case 'Mindfulness':
        return Colors.purple;
      case 'Distress Tolerance':
        return Colors.blue;
      case 'Emotion Regulation':
        return Colors.green;
      case 'Interpersonal Effectiveness':
        return Colors.orange;
      default:
        return Colors.grey;
    }
  }
}
