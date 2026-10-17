# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

import enum
from typing import Set

class Views(enum.Enum, str):
    HOME = 'home'
    ACTIVITY = 'activity'
    REPLAY_HOME = 'replay_home'
    REPLAY_PROJECTS = 'replay_projects'
    AGENTS = 'agents'
    LIBRARY = 'library'
    PREFERENCES = 'preferences'

FOREGROUND_SURFACE_EXPERIMENT = 'desktop-foreground-surface-experiment'
DROPBOX_DOMAIN = 'dropbox.com'
DROPBOXUSERCONTENT_DOMAIN = 'dropboxusercontent.com'
ALLOWED_EXACT_PATHS: 'Set[str]' = {
    '/share',
    '/requests',
    '/deleted_files'}
ALLOWED_PATH_PREFIXES: 'Set[str]' = {
    '/p',
    '/home',
    '/work',
    '/preview',
    '/personal'}
GATED_SCL_PATH_PREFIXES: 'Set[str]' = {
    '/scl/fi',
    '/scl/fo'}
BLOCKED_PATH_PREFIXES: 'Set[str]' = {
    '/oauth2/authorize'}
REJECTED_PATH_PATTERNS: 'Set[str]' = {
    '.paper'}
