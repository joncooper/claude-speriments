# Source Generated with Decompyle++
# File: quarantine_xattr.pyc (Python 3.11)

from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import IS_MAC
from dropbox.sync_event.report import report_sync_event, SyncEventName
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.mac.version import CATALINA, MAC_VERSION
    from dropbox.xattrs import xattr

def check_and_remove_quarantine_xattr(account = None):
    if not IS_MAC:
        return None
    if None < CATALINA:
        return None
# WARNING: Decompyle incomplete

