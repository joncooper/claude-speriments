import 'package:hive/hive.dart';

part 'diary_entry.g.dart';

@HiveType(typeId: 0)
class DiaryEntry extends HiveObject {
  @HiveField(0)
  late DateTime date;

  @HiveField(1)
  Map<String, int> emotions; // emotion name -> intensity (0-10)

  @HiveField(2)
  Map<String, int> urges; // urge name -> intensity (0-10)

  @HiveField(3)
  List<String> targetBehaviors; // behaviors that occurred

  @HiveField(4)
  List<String> skillsUsed; // DBT skills used

  @HiveField(5)
  String notes;

  @HiveField(6)
  int? sleepHours;

  @HiveField(7)
  bool? tookMedication;

  DiaryEntry({
    required this.date,
    Map<String, int>? emotions,
    Map<String, int>? urges,
    List<String>? targetBehaviors,
    List<String>? skillsUsed,
    String? notes,
    this.sleepHours,
    this.tookMedication,
  })  : emotions = emotions ?? {},
        urges = urges ?? {},
        targetBehaviors = targetBehaviors ?? [],
        skillsUsed = skillsUsed ?? [],
        notes = notes ?? '';

  // Get date without time for comparison
  DateTime get dateOnly => DateTime(date.year, date.month, date.day);

  // Calculate average emotion intensity
  double get averageEmotionIntensity {
    if (emotions.isEmpty) return 0.0;
    return emotions.values.reduce((a, b) => a + b) / emotions.length;
  }

  // Calculate average urge intensity
  double get averageUrgeIntensity {
    if (urges.isEmpty) return 0.0;
    return urges.values.reduce((a, b) => a + b) / urges.length;
  }

  // Check if entry has any content
  bool get hasContent {
    return emotions.isNotEmpty ||
        urges.isNotEmpty ||
        targetBehaviors.isNotEmpty ||
        skillsUsed.isNotEmpty ||
        notes.isNotEmpty ||
        sleepHours != null ||
        tookMedication != null;
  }
}
