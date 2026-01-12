import 'package:flutter/material.dart';

/// Application-wide constants
class AppConstants {
  // App info
  static const String appName = 'DBT Daily Logger';
  static const String appVersion = '1.0.0';

  // Module colors (centralized for consistency)
  static const Map<String, Color> moduleColors = {
    'Mindfulness': Colors.purple,
    'Distress Tolerance': Colors.blue,
    'Emotion Regulation': Colors.green,
    'Interpersonal Effectiveness': Colors.orange,
  };

  /// Get color for a DBT module
  static Color getModuleColor(String module) {
    return moduleColors[module] ?? Colors.grey;
  }

  /// Get icon for a DBT module
  static IconData getModuleIcon(String module) {
    switch (module) {
      case 'Mindfulness':
        return Icons.self_improvement;
      case 'Distress Tolerance':
        return Icons.favorite;
      case 'Emotion Regulation':
        return Icons.psychology;
      case 'Interpersonal Effectiveness':
        return Icons.people;
      default:
        return Icons.star;
    }
  }

  /// Get color for emotion/behavior intensity (0-10 scale)
  static Color getIntensityColor(int intensity) {
    if (intensity == 0) {
      return Colors.grey;
    } else if (intensity <= 3) {
      return Colors.green;
    } else if (intensity <= 7) {
      return Colors.orange;
    } else {
      return Colors.red;
    }
  }

  /// Get color for sleep hours
  static Color getSleepHoursColor(double hours) {
    if (hours == 0) {
      return Colors.grey;
    } else if (hours < 6) {
      return Colors.red;
    } else if (hours < 7) {
      return Colors.orange;
    } else if (hours <= 9) {
      return Colors.green;
    } else {
      return Colors.blue;
    }
  }

  /// Get color for sleep quality (0-5 scale)
  static Color getSleepQualityColor(int quality) {
    switch (quality) {
      case 0:
        return Colors.red.shade700;
      case 1:
        return Colors.red.shade400;
      case 2:
        return Colors.orange;
      case 3:
        return Colors.yellow.shade700;
      case 4:
        return Colors.lightGreen;
      case 5:
        return Colors.green;
      default:
        return Colors.grey;
    }
  }

  /// Get emoji for sleep quality (0-5 scale)
  static String getSleepQualityEmoji(int quality) {
    switch (quality) {
      case 0:
        return '😫';
      case 1:
        return '😔';
      case 2:
        return '😐';
      case 3:
        return '🙂';
      case 4:
        return '😊';
      case 5:
        return '😴';
      default:
        return '😐';
    }
  }
}
