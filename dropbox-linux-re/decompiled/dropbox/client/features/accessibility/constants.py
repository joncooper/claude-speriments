# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from enum import Enum
RUN_BOX_ACCESSIBILITY_MESSAGE = "!! TO YOU, THE DEVELOPER: You're using run-box, and accessibility is not enabled for your terminal. Please manually enable it via System Preferences -> Security & Privacy -> Privacy and checking your terminal application."
OPT_AX_GRANT = 'accessibility_grant'
OPT_AX_PROMPT = 'accessibility_prompt'
OPT_AX_PROMPT_COUNT = 'accessibility_prompt_count'
ACCESSIBILITY_HELP_URL = 'https://www.dropbox.com/help/9266#accessibility'
PROMPT_ACCESSIBILITY_ON_INIT_TIME_WINDOW = 120

class AccessibilityGrantState(Enum):
    NOT_GRANTED = 0
    GRANTED = 1
    DEPRECATED_TCC_MODIFIED = 2
    AX_SUCCESS = 3


class AccessibilityPromptState(Enum):
    ALWAYS = 0
    ON_DEMAND = 1
    NEVER = 2


class AccessibilityRequestReason(Enum):
    GENERIC = 0
    BADGE = 1

