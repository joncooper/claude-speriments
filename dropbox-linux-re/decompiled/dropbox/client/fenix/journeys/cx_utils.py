# Source Generated with Decompyle++
# File: cx_utils.pyc (Python 3.11)

from typing import List
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.sync_everything.v3.device_state import KnownFolder
from dropbox.client.ui.common.sync_everything import get_os_folders_to_hard_reset, reset_os_folders_locations_hard, reset_os_folders_locations_normal
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import IS_WINDOWS
from dropbox.trace import TRACE
if IS_WINDOWS:
    from dropbox.client.file_permissions.windows import fix_permissions_for_entire_dropbox
    from dropbox.hardlinks.win import convert_hardlinks_to_copies_in_dropbox, HardlinksFixFailedException
else:
    from dropbox.client.file_permissions.posix import fix_whole_dropbox_permissions
    from dropbox.hardlinks.posix import convert_hardlinks_to_copies_in_dropbox, HardlinkFixFailed
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

def fix_dropbox_permissions(app = None, account = None):
    pass
# WARNING: Decompyle incomplete


def fix_hardlinks(app = None, account = None):
    pass
# WARNING: Decompyle incomplete


def reset_fsw(app = None):
    pass
# WARNING: Decompyle incomplete


def reset_folder_os_location_normal(app = None, account = None, reset_op_session_id = None):
    return reset_os_folders_locations_normal(account, app.app_model.machine_context, reset_op_session_id)


def reset_folder_os_location_hard(app = None, account = None, reset_op_session_id = None, folders_to_reset = ('app', 'DropboxApplication', 'account', 'AccountInterface', 'reset_op_session_id', 'str', 'folders_to_reset', 'List[KnownFolder]', 'return', 'None')):
    return reset_os_folders_locations_hard(account, app.app_model.machine_context, folders_to_reset, reset_op_session_id)


def get_folders_to_hard_reset(app = None, account = None, reset_op_session_id = None):
    return get_os_folders_to_hard_reset(account, app.app_model.account_manager, app.app_model.machine_context, reset_op_session_id)

