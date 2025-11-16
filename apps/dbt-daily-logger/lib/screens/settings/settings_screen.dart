import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../providers/auth_provider.dart';
import '../../models/user_profile.dart';

/// Settings screen for app preferences and account management
class SettingsScreen extends StatelessWidget {
  const SettingsScreen({super.key});

  Future<void> _showSignOutConfirmation(BuildContext context) async {
    final confirmed = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Sign Out'),
        content: const Text('Are you sure you want to sign out?'),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(false),
            child: const Text('Cancel'),
          ),
          FilledButton(
            onPressed: () => Navigator.of(context).pop(true),
            child: const Text('Sign Out'),
          ),
        ],
      ),
    );

    if (confirmed == true && context.mounted) {
      final authProvider = Provider.of<AuthProvider>(context, listen: false);
      await authProvider.signOut();
    }
  }

  Future<void> _showDeleteAccountConfirmation(BuildContext context) async {
    final confirmed = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Delete Account'),
        content: const Text(
          'Are you sure you want to delete your account? This will permanently delete all your data and cannot be undone.',
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(false),
            child: const Text('Cancel'),
          ),
          FilledButton(
            onPressed: () => Navigator.of(context).pop(true),
            style: FilledButton.styleFrom(
              backgroundColor: Theme.of(context).colorScheme.error,
            ),
            child: const Text('Delete'),
          ),
        ],
      ),
    );

    if (confirmed == true && context.mounted) {
      final authProvider = Provider.of<AuthProvider>(context, listen: false);

      try {
        await authProvider.deleteAccount();
        if (context.mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Account deleted')),
          );
        }
      } catch (e) {
        if (context.mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(content: Text('Failed to delete account: $e')),
          );
        }
      }
    }
  }

  Future<void> _updateTheme(BuildContext context, String themeMode) async {
    final authProvider = Provider.of<AuthProvider>(context, listen: false);
    final currentProfile = authProvider.userProfile;

    if (currentProfile != null) {
      final updatedProfile = currentProfile.copyWith(themeMode: themeMode);
      await authProvider.updateProfile(updatedProfile);
    }
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Consumer<AuthProvider>(
      builder: (context, authProvider, _) {
        final profile = authProvider.userProfile;
        final currentTheme = profile?.themeMode ?? 'system';

        return ListView(
          padding: const EdgeInsets.all(16),
          children: [
            // Appearance Section
            _buildSectionHeader(context, 'Appearance', Icons.palette),
            const SizedBox(height: 8),
            Card(
              child: Column(
                children: [
                  RadioListTile<String>(
                    title: const Text('Light Mode'),
                    subtitle: const Text('Always use light theme'),
                    value: 'light',
                    groupValue: currentTheme,
                    onChanged: (value) {
                      if (value != null) _updateTheme(context, value);
                    },
                    secondary: const Icon(Icons.light_mode),
                  ),
                  const Divider(height: 1),
                  RadioListTile<String>(
                    title: const Text('Dark Mode'),
                    subtitle: const Text('Always use dark theme'),
                    value: 'dark',
                    groupValue: currentTheme,
                    onChanged: (value) {
                      if (value != null) _updateTheme(context, value);
                    },
                    secondary: const Icon(Icons.dark_mode),
                  ),
                  const Divider(height: 1),
                  RadioListTile<String>(
                    title: const Text('System Default'),
                    subtitle: const Text('Follow system theme'),
                    value: 'system',
                    groupValue: currentTheme,
                    onChanged: (value) {
                      if (value != null) _updateTheme(context, value);
                    },
                    secondary: const Icon(Icons.brightness_auto),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 24),

            // Account Section
            _buildSectionHeader(context, 'Account', Icons.person),
            const SizedBox(height: 8),
            Card(
              child: Column(
                children: [
                  ListTile(
                    leading: const Icon(Icons.account_circle),
                    title: const Text('Account Type'),
                    subtitle: Text(
                      authProvider.user?.isAnonymous == true
                          ? 'Anonymous'
                          : 'Email',
                    ),
                  ),
                  if (authProvider.user?.isAnonymous == true) ...[
                    const Divider(height: 1),
                    ListTile(
                      leading: Icon(Icons.info_outline, color: theme.colorScheme.primary),
                      title: const Text('Upgrade to Email'),
                      subtitle: const Text('Link your account to save data permanently'),
                      trailing: const Icon(Icons.arrow_forward_ios, size: 16),
                      onTap: () {
                        ScaffoldMessenger.of(context).showSnackBar(
                          const SnackBar(
                            content: Text('Email linking coming soon!'),
                          ),
                        );
                      },
                    ),
                  ],
                  const Divider(height: 1),
                  ListTile(
                    leading: const Icon(Icons.logout),
                    title: const Text('Sign Out'),
                    onTap: () => _showSignOutConfirmation(context),
                  ),
                  const Divider(height: 1),
                  ListTile(
                    leading: Icon(Icons.delete_forever, color: theme.colorScheme.error),
                    title: Text(
                      'Delete Account',
                      style: TextStyle(color: theme.colorScheme.error),
                    ),
                    subtitle: const Text('Permanently delete all data'),
                    onTap: () => _showDeleteAccountConfirmation(context),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 24),

            // Data Section
            _buildSectionHeader(context, 'Data', Icons.storage),
            const SizedBox(height: 8),
            Card(
              child: Column(
                children: [
                  ListTile(
                    leading: const Icon(Icons.cloud_outlined),
                    title: const Text('Offline Support'),
                    subtitle: const Text('Data syncs automatically'),
                    trailing: Icon(
                      Icons.check_circle,
                      color: Colors.green,
                    ),
                  ),
                  const Divider(height: 1),
                  ListTile(
                    leading: const Icon(Icons.download),
                    title: const Text('Export Data'),
                    subtitle: const Text('Download your entries'),
                    trailing: const Icon(Icons.arrow_forward_ios, size: 16),
                    onTap: () {
                      ScaffoldMessenger.of(context).showSnackBar(
                        const SnackBar(
                          content: Text('Export feature coming soon!'),
                        ),
                      );
                    },
                  ),
                ],
              ),
            ),
            const SizedBox(height: 24),

            // About Section
            _buildSectionHeader(context, 'About', Icons.info),
            const SizedBox(height: 8),
            Card(
              child: Column(
                children: [
                  const ListTile(
                    leading: Icon(Icons.favorite),
                    title: Text('DBT Daily Logger'),
                    subtitle: Text('Version 1.0.0'),
                  ),
                  const Divider(height: 1),
                  ListTile(
                    leading: const Icon(Icons.privacy_tip),
                    title: const Text('Privacy Policy'),
                    trailing: const Icon(Icons.arrow_forward_ios, size: 16),
                    onTap: () {
                      ScaffoldMessenger.of(context).showSnackBar(
                        const SnackBar(
                          content: Text('Your data is private and secure'),
                        ),
                      );
                    },
                  ),
                  const Divider(height: 1),
                  ListTile(
                    leading: const Icon(Icons.description),
                    title: const Text('About DBT'),
                    trailing: const Icon(Icons.arrow_forward_ios, size: 16),
                    onTap: () {
                      ScaffoldMessenger.of(context).showSnackBar(
                        const SnackBar(
                          content: Text('DBT info coming soon!'),
                        ),
                      );
                    },
                  ),
                ],
              ),
            ),
          ],
        );
      },
    );
  }

  Widget _buildSectionHeader(BuildContext context, String title, IconData icon) {
    return Row(
      children: [
        Icon(icon, size: 20),
        const SizedBox(width: 8),
        Text(
          title,
          style: Theme.of(context).textTheme.titleMedium?.copyWith(
                fontWeight: FontWeight.bold,
              ),
        ),
      ],
    );
  }
}
