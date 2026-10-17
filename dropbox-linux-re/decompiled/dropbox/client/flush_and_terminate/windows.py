# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

from __future__ import absolute_import, annotations, division, print_function
from typing import Optional, TYPE_CHECKING
import win32event
import win32process
import win32security
if TYPE_CHECKING:
    from pywintypes import HANDLEType
from winffi.advapi32.api import GetUserName
from common import FlushAndTerminateHandlerCommon
from dropbox.client.constants.win import DEFAULT_KILL_PROCESS_BY_NAME_TIMEOUT_MS, NAMED_PROCESS_EVENT_PREFIX
from dropbox.client.flush_and_terminate.constants import FLUSH_AND_TERMINATE
from dropbox.client.util.win import get_named_process_event
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE

def create_named_process_event(event_name = None):
    pid = win32process.GetCurrentProcessId()
    name = '%s_%s_%d' % (NAMED_PROCESS_EVENT_PREFIX, event_name, pid)
    admins = win32security.CreateWellKnownSid(win32security.WinBuiltinAdministratorsSid)
    (user, _, _) = win32security.LookupAccountName(None, GetUserName())
    dacl = win32security.ACL()
    dacl.AddAccessAllowedAce(win32security.ACL_REVISION, win32event.EVENT_MODIFY_STATE, admins)
    dacl.AddAccessAllowedAce(win32security.ACL_REVISION, win32event.EVENT_ALL_ACCESS, user)
    security_desc = win32security.SECURITY_DESCRIPTOR()
    security_desc.SetSecurityDescriptorDacl(1, dacl, 0)
    security_attr = win32security.SECURITY_ATTRIBUTES()
    security_attr.SECURITY_DESCRIPTOR = security_desc
    return win32event.CreateEvent(security_attr, 1, 0, name)


class FlushAndTerminateHandlerWindows(FlushAndTerminateHandlerCommon, StoppableThread):
    
    def __init__(self = None):
        FlushAndTerminateHandlerCommon.__init__(self)
        StoppableThread.__init__(self, name = FLUSH_AND_TERMINATE)
        self._flush_event = None
        self._stop_event = None
        
        try:
            self._stop_event = win32event.CreateEvent(None, 0, 0, None)
            self._flush_event = create_named_process_event(FLUSH_AND_TERMINATE)
            return None
        except Exception:
            report_exception(severity = Severity.DEBUG, component = DesktopComponent.UNKNOWN)
            TRACE('!! Failed to create events. Not listening to flush and terminate')
            return None


    
    def start(self = None):
        StoppableThread.start(self)

    
    def run(self = None):
        if not self._flush_event:
            TRACE('Not listening for events as event creation failed.')
            return None
        ret = win32event.WaitForMultipleObjects((self._stop_event, self._flush_event), False, win32event.INFINITE)
        if ret == win32event.WAIT_OBJECT_0:
            TRACE('Shutting down Flush and terminate thread.')
            return None
        if None == win32event.WAIT_OBJECT_0 + 1:
            self._try_to_exit(DEFAULT_KILL_PROCESS_BY_NAME_TIMEOUT_MS / 1000)
            win32event.ResetEvent(self._flush_event)
        else:
            TRACE('flush_and_terminate_handler failed wait with result %d', ret)
        continue

    
    def stop(self = None):
        if self._stop_event:
            win32event.SetEvent(self._stop_event)
            return None

    
    def signal(self = None, pid = None):
        pass
    # WARNING: Decompyle incomplete

    
    def set_wakeup_event(self = None):
        self.stop()
        if self._stop_event:
            win32event.ResetEvent(self._stop_event)
            return None


