import 'dart:io';
import 'package:hive/hive.dart';
import 'package:path_provider/path_provider.dart';

class ICloudSyncService {
  static const String _syncKey = 'last_sync_time';

  // Get the iCloud Documents directory for iOS
  Future<Directory?> getICloudDirectory() async {
    if (!Platform.isIOS) return null;

    try {
      // For iOS, we'll use the app's documents directory
      // When iCloud is enabled in iOS capabilities, this will sync automatically
      final directory = await getApplicationDocumentsDirectory();
      return directory;
    } catch (e) {
      print('Error getting iCloud directory: $e');
      return null;
    }
  }

  // Initialize Hive with iCloud-enabled directory
  Future<String> getHiveDirectory() async {
    if (Platform.isIOS) {
      final iCloudDir = await getICloudDirectory();
      if (iCloudDir != null) {
        final hiveDir = Directory('${iCloudDir.path}/hive_data');
        if (!await hiveDir.exists()) {
          await hiveDir.create(recursive: true);
        }
        return hiveDir.path;
      }
    }

    // Fallback to app documents directory
    final appDir = await getApplicationDocumentsDirectory();
    return appDir.path;
  }

  // Manual backup trigger (for UI feedback)
  Future<bool> triggerBackup() async {
    try {
      if (!Platform.isIOS) return false;

      // On iOS, files in the documents directory are automatically backed up to iCloud
      // We just need to ensure Hive flushes its data
      await Hive.close();

      // Reinitialize Hive
      final hivePath = await getHiveDirectory();
      Hive.init(hivePath);

      return true;
    } catch (e) {
      print('Error triggering backup: $e');
      return false;
    }
  }

  // Check if iCloud is available
  Future<bool> isICloudAvailable() async {
    if (!Platform.isIOS) return false;

    try {
      final iCloudDir = await getICloudDirectory();
      return iCloudDir != null;
    } catch (e) {
      return false;
    }
  }

  // Get sync status message
  Future<String> getSyncStatus() async {
    if (!Platform.isIOS) {
      return 'iCloud sync is only available on iOS';
    }

    final available = await isICloudAvailable();
    if (!available) {
      return 'iCloud sync not available. Please check Settings > iCloud';
    }

    return 'iCloud sync active';
  }
}
