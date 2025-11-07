import 'package:hive/hive.dart';
import '../models/diary_entry.dart';

class DiaryService {
  static const String _boxName = 'diary_entries';
  Box<DiaryEntry>? _box;

  // Initialize Hive and open box
  Future<void> init() async {
    _box = await Hive.openBox<DiaryEntry>(_boxName);
  }

  // Get box (throw error if not initialized)
  Box<DiaryEntry> get _diaryBox {
    if (_box == null) {
      throw Exception('DiaryService not initialized. Call init() first.');
    }
    return _box!;
  }

  // Save or update a diary entry
  Future<void> saveEntry(DiaryEntry entry) async {
    // Check if entry for this date already exists
    final existingKey = _findKeyForDate(entry.dateOnly);

    if (existingKey != null) {
      // Update existing entry
      await _diaryBox.put(existingKey, entry);
    } else {
      // Add new entry
      await _diaryBox.add(entry);
    }
  }

  // Get entry for a specific date
  DiaryEntry? getEntryForDate(DateTime date) {
    final dateOnly = DateTime(date.year, date.month, date.day);

    for (var entry in _diaryBox.values) {
      if (_isSameDate(entry.dateOnly, dateOnly)) {
        return entry;
      }
    }
    return null;
  }

  // Get all entries sorted by date (newest first)
  List<DiaryEntry> getAllEntries() {
    final entries = _diaryBox.values.toList();
    entries.sort((a, b) => b.date.compareTo(a.date));
    return entries;
  }

  // Get entries for a date range
  List<DiaryEntry> getEntriesInRange(DateTime start, DateTime end) {
    final startDate = DateTime(start.year, start.month, start.day);
    final endDate = DateTime(end.year, end.month, end.day, 23, 59, 59);

    final entries = _diaryBox.values.where((entry) {
      return entry.date.isAfter(startDate.subtract(const Duration(days: 1))) &&
          entry.date.isBefore(endDate.add(const Duration(days: 1)));
    }).toList();

    entries.sort((a, b) => b.date.compareTo(a.date));
    return entries;
  }

  // Get entries from last N days
  List<DiaryEntry> getRecentEntries(int days) {
    final startDate = DateTime.now().subtract(Duration(days: days));
    return getEntriesInRange(startDate, DateTime.now());
  }

  // Delete an entry
  Future<void> deleteEntry(DiaryEntry entry) async {
    await entry.delete();
  }

  // Delete entry for a specific date
  Future<void> deleteEntryForDate(DateTime date) async {
    final key = _findKeyForDate(date);
    if (key != null) {
      await _diaryBox.delete(key);
    }
  }

  // Clear all entries
  Future<void> clearAllEntries() async {
    await _diaryBox.clear();
  }

  // Get statistics
  Map<String, dynamic> getStats({int? lastDays}) {
    List<DiaryEntry> entries;

    if (lastDays != null) {
      entries = getRecentEntries(lastDays);
    } else {
      entries = getAllEntries();
    }

    if (entries.isEmpty) {
      return {
        'totalEntries': 0,
        'averageEmotionIntensity': 0.0,
        'averageUrgeIntensity': 0.0,
        'mostUsedSkills': <String, int>{},
        'mostCommonEmotions': <String, int>{},
      };
    }

    // Calculate stats
    double totalEmotionIntensity = 0;
    double totalUrgeIntensity = 0;
    Map<String, int> skillsCount = {};
    Map<String, int> emotionsCount = {};

    for (var entry in entries) {
      totalEmotionIntensity += entry.averageEmotionIntensity;
      totalUrgeIntensity += entry.averageUrgeIntensity;

      for (var skill in entry.skillsUsed) {
        skillsCount[skill] = (skillsCount[skill] ?? 0) + 1;
      }

      for (var emotion in entry.emotions.keys) {
        emotionsCount[emotion] = (emotionsCount[emotion] ?? 0) + 1;
      }
    }

    return {
      'totalEntries': entries.length,
      'averageEmotionIntensity': totalEmotionIntensity / entries.length,
      'averageUrgeIntensity': totalUrgeIntensity / entries.length,
      'mostUsedSkills': skillsCount,
      'mostCommonEmotions': emotionsCount,
    };
  }

  // Helper methods
  dynamic _findKeyForDate(DateTime date) {
    final dateOnly = DateTime(date.year, date.month, date.day);

    for (var key in _diaryBox.keys) {
      final entry = _diaryBox.get(key);
      if (entry != null && _isSameDate(entry.dateOnly, dateOnly)) {
        return key;
      }
    }
    return null;
  }

  bool _isSameDate(DateTime date1, DateTime date2) {
    return date1.year == date2.year &&
        date1.month == date2.month &&
        date1.day == date2.day;
  }
}
