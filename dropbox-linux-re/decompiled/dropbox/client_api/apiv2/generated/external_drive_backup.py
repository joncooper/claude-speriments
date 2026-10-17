# Source Generated with Decompyle++
# File: external_drive_backup.pyc (Python 3.11)

import datetime
from typing import Any, Callable, Dict, List, Optional, Tuple, TYPE_CHECKING, Union


stone_validators
import dropbox.api.v2.datatypes.device_sync = import stone.backends.python_rsrc.stone_validators, backends, python_rsrc
import dropbox.api.v2.datatypes.external_drive_backup as dropbox
import dropbox.api.v2.datatypes.files as dropbox
import dropbox.client.authentication.interface as dropbox
import dropbox.client_api.connection.interface as dropbox
import dropbox.foundation.futures.basic as dropbox

class ExternalDriveBackup:
    clear_all_quota_exempt = (lambda conn = None, auth = None, extra_headers = staticmethod: 