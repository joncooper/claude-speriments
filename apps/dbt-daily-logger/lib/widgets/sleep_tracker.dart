import 'package:flutter/material.dart';

/// Widget for tracking sleep and self-care
class SleepTracker extends StatelessWidget {
  final double? sleepHours;
  final int? sleepQuality;
  final bool exercised;
  final ValueChanged<double?> onSleepHoursChanged;
  final ValueChanged<int?> onSleepQualityChanged;
  final ValueChanged<bool> onExercisedChanged;

  const SleepTracker({
    super.key,
    required this.sleepHours,
    required this.sleepQuality,
    required this.exercised,
    required this.onSleepHoursChanged,
    required this.onSleepQualityChanged,
    required this.onExercisedChanged,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Sleep hours
            _buildSleepHoursSlider(context),
            const SizedBox(height: 24),

            // Sleep quality
            _buildSleepQualitySelector(context),
            const SizedBox(height: 16),

            // Exercise checkbox
            CheckboxListTile(
              title: const Text('Exercised today'),
              value: exercised,
              onChanged: (value) => onExercisedChanged(value ?? false),
              secondary: const Icon(Icons.fitness_center),
              contentPadding: EdgeInsets.zero,
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSleepHoursSlider(BuildContext context) {
    final hours = sleepHours ?? 0.0;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(
              'Sleep Hours',
              style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                    fontWeight: FontWeight.w500,
                  ),
            ),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
              decoration: BoxDecoration(
                color: _getSleepHoursColor(hours),
                borderRadius: BorderRadius.circular(12),
              ),
              child: Text(
                hours == 0 ? '-' : '${hours.toStringAsFixed(1)}h',
                style: const TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: 8),
        SliderTheme(
          data: SliderTheme.of(context).copyWith(
            activeTrackColor: _getSleepHoursColor(hours),
            thumbColor: _getSleepHoursColor(hours),
            overlayColor: _getSleepHoursColor(hours).withOpacity(0.2),
            valueIndicatorColor: _getSleepHoursColor(hours),
          ),
          child: Slider(
            value: hours,
            min: 0,
            max: 12,
            divisions: 24, // 0.5 hour increments
            label: hours == 0 ? 'None' : '${hours.toStringAsFixed(1)}h',
            onChanged: (value) {
              onSleepHoursChanged(value == 0 ? null : value);
            },
          ),
        ),
      ],
    );
  }

  Widget _buildSleepQualitySelector(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'Sleep Quality',
          style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                fontWeight: FontWeight.w500,
              ),
        ),
        const SizedBox(height: 12),
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: List.generate(6, (index) {
            final isSelected = sleepQuality == index;
            return Expanded(
              child: Padding(
                padding: EdgeInsets.only(
                  right: index < 5 ? 8 : 0,
                ),
                child: InkWell(
                  onTap: () => onSleepQualityChanged(index),
                  borderRadius: BorderRadius.circular(8),
                  child: Container(
                    padding: const EdgeInsets.symmetric(vertical: 8),
                    decoration: BoxDecoration(
                      color: isSelected
                          ? _getQualityColor(index)
                          : Theme.of(context).colorScheme.surfaceVariant.withOpacity(0.3),
                      borderRadius: BorderRadius.circular(8),
                      border: Border.all(
                        color: isSelected
                            ? _getQualityColor(index)
                            : Theme.of(context).colorScheme.outline.withOpacity(0.2),
                        width: 2,
                      ),
                    ),
                    child: Column(
                      children: [
                        Text(
                          _getQualityEmoji(index),
                          style: TextStyle(
                            fontSize: isSelected ? 24 : 20,
                          ),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          index.toString(),
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                            color: isSelected
                                ? Colors.white
                                : Theme.of(context).colorScheme.onSurface.withOpacity(0.6),
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            );
          }),
        ),
        const SizedBox(height: 8),
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(
              'Poor',
              style: Theme.of(context).textTheme.bodySmall?.copyWith(
                    color: Theme.of(context).colorScheme.onSurface.withOpacity(0.6),
                  ),
            ),
            Text(
              'Excellent',
              style: Theme.of(context).textTheme.bodySmall?.copyWith(
                    color: Theme.of(context).colorScheme.onSurface.withOpacity(0.6),
                  ),
            ),
          ],
        ),
      ],
    );
  }

  Color _getSleepHoursColor(double hours) {
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

  Color _getQualityColor(int quality) {
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

  String _getQualityEmoji(int quality) {
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
