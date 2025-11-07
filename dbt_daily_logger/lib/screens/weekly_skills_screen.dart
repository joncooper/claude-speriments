import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import '../models/dbt_skills.dart';
import '../services/simple_storage.dart';

class WeeklySkillsScreen extends StatefulWidget {
  const WeeklySkillsScreen({super.key});

  @override
  State<WeeklySkillsScreen> createState() => _WeeklySkillsScreenState();
}

class _WeeklySkillsScreenState extends State<WeeklySkillsScreen> {
  DateTime _currentWeekStart = DateTime.now();
  List<DailyEntryData> _weekEntries = [];
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _currentWeekStart = _getWeekStart(DateTime.now());
    _loadWeekData();
  }

  DateTime _getWeekStart(DateTime date) {
    // Get Monday of the week
    return date.subtract(Duration(days: date.weekday - 1));
  }

  Future<void> _loadWeekData() async {
    setState(() => _isLoading = true);

    final allEntries = await SimpleStorage.loadEntries();
    final weekEnd = _currentWeekStart.add(const Duration(days: 7));

    _weekEntries = allEntries.where((entry) {
      return entry.date.isAfter(_currentWeekStart.subtract(const Duration(days: 1))) &&
          entry.date.isBefore(weekEnd);
    }).toList();

    setState(() => _isLoading = false);
  }

  void _previousWeek() {
    setState(() {
      _currentWeekStart = _currentWeekStart.subtract(const Duration(days: 7));
    });
    _loadWeekData();
  }

  void _nextWeek() {
    setState(() {
      _currentWeekStart = _currentWeekStart.add(const Duration(days: 7));
    });
    _loadWeekData();
  }

  void _goToCurrentWeek() {
    setState(() {
      _currentWeekStart = _getWeekStart(DateTime.now());
    });
    _loadWeekData();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Weekly Skills Overview'),
        centerTitle: true,
        actions: [
          IconButton(
            icon: const Icon(Icons.today),
            tooltip: 'Current Week',
            onPressed: _goToCurrentWeek,
          ),
        ],
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : Column(
              children: [
                // Week navigation
                Container(
                  padding: const EdgeInsets.all(16),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      IconButton(
                        icon: const Icon(Icons.chevron_left),
                        onPressed: _previousWeek,
                      ),
                      Expanded(
                        child: Text(
                          _getWeekRangeText(),
                          textAlign: TextAlign.center,
                          style: const TextStyle(
                            fontSize: 16,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                      IconButton(
                        icon: const Icon(Icons.chevron_right),
                        onPressed: _nextWeek,
                      ),
                    ],
                  ),
                ),

                // Skills grid
                Expanded(
                  child: SingleChildScrollView(
                    child: Column(
                      children: [
                        _buildSkillsGrid(),
                        const SizedBox(height: 16),
                        _buildLegend(),
                        const SizedBox(height: 32),
                      ],
                    ),
                  ),
                ),
              ],
            ),
    );
  }

  String _getWeekRangeText() {
    final weekEnd = _currentWeekStart.add(const Duration(days: 6));
    final dateFormat = DateFormat('MMM d');

    if (_currentWeekStart.month == weekEnd.month) {
      return '${dateFormat.format(_currentWeekStart)} - ${weekEnd.day}, ${DateFormat('yyyy').format(_currentWeekStart)}';
    } else {
      return '${dateFormat.format(_currentWeekStart)} - ${dateFormat.format(weekEnd)}, ${DateFormat('yyyy').format(_currentWeekStart)}';
    }
  }

  Widget _buildSkillsGrid() {
    // Get all unique skills used this week
    final allSkillsUsed = <String>{};
    for (var entry in _weekEntries) {
      allSkillsUsed.addAll(entry.skillsUsedToday);
    }

    if (allSkillsUsed.isEmpty) {
      return Padding(
        padding: const EdgeInsets.all(32),
        child: Column(
          children: [
            Icon(Icons.psychology_outlined, size: 64, color: Colors.grey[400]),
            const SizedBox(height: 16),
            Text(
              'No skills tracked this week',
              style: TextStyle(
                fontSize: 18,
                color: Colors.grey[600],
              ),
            ),
            const SizedBox(height: 8),
            Text(
              'Start logging your daily entries to see skills here',
              style: TextStyle(color: Colors.grey[500]),
              textAlign: TextAlign.center,
            ),
          ],
        ),
      );
    }

    // Group skills by category
    final skillsByCategory = <String, List<String>>{};
    for (var skill in allSkillsUsed) {
      final category = DBTSkills.getCategoryForSkill(skill) ?? 'Other';
      skillsByCategory.putIfAbsent(category, () => []).add(skill);
    }

    return Column(
      children: [
        // Day headers
        _buildDayHeaders(),
        const Divider(),

        // Skills by category
        ...skillsByCategory.entries.map((categoryEntry) {
          return _buildCategorySection(
            categoryEntry.key,
            categoryEntry.value,
          );
        }),
      ],
    );
  }

  Widget _buildDayHeaders() {
    final days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];

    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      child: Row(
        children: [
          const SizedBox(width: 150), // Space for skill names
          Expanded(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: days.map((day) {
                final dayIndex = days.indexOf(day);
                final date = _currentWeekStart.add(Duration(days: dayIndex));
                final isToday = _isToday(date);

                return Expanded(
                  child: Container(
                    padding: const EdgeInsets.symmetric(vertical: 4),
                    decoration: isToday
                        ? BoxDecoration(
                            color: Colors.teal.withOpacity(0.2),
                            borderRadius: BorderRadius.circular(8),
                          )
                        : null,
                    child: Column(
                      children: [
                        Text(
                          day,
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: isToday ? FontWeight.bold : FontWeight.normal,
                            color: isToday ? Colors.teal : Colors.grey[700],
                          ),
                        ),
                        Text(
                          '${date.day}',
                          style: TextStyle(
                            fontSize: 10,
                            color: isToday ? Colors.teal : Colors.grey[600],
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              }).toList(),
            ),
          ),
        ],
      ),
    );
  }

  bool _isToday(DateTime date) {
    final now = DateTime.now();
    return date.year == now.year && date.month == now.month && date.day == now.day;
  }

  Widget _buildCategorySection(String category, List<String> skills) {
    final color = _getCategoryColor(category);

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Padding(
          padding: const EdgeInsets.fromLTRB(16, 16, 16, 8),
          child: Text(
            category,
            style: TextStyle(
              fontSize: 16,
              fontWeight: FontWeight.bold,
              color: color,
            ),
          ),
        ),
        ...skills.map((skill) => _buildSkillRow(skill, color)),
        const SizedBox(height: 8),
      ],
    );
  }

  Color _getCategoryColor(String category) {
    switch (category) {
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

  Widget _buildSkillRow(String skill, Color color) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
      child: Row(
        children: [
          // Skill name
          SizedBox(
            width: 150,
            child: Text(
              skill,
              style: const TextStyle(fontSize: 13),
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
            ),
          ),

          // Checkboxes for each day
          Expanded(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: List.generate(7, (dayIndex) {
                final date = _currentWeekStart.add(Duration(days: dayIndex));
                final hasSkill = _hasSkillOnDate(skill, date);

                return Expanded(
                  child: Center(
                    child: Container(
                      width: 20,
                      height: 20,
                      decoration: BoxDecoration(
                        color: hasSkill ? color : Colors.grey[200],
                        borderRadius: BorderRadius.circular(4),
                      ),
                      child: hasSkill
                          ? const Icon(
                              Icons.check,
                              size: 14,
                              color: Colors.white,
                            )
                          : null,
                    ),
                  ),
                );
              }),
            ),
          ),
        ],
      ),
    );
  }

  bool _hasSkillOnDate(String skill, DateTime date) {
    return _weekEntries.any((entry) {
      return entry.date.year == date.year &&
          entry.date.month == date.month &&
          entry.date.day == date.day &&
          entry.skillsUsedToday.contains(skill);
    });
  }

  Widget _buildLegend() {
    return Padding(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            'Legend',
            style: TextStyle(
              fontSize: 14,
              fontWeight: FontWeight.bold,
              color: Colors.grey[700],
            ),
          ),
          const SizedBox(height: 8),
          Row(
            children: [
              Container(
                width: 20,
                height: 20,
                decoration: BoxDecoration(
                  color: Colors.teal,
                  borderRadius: BorderRadius.circular(4),
                ),
                child: const Icon(Icons.check, size: 14, color: Colors.white),
              ),
              const SizedBox(width: 8),
              const Text('Skill used', style: TextStyle(fontSize: 13)),
              const SizedBox(width: 24),
              Container(
                width: 20,
                height: 20,
                decoration: BoxDecoration(
                  color: Colors.grey[200],
                  borderRadius: BorderRadius.circular(4),
                ),
              ),
              const SizedBox(width: 8),
              const Text('Not used', style: TextStyle(fontSize: 13)),
            ],
          ),
          const SizedBox(height: 16),
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: Colors.blue[50],
              borderRadius: BorderRadius.circular(8),
            ),
            child: Row(
              children: [
                Icon(Icons.lightbulb_outline, color: Colors.blue[700]),
                const SizedBox(width: 12),
                Expanded(
                  child: Text(
                    'Only skills you\'ve used this week are shown',
                    style: TextStyle(
                      fontSize: 13,
                      color: Colors.blue[900],
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
}
