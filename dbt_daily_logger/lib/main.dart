import 'package:flutter/material.dart';
import 'package:hive_flutter/hive_flutter.dart';
import 'package:provider/provider.dart';
import 'models/diary_entry.dart';
import 'services/diary_service.dart';
import 'services/theme_service.dart';
import 'services/icloud_sync_service.dart';
import 'screens/home_screen.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Initialize iCloud sync service
  final iCloudService = ICloudSyncService();
  final hivePath = await iCloudService.getHiveDirectory();

  // Initialize Hive with iCloud-enabled path
  await Hive.initFlutter(hivePath);

  // Register adapters
  Hive.registerAdapter(DiaryEntryAdapter());

  // Initialize services
  final diaryService = DiaryService();
  await diaryService.init();

  final themeService = ThemeService();
  await themeService.init();

  runApp(
    MultiProvider(
      providers: [
        Provider<DiaryService>(create: (_) => diaryService),
        Provider<ICloudSyncService>(create: (_) => iCloudService),
        ChangeNotifierProvider<ThemeService>(create: (_) => themeService),
      ],
      child: const DBTDailyLoggerApp(),
    ),
  );
}

class DBTDailyLoggerApp extends StatelessWidget {
  const DBTDailyLoggerApp({super.key});

  @override
  Widget build(BuildContext context) {
    return Consumer<ThemeService>(
      builder: (context, themeService, child) {
        return MaterialApp(
          title: 'DBT Daily Logger',
          debugShowCheckedModeBanner: false,
          themeMode: themeService.themeMode,
          theme: _buildLightTheme(),
          darkTheme: _buildDarkTheme(),
          home: const HomeScreen(),
        );
      },
    );
  }

  ThemeData _buildLightTheme() {
    return ThemeData(
      primarySwatch: Colors.teal,
      useMaterial3: true,
      colorScheme: ColorScheme.fromSeed(
        seedColor: Colors.teal,
        brightness: Brightness.light,
      ),
      appBarTheme: const AppBarTheme(
        centerTitle: true,
        elevation: 2,
      ),
      cardTheme: CardTheme(
        elevation: 2,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
      inputDecorationTheme: InputDecorationTheme(
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
        ),
        filled: true,
      ),
    );
  }

  ThemeData _buildDarkTheme() {
    return ThemeData(
      primarySwatch: Colors.teal,
      useMaterial3: true,
      colorScheme: ColorScheme.fromSeed(
        seedColor: Colors.teal,
        brightness: Brightness.dark,
      ),
      appBarTheme: const AppBarTheme(
        centerTitle: true,
        elevation: 2,
      ),
      cardTheme: CardTheme(
        elevation: 2,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
      inputDecorationTheme: InputDecorationTheme(
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
        ),
        filled: true,
      ),
    );
  }
}
