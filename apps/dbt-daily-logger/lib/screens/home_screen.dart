import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/entries_provider.dart';
import '../providers/auth_provider.dart';
import '../models/diary_entry.dart';
import 'package:intl/intl.dart';
import 'entry/new_entry_screen.dart';
import 'entry/entry_detail_screen.dart';

/// Home screen showing list of diary entries
class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _selectedIndex = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('DBT Daily Logger'),
        actions: [
          // Theme toggle (placeholder for now)
          IconButton(
            icon: const Icon(Icons.brightness_6),
            onPressed: () {
              // TODO: Implement theme toggle in settings
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(content: Text('Theme settings coming soon!')),
              );
            },
          ),
        ],
      ),
      body: _buildBody(),
      floatingActionButton: _selectedIndex == 0
          ? FloatingActionButton.extended(
              onPressed: () {
                Navigator.of(context).push(
                  MaterialPageRoute(
                    builder: (context) => const NewEntryScreen(),
                  ),
                );
              },
              icon: const Icon(Icons.add),
              label: const Text('New Entry'),
            )
          : null,
      bottomNavigationBar: NavigationBar(
        selectedIndex: _selectedIndex,
        onDestinationSelected: (index) {
          setState(() {
            _selectedIndex = index;
          });
        },
        destinations: const [
          NavigationDestination(
            icon: Icon(Icons.home_outlined),
            selectedIcon: Icon(Icons.home),
            label: 'Home',
          ),
          NavigationDestination(
            icon: Icon(Icons.grid_on_outlined),
            selectedIcon: Icon(Icons.grid_on),
            label: 'Weekly',
          ),
          NavigationDestination(
            icon: Icon(Icons.school_outlined),
            selectedIcon: Icon(Icons.school),
            label: 'Skills',
          ),
          NavigationDestination(
            icon: Icon(Icons.settings_outlined),
            selectedIcon: Icon(Icons.settings),
            label: 'Settings',
          ),
        ],
      ),
    );
  }

  Widget _buildBody() {
    switch (_selectedIndex) {
      case 0:
        return _buildEntriesList();
      case 1:
        return _buildPlaceholder('Weekly Skills Grid');
      case 2:
        return _buildPlaceholder('Skills Reference');
      case 3:
        return _buildPlaceholder('Settings');
      default:
        return _buildEntriesList();
    }
  }

  Widget _buildEntriesList() {
    return Consumer<EntriesProvider>(
      builder: (context, entriesProvider, _) {
        if (entriesProvider.isLoading) {
          return const Center(child: CircularProgressIndicator());
        }

        if (entriesProvider.error != null) {
          return Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(
                  Icons.error_outline,
                  size: 64,
                  color: Theme.of(context).colorScheme.error,
                ),
                const SizedBox(height: 16),
                Text(
                  'Error loading entries',
                  style: Theme.of(context).textTheme.titleLarge,
                ),
                const SizedBox(height: 8),
                Text(
                  entriesProvider.error!,
                  style: Theme.of(context).textTheme.bodyMedium,
                  textAlign: TextAlign.center,
                ),
              ],
            ),
          );
        }

        if (entriesProvider.entries.isEmpty) {
          return Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(
                  Icons.note_add_outlined,
                  size: 64,
                  color: Theme.of(context).colorScheme.primary.withOpacity(0.5),
                ),
                const SizedBox(height: 16),
                Text(
                  'No entries yet',
                  style: Theme.of(context).textTheme.titleLarge,
                ),
                const SizedBox(height: 8),
                Text(
                  'Tap the button below to create your first entry',
                  style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                        color: Theme.of(context).colorScheme.onSurface.withOpacity(0.7),
                      ),
                  textAlign: TextAlign.center,
                ),
              ],
            ),
          );
        }

        return ListView.builder(
          padding: const EdgeInsets.all(16),
          itemCount: entriesProvider.entries.length,
          itemBuilder: (context, index) {
            final entry = entriesProvider.entries[index];
            return _buildEntryCard(entry);
          },
        );
      },
    );
  }

  Widget _buildEntryCard(DiaryEntry entry) {
    final dateFormat = DateFormat('EEEE, MMMM d, yyyy');
    final timeFormat = DateFormat('h:mm a');

    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: InkWell(
        onTap: () {
          Navigator.of(context).push(
            MaterialPageRoute(
              builder: (context) => EntryDetailScreen(entry: entry),
            ),
          );
        },
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Date header
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text(
                    dateFormat.format(entry.date),
                    style: Theme.of(context).textTheme.titleMedium?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                  ),
                  Text(
                    timeFormat.format(entry.createdAt),
                    style: Theme.of(context).textTheme.bodySmall?.copyWith(
                          color: Theme.of(context).colorScheme.onSurface.withOpacity(0.6),
                        ),
                  ),
                ],
              ),
              const SizedBox(height: 12),

              // Quick summary
              Wrap(
                spacing: 8,
                runSpacing: 8,
                children: [
                  if (entry.emotions.isNotEmpty)
                    _buildSummaryChip(
                      Icons.sentiment_satisfied,
                      '${entry.emotions.length} emotions',
                    ),
                  if (entry.behaviors.isNotEmpty)
                    _buildSummaryChip(
                      Icons.warning_outlined,
                      '${entry.behaviors.length} behaviors',
                    ),
                  if (entry.skillsUsed.isNotEmpty)
                    _buildSummaryChip(
                      Icons.psychology,
                      '${entry.skillsUsed.length} skills',
                    ),
                  if (entry.sleepHours != null)
                    _buildSummaryChip(
                      Icons.bedtime,
                      '${entry.sleepHours}h sleep',
                    ),
                ],
              ),

              // Notes preview
              if (entry.notes != null && entry.notes!.isNotEmpty) ...[
                const SizedBox(height: 12),
                Text(
                  entry.notes!,
                  maxLines: 2,
                  overflow: TextOverflow.ellipsis,
                  style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                        color: Theme.of(context).colorScheme.onSurface.withOpacity(0.7),
                      ),
                ),
              ],
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildSummaryChip(IconData icon, String label) {
    return Chip(
      avatar: Icon(icon, size: 16),
      label: Text(label),
      visualDensity: VisualDensity.compact,
      padding: EdgeInsets.zero,
    );
  }

  Widget _buildPlaceholder(String title) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(
            Icons.construction,
            size: 64,
            color: Theme.of(context).colorScheme.primary.withOpacity(0.5),
          ),
          const SizedBox(height: 16),
          Text(
            title,
            style: Theme.of(context).textTheme.titleLarge,
          ),
          const SizedBox(height: 8),
          Text(
            'Coming soon!',
            style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                  color: Theme.of(context).colorScheme.onSurface.withOpacity(0.7),
                ),
          ),
        ],
      ),
    );
  }
}
