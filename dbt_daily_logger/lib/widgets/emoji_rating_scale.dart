import 'package:flutter/material.dart';

class EmojiRatingScale extends StatelessWidget {
  final String label;
  final int? value;
  final int maxValue;
  final Function(int) onChanged;
  final List<String> emojis;
  final Color color;

  const EmojiRatingScale({
    super.key,
    required this.label,
    required this.value,
    required this.onChanged,
    this.maxValue = 5,
    this.emojis = const ['😌', '🙂', '😐', '😟', '😰', '😱'],
    this.color = Colors.teal,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Padding(
          padding: const EdgeInsets.only(bottom: 12),
          child: Text(
            label,
            style: Theme.of(context).textTheme.titleMedium?.copyWith(
                  fontWeight: FontWeight.w600,
                ),
          ),
        ),
        Container(
          decoration: BoxDecoration(
            color: color.withOpacity(0.1),
            borderRadius: BorderRadius.circular(16),
          ),
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              // Emoji display
              if (value != null)
                TweenAnimationBuilder<double>(
                  duration: const Duration(milliseconds: 300),
                  tween: Tween(begin: 0.8, end: 1.0),
                  builder: (context, scale, child) {
                    return Transform.scale(
                      scale: scale,
                      child: Text(
                        emojis[value!],
                        style: const TextStyle(fontSize: 48),
                      ),
                    );
                  },
                ),
              const SizedBox(height: 16),

              // Bubble selector - use Wrap for larger scales
              Wrap(
                spacing: 8,
                runSpacing: 8,
                alignment: WrapAlignment.center,
                children: List.generate(maxValue + 1, (index) {
                  final isSelected = value == index;
                  // Smaller bubbles for scales with more values
                  final double bubbleSize = maxValue > 5 ?
                      (isSelected ? 42 : 34) :
                      (isSelected ? 56 : 44);
                  final double fontSize = maxValue > 5 ?
                      (isSelected ? 16 : 14) :
                      (isSelected ? 20 : 16);

                  return GestureDetector(
                    onTap: () => onChanged(index),
                    child: AnimatedContainer(
                      duration: const Duration(milliseconds: 200),
                      width: bubbleSize,
                      height: bubbleSize,
                      decoration: BoxDecoration(
                        color: isSelected ? color : Colors.white,
                        shape: BoxShape.circle,
                        border: Border.all(
                          color: color,
                          width: isSelected ? 3 : 2,
                        ),
                        boxShadow: isSelected
                            ? [
                                BoxShadow(
                                  color: color.withOpacity(0.4),
                                  blurRadius: 8,
                                  spreadRadius: 2,
                                )
                              ]
                            : null,
                      ),
                      child: Center(
                        child: Text(
                          '$index',
                          style: TextStyle(
                            fontSize: fontSize,
                            fontWeight:
                                isSelected ? FontWeight.bold : FontWeight.w500,
                            color: isSelected ? Colors.white : color,
                          ),
                        ),
                      ),
                    ),
                  );
                }),
              ),

              // Scale description
              if (value != null) ...[
                const SizedBox(height: 12),
                Text(
                  _getDescription(value!),
                  style: TextStyle(
                    color: Colors.grey[700],
                    fontSize: 14,
                    fontStyle: FontStyle.italic,
                  ),
                  textAlign: TextAlign.center,
                ),
              ],
            ],
          ),
        ),
      ],
    );
  }

  String _getDescription(int value) {
    switch (value) {
      case 0:
        return 'Not at all';
      case 1:
        return 'A bit';
      case 2:
        return 'Somewhat';
      case 3:
        return 'Rather strong';
      case 4:
        return 'Very strong';
      case 5:
        return 'Extremely strong';
      default:
        return '';
    }
  }
}
