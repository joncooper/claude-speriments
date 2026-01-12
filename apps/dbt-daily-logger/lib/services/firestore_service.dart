import 'package:cloud_firestore/cloud_firestore.dart';
import '../models/diary_entry.dart';
import '../models/user_profile.dart';

/// Firestore service for managing diary entries and user profiles
class FirestoreService {
  final FirebaseFirestore _firestore = FirebaseFirestore.instance;

  // ========== User Profile Operations ==========

  /// Get user profile reference
  DocumentReference<Map<String, dynamic>> _userProfileRef(String userId) {
    return _firestore.collection('users').doc(userId).collection('profile').doc('settings');
  }

  /// Get or create user profile
  Future<UserProfile> getUserProfile(String userId) async {
    try {
      final doc = await _userProfileRef(userId).get();

      if (doc.exists) {
        return UserProfile.fromFirestore(doc);
      } else {
        // Create default profile
        final profile = UserProfile.defaultProfile(userId);
        await updateUserProfile(profile);
        return profile;
      }
    } catch (e) {
      print('Error getting user profile: $e');
      rethrow;
    }
  }

  /// Update user profile
  Future<void> updateUserProfile(UserProfile profile) async {
    try {
      await _userProfileRef(profile.userId).set(profile.toFirestore());
    } catch (e) {
      print('Error updating user profile: $e');
      rethrow;
    }
  }

  // ========== Diary Entry Operations ==========

  /// Get entries collection reference for a user
  CollectionReference<Map<String, dynamic>> _entriesRef(String userId) {
    return _firestore.collection('users').doc(userId).collection('entries');
  }

  /// Create a new diary entry
  Future<DiaryEntry> createEntry(DiaryEntry entry) async {
    try {
      final docRef = await _entriesRef(entry.userId).add(entry.toFirestore());
      final doc = await docRef.get();
      return DiaryEntry.fromFirestore(doc);
    } catch (e) {
      print('Error creating entry: $e');
      rethrow;
    }
  }

  /// Update an existing diary entry
  Future<void> updateEntry(DiaryEntry entry) async {
    try {
      final updatedEntry = entry.copyWith(updatedAt: DateTime.now());
      await _entriesRef(entry.userId).doc(entry.id).update(updatedEntry.toFirestore());
    } catch (e) {
      print('Error updating entry: $e');
      rethrow;
    }
  }

  /// Delete a diary entry
  Future<void> deleteEntry(String userId, String entryId) async {
    try {
      await _entriesRef(userId).doc(entryId).delete();
    } catch (e) {
      print('Error deleting entry: $e');
      rethrow;
    }
  }

  /// Get a single entry by ID
  Future<DiaryEntry?> getEntry(String userId, String entryId) async {
    try {
      final doc = await _entriesRef(userId).doc(entryId).get();

      if (doc.exists) {
        return DiaryEntry.fromFirestore(doc);
      }
      return null;
    } catch (e) {
      print('Error getting entry: $e');
      rethrow;
    }
  }

  /// Get entry for a specific date
  Future<DiaryEntry?> getEntryForDate(String userId, DateTime date) async {
    try {
      // Normalize date to start of day
      final startOfDay = DateTime(date.year, date.month, date.day);
      final endOfDay = DateTime(date.year, date.month, date.day, 23, 59, 59);

      final query = await _entriesRef(userId)
          .where('date', isGreaterThanOrEqualTo: Timestamp.fromDate(startOfDay))
          .where('date', isLessThanOrEqualTo: Timestamp.fromDate(endOfDay))
          .limit(1)
          .get();

      if (query.docs.isNotEmpty) {
        return DiaryEntry.fromFirestore(query.docs.first);
      }
      return null;
    } catch (e) {
      print('Error getting entry for date: $e');
      rethrow;
    }
  }

  /// Get all entries for a user (paginated)
  Stream<List<DiaryEntry>> getEntriesStream(String userId, {int limit = 50}) {
    return _entriesRef(userId)
        .orderBy('date', descending: true)
        .limit(limit)
        .snapshots()
        .map((snapshot) {
      return snapshot.docs.map((doc) => DiaryEntry.fromFirestore(doc)).toList();
    });
  }

  /// Get entries for a specific date range
  Future<List<DiaryEntry>> getEntriesInRange(
    String userId,
    DateTime startDate,
    DateTime endDate,
  ) async {
    try {
      final query = await _entriesRef(userId)
          .where('date', isGreaterThanOrEqualTo: Timestamp.fromDate(startDate))
          .where('date', isLessThanOrEqualTo: Timestamp.fromDate(endDate))
          .orderBy('date', descending: false)
          .get();

      return query.docs.map((doc) => DiaryEntry.fromFirestore(doc)).toList();
    } catch (e) {
      print('Error getting entries in range: $e');
      rethrow;
    }
  }

  /// Get entries for a specific week
  Future<List<DiaryEntry>> getEntriesForWeek(String userId, DateTime weekStart) async {
    final weekEnd = weekStart.add(const Duration(days: 7));
    return getEntriesInRange(userId, weekStart, weekEnd);
  }

  /// Get entries for a specific month
  Future<List<DiaryEntry>> getEntriesForMonth(String userId, DateTime month) async {
    final startOfMonth = DateTime(month.year, month.month, 1);
    final endOfMonth = DateTime(month.year, month.month + 1, 0, 23, 59, 59);
    return getEntriesInRange(userId, startOfMonth, endOfMonth);
  }

  /// Delete all entries for a user
  /// Warning: This permanently deletes all user data
  Future<void> deleteAllEntries(String userId) async {
    try {
      final entries = await _entriesRef(userId).get();

      // Delete in batches
      final batch = _firestore.batch();
      for (final doc in entries.docs) {
        batch.delete(doc.reference);
      }
      await batch.commit();
    } catch (e) {
      print('Error deleting all entries: $e');
      rethrow;
    }
  }
}
