import 'package:flutter/material.dart';
import '../models/dbt_skills.dart';

/// Widget for selecting DBT skills used
/// Organized by module with expandable sections
class SkillsSelector extends StatefulWidget {
  final Set<String> selectedSkills;
  final ValueChanged<Set<String>> onChanged;

  const SkillsSelector({
    super.key,
    required this.selectedSkills,
    required this.onChanged,
  });

  @override
  State<SkillsSelector> createState() => _SkillsSelectorState();
}

class _SkillsSelectorState extends State<SkillsSelector> {
  final Set<String> _expandedModules = {};

  @override
  void initState() {
    super.initState();
    // Expand all modules by default
    _expandedModules.addAll(DBTSkills.modules);
  }

  void _toggleSkill(String skill) {
    final updated = Set<String>.from(widget.selectedSkills);

    if (updated.contains(skill)) {
      updated.remove(skill);
    } else {
      updated.add(skill);
    }

    widget.onChanged(updated);
  }

  void _toggleModule(String module) {
    setState(() {
      if (_expandedModules.contains(module)) {
        _expandedModules.remove(module);
      } else {
        _expandedModules.add(module);
      }
    });
  }

  Color _getModuleColor(String module) {
    switch (module) {
      case 'Mindfulness':
        return Colors.purple;
      case 'Distress Tolerance':
        return Colors.blue;
      case 'Emotion Regulation':
        return Colors.green;
      case 'Interpersonal Effectiveness':
        return Colors.orange;
      default:
        return Colors.grey;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Selected count
            if (widget.selectedSkills.isNotEmpty)
              Padding(
                padding: const EdgeInsets.only(bottom: 12),
                child: Text(
                  '${widget.selectedSkills.length} skill(s) selected',
                  style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                        color: Theme.of(context).colorScheme.primary,
                        fontWeight: FontWeight.w500,
                      ),
                ),
              ),

            // Modules
            ...DBTSkills.modules.map((module) {
              final skills = DBTSkills.skillsByModule[module] ?? [];
              final selectedInModule = skills.where((s) => widget.selectedSkills.contains(s)).length;
              final isExpanded = _expandedModules.contains(module);

              return Column(
                children: [
                  // Module header
                  InkWell(
                    onTap: () => _toggleModule(module),
                    borderRadius: BorderRadius.circular(8),
                    child: Container(
                      padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 8),
                      child: Row(
                        children: [
                          Container(
                            width: 4,
                            height: 24,
                            decoration: BoxDecoration(
                              color: _getModuleColor(module),
                              borderRadius: BorderRadius.circular(2),
                            ),
                          ),
                          const SizedBox(width: 12),
                          Expanded(
                            child: Text(
                              module,
                              style: Theme.of(context).textTheme.titleSmall?.copyWith(
                                    fontWeight: FontWeight.bold,
                                    color: _getModuleColor(module),
                                  ),
                            ),
                          ),
                          if (selectedInModule > 0)
                            Container(
                              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                              decoration: BoxDecoration(
                                color: _getModuleColor(module).withOpacity(0.2),
                                borderRadius: BorderRadius.circular(12),
                              ),
                              child: Text(
                                selectedInModule.toString(),
                                style: TextStyle(
                                  fontSize: 12,
                                  fontWeight: FontWeight.bold,
                                  color: _getModuleColor(module),
                                ),
                              ),
                            ),
                          const SizedBox(width: 8),
                          Icon(
                            isExpanded ? Icons.expand_less : Icons.expand_more,
                            color: _getModuleColor(module),
                          ),
                        ],
                      ),
                    ),
                  ),

                  // Skills checkboxes
                  if (isExpanded)
                    Padding(
                      padding: const EdgeInsets.only(left: 16, bottom: 8),
                      child: Column(
                        children: skills.map((skill) {
                          final isSelected = widget.selectedSkills.contains(skill);
                          return CheckboxListTile(
                            value: isSelected,
                            onChanged: (_) => _toggleSkill(skill),
                            title: Text(skill),
                            dense: true,
                            controlAffinity: ListTileControlAffinity.leading,
                            activeColor: _getModuleColor(module),
                          );
                        }).toList(),
                      ),
                    ),
                ],
              );
            }).toList(),
          ],
        ),
      ),
    );
  }
}
