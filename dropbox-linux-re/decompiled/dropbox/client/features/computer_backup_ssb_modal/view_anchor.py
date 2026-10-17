# Source Generated with Decompyle++
# File: view_anchor.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional, Text
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.computer_backup_ssb_modal.bridge_gen.bridge_interface_computer_backup_ssb_modal_view_anchor import ComputerBackupSsbModalViewAnchorBridgeInterface
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.sync_everything.view_model.sync_everything_manager_view_model import SyncEverythingManagerViewModel
from dropbox.client.multiaccount.role import Roles
from dropbox.client.ui.common.sync_everything import get_sync_everything_accounts
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.html_views.common.interface import ViewAnchorConfiguration, ViewAnchorInterface

class ComputerBackupSsbModalViewAnchor(Actor, ComputerBackupSsbModalViewAnchorBridgeInterface, ViewAnchorInterface):
    pass
# WARNING: Decompyle incomplete

