import 'package:flutter/material.dart';
import '../models/dbt_constants.dart';

class UrgeTracker extends StatefulWidget {
  final Map<String, int> urges;
  final Function(Map<String, int>) onChanged;

  const UrgeTracker({
    super.key,
    required this.urges,
    required this.onChanged,
  });

  @override
  State<UrgeTracker> createState() => _UrgeTrackerState();
}

class _UrgeTrackerState extends State<UrgeTracker> {
  String? _selectedUrge;
  int _intensity = 5;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Display current urges
        if (widget.urges.isNotEmpty) ...[
          ...widget.urges.entries.map((entry) {
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
                              final updated = Map<String, int>.from(widget.urges);
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
                      final updated = Map<String, int>.from(widget.urges);
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

        // Add new urge
        Row(
          children: [
            Expanded(
              child: DropdownButtonFormField<String>(
                decoration: const InputDecoration(
                  labelText: 'Add urge',
                  border: OutlineInputBorder(),
                ),
                value: _selectedUrge,
                items: [
                  ...CommonUrges.urges
                      .where((u) => !widget.urges.containsKey(u))
                      .map((urge) => DropdownMenuItem(
                            value: urge,
                            child: Text(urge),
                          )),
                  const DropdownMenuItem(
                    value: '__custom__',
                    child: Text('Custom urge...'),
                  ),
                ],
                onChanged: (value) {
                  if (value == '__custom__') {
                    _showCustomUrgeDialog();
                  } else {
                    setState(() {
                      _selectedUrge = value;
                    });
                  }
                },
              ),
            ),
          ],
        ),
        if (_selectedUrge != null && _selectedUrge != '__custom__') ...[
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
            onPressed: _addUrge,
            icon: const Icon(Icons.add),
            label: const Text('Add'),
          ),
        ],
      ],
    );
  }

  void _addUrge() {
    if (_selectedUrge != null && _selectedUrge != '__custom__') {
      final updated = Map<String, int>.from(widget.urges);
      updated[_selectedUrge!] = _intensity;
      widget.onChanged(updated);
      setState(() {
        _selectedUrge = null;
        _intensity = 5;
      });
    }
  }

  Future<void> _showCustomUrgeDialog() async {
    final controller = TextEditingController();
    final result = await showDialog<String>(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Custom Urge'),
        content: TextField(
          controller: controller,
          decoration: const InputDecoration(
            labelText: 'Urge description',
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
        _selectedUrge = result;
      });
    } else {
      setState(() {
        _selectedUrge = null;
      });
    }
  }
}
