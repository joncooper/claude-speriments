import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../providers/auth_provider.dart';
import '../../providers/entries_provider.dart';
import 'login_screen.dart';
import '../home_screen.dart';

/// Wrapper that handles authentication state and routing
class AuthWrapper extends StatelessWidget {
  const AuthWrapper({super.key});

  @override
  Widget build(BuildContext context) {
    return Consumer<AuthProvider>(
      builder: (context, authProvider, _) {
        // Show loading indicator while checking auth state
        if (authProvider.isLoading) {
          return const Scaffold(
            body: Center(
              child: CircularProgressIndicator(),
            ),
          );
        }

        // If user is authenticated, initialize entries provider and show home
        if (authProvider.isAuthenticated && authProvider.user != null) {
          // Initialize entries provider with current user
          WidgetsBinding.instance.addPostFrameCallback((_) {
            final entriesProvider = Provider.of<EntriesProvider>(context, listen: false);
            entriesProvider.initialize(authProvider.user!.uid);
          });

          return const HomeScreen();
        }

        // Otherwise show login screen
        return const LoginScreen();
      },
    );
  }
}
