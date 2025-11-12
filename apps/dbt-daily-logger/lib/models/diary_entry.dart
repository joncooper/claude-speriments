import 'package:cloud_firestore/cloud_firestore.dart';

/// Represents a single day's diary entry
class DiaryEntry {
  final String id;
  final String userId;
  final DateTime date;

  // Emotions (0-10 scale)
  final Map<String, int> emotions; // anger, fear, joy, sadness, guilt, shame

  // Urges (0-10 scale)
  final Map<String, int> urges;

  // Target behaviors (occurrence count)
  final Map<String, int> behaviors; // SI, NSSI, conflict, isolate, avoid, withhold, substance

  // DBT Skills used
  final List<String> skillsUsed;

  // Daily basics
  final double? sleepHours;
  final int? sleepQuality; // 0-5 scale
  final bool? exercised;
  final bool? tookMedication;

  // Notes
  final String? notes;

  // Metadata
  final DateTime createdAt;
  final DateTime updatedAt;

  DiaryEntry({
    required this.id,
    required this.userId,
    required this.date,
    required this.emotions,
    required this.urges,
    required this.behaviors,
    required this.skillsUsed,
    this.sleepHours,
    this.sleepQuality,
    this.exercised,
    this.tookMedication,
    this.notes,
    required this.createdAt,
    required this.updatedAt,
  });

  /// Convert to Firestore document
  Map<String, dynamic> toFirestore() {
    return {
      'userId': userId,
      'date': Timestamp.fromDate(date),
      'emotions': emotions,
      'urges': urges,
      'behaviors': behaviors,
      'skillsUsed': skillsUsed,
      'sleepHours': sleepHours,
      'sleepQuality': sleepQuality,
      'exercised': exercised,
      'tookMedication': tookMedication,
      'notes': notes,
      'createdAt': Timestamp.fromDate(createdAt),
      'updatedAt': Timestamp.fromDate(updatedAt),
    };
  }

  /// Create from Firestore document
  factory DiaryEntry.fromFirestore(DocumentSnapshot doc) {
    final data = doc.data() as Map<String, dynamic>;

    return DiaryEntry(
      id: doc.id,
      userId: data['userId'] as String,
      date: (data['date'] as Timestamp).toDate(),
      emotions: Map<String, int>.from(data['emotions'] ?? {}),
      urges: Map<String, int>.from(data['urges'] ?? {}),
      behaviors: Map<String, int>.from(data['behaviors'] ?? {}),
      skillsUsed: List<String>.from(data['skillsUsed'] ?? []),
      sleepHours: data['sleepHours']?.toDouble(),
      sleepQuality: data['sleepQuality'] as int?,
      exercised: data['exercised'] as bool?,
      tookMedication: data['tookMedication'] as bool?,
      notes: data['notes'] as String?,
      createdAt: (data['createdAt'] as Timestamp).toDate(),
      updatedAt: (data['updatedAt'] as Timestamp).toDate(),
    );
  }

  /// Create a copy with updated fields
  DiaryEntry copyWith({
    String? id,
    String? userId,
    DateTime? date,
    Map<String, int>? emotions,
    Map<String, int>? urges,
    Map<String, int>? behaviors,
    List<String>? skillsUsed,
    double? sleepHours,
    int? sleepQuality,
    bool? exercised,
    bool? tookMedication,
    String? notes,
    DateTime? createdAt,
    DateTime? updatedAt,
  }) {
    return DiaryEntry(
      id: id ?? this.id,
      userId: userId ?? this.userId,
      date: date ?? this.date,
      emotions: emotions ?? this.emotions,
      urges: urges ?? this.urges,
      behaviors: behaviors ?? this.behaviors,
      skillsUsed: skillsUsed ?? this.skillsUsed,
      sleepHours: sleepHours ?? this.sleepHours,
      sleepQuality: sleepQuality ?? this.sleepQuality,
      exercised: exercised ?? this.exercised,
      tookMedication: tookMedication ?? this.tookMedication,
      notes: notes ?? this.notes,
      createdAt: createdAt ?? this.createdAt,
      updatedAt: updatedAt ?? this.updatedAt,
    );
  }

  /// Create an empty entry for a new day
  factory DiaryEntry.empty({
    required String userId,
    required DateTime date,
  }) {
    final now = DateTime.now();
    return DiaryEntry(
      id: '', // Will be set by Firestore
      userId: userId,
      date: date,
      emotions: {},
      urges: {},
      behaviors: {},
      skillsUsed: [],
      createdAt: now,
      updatedAt: now,
    );
  }
}

/// Standard emotions tracked in DBT
class Emotions {
  static const String anger = 'Anger';
  static const String fear = 'Fear';
  static const String joy = 'Joy';
  static const String sadness = 'Sadness';
  static const String guilt = 'Guilt';
  static const String shame = 'Shame';

  static const List<String> all = [
    anger,
    fear,
    joy,
    sadness,
    guilt,
    shame,
  ];
}

/// Standard target behaviors tracked in DBT
class TargetBehaviors {
  static const String suicidalIdeation = 'SI';
  static const String selfHarm = 'NSSI';
  static const String conflict = 'Conflict';
  static const String isolate = 'Isolate';
  static const String avoid = 'Avoid';
  static const String withhold = 'Withhold';
  static const String substance = 'Substance';

  static const List<String> all = [
    suicidalIdeation,
    selfHarm,
    conflict,
    isolate,
    avoid,
    withhold,
    substance,
  ];
}
