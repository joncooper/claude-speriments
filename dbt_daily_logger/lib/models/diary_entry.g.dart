// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'diary_entry.dart';

// **************************************************************************
// TypeAdapterGenerator
// **************************************************************************

class DiaryEntryAdapter extends TypeAdapter<DiaryEntry> {
  @override
  final int typeId = 0;

  @override
  DiaryEntry read(BinaryReader reader) {
    final numOfFields = reader.readByte();
    final fields = <int, dynamic>{
      for (int i = 0; i < numOfFields; i++) reader.readByte(): reader.read(),
    };
    return DiaryEntry(
      date: fields[0] as DateTime,
      emotions: (fields[1] as Map?)?.cast<String, int>(),
      urges: (fields[2] as Map?)?.cast<String, int>(),
      targetBehaviors: (fields[3] as List?)?.cast<String>(),
      skillsUsed: (fields[4] as List?)?.cast<String>(),
      notes: fields[5] as String?,
      sleepHours: fields[6] as int?,
      tookMedication: fields[7] as bool?,
    );
  }

  @override
  void write(BinaryWriter writer, DiaryEntry obj) {
    writer
      ..writeByte(8)
      ..writeByte(0)
      ..write(obj.date)
      ..writeByte(1)
      ..write(obj.emotions)
      ..writeByte(2)
      ..write(obj.urges)
      ..writeByte(3)
      ..write(obj.targetBehaviors)
      ..writeByte(4)
      ..write(obj.skillsUsed)
      ..writeByte(5)
      ..write(obj.notes)
      ..writeByte(6)
      ..write(obj.sleepHours)
      ..writeByte(7)
      ..write(obj.tookMedication);
  }

  @override
  int get hashCode => typeId.hashCode;

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is DiaryEntryAdapter &&
          runtimeType == other.runtimeType &&
          typeId == other.typeId;
}
