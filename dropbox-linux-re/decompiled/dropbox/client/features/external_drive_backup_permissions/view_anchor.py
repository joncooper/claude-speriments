# Source Generated with Decompyle++
# File: view_anchor.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from bridge_gen.bridge_interface_external_drive_backup_permissions_view_anchor import ExternalDriveBackupPermissionsViewAnchorBridgeInterface
from dropbox.client.features.external_drive_backup_permissions.view_model.view_model import ExternalDriveBackupPermissionsViewModel
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.html_views.common.interface import ViewAnchorConfiguration
from dropbox.foundation.html_views.common.view_anchor import ViewAnchorBase
from dropbox.platform import IS_MAC
if IS_MAC:
    from dropbox.mac.system_preferences import open_security_pane_privacy, SecurityPaneServiceType

class ExternalDriveBackupPermissionsViewAnchor(ExternalDriveBackupPermissionsViewAnchorBridgeInterface, ViewAnchorBase):
    pass
# WARNING: Decompyle incomplete

