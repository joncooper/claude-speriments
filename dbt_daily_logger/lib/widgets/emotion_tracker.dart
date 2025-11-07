import 'package:flutter/material.dart';
import '../models/dbt_constants.dart';

class EmotionTracker extends StatefulWidget {
  final Map<String, int> emotions;
  final Function(Map<String, int>) onChanged;

  const EmotionTracker({
    super.key,
    required this.emotions,
    required this.onChanged,
  });

  @override
  State<EmotionTracker> createState() => _EmotionTrackerState();
}

class _EmotionTrackerState extends State<EmotionTracker> {
  String? _selectedEmotion;
  int _intensity = 5;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Display current emotions
        if (widget.emotions.isNotEmpty) ...[
          ...widget.emotions.entries.map((entry) {
            return Padding(
              padding: const EdgeInsets.only(bottom: 12),
              child: Row(
                children: [
                  Expanded(
                    flex: 2,
                    child: Text(
                      entry.key,
                      style: const TextStyle(fontSize: 16),
                    ),
                  ),
                  Expanded(
                    flex: 3,
                    child: Row(
                      children: [
                        Expanded(
                          child: Slider(
                            value: entry.value.toDouble(),
                            min: 0,
                            max: 10,
                            divisions: 10,
                            label: entry.value.toString(),
                            onChanged: (value) {
                              final updated = Map<String, int>.from(widget.emotions);
                              updated[entry.key] = value.toInt();
                              widget.onChanged(updated);
                            },
                          ),
                        ),
                        SizedBox(
                          width: 30,
                          child: Text(
                            '${entry.value}',
                            style: const TextStyle(
                              fontWeight: FontWeight.bold,
                              fontSize: 16,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                  IconButton(
                    icon: const Icon(Icons.close, size: 20),
                    onPressed: () {
                      final updated = Map<String, int>.from(widget.emotions);
                      updated.remove(entry.key);
                      widget.onChanged(updated);
                    },
                  ),
                ],
              ),
            );
          }).toList(),
          const Divider(height: 24),
        ],

        // Add new emotion
        Row(
          children: [
            Expanded(
              child: DropdownButtonFormField<String>(
                decoration: const InputDecoration(
                  labelText: 'Add emotion',
                  border: OutlineInputBorder(),
                ),
                value: _selectedEmotion,
                items: [
                  ...CommonEmotions.emotions
                      .where((e) => !widget.emotions.containsKey(e))
                      .map((emotion) => DropdownMenuItem(
                            value: emotion,
                            child: Text(emotion),
                          )),
                  const DropdownMenuItem(
                    value: '__custom__',
                    child: Text('Custom emotion...'),
                  ),
                ],
                onChanged: (value) {
                  if (value == '__custom__') {
                    _showCustomEmotionDialog();
                  } else {
                    setState(() {
                      _selectedEmotion = value;
                    });
                  }
                },
              ),
            ),
          ],
        ),
        if (_selectedEmotion != null && _selectedEmotion != '__custom__') ...[
          const SizedBox(height: 12),
          Row(
            children: [
              const Text('Intensity: '),
              Expanded(
                child: Slider(
                  value: _intensity.toDouble(),
                  min: 0,
                  max: 10,
                  divisions: 10,
                  label: _intensity.toString(),
                  onChanged: (value) {
                    setState(() {
                      _intensity = value.toInt();
                    });
                  },
                ),
              ),
              SizedBox(
                width: 30,
                child: Text(
                  '$_intensity',
                  style: const TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 16,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 8),
          ElevatedButton.icon(
            onPressed: _addEmotion,
            icon: const Icon(Icons.add),
            label: const Text('Add'),
          ),
        ],
      ],
    );
  }

  void _addEmotion() {
    if (_selectedEmotion != null && _selectedEmotion != '__custom__') {
      final updated = Map<String, int>.from(widget.emotions);
      updated[_selectedEmotion!] = _intensity;
      widget.onChanged(updated);
      setState(() {
        _selectedEmotion = null;
        _intensity = 5;
      });
    }
  }

  Future<void> _showCustomEmotionDialog() async {
    final controller = TextEditingController();
    final result = await showDialog<String>(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Custom Emotion'),
        content: TextField(
          controller: controller,
          decoration: const InputDecoration(
            labelText: 'Emotion name',
            border: OutlineInputBorder(),
          ),
          autofocus: true,
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Cancel'),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context, controller.text),
            child: const Text('Add'),
          ),
        ],
      ),
    );

    if (result != null && result.isNotEmpty) {
      setState(() {
        _selectedEmotion = result;
      });
    } else {
      setState(() {
        _selectedEmotion = null;
      });
    }
  }
}
