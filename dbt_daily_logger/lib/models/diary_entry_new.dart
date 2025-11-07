import 'package:hive/hive.dart';

part 'diary_entry_new.g.dart';

@HiveType(typeId: 1)
class DailyEntry extends HiveObject {
  @HiveField(0)
  late DateTime date;

  // Behaviors (0-5 scale)
  @HiveField(1)
  int? si; // Self-Injury

  @HiveField(2)
  int? nssi; // Non-Suicidal Self-Injury

  @HiveField(3)
  int? familyConflict;

  @HiveField(4)
  int? isolate;

  @HiveField(5)
  int? avoidProcrastinate;

  @HiveField(6)
  int? withhold;

  @HiveField(7)
  int? substanceUse;

  // Eating
  @HiveField(8)
  String? eatingFrequency; // "Freq"

  @HiveField(9)
  int? numberOfMeals;

  // Physical Activity
  @HiveField(10)
  String? physicalActivityAmount;

  // Sleep
  @HiveField(11)
  String? sleepTime; // "7:01"

  @HiveField(12)
  String? wakeTime; // "Y" (awake on time?) or actual time

  @HiveField(13)
  String? bedTime;

  // Medications
  @HiveField(14)
  bool? tookMedication; // Y/N

  // Emotions (0-5 scale)
  @HiveField(15)
  int? anger;

  @HiveField(16)
  int? fearAnxiety;

  @HiveField(17)
  int? joy;

  @HiveField(18)
  int? sadness;

  @HiveField(19)
  int? guilt;

  @HiveField(20)
  int? shame;

  // Skills Usage (0-7 scale)
  @HiveField(21)
  int? usedSkills;

  // Notes
  @HiveField(22)
  String notes;

  DailyEntry({
    required this.date,
    this.si,
    this.nssi,
    this.familyConflict,
    this.isolate,
    this.avoidProcrastinate,
    this.withhold,
    this.substanceUse,
    this.eatingFrequency,
    this.numberOfMeals,
    this.physicalActivityAmount,
    this.sleepTime,
    this.wakeTime,
    this.bedTime,
    this.tookMedication,
    this.anger,
    this.fearAnxiety,
    this.joy,
    this.sadness,
    this.guilt,
    this.shame,
    this.usedSkills,
    String? notes,
  }) : notes = notes ?? '';

  // Get date without time for comparison
  DateTime get dateOnly => DateTime(date.year, date.month, date.day);

  // Calculate completion percentage
  double get completionPercentage {
    int totalFields = 23; // Total trackable fields
    int filledFields = 0;

    if (si != null) filledFields++;
    if (nssi != null) filledFields++;
    if (familyConflict != null) filledFields++;
    if (isolate != null) filledFields++;
    if (avoidProcrastinate != null) filledFields++;
    if (withhold != null) filledFields++;
    if (substanceUse != null) filledFields++;
    if (eatingFrequency != null) filledFields++;
    if (numberOfMeals != null) filledFields++;
    if (physicalActivityAmount != null) filledFields++;
    if (sleepTime != null) filledFields++;
    if (wakeTime != null) filledFields++;
    if (bedTime != null) filledFields++;
    if (tookMedication != null) filledFields++;
    if (anger != null) filledFields++;
    if (fearAnxiety != null) filledFields++;
    if (joy != null) filledFields++;
    if (sadness != null) filledFields++;
    if (guilt != null) filledFields++;
    if (shame != null) filledFields++;
    if (usedSkills != null) filledFields++;
    if (notes.isNotEmpty) filledFields++;

    return filledFields / totalFields;
  }

  // Check if entry has any content
  bool get hasContent {
    return si != null ||
        nssi != null ||
        familyConflict != null ||
        isolate != null ||
        avoidProcrastinate != null ||
        withhold != null ||
        substanceUse != null ||
        eatingFrequency != null ||
        numberOfMeals != null ||
        physicalActivityAmount != null ||
        sleepTime != null ||
        wakeTime != null ||
        bedTime != null ||
        tookMedication != null ||
        anger != null ||
        fearAnxiety != null ||
        joy != null ||
        sadness != null ||
        guilt != null ||
        shame != null ||
        usedSkills != null ||
        notes.isNotEmpty;
  }
}

@HiveType(typeId: 2)
class WeeklySkills extends HiveObject {
  @HiveField(0)
  late DateTime weekStart; // Monday of the week

  // Map of skill name -> list of 7 bools (Mon-Sun)
  @HiveField(1)
  Map<String, List<bool>> mindfulnessSkills;

  @HiveField(2)
  Map<String, List<bool>> emotionRegulationSkills;

  @HiveField(3)
  Map<String, List<bool>> distressToleranceSkills;

  @HiveField(4)
  Map<String, List<bool>> middlePathSkills;

  WeeklySkills({
    required this.weekStart,
    Map<String, List<bool>>? mindfulnessSkills,
    Map<String, List<bool>>? emotionRegulationSkills,
    Map<String, List<bool>>? distressToleranceSkills,
    Map<String, List<bool>>? middlePathSkills,
  })  : mindfulnessSkills = mindfulnessSkills ?? {},
        emotionRegulationSkills = emotionRegulationSkills ?? {},
        distressToleranceSkills = distressToleranceSkills ?? {},
        middlePathSkills = middlePathSkills ?? {};

  // Helper to get/set skill for a specific day
  void setSkill(String category, String skillName, int dayIndex, bool value) {
    Map<String, List<bool>> categoryMap;
    switch (category) {
      case 'Mindfulness':
        categoryMap = mindfulnessSkills;
        break;
      case 'Emotion Regulation':
        categoryMap = emotionRegulationSkills;
        break;
      case 'Distress Tolerance':
        categoryMap = distressToleranceSkills;
        break;
      case 'Middle Path':
        categoryMap = middlePathSkills;
        break;
      default:
        return;
    }

    if (!categoryMap.containsKey(skillName)) {
      categoryMap[skillName] = List.filled(7, false);
    }
    categoryMap[skillName]![dayIndex] = value;
  }

  bool getSkill(String category, String skillName, int dayIndex) {
    Map<String, List<bool>> categoryMap;
    switch (category) {
      case 'Mindfulness':
        categoryMap = mindfulnessSkills;
        break;
      case 'Emotion Regulation':
        categoryMap = emotionRegulationSkills;
        break;
      case 'Distress Tolerance':
        categoryMap = distressToleranceSkills;
        break;
      case 'Middle Path':
        categoryMap = middlePathSkills;
        break;
      default:
        return false;
    }

    if (!categoryMap.containsKey(skillName)) {
      return false;
    }
    return categoryMap[skillName]![dayIndex];
  }
}
