# Source Generated with Decompyle++
# File: finder.pyc (Python 3.11)

from __future__ import absolute_import
import threading
import objc
from AppKit import NSWorkspace, NSWorkspaceLaunchWithoutActivation
from Foundation import NSError, NSObject, NSRunningApplication
from internal import find_finder_pid, osa_send_piped
from version import MAC_VERSION, MONTEREY
from dropbox.exception.reporting import report_bad_assumption
from dropbox.gui import event_handler
from dropbox.mac.internal import autoreleasepool
from dropbox.threadutils import SafeValue
from dropbox.trace import TRACE
if MAC_VERSION >= MONTEREY:
    from AppKit import NSWorkspaceOpenConfiguration

class FinderNotRunningError(Exception):
    pass


class FinderTimeoutError(Exception):
    pass


class FinderBusyError(Exception):
    pass


class FinderRestartError(Exception):
    pass


class FinderRestartSendOSAScriptFailed(Exception):
    pass


class EFFinderRestartHelper(NSObject):
    FinderTerminatedContext = 72
    FinderRestartTimeLimit = 5
    FinderIdentifier = 'com.apple.finder'
    FinderTerminationKey = 'isTerminated'
    restartFinder = (lambda cls = None: if threading.current_thread().name == 'MainThread':
raise Exception('Attempting to restart the Finder on the MainThread.')apps = NSRunningApplication.runningApplicationsWithBundleIdentifier_(cls.FinderIdentifier)if not apps:
raise FinderNotRunningError()finder = apps[0]safe_val = SafeValue()helper = EFFinderRestartHelper.alloc().initWithSafeValue_(safe_val)TRACE('Terminating finder %r', finder)finder.addObserver_forKeyPath_options_context_(helper, cls.FinderTerminationKey, 0, cls.FinderTerminatedContext)try:
finder.terminate()ret = safe_val.wait(cls.FinderRestartTimeLimit)finder.removeObserver_forKeyPath_(helper, cls.FinderTerminationKey)except:
finder.removeObserver_forKeyPath_(helper, cls.FinderTerminationKey)# WARNING: Decompyle incomplete
)()
    
    def initWithSafeValue_(self = None, ret = None):
        self = objc.super(EFFinderRestartHelper, self).init()
    # WARNING: Decompyle incomplete

    observeValueForKeyPath_ofObject_change_context_ = (lambda self, path, obj, change, context: pass# WARNING: Decompyle incomplete
)()


def restart(skip_error_reporting = (False,)):
    if not skip_error_reporting:
        report_bad_assumption('Trying to restart finder.')
    autoreleasepool()
    None(None, None)
    return 
    with None:
        if not None, EFFinderRestartHelper.restartFinder():
            pass


def has_progress_windows():
    script = '\n    tell application "Finder"\n        set wnds to every window\n        repeat with wnd in wnds\n                if class of wnd is window and wnd is not closeable then return yes\n        end repeat\n    end tell\n    return no\n    '
    
    try:
        (out, err) = osa_send_piped(script, trace = False, parse_results = True)
        return out == 'yes'
    except Exception:
        e = None
        TRACE('Failed to send apple script event to Finder %r', e)
        raise FinderRestartSendOSAScriptFailed()
        e = None
        del e


