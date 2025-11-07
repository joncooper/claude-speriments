// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'diary_entry_new.dart';

// **************************************************************************
// TypeAdapterGenerator
// **************************************************************************

class DailyEntryAdapter extends TypeAdapter<DailyEntry> {
  @override
  final int typeId = 1;

  @override
  DailyEntry read(BinaryReader reader) {
    final numOfFields = reader.readByte();
    final fields = <int, dynamic>{
      for (int i = 0; i < numOfFields; i++) reader.readByte(): reader.read(),
    };
    return DailyEntry(
      date: fields[0] as DateTime,
      si: fields[1] as int?,
      nssi: fields[2] as int?,
      familyConflict: fields[3] as int?,
      isolate: fields[4] as int?,
      avoidProcrastinate: fields[5] as int?,
      withhold: fields[6] as int?,
      substanceUse: fields[7] as int?,
      eatingFrequency: fields[8] as String?,
      numberOfMeals: fields[9] as int?,
      physicalActivityAmount: fields[10] as String?,
      sleepTime: fields[11] as String?,
      wakeTime: fields[12] as String?,
      bedTime: fields[13] as String?,
      tookMedication: fields[14] as bool?,
      anger: fields[15] as int?,
      fearAnxiety: fields[16] as int?,
      joy: fields[17] as int?,
      sadness: fields[18] as int?,
      guilt: fields[19] as int?,
      shame: fields[20] as int?,
      usedSkills: fields[21] as int?,
      notes: fields[22] as String?,
    );
  }

  @override
  void write(BinaryWriter writer, DailyEntry obj) {
    writer
      ..writeByte(23)
      ..writeByte(0)
      ..write(obj.date)
      ..writeByte(1)
      ..write(obj.si)
      ..writeByte(2)
      ..write(obj.nssi)
      ..writeByte(3)
      ..write(obj.familyConflict)
      ..writeByte(4)
      ..write(obj.isolate)
      ..writeByte(5)
      ..write(obj.avoidProcrastinate)
      ..writeByte(6)
      ..write(obj.withhold)
      ..writeByte(7)
      ..write(obj.substanceUse)
      ..writeByte(8)
      ..write(obj.eatingFrequency)
      ..writeByte(9)
      ..write(obj.numberOfMeals)
      ..writeByte(10)
      ..write(obj.physicalActivityAmount)
      ..writeByte(11)
      ..write(obj.sleepTime)
      ..writeByte(12)
      ..write(obj.wakeTime)
      ..writeByte(13)
      ..write(obj.bedTime)
      ..writeByte(14)
      ..write(obj.tookMedication)
      ..writeByte(15)
      ..write(obj.anger)
      ..writeByte(16)
      ..write(obj.fearAnxiety)
      ..writeByte(17)
      ..write(obj.joy)
      ..writeByte(18)
      ..write(obj.sadness)
      ..writeByte(19)
      ..write(obj.guilt)
      ..writeByte(20)
      ..write(obj.shame)
      ..writeByte(21)
      ..write(obj.usedSkills)
      ..writeByte(22)
      ..write(obj.notes);
  }

  @override
  int get hashCode => typeId.hashCode;

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is DailyEntryAdapter &&
          runtimeType == other.runtimeType &&
          typeId == other.typeId;
}

class WeeklySkillsAdapter extends TypeAdapter<WeeklySkills> {
  @override
  final int typeId = 2;

  @override
  WeeklySkills read(BinaryReader reader) {
    final numOfFields = reader.readByte();
    final fields = <int, dynamic>{
      for (int i = 0; i < numOfFields; i++) reader.readByte(): reader.read(),
    };
    return WeeklySkills(
      weekStart: fields[0] as DateTime,
      mindfulnessSkills: (fields[1] as Map?)?.map((dynamic k, dynamic v) =>
          MapEntry(k as String, (v as List).cast<bool>())),
      emotionRegulationSkills: (fields[2] as Map?)?.map(
          (dynamic k, dynamic v) =>
              MapEntry(k as String, (v as List).cast<bool>())),
      distressToleranceSkills: (fields[3] as Map?)?.map(
          (dynamic k, dynamic v) =>
              MapEntry(k as String, (v as List).cast<bool>())),
      middlePathSkills: (fields[4] as Map?)?.map((dynamic k, dynamic v) =>
          MapEntry(k as String, (v as List).cast<bool>())),
    );
  }

  @override
  void write(BinaryWriter writer, WeeklySkills obj) {
    writer
      ..writeByte(5)
      ..writeByte(0)
      ..write(obj.weekStart)
      ..writeByte(1)
      ..write(obj.mindfulnessSkills)
      ..writeByte(2)
      ..write(obj.emotionRegulationSkills)
      ..writeByte(3)
      ..write(obj.distressToleranceSkills)
      ..writeByte(4)
      ..write(obj.middlePathSkills);
  }

  @override
  int get hashCode => typeId.hashCode;

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is WeeklySkillsAdapter &&
          runtimeType == other.runtimeType &&
          typeId == other.typeId;
}
