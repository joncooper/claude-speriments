import 'package:flutter/foundation.dart';
import 'package:firebase_auth/firebase_auth.dart';
import '../services/auth_service.dart';
import '../services/firestore_service.dart';
import '../models/user_profile.dart';

/// Provider for authentication state
class AuthProvider with ChangeNotifier {
  final AuthService _authService = AuthService();
  final FirestoreService _firestoreService = FirestoreService();

  User? _user;
  UserProfile? _userProfile;
  bool _isLoading = false;
  String? _error;

  User? get user => _user;
  UserProfile? get userProfile => _userProfile;
  bool get isLoading => _isLoading;
  String? get error => _error;
  bool get isAuthenticated => _user != null;

  AuthProvider() {
    // Listen to auth state changes
    _authService.authStateChanges.listen((user) {
      _user = user;
      _error = null;

      if (user != null) {
        _loadUserProfile();
      } else {
        _userProfile = null;
      }

      notifyListeners();
    });
  }

  /// Load user profile from Firestore
  Future<void> _loadUserProfile() async {
    if (_user == null) return;

    try {
      _userProfile = await _firestoreService.getUserProfile(_user!.uid);
      notifyListeners();
    } catch (e) {
      print('Error loading user profile: $e');
      _error = e.toString();
      notifyListeners();
    }
  }

  /// Sign in anonymously
  Future<void> signInAnonymously() async {
    _isLoading = true;
    _error = null;
    notifyListeners();

    try {
      await _authService.signInAnonymously();
      // User and profile will be loaded via authStateChanges listener
    } catch (e) {
      _error = 'Failed to sign in: $e';
      print('Error signing in: $e');
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  /// Sign in with email and password
  Future<void> signInWithEmail(String email, String password) async {
    _isLoading = true;
    _error = null;
    notifyListeners();

    try {
      await _authService.signInWithEmail(email, password);
    } catch (e) {
      _error = 'Failed to sign in: $e';
      print('Error signing in: $e');
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  /// Create account with email and password
  Future<void> createAccount(String email, String password) async {
    _isLoading = true;
    _error = null;
    notifyListeners();

    try {
      await _authService.createAccountWithEmail(email, password);
    } catch (e) {
      _error = 'Failed to create account: $e';
      print('Error creating account: $e');
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  /// Link anonymous account with email
  Future<void> linkWithEmail(String email, String password) async {
    _isLoading = true;
    _error = null;
    notifyListeners();

    try {
      await _authService.linkAnonymousWithEmail(email, password);
    } catch (e) {
      _error = 'Failed to link account: $e';
      print('Error linking account: $e');
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  /// Sign out
  Future<void> signOut() async {
    _isLoading = true;
    _error = null;
    notifyListeners();

    try {
      await _authService.signOut();
      _user = null;
      _userProfile = null;
    } catch (e) {
      _error = 'Failed to sign out: $e';
      print('Error signing out: $e');
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  /// Update user profile settings
  Future<void> updateProfile(UserProfile profile) async {
    _isLoading = true;
    _error = null;
    notifyListeners();

    try {
      await _firestoreService.updateUserProfile(profile);
      _userProfile = profile;
    } catch (e) {
      _error = 'Failed to update profile: $e';
      print('Error updating profile: $e');
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  /// Delete account and all data
  Future<void> deleteAccount() async {
    if (_user == null) return;

    _isLoading = true;
    _error = null;
    notifyListeners();

    try {
      // Delete all entries first
      await _firestoreService.deleteAllEntries(_user!.uid);

      // Delete auth account
      await _authService.deleteAccount();

      _user = null;
      _userProfile = null;
    } catch (e) {
      _error = 'Failed to delete account: $e';
      print('Error deleting account: $e');
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }
}
