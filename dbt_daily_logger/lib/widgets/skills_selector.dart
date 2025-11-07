import 'package:flutter/material.dart';
import '../models/dbt_constants.dart';

class SkillsSelector extends StatefulWidget {
  final List<String> selectedSkills;
  final Function(List<String>) onChanged;

  const SkillsSelector({
    super.key,
    required this.selectedSkills,
    required this.onChanged,
  });

  @override
  State<SkillsSelector> createState() => _SkillsSelectorState();
}

class _SkillsSelectorState extends State<SkillsSelector> {
  String? _expandedModule;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Display selected skills
        if (widget.selectedSkills.isNotEmpty) ...[
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: widget.selectedSkills.map((skill) {
              final module = DBTSkills.getModuleForSkill(skill);
              return Chip(
                label: Text(skill),
                deleteIcon: const Icon(Icons.close, size: 18),
                onDeleted: () {
                  final updated = List<String>.from(widget.selectedSkills);
                  updated.remove(skill);
                  widget.onChanged(updated);
                },
                backgroundColor: _getModuleColor(module),
              );
            }).toList(),
          ),
          const Divider(height: 24),
        ],

        // Skill selection by module
        const Text(
          'Select skills by module:',
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
        const SizedBox(height: 12),

        ...DBTSkills.skillsByModule.entries.map((moduleEntry) {
          final isExpanded = _expandedModule == moduleEntry.key;
          return Card(
            margin: const EdgeInsets.only(bottom: 8),
            child: Column(
              children: [
                ListTile(
                  title: Text(
                    moduleEntry.key,
                    style: const TextStyle(fontWeight: FontWeight.bold),
                  ),
                  trailing: Icon(
                    isExpanded ? Icons.expand_less : Icons.expand_more,
                  ),
                  onTap: () {
                    setState(() {
                      _expandedModule = isExpanded ? null : moduleEntry.key;
                    });
                  },
                ),
                if (isExpanded) ...[
                  const Divider(height: 1),
                  Padding(
                    padding: const EdgeInsets.all(12),
                    child: Wrap(
                      spacing: 8,
                      runSpacing: 8,
                      children: moduleEntry.value.map((skill) {
                        final isSelected =
                            widget.selectedSkills.contains(skill);
                        return FilterChip(
                          label: Text(skill),
                          selected: isSelected,
                          onSelected: (selected) {
                            final updated =
                                List<String>.from(widget.selectedSkills);
                            if (selected) {
                              updated.add(skill);
                            } else {
                              updated.remove(skill);
                            }
                            widget.onChanged(updated);
                          },
                          selectedColor: _getModuleColor(moduleEntry.key),
                        );
                      }).toList(),
                    ),
                  ),
                ],
              ],
            ),
          );
        }).toList(),
      ],
    );
  }

  Color _getModuleColor(String? module) {
    switch (module) {
      case 'Mindfulness':
        return Colors.purple[100]!;
      case 'Distress Tolerance':
        return Colors.orange[100]!;
      case 'Emotion Regulation':
        return Colors.blue[100]!;
      case 'Interpersonal Effectiveness':
        return Colors.green[100]!;
      default:
        return Colors.grey[100]!;
    }
  }
}
