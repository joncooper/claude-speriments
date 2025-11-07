import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:fl_chart/fl_chart.dart';
import 'package:intl/intl.dart';
import '../models/diary_entry.dart';
import '../services/diary_service.dart';

class InsightsScreen extends StatefulWidget {
  const InsightsScreen({super.key});

  @override
  State<InsightsScreen> createState() => _InsightsScreenState();
}

class _InsightsScreenState extends State<InsightsScreen> {
  int _selectedDays = 30;

  @override
  Widget build(BuildContext context) {
    final diaryService = Provider.of<DiaryService>(context, listen: false);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Insights & Trends'),
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          // Time range selector
          Card(
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Time Range',
                    style: Theme.of(context).textTheme.titleMedium?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                  ),
                  const SizedBox(height: 12),
                  SegmentedButton<int>(
                    segments: const [
                      ButtonSegment(value: 7, label: Text('7 days')),
                      ButtonSegment(value: 30, label: Text('30 days')),
                      ButtonSegment(value: 90, label: Text('90 days')),
                    ],
                    selected: {_selectedDays},
                    onSelectionChanged: (Set<int> selected) {
                      setState(() {
                        _selectedDays = selected.first;
                      });
                    },
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(height: 16),

          // Emotion trends chart
          _buildEmotionTrendsCard(diaryService),
          const SizedBox(height: 16),

          // Urge trends chart
          _buildUrgeTrendsCard(diaryService),
          const SizedBox(height: 16),

          // Skills usage chart
          _buildSkillsUsageCard(diaryService),
          const SizedBox(height: 16),

          // Statistics summary
          _buildStatsSummaryCard(diaryService),
        ],
      ),
    );
  }

  Widget _buildEmotionTrendsCard(DiaryService diaryService) {
    final entries = diaryService.getRecentEntries(_selectedDays);

    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                const Icon(Icons.mood, color: Colors.blue),
                const SizedBox(width: 8),
                Text(
                  'Emotion Intensity Trends',
                  style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                ),
              ],
            ),
            const SizedBox(height: 24),
            SizedBox(
              height: 200,
              child: _buildEmotionLineChart(entries),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildEmotionLineChart(List<DiaryEntry> entries) {
    if (entries.isEmpty) {
      return const Center(
        child: Text('No data available for this time period'),
      );
    }

    final spots = <FlSpot>[];
    for (int i = 0; i < entries.length; i++) {
      final entry = entries[entries.length - 1 - i];
      if (entry.emotions.isNotEmpty) {
        spots.add(FlSpot(
          i.toDouble(),
          entry.averageEmotionIntensity,
        ));
      }
    }

    if (spots.isEmpty) {
      return const Center(
        child: Text('No emotion data available'),
      );
    }

    return LineChart(
      LineChartData(
        gridData: FlGridData(
          show: true,
          drawVerticalLine: false,
          horizontalInterval: 2,
        ),
        titlesData: FlTitlesData(
          leftTitles: AxisTitles(
            sideTitles: SideTitles(
              showTitles: true,
              interval: 2,
              reservedSize: 30,
            ),
          ),
          rightTitles: const AxisTitles(
            sideTitles: SideTitles(showTitles: false),
          ),
          topTitles: const AxisTitles(
            sideTitles: SideTitles(showTitles: false),
          ),
          bottomTitles: const AxisTitles(
            sideTitles: SideTitles(showTitles: false),
          ),
        ),
        borderData: FlBorderData(show: false),
        minY: 0,
        maxY: 10,
        lineBarsData: [
          LineChartBarData(
            spots: spots,
            isCurved: true,
            color: Colors.blue,
            barWidth: 3,
            dotData: const FlDotData(show: true),
            belowBarData: BarAreaData(
              show: true,
              color: Colors.blue.withOpacity(0.1),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildUrgeTrendsCard(DiaryService diaryService) {
    final entries = diaryService.getRecentEntries(_selectedDays);

    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                const Icon(Icons.warning_amber_rounded, color: Colors.orange),
                const SizedBox(width: 8),
                Text(
                  'Urge Intensity Trends',
                  style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                ),
              ],
            ),
            const SizedBox(height: 24),
            SizedBox(
              height: 200,
              child: _buildUrgeLineChart(entries),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildUrgeLineChart(List<DiaryEntry> entries) {
    if (entries.isEmpty) {
      return const Center(
        child: Text('No data available for this time period'),
      );
    }

    final spots = <FlSpot>[];
    for (int i = 0; i < entries.length; i++) {
      final entry = entries[entries.length - 1 - i];
      if (entry.urges.isNotEmpty) {
        spots.add(FlSpot(
          i.toDouble(),
          entry.averageUrgeIntensity,
        ));
      }
    }

    if (spots.isEmpty) {
      return const Center(
        child: Text('No urge data available'),
      );
    }

    return LineChart(
      LineChartData(
        gridData: FlGridData(
          show: true,
          drawVerticalLine: false,
          horizontalInterval: 2,
        ),
        titlesData: FlTitlesData(
          leftTitles: AxisTitles(
            sideTitles: SideTitles(
              showTitles: true,
              interval: 2,
              reservedSize: 30,
            ),
          ),
          rightTitles: const AxisTitles(
            sideTitles: SideTitles(showTitles: false),
          ),
          topTitles: const AxisTitles(
            sideTitles: SideTitles(showTitles: false),
          ),
          bottomTitles: const AxisTitles(
            sideTitles: SideTitles(showTitles: false),
          ),
        ),
        borderData: FlBorderData(show: false),
        minY: 0,
        maxY: 10,
        lineBarsData: [
          LineChartBarData(
            spots: spots,
            isCurved: true,
            color: Colors.orange,
            barWidth: 3,
            dotData: const FlDotData(show: true),
            belowBarData: BarAreaData(
              show: true,
              color: Colors.orange.withOpacity(0.1),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSkillsUsageCard(DiaryService diaryService) {
    final stats = diaryService.getStats(lastDays: _selectedDays);
    final skillsCount = stats['mostUsedSkills'] as Map<String, int>;

    // Get top 5 skills
    final sortedSkills = skillsCount.entries.toList()
      ..sort((a, b) => b.value.compareTo(a.value));
    final topSkills = sortedSkills.take(5).toList();

    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                const Icon(Icons.psychology, color: Colors.green),
                const SizedBox(width: 8),
                Text(
                  'Most Used Skills',
                  style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                ),
              ],
            ),
            const SizedBox(height: 16),
            if (topSkills.isEmpty)
              const Center(
                child: Text('No skills data available'),
              )
            else
              SizedBox(
                height: 200,
                child: BarChart(
                  BarChartData(
                    alignment: BarChartAlignment.spaceAround,
                    maxY: topSkills.first.value.toDouble() * 1.2,
                    barGroups: topSkills.asMap().entries.map((entry) {
                      return BarChartGroupData(
                        x: entry.key,
                        barRods: [
                          BarChartRodData(
                            toY: entry.value.value.toDouble(),
                            color: Colors.green,
                            width: 20,
                            borderRadius: const BorderRadius.vertical(
                              top: Radius.circular(4),
                            ),
                          ),
                        ],
                      );
                    }).toList(),
                    titlesData: FlTitlesData(
                      leftTitles: AxisTitles(
                        sideTitles: SideTitles(
                          showTitles: true,
                          reservedSize: 30,
                        ),
                      ),
                      rightTitles: const AxisTitles(
                        sideTitles: SideTitles(showTitles: false),
                      ),
                      topTitles: const AxisTitles(
                        sideTitles: SideTitles(showTitles: false),
                      ),
                      bottomTitles: const AxisTitles(
                        sideTitles: SideTitles(showTitles: false),
                      ),
                    ),
                    borderData: FlBorderData(show: false),
                    gridData: const FlGridData(show: false),
                  ),
                ),
              ),
            const SizedBox(height: 12),
            ...topSkills.map((skill) => Padding(
                  padding: const EdgeInsets.symmetric(vertical: 4),
                  child: Row(
                    children: [
                      Container(
                        width: 12,
                        height: 12,
                        decoration: BoxDecoration(
                          color: Colors.green,
                          borderRadius: BorderRadius.circular(2),
                        ),
                      ),
                      const SizedBox(width: 8),
                      Expanded(
                        child: Text(
                          skill.key,
                          style: const TextStyle(fontSize: 12),
                        ),
                      ),
                      Text(
                        '${skill.value}x',
                        style: const TextStyle(
                          fontWeight: FontWeight.bold,
                          fontSize: 12,
                        ),
                      ),
                    ],
                  ),
                )),
          ],
        ),
      ),
    );
  }

  Widget _buildStatsSummaryCard(DiaryService diaryService) {
    final stats = diaryService.getStats(lastDays: _selectedDays);
    final totalEntries = stats['totalEntries'] as int;
    final avgEmotion = stats['averageEmotionIntensity'] as double;
    final avgUrge = stats['averageUrgeIntensity'] as double;

    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Summary Statistics',
              style: Theme.of(context).textTheme.titleMedium?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
            ),
            const SizedBox(height: 16),
            _buildStatRow(
              'Total Entries',
              totalEntries.toString(),
              Icons.edit_note,
              Colors.purple,
            ),
            const SizedBox(height: 12),
            _buildStatRow(
              'Avg Emotion Intensity',
              avgEmotion.toStringAsFixed(1),
              Icons.mood,
              Colors.blue,
            ),
            const SizedBox(height: 12),
            _buildStatRow(
              'Avg Urge Intensity',
              avgUrge.toStringAsFixed(1),
              Icons.warning_amber_rounded,
              Colors.orange,
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildStatRow(String label, String value, IconData icon, Color color) {
    return Row(
      children: [
        Icon(icon, color: color, size: 24),
        const SizedBox(width: 12),
        Expanded(
          child: Text(
            label,
            style: const TextStyle(fontSize: 16),
          ),
        ),
        Text(
          value,
          style: TextStyle(
            fontSize: 20,
            fontWeight: FontWeight.bold,
            color: color,
          ),
        ),
      ],
    );
  }
}
