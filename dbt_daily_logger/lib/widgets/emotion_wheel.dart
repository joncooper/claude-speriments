import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../models/dbt_constants.dart';

class EmotionWheel extends StatefulWidget {
  final Function(String) onEmotionSelected;

  const EmotionWheel({
    super.key,
    required this.onEmotionSelected,
  });

  @override
  State<EmotionWheel> createState() => _EmotionWheelState();
}

class _EmotionWheelState extends State<EmotionWheel>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  String? _hoveredEmotion;

  final List<EmotionSegment> _emotions = [
    EmotionSegment('Joy', Colors.yellow),
    EmotionSegment('Sadness', Colors.blue),
    EmotionSegment('Anger', Colors.red),
    EmotionSegment('Fear', Colors.purple),
    EmotionSegment('Anxiety', Colors.orange),
    EmotionSegment('Love', Colors.pink),
    EmotionSegment('Shame', Colors.brown),
    EmotionSegment('Guilt', Colors.deepPurple),
  ];

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 300),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        SizedBox(
          width: 300,
          height: 300,
          child: GestureDetector(
            onTapUp: (details) {
              final RenderBox box = context.findRenderObject() as RenderBox;
              final localPosition = box.globalToLocal(details.globalPosition);
              final emotion = _getEmotionFromPosition(
                localPosition,
                box.size,
              );
              if (emotion != null) {
                widget.onEmotionSelected(emotion);
                _controller.forward(from: 0);
              }
            },
            child: CustomPaint(
              painter: EmotionWheelPainter(
                emotions: _emotions,
                hoveredEmotion: _hoveredEmotion,
                animation: _controller,
              ),
            ),
          ),
        ),
        const SizedBox(height: 16),
        if (_hoveredEmotion != null)
          Text(
            _hoveredEmotion!,
            style: Theme.of(context).textTheme.titleLarge?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
          )
        else
          Text(
            'Tap an emotion',
            style: Theme.of(context).textTheme.titleMedium?.copyWith(
                  color: Colors.grey,
                ),
          ),
      ],
    );
  }

  String? _getEmotionFromPosition(Offset position, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final dx = position.dx - center.dx;
    final dy = position.dy - center.dy;

    final distance = math.sqrt(dx * dx + dy * dy);
    final radius = size.width / 2 - 20;

    if (distance < 30 || distance > radius) {
      return null;
    }

    var angle = math.atan2(dy, dx);
    if (angle < 0) angle += 2 * math.pi;

    final segmentAngle = 2 * math.pi / _emotions.length;
    final index = ((angle + segmentAngle / 2) / segmentAngle).floor() % _emotions.length;

    return _emotions[index].name;
  }
}

class EmotionSegment {
  final String name;
  final Color color;

  EmotionSegment(this.name, this.color);
}

class EmotionWheelPainter extends CustomPainter {
  final List<EmotionSegment> emotions;
  final String? hoveredEmotion;
  final Animation<double> animation;

  EmotionWheelPainter({
    required this.emotions,
    this.hoveredEmotion,
    required this.animation,
  }) : super(repaint: animation);

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final radius = size.width / 2 - 20;
    final segmentAngle = 2 * math.pi / emotions.length;

    // Draw segments
    for (int i = 0; i < emotions.length; i++) {
      final emotion = emotions[i];
      final startAngle = i * segmentAngle - math.pi / 2;
      final isHovered = emotion.name == hoveredEmotion;

      final paint = Paint()
        ..color = emotion.color.withOpacity(isHovered ? 0.9 : 0.7)
        ..style = PaintingStyle.fill;

      final segmentRadius = isHovered ? radius + 5 : radius;

      canvas.drawArc(
        Rect.fromCircle(center: center, radius: segmentRadius),
        startAngle,
        segmentAngle,
        true,
        paint,
      );

      // Draw segment border
      final borderPaint = Paint()
        ..color = Colors.white
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2;

      canvas.drawArc(
        Rect.fromCircle(center: center, radius: segmentRadius),
        startAngle,
        segmentAngle,
        true,
        borderPaint,
      );

      // Draw text
      final textAngle = startAngle + segmentAngle / 2;
      final textRadius = segmentRadius * 0.7;
      final textPosition = Offset(
        center.dx + textRadius * math.cos(textAngle),
        center.dy + textRadius * math.sin(textAngle),
      );

      final textPainter = TextPainter(
        text: TextSpan(
          text: emotion.name,
          style: TextStyle(
            color: Colors.white,
            fontSize: isHovered ? 14 : 12,
            fontWeight: isHovered ? FontWeight.bold : FontWeight.normal,
            shadows: const [
              Shadow(
                blurRadius: 2,
                color: Colors.black45,
              ),
            ],
          ),
        ),
        textDirection: TextDirection.ltr,
      );

      textPainter.layout();

      canvas.save();
      canvas.translate(textPosition.dx, textPosition.dy);

      // Rotate text to be readable
      double rotationAngle = textAngle + math.pi / 2;
      if (rotationAngle > math.pi / 2 && rotationAngle < 3 * math.pi / 2) {
        rotationAngle += math.pi;
      }
      canvas.rotate(rotationAngle);

      textPainter.paint(
        canvas,
        Offset(-textPainter.width / 2, -textPainter.height / 2),
      );

      canvas.restore();
    }

    // Draw center circle
    final centerPaint = Paint()
      ..color = Colors.white
      ..style = PaintingStyle.fill;

    canvas.drawCircle(center, 30, centerPaint);

    // Draw center icon
    final iconPainter = TextPainter(
      text: const TextSpan(
        text: '😊',
        style: TextStyle(fontSize: 24),
      ),
      textDirection: TextDirection.ltr,
    );

    iconPainter.layout();
    iconPainter.paint(
      canvas,
      Offset(
        center.dx - iconPainter.width / 2,
        center.dy - iconPainter.height / 2,
      ),
    );
  }

  @override
  bool shouldRepaint(EmotionWheelPainter oldDelegate) {
    return oldDelegate.hoveredEmotion != hoveredEmotion;
  }
}
