import 'package:flutter/material.dart';
import 'dart:math';
import '../models/diary_entry.dart';

/// Widget for rating emotions on a 0-10 scale
/// Randomizes order to prevent sequencing bias
class EmotionSlider extends StatefulWidget {
  final Map<String, int> emotions;
  final ValueChanged<Map<String, int>> onChanged;
  final List<String>? customLabels;

  const EmotionSlider({
    super.key,
    required this.emotions,
    required this.onChanged,
    this.customLabels,
  });

  @override
  State<EmotionSlider> createState() => _EmotionSliderState();
}

class _EmotionSliderState extends State<EmotionSlider> {
  late List<String> _emotionOrder;
  final Random _random = Random();

  @override
  void initState() {
    super.initState();
    // Get emotion labels and randomize order
    final emotionList = widget.customLabels ?? Emotions.all;
    _emotionOrder = List.from(emotionList)..shuffle(_random);
  }

  void _updateEmotion(String emotion, double value) {
    final updated = Map<String, int>.from(widget.emotions);
    final intValue = value.round();

    if (intValue == 0) {
      updated.remove(emotion);
    } else {
      updated[emotion] = intValue;
    }

    widget.onChanged(updated);
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: _emotionOrder.map((emotion) {
            return _buildEmotionSlider(emotion);
          }).toList(),
        ),
      ),
    );
  }

  Widget _buildEmotionSlider(String emotion) {
    final currentValue = widget.emotions[emotion]?.toDouble() ?? 0.0;
    final emoji = _getEmoji(emotion, currentValue.toInt());

    return Padding(
      padding: const EdgeInsets.only(bottom: 16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Row(
                children: [
                  Text(
                    emoji,
                    style: const TextStyle(fontSize: 24),
                  ),
                  const SizedBox(width: 12),
                  Text(
                    emotion,
                    style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                          fontWeight: FontWeight.w500,
                        ),
                  ),
                ],
              ),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
                decoration: BoxDecoration(
                  color: _getIntensityColor(currentValue.toInt()),
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Text(
                  currentValue.toInt() == 0 ? '-' : currentValue.toInt().toString(),
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
              activeTrackColor: _getIntensityColor(currentValue.toInt()),
              thumbColor: _getIntensityColor(currentValue.toInt()),
              overlayColor: _getIntensityColor(currentValue.toInt()).withOpacity(0.2),
              valueIndicatorColor: _getIntensityColor(currentValue.toInt()),
            ),
            child: Slider(
              value: currentValue,
              min: 0,
              max: 10,
              divisions: 10,
              label: currentValue.toInt() == 0 ? 'None' : currentValue.toInt().toString(),
              onChanged: (value) => _updateEmotion(emotion, value),
            ),
          ),
        ],
      ),
    );
  }

  String _getEmoji(String emotion, int intensity) {
    if (intensity == 0) {
      return '😶'; // Neutral for not experienced
    }

    // Emotion-specific emojis
    switch (emotion.toLowerCase()) {
      case 'anger':
        if (intensity <= 3) return '😠';
        if (intensity <= 7) return '😡';
        return '🤬';
      case 'fear':
        if (intensity <= 3) return '😟';
        if (intensity <= 7) return '😨';
        return '😱';
      case 'joy':
        if (intensity <= 3) return '🙂';
        if (intensity <= 7) return '😊';
        return '😄';
      case 'sadness':
        if (intensity <= 3) return '🙁';
        if (intensity <= 7) return '😢';
        return '😭';
      case 'guilt':
        if (intensity <= 3) return '😔';
        if (intensity <= 7) return '😞';
        return '😣';
      case 'shame':
        if (intensity <= 3) return '😳';
        if (intensity <= 7) return '😖';
        return '😓';
      // Custom urges
      case 'self-harm':
        return '⚠️';
      case 'substance use':
        return '🚫';
      case 'avoid':
        return '🏃';
      default:
        return '😐';
    }
  }

  Color _getIntensityColor(int intensity) {
    if (intensity == 0) {
      return Colors.grey;
    } else if (intensity <= 3) {
      return Colors.green;
    } else if (intensity <= 7) {
      return Colors.orange;
    } else {
      return Colors.red;
    }
  }
}
