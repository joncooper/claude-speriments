import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:intl/intl.dart';
import '../../providers/entries_provider.dart';
import '../../providers/auth_provider.dart';
import '../../models/diary_entry.dart';
import '../../models/dbt_skills.dart';

/// Weekly skills grid showing Mon-Sun visualization
class WeeklySkillsScreen extends StatefulWidget {
  const WeeklySkillsScreen({super.key});

  @override
  State<WeeklySkillsScreen> createState() => _WeeklySkillsScreenState();
}

class _WeeklySkillsScreenState extends State<WeeklySkillsScreen> {
  DateTime _selectedWeekStart = _getWeekStart(DateTime.now());
  bool _isLoading = false;
  List<DiaryEntry> _weekEntries = [];

  static DateTime _getWeekStart(DateTime date) {
    // Start week on Monday
    final daysFromMonday = (date.weekday - DateTime.monday) % 7;
    return DateTime(date.year, date.month, date.day).subtract(Duration(days: daysFromMonday));
  }

  @override
  void initState() {
    super.initState();
    _loadWeekData();
  }

  Future<void> _loadWeekData() async {
    final authProvider = Provider.of<AuthProvider>(context, listen: false);
    final entriesProvider = Provider.of<EntriesProvider>(context, listen: false);

    if (authProvider.user == null) return;

    setState(() {
      _isLoading = true;
    });

    try {
      final entries = await entriesProvider.getEntriesForWeek(
        authProvider.user!.uid,
        _selectedWeekStart,
      );

      if (mounted) {
        setState(() {
          _weekEntries = entries;
          _isLoading = false;
        });
      }
    } catch (e) {
      if (mounted) {
        setState(() {
          _isLoading = false;
        });
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Failed to load week data: $e')),
        );
      }
    }
  }

  void _previousWeek() {
    setState(() {
      _selectedWeekStart = _selectedWeekStart.subtract(const Duration(days: 7));
    });
    _loadWeekData();
  }

  void _nextWeek() {
    setState(() {
      _selectedWeekStart = _selectedWeekStart.add(const Duration(days: 7));
    });
    _loadWeekData();
  }

  void _goToCurrentWeek() {
    setState(() {
      _selectedWeekStart = _getWeekStart(DateTime.now());
    });
    _loadWeekData();
  }

  DiaryEntry? _getEntryForDate(DateTime date) {
    try {
      return _weekEntries.firstWhere((entry) {
        return entry.date.year == date.year &&
            entry.date.month == date.month &&
            entry.date.day == date.day;
      });
    } catch (e) {
      return null;
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

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final weekEnd = _selectedWeekStart.add(const Duration(days: 6));
    final dateFormat = DateFormat('MMM d');

    return Column(
      children: [
        // Week navigation
        Card(
          margin: const EdgeInsets.all(16),
          child: Padding(
            padding: const EdgeInsets.all(12),
            child: Row(
              children: [
                IconButton(
                  icon: const Icon(Icons.chevron_left),
                  onPressed: _previousWeek,
                ),
                Expanded(
                  child: Column(
                    children: [
                      Text(
                        '${dateFormat.format(_selectedWeekStart)} - ${dateFormat.format(weekEnd)}',
                        style: theme.textTheme.titleMedium?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                        textAlign: TextAlign.center,
                      ),
                      TextButton.icon(
                        onPressed: _goToCurrentWeek,
                        icon: const Icon(Icons.today, size: 16),
                        label: const Text('This Week'),
                        style: TextButton.styleFrom(
                          visualDensity: VisualDensity.compact,
                        ),
                      ),
                    ],
                  ),
                ),
                IconButton(
                  icon: const Icon(Icons.chevron_right),
                  onPressed: _nextWeek,
                ),
              ],
            ),
          ),
        ),

        // Content
        Expanded(
          child: _isLoading
              ? const Center(child: CircularProgressIndicator())
              : _weekEntries.isEmpty
                  ? Center(
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(
                            Icons.event_busy,
                            size: 64,
                            color: theme.colorScheme.primary.withOpacity(0.5),
                          ),
                          const SizedBox(height: 16),
                          Text(
                            'No entries this week',
                            style: theme.textTheme.titleLarge,
                          ),
                          const SizedBox(height: 8),
                          Text(
                            'Create diary entries to see your weekly skills',
                            style: theme.textTheme.bodyMedium?.copyWith(
                              color: theme.colorScheme.onSurface.withOpacity(0.7),
                            ),
                            textAlign: TextAlign.center,
                          ),
                        ],
                      ),
                    )
                  : _buildWeekGrid(),
        ),
      ],
    );
  }

  Widget _buildWeekGrid() {
    return ListView(
      padding: const EdgeInsets.symmetric(horizontal: 16),
      children: [
        // Summary cards
        _buildSummaryCards(),
        const SizedBox(height: 16),

        // Daily breakdown
        ...List.generate(7, (index) {
          final date = _selectedWeekStart.add(Duration(days: index));
          final entry = _getEntryForDate(date);
          return _buildDayCard(date, entry);
        }),
        const SizedBox(height: 16),
      ],
    );
  }

  Widget _buildSummaryCards() {
    final allSkillsUsed = <String>{};
    final skillCounts = <String, int>{};

    for (final entry in _weekEntries) {
      for (final skill in entry.skillsUsed) {
        allSkillsUsed.add(skill);
        skillCounts[skill] = (skillCounts[skill] ?? 0) + 1;
      }
    }

    // Get most used skills
    final sortedSkills = skillCounts.entries.toList()
      ..sort((a, b) => b.value.compareTo(a.value));

    return Row(
      children: [
        Expanded(
          child: Card(
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                children: [
                  Icon(
                    Icons.psychology,
                    color: Theme.of(context).colorScheme.primary,
                    size: 32,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '${allSkillsUsed.length}',
                    style: Theme.of(context).textTheme.headlineMedium?.copyWith(
                          fontWeight: FontWeight.bold,
                          color: Theme.of(context).colorScheme.primary,
                        ),
                  ),
                  Text(
                    'Unique Skills',
                    style: Theme.of(context).textTheme.bodySmall,
                    textAlign: TextAlign.center,
                  ),
                ],
              ),
            ),
          ),
        ),
        const SizedBox(width: 8),
        Expanded(
          child: Card(
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                children: [
                  Icon(
                    Icons.event_available,
                    color: Theme.of(context).colorScheme.secondary,
                    size: 32,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '${_weekEntries.length}',
                    style: Theme.of(context).textTheme.headlineMedium?.copyWith(
                          fontWeight: FontWeight.bold,
                          color: Theme.of(context).colorScheme.secondary,
                        ),
                  ),
                  Text(
                    'Days Logged',
                    style: Theme.of(context).textTheme.bodySmall,
                    textAlign: TextAlign.center,
                  ),
                ],
              ),
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildDayCard(DateTime date, DiaryEntry? entry) {
    final theme = Theme.of(context);
    final dayName = DateFormat('EEEE').format(date);
    final dateStr = DateFormat('MMM d').format(date);
    final isToday = DateTime.now().difference(date).inDays == 0 &&
        DateTime.now().day == date.day;

    if (entry == null) {
      return Card(
        margin: const EdgeInsets.only(bottom: 12),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Row(
            children: [
              Container(
                width: 4,
                height: 40,
                decoration: BoxDecoration(
                  color: theme.colorScheme.outline.withOpacity(0.3),
                  borderRadius: BorderRadius.circular(2),
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      children: [
                        Text(
                          dayName,
                          style: theme.textTheme.titleSmall?.copyWith(
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        if (isToday) ...[
                          const SizedBox(width: 8),
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                            decoration: BoxDecoration(
                              color: theme.colorScheme.primary,
                              borderRadius: BorderRadius.circular(8),
                            ),
                            child: Text(
                              'Today',
                              style: theme.textTheme.labelSmall?.copyWith(
                                color: theme.colorScheme.onPrimary,
                              ),
                            ),
                          ),
                        ],
                      ],
                    ),
                    Text(
                      dateStr,
                      style: theme.textTheme.bodySmall?.copyWith(
                        color: theme.colorScheme.onSurface.withOpacity(0.6),
                      ),
                    ),
                  ],
                ),
              ),
              Text(
                'No entry',
                style: theme.textTheme.bodySmall?.copyWith(
                  color: theme.colorScheme.onSurface.withOpacity(0.5),
                  fontStyle: FontStyle.italic,
                ),
              ),
            ],
          ),
        ),
      );
    }

    // Group skills by module
    final skillsByModule = <String, List<String>>{};
    for (final skill in entry.skillsUsed) {
      final module = DBTSkills.getModuleForSkill(skill);
      if (module != null) {
        skillsByModule.putIfAbsent(module, () => []).add(skill);
      }
    }

    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Container(
                  width: 4,
                  height: 40,
                  decoration: BoxDecoration(
                    color: theme.colorScheme.primary,
                    borderRadius: BorderRadius.circular(2),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        children: [
                          Text(
                            dayName,
                            style: theme.textTheme.titleSmall?.copyWith(
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          if (isToday) ...[
                            const SizedBox(width: 8),
                            Container(
                              padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                              decoration: BoxDecoration(
                                color: theme.colorScheme.primary,
                                borderRadius: BorderRadius.circular(8),
                              ),
                              child: Text(
                                'Today',
                                style: theme.textTheme.labelSmall?.copyWith(
                                  color: theme.colorScheme.onPrimary,
                                ),
                              ),
                            ),
                          ],
                        ],
                      ),
                      Text(
                        dateStr,
                        style: theme.textTheme.bodySmall?.copyWith(
                          color: theme.colorScheme.onSurface.withOpacity(0.6),
                        ),
                      ),
                    ],
                  ),
                ),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                  decoration: BoxDecoration(
                    color: theme.colorScheme.primary.withOpacity(0.2),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Text(
                    '${entry.skillsUsed.length} skill${entry.skillsUsed.length == 1 ? '' : 's'}',
                    style: theme.textTheme.labelSmall?.copyWith(
                      fontWeight: FontWeight.bold,
                      color: theme.colorScheme.primary,
                    ),
                  ),
                ),
              ],
            ),
            if (skillsByModule.isNotEmpty) ...[
              const SizedBox(height: 12),
              ...skillsByModule.entries.map((moduleEntry) {
                final module = moduleEntry.key;
                final skills = moduleEntry.value;
                return Padding(
                  padding: const EdgeInsets.only(bottom: 8),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        module,
                        style: theme.textTheme.labelSmall?.copyWith(
                          fontWeight: FontWeight.bold,
                          color: _getModuleColor(module),
                        ),
                      ),
                      const SizedBox(height: 4),
                      Wrap(
                        spacing: 6,
                        runSpacing: 6,
                        children: skills.map((skill) {
                          return Chip(
                            label: Text(skill),
                            visualDensity: VisualDensity.compact,
                            backgroundColor: _getModuleColor(module).withOpacity(0.15),
                            labelStyle: TextStyle(
                              fontSize: 11,
                              color: _getModuleColor(module),
                            ),
                            padding: EdgeInsets.zero,
                          );
                        }).toList(),
                      ),
                    ],
                  ),
                );
              }).toList(),
            ],
          ],
        ),
      ),
    );
  }
}
