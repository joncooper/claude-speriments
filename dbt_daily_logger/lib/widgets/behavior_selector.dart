import 'package:flutter/material.dart';
import '../models/dbt_constants.dart';

class BehaviorSelector extends StatefulWidget {
  final List<String> selectedBehaviors;
  final Function(List<String>) onChanged;

  const BehaviorSelector({
    super.key,
    required this.selectedBehaviors,
    required this.onChanged,
  });

  @override
  State<BehaviorSelector> createState() => _BehaviorSelectorState();
}

class _BehaviorSelectorState extends State<BehaviorSelector> {
  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const Text(
          'Select target behaviors that occurred today:',
          style: TextStyle(fontSize: 14, color: Colors.black87),
        ),
        const SizedBox(height: 12),

        // Common behaviors as checkboxes
        ...CommonTargetBehaviors.behaviors.map((behavior) {
          final isSelected = widget.selectedBehaviors.contains(behavior);
          return CheckboxListTile(
            value: isSelected,
            onChanged: (selected) {
              final updated = List<String>.from(widget.selectedBehaviors);
              if (selected == true) {
                updated.add(behavior);
              } else {
                updated.remove(behavior);
              }
              widget.onChanged(updated);
            },
            title: Text(behavior),
            contentPadding: EdgeInsets.zero,
            dense: true,
          );
        }).toList(),

        const SizedBox(height: 8),

        // Custom behavior option
        TextButton.icon(
          onPressed: _showCustomBehaviorDialog,
          icon: const Icon(Icons.add),
          label: const Text('Add custom behavior'),
        ),

        // Display custom behaviors
        if (widget.selectedBehaviors.any(
            (b) => !CommonTargetBehaviors.behaviors.contains(b))) ...[
          const SizedBox(height: 8),
          const Text(
            'Custom behaviors:',
            style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12),
          ),
          const SizedBox(height: 4),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: widget.selectedBehaviors
                .where((b) => !CommonTargetBehaviors.behaviors.contains(b))
                .map((behavior) => Chip(
                      label: Text(behavior),
                      deleteIcon: const Icon(Icons.close, size: 18),
                      onDeleted: () {
                        final updated =
                            List<String>.from(widget.selectedBehaviors);
                        updated.remove(behavior);
                        widget.onChanged(updated);
                      },
                      backgroundColor: Colors.red[50],
                    ))
                .toList(),
          ),
        ],
      ],
    );
  }

  Future<void> _showCustomBehaviorDialog() async {
    final controller = TextEditingController();
    final result = await showDialog<String>(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Custom Target Behavior'),
        content: TextField(
          controller: controller,
          decoration: const InputDecoration(
            labelText: 'Behavior description',
            border: OutlineInputBorder(),
          ),
          autofocus: true,
          maxLines: 2,
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
      final updated = List<String>.from(widget.selectedBehaviors);
      updated.add(result);
      widget.onChanged(updated);
    }
  }
}
