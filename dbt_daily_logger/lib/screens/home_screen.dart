import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:provider/provider.dart';
import '../models/diary_entry.dart';
import '../services/diary_service.dart';
import 'entry_form_screen.dart';
import 'entry_detail_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  @override
  Widget build(BuildContext context) {
    final diaryService = Provider.of<DiaryService>(context, listen: false);

    return Scaffold(
      appBar: AppBar(
        title: const Text('DBT Daily Logger'),
        actions: [
          IconButton(
            icon: const Icon(Icons.info_outline),
            onPressed: () => _showAboutDialog(context),
          ),
        ],
      ),
      body: FutureBuilder<List<DiaryEntry>>(
        future: Future.value(diaryService.getAllEntries()),
        builder: (context, snapshot) {
          if (!snapshot.hasData) {
            return const Center(child: CircularProgressIndicator());
          }

          final entries = snapshot.data!;

          if (entries.isEmpty) {
            return Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(
                    Icons.edit_note,
                    size: 80,
                    color: Colors.grey[400],
                  ),
                  const SizedBox(height: 16),
                  Text(
                    'No entries yet',
                    style: Theme.of(context).textTheme.headlineSmall?.copyWith(
                          color: Colors.grey[600],
                        ),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    'Tap the + button to create your first diary entry',
                    style: TextStyle(color: Colors.grey[600]),
                  ),
                ],
              ),
            );
          }

          return RefreshIndicator(
            onRefresh: () async {
              setState(() {});
            },
            child: ListView.builder(
              padding: const EdgeInsets.all(16),
              itemCount: entries.length,
              itemBuilder: (context, index) {
                final entry = entries[index];
                return _EntryCard(
                  entry: entry,
                  onTap: () => _navigateToDetail(context, entry),
                  onDelete: () => _deleteEntry(context, entry),
                );
              },
            ),
          );
        },
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () => _navigateToNewEntry(context),
        icon: const Icon(Icons.add),
        label: const Text('New Entry'),
      ),
    );
  }

  void _navigateToNewEntry(BuildContext context) async {
    final result = await Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => EntryFormScreen(date: DateTime.now()),
      ),
    );

    if (result == true) {
      setState(() {});
    }
  }

  void _navigateToDetail(BuildContext context, DiaryEntry entry) async {
    final result = await Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => EntryDetailScreen(entry: entry),
      ),
    );

    if (result == true) {
      setState(() {});
    }
  }

  void _deleteEntry(BuildContext context, DiaryEntry entry) async {
    final confirmed = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Delete Entry'),
        content: const Text('Are you sure you want to delete this entry?'),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: const Text('Cancel'),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context, true),
            child: const Text('Delete'),
          ),
        ],
      ),
    );

    if (confirmed == true && mounted) {
      final diaryService = Provider.of<DiaryService>(context, listen: false);
      await diaryService.deleteEntry(entry);
      setState(() {});

      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('Entry deleted')),
        );
      }
    }
  }

  void _showAboutDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('About DBT Daily Logger'),
        content: const Text(
          'This app helps you track your daily DBT (Dialectical Behavior Therapy) '
          'diary card entries.\n\n'
          'Track emotions, urges, target behaviors, skills used, and more.',
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('OK'),
          ),
        ],
      ),
    );
  }
}

class _EntryCard extends StatelessWidget {
  final DiaryEntry entry;
  final VoidCallback onTap;
  final VoidCallback onDelete;

  const _EntryCard({
    required this.entry,
    required this.onTap,
    required this.onDelete,
  });

  @override
  Widget build(BuildContext context) {
    final dateFormat = DateFormat('EEEE, MMMM d, y');

    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Expanded(
                    child: Text(
                      dateFormat.format(entry.date),
                      style: Theme.of(context).textTheme.titleMedium?.copyWith(
                            fontWeight: FontWeight.bold,
                          ),
                    ),
                  ),
                  IconButton(
                    icon: const Icon(Icons.delete_outline),
                    onPressed: onDelete,
                    color: Colors.red[400],
                  ),
                ],
              ),
              const SizedBox(height: 12),
              if (entry.emotions.isNotEmpty) ...[
                _buildInfoChip(
                  context,
                  Icons.mood,
                  '${entry.emotions.length} emotions tracked',
                  Colors.blue,
                ),
                const SizedBox(height: 8),
              ],
              if (entry.urges.isNotEmpty) ...[
                _buildInfoChip(
                  context,
                  Icons.warning_amber_rounded,
                  '${entry.urges.length} urges tracked',
                  Colors.orange,
                ),
                const SizedBox(height: 8),
              ],
              if (entry.skillsUsed.isNotEmpty) ...[
                _buildInfoChip(
                  context,
                  Icons.psychology,
                  '${entry.skillsUsed.length} skills used',
                  Colors.green,
                ),
                const SizedBox(height: 8),
              ],
              if (entry.targetBehaviors.isNotEmpty) ...[
                _buildInfoChip(
                  context,
                  Icons.flag,
                  '${entry.targetBehaviors.length} behaviors',
                  Colors.red,
                ),
                const SizedBox(height: 8),
              ],
              if (entry.notes.isNotEmpty) ...[
                _buildInfoChip(
                  context,
                  Icons.note,
                  'Has notes',
                  Colors.purple,
                ),
              ],
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildInfoChip(
    BuildContext context,
    IconData icon,
    String label,
    Color color,
  ) {
    return Row(
      children: [
        Icon(icon, size: 16, color: color),
        const SizedBox(width: 8),
        Text(
          label,
          style: TextStyle(color: Colors.grey[700]),
        ),
      ],
    );
  }
}
