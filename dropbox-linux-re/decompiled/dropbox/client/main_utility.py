# Source Generated with Decompyle++
# File: main_utility.pyc (Python 3.11)

import errno
import itertools
import os
import pprint
import sys
import threading
import time
import traceback
import uuid
from getopt import gnu_getopt as _getopt
from typing import Callable, Dict, Iterable, List, Optional, Tuple
import psutil
from apex.context import ApexContext
from apex.panic import RustPanicError, set_panic_handler
from apex.watchdog import is_monitored, monitor_session_id
import build_number
from build_number.environment import DropboxData
from lib.crashpad.api import add_simple_annotation
from dropbox import fsutil
from dropbox.build_common import get_build_number
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.background_worker import BackgroundWorkerThread
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.configuration.manager import ConfigurationManager
from dropbox.client.constants import AppDataPaths, DEFAULT_DROPBOX_FOLDER_NAME, LOCAL_FORM
from dropbox.client.databases import load_dropbox_config
from dropbox.client.delete_on_unlink import DeleteOnUnlink
from dropbox.client.device_info import get_device_info, get_process_start_time, UNSAFE_get_raw_machine_uuid
from dropbox.client.features.app_model_watcher.app_model_watcher import ApplicationModelWatcher
from dropbox.client.flow_tracker import FlowTracker
from dropbox.client.gandalf import Gandalf
from dropbox.client.high_trace import add_trace_account, barrier as rtrace_barrier, force_flush, has_unsent_exception, send_trace_log, start_trace_thread
from dropbox.client.installer.install_event import InstallEventReporter
from dropbox.client.installer_tag import InstallerTag
from dropbox.client.logging.dbxlog_logger import DbxLogger
from dropbox.client.mapreduce import DBKeyStore
from dropbox.client.multiaccount.instance_database import InstanceConfig
from dropbox.client.multiaccount.multibox import MultiBoxServer
from dropbox.client.quit_handlers import QuitHandlerPriorities
from dropbox.client.reporting.event import EventReporterManager
from dropbox.client.rtrace_api import report_unsent_exceptions
from dropbox.client.startup import install_early_in_boot, pre_appdata_use_startup
from dropbox.client.startup_handlers import StartupHandlers
from dropbox.client.ui.common.boot_error import boot_error, get_extra_trace_info, help_page_by_exception
from dropbox.client.ui.common.dialogs import BaseDialogController
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.client.unlink_cookie import get_host_secret_from_unlink_cookie, HOST_SECRET_KEYNAME
from dropbox.client.util import clean_tray, get_platform_info, get_user_agent_dict, hard_exit, kill_other_instances, on_exit, restart
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.dirtraverse import Directory
from dropbox.event import report
from dropbox.exception.exception_context import get_import_cycle_attrs
from dropbox.exception.persistence import configure_exceptions_dir
from dropbox.exception.reporting import initialize_exception_reporting, report_exception
from dropbox.exception.sentry import initialize_sentry
from dropbox.exception.severity import Severity
from dropbox.foundation.futures.basic import allow_blocking_on_main_thread
from dropbox.foundation.platform_version import PLATFORM_VERSION
from dropbox.foundation.reporting import report_app_framework_event_restricted
from dropbox.foundation.runtime import AutorestartRequestManager, install_interpreter_exception_hooks
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.foundation.startup_flags import StartupFlags
from dropbox.functions import python_version_string
from dropbox.hostname import get_local_host_display_name
from dropbox.i18n import safe_activate_translation, trans
from dropbox.keystore import KeystoreRegKeyError
from dropbox.list_legacy.controller import ListLegacyAdapter
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS, platform
from dropbox.stopwatch import global_sw_init
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.factory import SyncEngineFactory
from dropbox.sync_engine_boundary.file_system import AbstractFileSystem
from dropbox.sync_root.accessor import RootManagerAccessor
from dropbox.sync_root.interface import SyncRootManagerInterface
from dropbox.sync_root.manager import SyncRootManager
from dropbox.threadutils import set_thread_cpu_counter_name
from dropbox.trace import set_debugging, TRACE
from dropbox.traces.formatted_traces import FormattedTraceReporter
from dropbox.url_info import dropbox_url_info
if IS_WINDOWS:
    from dropbox.client.installer.win import install, install_dev, migrate_sparse_to_full, self_uninstall, uninstall_dev
    from dropbox.client.startup.win import restart_explorer
    from dropbox.client.util.win import kill_process_by_name
else:
    from dropbox.client.file_permissions.posix import fix_perm_on_directory
if IS_MAC:
    import DropboxExtensionUtil
    from dropbox.client.startup.mac import check_other_version, detect_launch_from_dmg, preload_dlls
    from dropbox.client.ui.cocoa.pump_loop_helper import pump_event_loop
    from dropbox.client.util.mac import kill_parent_instance, launch_newer_version, running_from_dmg
elif IS_LINUX:
    from dropbox.client.startup.linux import check_other_version, handle_linux_autorestart
    from dropbox.client.util.linux import launch_newer_version
elif IS_WINDOWS:
    from dropbox.client.features.foundation.custom_url_scheme_handler.registrar_win import sanitize_custom_url_input_args
MYPY = False
if MYPY:
    from mypy_extensions import Arg
BUILD_KEY = build_number.BUILD_KEY
SKIP_INSTANCE_CONFIG_FLAGS = set([
    '/killeveryone',
    '/self_uninstall',
    '/migrate_sparse_to_full'])

class DropboxApplicationUtility:
    
    def __init__(self = None, unicode_argv = None, context = None):
        pass
    # WARNING: Decompyle incomplete

    
    def register_context_cleanup(self = None):
        self.add_quit_handler(self._context_cleanup, priority = QuitHandlerPriorities.TEARDOWN_APEX_CONTEXT)

    
    def _parse_command_line_flags(self = None):
        cmd_line = self.argv
        if IS_WINDOWS:
            cmd_line = sanitize_custom_url_input_args(cmd_line)
        cmd_line = list(cmd_line)
        TRACE('Command line: %r', cmd_line)
        (optlist, remaining) = _getopt(cmd_line, '', [
            'client=',
            'channel-id=',
            'move-to-dropbox=',
            'remote-debugging=',
            'autorestarted',
            'restart-for='])
        TRACE('Command flags: %r', optlist)
        self.argv = remaining
        return dict(optlist)

    
    def _parse_dbdata(self = None):
        dbdata_str = ''
        self.dbdata = { }
        for i, arg in enumerate(self.argv):
            if arg.startswith('/DBData:'):
                dbdata_str = arg[len('/DBData:'):]
                del self.argv[i]
                TRACE('DBData: %r', dbdata_str)
            
            if dbdata_str:
                
                try:
                    self.dbdata = DropboxData.decode(dbdata_str)
                    TRACE('Decoded DBData: %r', self.dbdata)
                    return None
                except (SyntaxError, TypeError, ValueError):
                    TRACE('Failed to parse DBData')
                    return None
                    return None


    
    def _get_installer_args(self = None):
        tag_str = ''
        for i, arg in enumerate(self.argv):
            if arg.startswith('/TAGS:'):
                tag_str = arg[len('/TAGS:'):]
                del self.argv[i]
            
            if self.dbdata and self.dbdata.get('TAGS'):
                if tag_str:
                    TRACE('Warning - existing TAGS %r replaced with %r from DBData', tag_str, self.dbdata.get('TAGS'))
                if not self.dbdata.get('TAGS'):
                    tag_str = ''
                    TRACE('installer tag: %r', tag_str)
                    
                    try:
                        self.installer_tag = InstallerTag(tag_str)
                        return None
                    except Exception:
                        self.installer_tag = InstallerTag('')
                        return None


    
    def _is_installer(self = None):
