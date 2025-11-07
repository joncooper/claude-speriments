import 'dart:convert';
import 'dart:io';
import 'package:path_provider/path_provider.dart';

// Simplified storage for quick implementation
class DailyEntryData {
  final DateTime date;
  Map<String, int?> behaviors = {};
  Map<String, int?> emotions = {};
  String? sleepTime;
  String? wakeTime;
  String? bedTime;
  bool? tookMeds;
  String? notes;
  int? usedSkills;
  List<String> skillsUsedToday = []; // Specific DBT skills used

  DailyEntryData({required this.date});

  Map<String, dynamic> toJson() => {
        'date': date.toIso8601String(),
        'behaviors': behaviors,
        'emotions': emotions,
        'sleepTime': sleepTime,
        'wakeTime': wakeTime,
        'bedTime': bedTime,
        'tookMeds': tookMeds,
        'notes': notes,
        'usedSkills': usedSkills,
        'skillsUsedToday': skillsUsedToday,
      };

  factory DailyEntryData.fromJson(Map<String, dynamic> json) {
    final entry = DailyEntryData(date: DateTime.parse(json['date']));
    entry.behaviors = Map<String, int?>.from(json['behaviors'] ?? {});
    entry.emotions = Map<String, int?>.from(json['emotions'] ?? {});
    entry.sleepTime = json['sleepTime'];
    entry.wakeTime = json['wakeTime'];
    entry.bedTime = json['bedTime'];
    entry.tookMeds = json['tookMeds'];
    entry.notes = json['notes'];
    entry.usedSkills = json['usedSkills'];
    entry.skillsUsedToday = List<String>.from(json['skillsUsedToday'] ?? []);
    return entry;
  }
}

class SimpleStorage {
  static Future<String> get _localPath async {
    final directory = await getApplicationDocumentsDirectory();
    return directory.path;
  }

  static Future<File> get _localFile async {
    final path = await _localPath;
    return File('$path/dbt_entries.json');
  }

  static Future<List<DailyEntryData>> loadEntries() async {
    try {
      final file = await _localFile;
      if (!await file.exists()) return [];

      final contents = await file.readAsString();
      final List<dynamic> jsonList = json.decode(contents);
      return jsonList.map((j) => DailyEntryData.fromJson(j)).toList();
    } catch (e) {
      return [];
    }
  }

  static Future<void> saveEntry(DailyEntryData entry) async {
    print('💾 Saving entry for date: ${entry.date}');
    final entries = await loadEntries();
    print('📋 Loaded ${entries.length} existing entries');

    // Remove existing entry for same date
    entries.removeWhere((e) =>
      e.date.year == entry.date.year &&
      e.date.month == entry.date.month &&
      e.date.day == entry.date.day
    );

    entries.add(entry);
    entries.sort((a, b) => b.date.compareTo(a.date));
    print('✅ Now have ${entries.length} total entries');

    final file = await _localFile;
    await file.writeAsString(json.encode(entries.map((e) => e.toJson()).toList()));
    print('💿 Saved to file: ${file.path}');
  }

  static Future<DailyEntryData?> getEntryForDate(DateTime date) async {
    final entries = await loadEntries();
    try {
      return entries.firstWhere((e) =>
        e.date.year == date.year &&
        e.date.month == date.month &&
        e.date.day == date.day
      );
    } catch (e) {
      return null;
    }
  }
}
