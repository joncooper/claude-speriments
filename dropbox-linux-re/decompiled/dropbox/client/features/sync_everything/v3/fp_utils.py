# Source Generated with Decompyle++
# File: fp_utils.pyc (Python 3.11)

import threading
from contextlib import contextmanager
from enum import auto, Enum
from typing import Iterator, Optional
from build_number.platform import IS_MAC
from dropbox.client.features.sync_everything.v3.nodep_utils import SE_TRACE
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2 import destroying
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
if IS_MAC:
    from macffi.System import DatalessFilePolicy, getiopolicy_np, IOScope, IOType, setiopolicy_np
    from dropbox.mac.version import MAC_VERSION, MONTEREY

class DatalessContext(Enum):
    tests = auto()
    create_breadcrumbs = auto()
    unmerge_cancel_check = auto()
    unmerge_breadcrumb = auto()
    generic_on_same_volume = auto()
    global_disable_sanity = auto()
    folder_exists_in_dropbox = auto()
    get_os_folder_root_file_count = auto()
    move_screenshot_folder_in_dropbox = auto()
    can_access_screenshot_path = auto()
    get_xattr_screenshot_path = auto()
    set_xattr_screenshot_path = auto()
    fp_recursive_listdir_workaround = auto()


def _dataless_policy_matters(user_context = None):
    if IS_MAC or MAC_VERSION < MONTEREY:
        return False
    nucleus_wrapper = destroying(NucleusWrapper.from_context(user_context))
    None(None, None)
    return 
    with None:
        if not None, nucleus_wrapper().is_file_provider():
            pass

allow_dataless_recall = (lambda user_context = None, caller_context = None: pass# WARNING: Decompyle incomplete
)()
