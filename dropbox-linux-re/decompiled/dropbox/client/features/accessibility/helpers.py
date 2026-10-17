# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

from typing import Any, Optional
from AppKit import NSWorkspace
from Foundation import NSURL
from macffi.ApplicationServices import is_accessibility_enabled
from build_number import is_run_box
from constants import ACCESSIBILITY_HELP_URL, AccessibilityGrantState, AccessibilityPromptState, AccessibilityRequestReason, RUN_BOX_ACCESSIBILITY_MESSAGE
from dropbox.client.configuration.wrapper import MachineConfigurationWrapper
from dropbox.client.ui.cocoa.alert_dialog.alert_dialog import CocoaAlertDialog
from dropbox.client.ui.cocoa.constants import ENTER_KEY, ESCAPE_KEY
from dropbox.client.ui.common.harmony_strings import HarmonyStrings
from dropbox.client.ui.common.uikit import on_ui_thread_returns_none
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption
from dropbox.gui import assert_message_queue
from dropbox.harmony.mac.util import log_accessibility_event
from dropbox.mac.system_preferences import open_accessibility_preferences
from dropbox.mac.version import GOLDEN_GATE, MAC_VERSION, MOJAVE
from dropbox.trace import TRACE
errWindowDoesNotHaveProxy = -5602
errUnknownControl = -30584
fnfErr = -43
_ACCESSIBILITY_PROMPT: 'Optional[CocoaAlertDialog]' = None
_REQUEST_REASON: 'Optional[AccessibilityRequestReason]' = None

def prompt_for_accessibility_if_needed(machine_config = None, reason = None):
    if is_accessibility_enabled():
        return None
    if is_run_box():
        TRACE('%s', RUN_BOX_ACCESSIBILITY_MESSAGE)
    _prompt_for_accessibility(machine_config, reason)


def open_accessibility_help():
    url = NSURL.URLWithString_(ACCESSIBILITY_HELP_URL)
    NSWorkspace.sharedWorkspace().openURL_(url)


def get_prompt_count(machine_config = None):
    
    try:
        return int(machine_config.accessibility_prompt_count)
    except (KeyError, ValueError):
        TRACE('Invalid Accessibility prompt count. Resetting to 0')
        machine_config.accessibility_prompt_count = 0
        return 0



def get_accessibility_grant_state(machine_config = None):
    
    try:
        return machine_config.accessibility_grant_state
    except KeyError:
        TRACE('!! No previous Accessibility grant state. Defaulting to NOT_GRANTED')
        machine_config.accessibility_grant_state = AccessibilityGrantState.NOT_GRANTED
        return 
        except ValueError:
            report_bad_assumption('Invalid Accessibility grant state. Resetting to NOT_GRANTED')
            return 



def get_accessibility_prompt_state(machine_config = None):
    
    try:
        return machine_config.accessibility_prompt_state
    except KeyError:
        TRACE('!! No previous Accessibility prompt state. Defaulting to ALWAYS')
        machine_config.accessibility_prompt_state = AccessibilityPromptState.ALWAYS
        return 
        except ValueError:
            report_bad_assumption('Invalid Accessibility prompt state. Resetting to ALWAYS')
            return 


_prompt_for_accessibility = (lambda machine_config = None, reason = None: pass# WARNING: Decompyle incomplete
)()
