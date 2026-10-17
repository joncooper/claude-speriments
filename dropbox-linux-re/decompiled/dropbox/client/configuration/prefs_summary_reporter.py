# Source Generated with Decompyle++
# File: prefs_summary_reporter.pyc (Python 3.11)

import os
from typing import Any, Dict, FrozenSet, List, Optional
from six import iteritems
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.configuration.manager import ConfigurationManager
from dropbox.client.configuration.prefs_report_origin import PrefsReportOrigin
from dropbox.client.configuration.utils import DEFAULT_PREFERENCES, NOTIFICATION_PREFERENCES
from dropbox.client.constants import DEFAULT_DROPBOX_PATH
from dropbox.client.features.accessibility.constants import OPT_AX_GRANT, OPT_AX_PROMPT
from dropbox.client.periodic import PeriodicScheduler
from dropbox.components.desktop_components import DesktopComponent
from dropbox.connection_backoff import get_jittered_seconds
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.preferences import NOTIF_HAS_MODIFIED_SUFFIX, OPT_CB_STARTUP, OPT_DROPBOX_FOLDER_OPENER_APP, OPT_HARMONY, OPT_HARMONY_OUTSIDE_DROPBOX, OPT_HARMONY_VISIBILITY, OPT_LANG, OPT_P2P, OPT_PHOTO, OPT_SCREENSHOTS, OPT_STARTUP, OPT_VIDEO
from dropbox.shared.server_path import RRCasedServerPath
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_root.interface import SyncRootManagerInterface, SyncRootType
from dropbox.trace import TRACE
PrefSummary = Dict[(str, Any)]

class PrefsSummaryReporter:
    
    def __init__(self, config_manager = None, account_manager = None, sync_engine_adapter = None, root_manager = ('config_manager', 'ConfigurationManager', 'account_manager', 'AccountManagerInterface', 'sync_engine_adapter', 'SyncEngineAdapter', 'root_manager', 'SyncRootManagerInterface', 'return', 'None')):
        self._config_manager = config_manager
        self._account_manager = account_manager
        self._sync_engine_adapter = sync_engine_adapter
        self._root_manager = root_manager

    report_prefs_summary = (lambda self = None, report_origin = None: pass# WARNING: Decompyle incomplete
)()
    
    def schedule_daily_reporting(self = None, periodic_scheduler = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_reportable_summary(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_external_summary(self = None, summary = None):
        pass
    # WARNING: Decompyle incomplete


