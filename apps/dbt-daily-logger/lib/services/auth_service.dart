import 'package:firebase_auth/firebase_auth.dart';

/// Authentication service handling Firebase Auth
class AuthService {
  final FirebaseAuth _auth = FirebaseAuth.instance;

  /// Get current user
  User? get currentUser => _auth.currentUser;

  /// Stream of auth state changes
  Stream<User?> get authStateChanges => _auth.authStateChanges();

  /// Sign in anonymously
  /// Used for low-friction initial setup
  Future<User?> signInAnonymously() async {
    try {
      final userCredential = await _auth.signInAnonymously();
      return userCredential.user;
    } catch (e) {
      print('Error signing in anonymously: $e');
      rethrow;
    }
  }

  /// Sign in with email and password
  /// Future feature for account linking
  Future<User?> signInWithEmail(String email, String password) async {
    try {
      final userCredential = await _auth.signInWithEmailAndPassword(
        email: email,
        password: password,
      );
      return userCredential.user;
    } catch (e) {
      print('Error signing in with email: $e');
      rethrow;
    }
  }

  /// Create account with email and password
  /// Future feature for account linking
  Future<User?> createAccountWithEmail(String email, String password) async {
    try {
      final userCredential = await _auth.createUserWithEmailAndPassword(
        email: email,
        password: password,
      );
      return userCredential.user;
    } catch (e) {
      print('Error creating account: $e');
      rethrow;
    }
  }

  /// Link anonymous account with email credentials
  /// Preserves user data when upgrading from anonymous to email auth
  Future<User?> linkAnonymousWithEmail(String email, String password) async {
    try {
      final user = currentUser;
      if (user == null || !user.isAnonymous) {
        throw Exception('No anonymous user to link');
      }

      final credential = EmailAuthProvider.credential(
        email: email,
        password: password,
      );

      final userCredential = await user.linkWithCredential(credential);
      return userCredential.user;
    } catch (e) {
      print('Error linking anonymous account: $e');
      rethrow;
    }
  }

  /// Sign out
  Future<void> signOut() async {
    try {
      await _auth.signOut();
    } catch (e) {
      print('Error signing out: $e');
      rethrow;
    }
  }

  /// Delete current user account
  /// Warning: This permanently deletes all user data
  Future<void> deleteAccount() async {
    try {
      final user = currentUser;
      if (user != null) {
        await user.delete();
      }
    } catch (e) {
      print('Error deleting account: $e');
      rethrow;
    }
  }
}
