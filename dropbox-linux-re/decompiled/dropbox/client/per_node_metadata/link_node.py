# Source Generated with Decompyle++
# File: link_node.pyc (Python 3.11)

import os
from functools import partial
from typing import cast, Dict, Iterable, List, Optional, Text, Tuple
from dropbox.client.authentication.account import Account
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.plusplus.logger import EventAction, EventObject, PlusPlusActionSurface, PlusPlusLogger
from dropbox.client.file_activation.constants import FileActivationError
from dropbox.client.file_activation.events import FileOpenInfo, FileOpenOrigin
from dropbox.client.file_activation.interface import ExtensionHandler
from dropbox.client.multiaccount.role import Roles
from dropbox.client.per_node_metadata.constants import SupportedExtension
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_assertion_error, report_bad_assumption, Severity, UnexpectedNoneError
from dropbox.foundation.account_manager import AccountModel
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future
from dropbox.foundation.futures.basic import flatten_future
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.proto.per_node_metadata.link_node_pb2 import LinkNodeAction
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties
from dropbox.sync_engine_boundary.types.remote_props import FileLikeProperties, MountProperties, RemoteLocationProperties
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info

def get_extension(filename = None):
    return os.path.splitext(filename)[1]


def get_personal_account(account_models = None):
    for account in account_models:
        if account.role == Roles.PERSONAL:
            
            return None, account
        return None


class LinkNodeOpener(ExtensionHandler):
    
    def handle_open(self = None, files = None):
        pass
    # WARNING: Decompyle incomplete

    
    def handle_error(self = None, errors = None):
        pass

    _get_remote_properties = (lambda self = None, nucleus_interface = None, properties = GlobalPool.dispatched_as_3('LinkNodeOpener._get_remote_properties'): pass# WARNING: Decompyle incomplete
)()
    _handle_link_node_action = (lambda self = None, user_context = None, open_info = GlobalPool.dispatched_as_4('LinkNodeOpener._handle_link_node_action'), properties = ('user_context', 'UserContext', 'open_info', 'FileOpenInfo', 'properties', 'Optional[RemoteLocationProperties]', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()
    handled_extensions = (lambda cls = None: map(str, [
SupportedExtension.DBX_BACKUP,
SupportedExtension.DBX_PASSWORDS]))()
    
    def handle_open_backups_link(self = None, user_context = None, open_info = None):
        if open_info.origin == FileOpenOrigin.DESKTOP_NATIVE:
            PlusPlusLogger.report_event_hive(user_context.account, EventAction.select, EventObject.backup_set_up, PlusPlusActionSurface.finder_explorer)
        ComputerBackupManagerWrapper.on_link_node_clicked(user_context)

    
    def handle_open_passwords_link(self = None, user_context = None, open_info = None):
        if open_info.origin == FileOpenOrigin.DESKTOP_NATIVE:
            PlusPlusLogger.report_event_hive(user_context.account, EventAction.select, EventObject.passwords_set_up, PlusPlusActionSurface.finder_explorer)
        if not dropbox_url_info.launch_custom_url('dropbox-passwords://') or dropbox_url_info.launch_full_url(dropbox_url_info.construct_full_url('/getpasswords')):
            report_bad_assumption('Failed to launch Passwords app or open URL')
            return None
        return None


