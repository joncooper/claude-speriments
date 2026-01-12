import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';

/// User profile and settings
class UserProfile {
  final String userId;
  final DateTime createdAt;
  final String themeMode; // 'light', 'dark', or 'system'
  final bool notificationsEnabled;

  UserProfile({
    required this.userId,
    required this.createdAt,
    this.themeMode = 'system',
    this.notificationsEnabled = false,
  });

  /// Convert to Firestore document
  Map<String, dynamic> toFirestore() {
    return {
      'createdAt': Timestamp.fromDate(createdAt),
      'themeMode': themeMode,
      'notificationsEnabled': notificationsEnabled,
    };
  }

  /// Create from Firestore document
  factory UserProfile.fromFirestore(DocumentSnapshot doc) {
    final data = doc.data() as Map<String, dynamic>;

    return UserProfile(
      userId: doc.id,
      createdAt: (data['createdAt'] as Timestamp).toDate(),
      themeMode: data['themeMode'] as String? ?? 'system',
      notificationsEnabled: data['notificationsEnabled'] as bool? ?? false,
    );
  }

  /// Create a copy with updated fields
  UserProfile copyWith({
    String? userId,
    DateTime? createdAt,
    String? themeMode,
    bool? notificationsEnabled,
  }) {
    return UserProfile(
      userId: userId ?? this.userId,
      createdAt: createdAt ?? this.createdAt,
      themeMode: themeMode ?? this.themeMode,
      notificationsEnabled: notificationsEnabled ?? this.notificationsEnabled,
    );
  }

  /// Convert theme mode string to ThemeMode enum
  ThemeMode get themeModeEnum {
    switch (themeMode) {
      case 'light':
        return ThemeMode.light;
      case 'dark':
        return ThemeMode.dark;
      default:
        return ThemeMode.system;
    }
  }

  /// Create default profile for new user
  factory UserProfile.defaultProfile(String userId) {
    return UserProfile(
      userId: userId,
      createdAt: DateTime.now(),
      themeMode: 'system',
      notificationsEnabled: false,
    );
  }
}
