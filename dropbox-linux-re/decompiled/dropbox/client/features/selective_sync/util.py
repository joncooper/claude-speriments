# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

import re
from typing import Dict, NewType, Optional, Text
from dropbox.api.v2.datatypes.team_selective_sync import ListTeamSelectiveSyncSettingsArgs, ListTeamSelectiveSyncSettingsResponse
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client_api.apiv2.generated.team_selective_sync import TeamSelectiveSync
from dropbox.client_api.connection.interface import HostKeyAuth
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcInfo
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.shared.server_path import RRLowerServerPath
SELSYNC_PATH_REGEX = re.compile('^\\/.*')
SelSyncPath = NewType('SelSyncPath', str)

def selsync_path(path = None):
    if SELSYNC_PATH_REGEX.match(path):
        return SelSyncPath(path)
    report_exception(severity = Severity.CRITICAL, component = DesktopComponent.SELECTIVE_SYNC_UI)
    raise ValueError('Failed to convert path to SelSyncPath')


def list_team_selective_sync_settings(account = None, conn = None):
    pass
# WARNING: Decompyle incomplete

