import 'package:flutter/material.dart';
import 'dart:math';
import '../models/diary_entry.dart';

/// Widget for tracking target behaviors
/// Randomizes order to prevent sequencing bias
class BehaviorSelector extends StatefulWidget {
  final Map<String, int> behaviors;
  final ValueChanged<Map<String, int>> onChanged;

  const BehaviorSelector({
    super.key,
    required this.behaviors,
    required this.onChanged,
  });

  @override
  State<BehaviorSelector> createState() => _BehaviorSelectorState();
}

class _BehaviorSelectorState extends State<BehaviorSelector> {
  late List<String> _behaviorOrder;
  final Random _random = Random();

  @override
  void initState() {
    super.initState();
    // Randomize behavior order
    _behaviorOrder = List.from(TargetBehaviors.all)..shuffle(_random);
  }

  void _updateBehavior(String behavior, int count) {
    final updated = Map<String, int>.from(widget.behaviors);

    if (count == 0) {
      updated.remove(behavior);
    } else {
      updated[behavior] = count;
    }

    widget.onChanged(updated);
  }

  void _increment(String behavior) {
    final current = widget.behaviors[behavior] ?? 0;
    _updateBehavior(behavior, current + 1);
  }

  void _decrement(String behavior) {
    final current = widget.behaviors[behavior] ?? 0;
    if (current > 0) {
      _updateBehavior(behavior, current - 1);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: _behaviorOrder.map((behavior) {
            return _buildBehaviorRow(behavior);
          }).toList(),
        ),
      ),
    );
  }

  Widget _buildBehaviorRow(String behavior) {
    final count = widget.behaviors[behavior] ?? 0;
    final behaviorName = _getBehaviorName(behavior);
    final behaviorDescription = _getBehaviorDescription(behavior);

    return Padding(
      padding: const EdgeInsets.only(bottom: 12),
      child: Row(
        children: [
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  behaviorName,
                  style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                        fontWeight: FontWeight.w500,
                      ),
                ),
                Text(
                  behaviorDescription,
                  style: Theme.of(context).textTheme.bodySmall?.copyWith(
                        color: Theme.of(context).colorScheme.onSurface.withOpacity(0.6),
                      ),
                ),
              ],
            ),
          ),
          const SizedBox(width: 16),
          Row(
            children: [
              IconButton(
                icon: const Icon(Icons.remove_circle_outline),
                onPressed: count > 0 ? () => _decrement(behavior) : null,
                color: Theme.of(context).colorScheme.primary,
              ),
              Container(
                width: 40,
                alignment: Alignment.center,
                child: Text(
                  count.toString(),
                  style: Theme.of(context).textTheme.titleLarge?.copyWith(
                        fontWeight: FontWeight.bold,
                        color: count > 0
                            ? Theme.of(context).colorScheme.primary
                            : Theme.of(context).colorScheme.onSurface.withOpacity(0.5),
                      ),
                ),
              ),
              IconButton(
                icon: const Icon(Icons.add_circle_outline),
                onPressed: () => _increment(behavior),
                color: Theme.of(context).colorScheme.primary,
              ),
            ],
          ),
        ],
      ),
    );
  }

  String _getBehaviorName(String abbreviation) {
    switch (abbreviation) {
      case 'SI':
        return 'SI';
      case 'NSSI':
        return 'NSSI';
      case 'Conflict':
        return 'Conflict';
      case 'Isolate':
        return 'Isolate';
      case 'Avoid':
        return 'Avoid';
      case 'Withhold':
        return 'Withhold';
      case 'Substance':
        return 'Substance';
      default:
        return abbreviation;
    }
  }

  String _getBehaviorDescription(String abbreviation) {
    switch (abbreviation) {
      case 'SI':
        return 'Suicidal ideation';
      case 'NSSI':
        return 'Non-suicidal self-injury';
      case 'Conflict':
        return 'Interpersonal conflict';
      case 'Isolate':
        return 'Social isolation';
      case 'Avoid':
        return 'Avoidance behavior';
      case 'Withhold':
        return 'Withhold information';
      case 'Substance':
        return 'Substance use';
      default:
        return '';
    }
  }
}
