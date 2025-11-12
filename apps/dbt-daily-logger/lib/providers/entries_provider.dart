import 'package:flutter/foundation.dart';
import 'dart:async';
import '../models/diary_entry.dart';
import '../services/firestore_service.dart';

/// Provider for managing diary entries
class EntriesProvider with ChangeNotifier {
  final FirestoreService _firestoreService = FirestoreService();

  List<DiaryEntry> _entries = [];
  bool _isLoading = false;
  String? _error;
  StreamSubscription<List<DiaryEntry>>? _entriesSubscription;

  List<DiaryEntry> get entries => _entries;
  bool get isLoading => _isLoading;
  String? get error => _error;

  /// Initialize provider with user ID and start listening to entries
  void initialize(String userId) {
    _entriesSubscription?.cancel();

    _isLoading = true;
    notifyListeners();

    _entriesSubscription = _firestoreService.getEntriesStream(userId).listen(
      (entries) {
        _entries = entries;
        _isLoading = false;
        _error = null;
        notifyListeners();
      },
      onError: (error) {
        print('Error loading entries: $error');
        _error = error.toString();
        _isLoading = false;
        notifyListeners();
      },
    );
  }

  /// Dispose and clean up subscriptions
  @override
  void dispose() {
    _entriesSubscription?.cancel();
    super.dispose();
  }

  /// Create a new entry
  Future<DiaryEntry> createEntry(DiaryEntry entry) async {
    _isLoading = true;
    _error = null;
    notifyListeners();

    try {
      final newEntry = await _firestoreService.createEntry(entry);
      // Entry will be added to list via stream listener
      return newEntry;
    } catch (e) {
      _error = 'Failed to create entry: $e';
      print('Error creating entry: $e');
      rethrow;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  /// Update an existing entry
  Future<void> updateEntry(DiaryEntry entry) async {
    _isLoading = true;
    _error = null;
    notifyListeners();

    try {
      await _firestoreService.updateEntry(entry);
      // Entry will be updated in list via stream listener
    } catch (e) {
      _error = 'Failed to update entry: $e';
      print('Error updating entry: $e');
      rethrow;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  /// Delete an entry
  Future<void> deleteEntry(String userId, String entryId) async {
    _isLoading = true;
    _error = null;
    notifyListeners();

    try {
      await _firestoreService.deleteEntry(userId, entryId);
      // Entry will be removed from list via stream listener
    } catch (e) {
      _error = 'Failed to delete entry: $e';
      print('Error deleting entry: $e');
      rethrow;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  /// Get entry for a specific date
  Future<DiaryEntry?> getEntryForDate(String userId, DateTime date) async {
    try {
      return await _firestoreService.getEntryForDate(userId, date);
    } catch (e) {
      _error = 'Failed to get entry: $e';
      print('Error getting entry for date: $e');
      notifyListeners();
      return null;
    }
  }

  /// Get entries for a specific week
  Future<List<DiaryEntry>> getEntriesForWeek(String userId, DateTime weekStart) async {
    try {
      return await _firestoreService.getEntriesForWeek(userId, weekStart);
    } catch (e) {
      _error = 'Failed to get entries: $e';
      print('Error getting entries for week: $e');
      notifyListeners();
      return [];
    }
  }

  /// Get entries for a specific month
  Future<List<DiaryEntry>> getEntriesForMonth(String userId, DateTime month) async {
    try {
      return await _firestoreService.getEntriesForMonth(userId, month);
    } catch (e) {
      _error = 'Failed to get entries: $e';
      print('Error getting entries for month: $e');
      notifyListeners();
      return [];
    }
  }

  /// Get entry by ID from loaded entries
  DiaryEntry? getEntryById(String entryId) {
    try {
      return _entries.firstWhere((entry) => entry.id == entryId);
    } catch (e) {
      return null;
    }
  }

  /// Check if an entry exists for a specific date
  bool hasEntryForDate(DateTime date) {
    final startOfDay = DateTime(date.year, date.month, date.day);
    final endOfDay = DateTime(date.year, date.month, date.day, 23, 59, 59);

    return _entries.any((entry) =>
        entry.date.isAfter(startOfDay) && entry.date.isBefore(endOfDay));
  }

  /// Clear error
  void clearError() {
    _error = null;
    notifyListeners();
  }
}
