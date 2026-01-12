import 'package:flutter/material.dart';
import '../../models/dbt_skills.dart';
import '../../constants/skill_descriptions.dart';
import '../../constants/app_constants.dart';

/// Skills reference screen with detailed explanations
class SkillsReferenceScreen extends StatefulWidget {
  const SkillsReferenceScreen({super.key});

  @override
  State<SkillsReferenceScreen> createState() => _SkillsReferenceScreenState();
}

class _SkillsReferenceScreenState extends State<SkillsReferenceScreen> {
  String? _expandedModule;
  String _searchQuery = '';

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

  IconData _getModuleIcon(String module) {
    switch (module) {
      case 'Mindfulness':
        return Icons.self_improvement;
      case 'Distress Tolerance':
        return Icons.favorite;
      case 'Emotion Regulation':
        return Icons.psychology;
      case 'Interpersonal Effectiveness':
        return Icons.people;
      default:
        return Icons.star;
    }
  }

  List<String> _getFilteredModules() {
    if (_searchQuery.isEmpty) {
      return DBTSkills.modules;
    }

    final filteredModules = <String>[];
    for (final module in DBTSkills.modules) {
      final skills = DBTSkills.skillsByModule[module] ?? [];
      final hasMatch = skills.any(
        (skill) => skill.toLowerCase().contains(_searchQuery.toLowerCase()),
      );
      if (hasMatch) {
        filteredModules.add(module);
      }
    }
    return filteredModules;
  }

  List<String> _getFilteredSkills(String module) {
    final skills = DBTSkills.skillsByModule[module] ?? [];
    if (_searchQuery.isEmpty) {
      return skills;
    }

    return skills.where(
      (skill) => skill.toLowerCase().contains(_searchQuery.toLowerCase()),
    ).toList();
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final filteredModules = _getFilteredModules();

    return Column(
      children: [
        // Search bar
        Padding(
          padding: const EdgeInsets.all(16),
          child: TextField(
            decoration: InputDecoration(
              hintText: 'Search skills...',
              prefixIcon: const Icon(Icons.search),
              suffixIcon: _searchQuery.isNotEmpty
                  ? IconButton(
                      icon: const Icon(Icons.clear),
                      onPressed: () {
                        setState(() {
                          _searchQuery = '';
                        });
                      },
                    )
                  : null,
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(12),
              ),
            ),
            onChanged: (value) {
              setState(() {
                _searchQuery = value;
              });
            },
          ),
        ),

        // Skills list
        Expanded(
          child: filteredModules.isEmpty
              ? Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(
                        Icons.search_off,
                        size: 64,
                        color: theme.colorScheme.primary.withOpacity(0.5),
                      ),
                      const SizedBox(height: 16),
                      Text(
                        'No skills found',
                        style: theme.textTheme.titleLarge,
                      ),
                      const SizedBox(height: 8),
                      Text(
                        'Try a different search term',
                        style: theme.textTheme.bodyMedium?.copyWith(
                          color: theme.colorScheme.onSurface.withOpacity(0.7),
                        ),
                      ),
                    ],
                  ),
                )
              : ListView.builder(
                  padding: const EdgeInsets.only(bottom: 16),
                  itemCount: filteredModules.length,
                  itemBuilder: (context, index) {
                    final module = filteredModules[index];
                    final skills = _getFilteredSkills(module);
                    final isExpanded = _expandedModule == module;

                    return Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
                      child: Card(
                        clipBehavior: Clip.antiAlias,
                        child: Column(
                          children: [
                            // Module header
                            InkWell(
                              onTap: () {
                                setState(() {
                                  _expandedModule = isExpanded ? null : module;
                                });
                              },
                              child: Container(
                                padding: const EdgeInsets.all(16),
                                decoration: BoxDecoration(
                                  color: _getModuleColor(module).withOpacity(0.1),
                                ),
                                child: Row(
                                  children: [
                                    Icon(
                                      _getModuleIcon(module),
                                      color: _getModuleColor(module),
                                      size: 28,
                                    ),
                                    const SizedBox(width: 16),
                                    Expanded(
                                      child: Column(
                                        crossAxisAlignment: CrossAxisAlignment.start,
                                        children: [
                                          Text(
                                            module,
                                            style: theme.textTheme.titleMedium?.copyWith(
                                              fontWeight: FontWeight.bold,
                                              color: _getModuleColor(module),
                                            ),
                                          ),
                                          Text(
                                            '${skills.length} skill${skills.length == 1 ? '' : 's'}',
                                            style: theme.textTheme.bodySmall?.copyWith(
                                              color: theme.colorScheme.onSurface.withOpacity(0.6),
                                            ),
                                          ),
                                        ],
                                      ),
                                    ),
                                    Icon(
                                      isExpanded ? Icons.expand_less : Icons.expand_more,
                                      color: _getModuleColor(module),
                                    ),
                                  ],
                                ),
                              ),
                            ),

                            // Skills list
                            if (isExpanded)
                              ...skills.map((skill) {
                                return _buildSkillTile(skill, module);
                              }).toList(),
                          ],
                        ),
                      ),
                    );
                  },
                ),
        ),
      ],
    );
  }

  Widget _buildSkillTile(String skill, String module) {
    final description = SkillDescriptions.getDescription(skill);
    final color = _getModuleColor(module);

    return Container(
      decoration: BoxDecoration(
        border: Border(
          top: BorderSide(
            color: Theme.of(context).colorScheme.outline.withOpacity(0.2),
          ),
        ),
      ),
      child: ExpansionTile(
        tilePadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
        childrenPadding: const EdgeInsets.only(
          left: 16,
          right: 16,
          bottom: 16,
        ),
        leading: Container(
          width: 4,
          height: 40,
          decoration: BoxDecoration(
            color: color,
            borderRadius: BorderRadius.circular(2),
          ),
        ),
        title: Text(
          skill,
          style: const TextStyle(
            fontWeight: FontWeight.w600,
          ),
        ),
        children: [
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: color.withOpacity(0.05),
              borderRadius: BorderRadius.circular(8),
            ),
            child: Text(
              description,
              style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                    height: 1.5,
                  ),
            ),
          ),
        ],
      ),
    );
  }
}
