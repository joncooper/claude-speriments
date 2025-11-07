import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:table_calendar/table_calendar.dart';
import 'package:confetti/confetti.dart';
import '../models/diary_entry.dart';
import '../services/diary_service.dart';
import 'entry_form_screen.dart';
import 'entry_detail_screen.dart';

class CalendarScreen extends StatefulWidget {
  const CalendarScreen({super.key});

  @override
  State<CalendarScreen> createState() => _CalendarScreenState();
}

class _CalendarScreenState extends State<CalendarScreen> {
  DateTime _focusedDay = DateTime.now();
  DateTime? _selectedDay;
  late ConfettiController _confettiController;

  @override
  void initState() {
    super.initState();
    _confettiController = ConfettiController(duration: const Duration(seconds: 2));
  }

  @override
  void dispose() {
    _confettiController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final diaryService = Provider.of<DiaryService>(context, listen: false);
    final entries = diaryService.getAllEntries();
    final currentStreak = _calculateCurrentStreak(entries);
    final longestStreak = _calculateLongestStreak(entries);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Calendar & Streaks'),
      ),
      body: Stack(
        children: [
          ListView(
            padding: const EdgeInsets.all(16),
            children: [
              // Streak cards
              Row(
                children: [
                  Expanded(
                    child: _buildStreakCard(
                      'Current Streak',
                      currentStreak,
                      Icons.local_fire_department,
                      Colors.orange,
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: _buildStreakCard(
                      'Longest Streak',
                      longestStreak,
                      Icons.emoji_events,
                      Colors.amber,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 16),

              // Calendar
              Card(
                child: Padding(
                  padding: const EdgeInsets.all(8),
                  child: TableCalendar(
                    firstDay: DateTime.utc(2020, 1, 1),
                    lastDay: DateTime.now(),
                    focusedDay: _focusedDay,
                    selectedDayPredicate: (day) {
                      return isSameDay(_selectedDay, day);
                    },
                    onDaySelected: (selectedDay, focusedDay) {
                      setState(() {
                        _selectedDay = selectedDay;
                        _focusedDay = focusedDay;
                      });
                      _onDaySelected(selectedDay, diaryService);
                    },
                    calendarBuilders: CalendarBuilders(
                      markerBuilder: (context, date, events) {
                        final hasEntry = _hasEntryForDate(date, entries);
                        if (hasEntry) {
                          return Positioned(
                            bottom: 1,
                            child: Container(
                              width: 6,
                              height: 6,
                              decoration: BoxDecoration(
                                shape: BoxShape.circle,
                                color: Theme.of(context).colorScheme.primary,
                              ),
                            ),
                          );
                        }
                        return null;
                      },
                      defaultBuilder: (context, date, focusedDay) {
                        final hasEntry = _hasEntryForDate(date, entries);
                        return Container(
                          margin: const EdgeInsets.all(4),
                          decoration: BoxDecoration(
                            color: hasEntry
                                ? Theme.of(context)
                                    .colorScheme
                                    .primary
                                    .withOpacity(0.1)
                                : null,
                            borderRadius: BorderRadius.circular(8),
                          ),
                          child: Center(
                            child: Text(
                              '${date.day}',
                              style: TextStyle(
                                color: hasEntry
                                    ? Theme.of(context).colorScheme.primary
                                    : null,
                                fontWeight:
                                    hasEntry ? FontWeight.bold : FontWeight.normal,
                              ),
                            ),
                          ),
                        );
                      },
                    ),
                    calendarStyle: CalendarStyle(
                      todayDecoration: BoxDecoration(
                        color: Theme.of(context).colorScheme.secondary,
                        shape: BoxShape.circle,
                      ),
                      selectedDecoration: BoxDecoration(
                        color: Theme.of(context).colorScheme.primary,
                        shape: BoxShape.circle,
                      ),
                    ),
                    headerStyle: const HeaderStyle(
                      formatButtonVisible: false,
                      titleCentered: true,
                    ),
                  ),
                ),
              ),
              const SizedBox(height: 16),

              // Completion stats
              _buildCompletionStatsCard(entries),
            ],
          ),

          // Confetti for celebrations
          Align(
            alignment: Alignment.topCenter,
            child: ConfettiWidget(
              confettiController: _confettiController,
              blastDirection: 3.14 / 2,
              maxBlastForce: 5,
              minBlastForce: 2,
              emissionFrequency: 0.05,
              numberOfParticles: 50,
              gravity: 0.3,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildStreakCard(
      String label, int streak, IconData icon, Color color) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            Icon(icon, color: color, size: 32),
            const SizedBox(height: 8),
            Text(
              '$streak',
              style: TextStyle(
                fontSize: 32,
                fontWeight: FontWeight.bold,
                color: color,
              ),
            ),
            Text(
              label,
              style: const TextStyle(
                fontSize: 12,
                color: Colors.grey,
              ),
              textAlign: TextAlign.center,
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildCompletionStatsCard(List<DiaryEntry> entries) {
    final thisMonth = DateTime.now();
    final daysInMonth = DateTime(thisMonth.year, thisMonth.month + 1, 0).day;
    final entriesThisMonth = entries
        .where((e) =>
            e.date.year == thisMonth.year && e.date.month == thisMonth.month)
        .length;
    final completionRate = (entriesThisMonth / daysInMonth * 100).round();

    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'This Month',
              style: Theme.of(context).textTheme.titleMedium?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
            ),
            const SizedBox(height: 16),
            Row(
              children: [
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text('Entries Logged'),
                      const SizedBox(height: 4),
                      Text(
                        '$entriesThisMonth / $daysInMonth',
                        style: const TextStyle(
                          fontSize: 24,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),
                SizedBox(
                  width: 80,
                  height: 80,
                  child: Stack(
                    children: [
                      CircularProgressIndicator(
                        value: entriesThisMonth / daysInMonth,
                        strokeWidth: 8,
                        backgroundColor: Colors.grey[200],
                      ),
                      Center(
                        child: Text(
                          '$completionRate%',
                          style: const TextStyle(
                            fontSize: 18,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  bool _hasEntryForDate(DateTime date, List<DiaryEntry> entries) {
    return entries.any((entry) =>
        entry.date.year == date.year &&
        entry.date.month == date.month &&
        entry.date.day == date.day);
  }

  int _calculateCurrentStreak(List<DiaryEntry> entries) {
    if (entries.isEmpty) return 0;

    final sortedDates = entries.map((e) => e.dateOnly).toSet().toList()
      ..sort((a, b) => b.compareTo(a));

    int streak = 0;
    DateTime checkDate = DateTime.now();
    checkDate = DateTime(checkDate.year, checkDate.month, checkDate.day);

    for (var date in sortedDates) {
      if (date.isAtSameMomentAs(checkDate) ||
          date.isAtSameMomentAs(checkDate.subtract(const Duration(days: 1)))) {
        streak++;
        checkDate = date.subtract(const Duration(days: 1));
      } else {
        break;
      }
    }

    // Trigger confetti for milestones
    if (streak > 0 && streak % 7 == 0) {
      _confettiController.play();
    }

    return streak;
  }

  int _calculateLongestStreak(List<DiaryEntry> entries) {
    if (entries.isEmpty) return 0;

    final sortedDates = entries.map((e) => e.dateOnly).toSet().toList()
      ..sort();

    int longestStreak = 1;
    int currentStreak = 1;

    for (int i = 1; i < sortedDates.length; i++) {
      final diff = sortedDates[i].difference(sortedDates[i - 1]).inDays;
      if (diff == 1) {
        currentStreak++;
        longestStreak = currentStreak > longestStreak ? currentStreak : longestStreak;
      } else {
        currentStreak = 1;
      }
    }

    return longestStreak;
  }

  void _onDaySelected(DateTime selectedDay, DiaryService diaryService) async {
    final entry = diaryService.getEntryForDate(selectedDay);

    if (entry != null) {
      // View existing entry
      final result = await Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => EntryDetailScreen(entry: entry),
        ),
      );

      if (result == true) {
        setState(() {});
      }
    } else {
      // Create new entry for this date
      final confirm = await showDialog<bool>(
        context: context,
        builder: (context) => AlertDialog(
          title: const Text('Create Entry'),
          content: Text(
              'Would you like to create an entry for ${selectedDay.month}/${selectedDay.day}/${selectedDay.year}?'),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context, false),
              child: const Text('Cancel'),
            ),
            TextButton(
              onPressed: () => Navigator.pop(context, true),
              child: const Text('Create'),
            ),
          ],
        ),
      );

      if (confirm == true && mounted) {
        final result = await Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => EntryFormScreen(date: selectedDay),
          ),
        );

        if (result == true) {
          setState(() {});
        }
      }
    }
  }
}
