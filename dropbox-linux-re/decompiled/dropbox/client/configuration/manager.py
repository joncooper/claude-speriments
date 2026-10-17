# Source Generated with Decompyle++
# File: manager.pyc (Python 3.11)

import os
from typing import Any, Dict, Optional, Text, Union
from apex.metrics import Metric
from build_number.features import feature_enabled
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.configuration.context_aware_config_dict import ContextAwareConfigDict
from dropbox.client.configuration.interface import ConfigurationManagerInterface, LocalConfigurationInterface
from dropbox.client.configuration.local_configuration import LocalConfiguration
from dropbox.client.configuration.network_controls import register_network_throttle_webdebugger_hooks
from dropbox.client.configuration.utils import DEFAULT_PREFERENCES
from dropbox.client.databases import cleanup_corrupt_databases, clear_appdata_for_unlink
from dropbox.client.mapreduce import DBKeyStore
from dropbox.client.unlink_cookie import get_host_secret_from_unlink_cookie, write_unlink_cookie_no_sync_engine
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.preferences import OPT_NOTIFS_BLUENOTE_ASSIGNED_TASKS, OPT_NOTIFS_BLUENOTE_FOLLOWED_COMMENTS, OPT_NOTIFS_BLUENOTE_MENTIONS, OPT_NOTIFS_BLUENOTE_SHARED_CONTENT, OPT_NOTIFS_BLUENOTE_VIEWS, OPT_NOTIFS_SYNC_ADD, OPT_NOTIFS_SYNC_EDIT_DELETE, OPT_SCREENSHOTS
from dropbox.trace import TRACE
from dropbox.webdebugger.server import WebDebugger
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.main_utility import DropboxApplicationUtility
    from dropbox.client.multiaccount.instance_database import InstanceConfig

class ConfigurationManager(ConfigurationManagerInterface):
    
    def __init__(self = None, app = None):
        self._app = app
        self._local_config = { }
        self._instance_config = None
        self._corruptdb = False
        self._corruptdb_secondary = False
        self._corruptdb_name = None

    instance_config = (lambda self = None: self._instance_config)()
    instance_config = (lambda self = None, instance_config = None: self._instance_config = instance_config)()
    corruptdb = (lambda self = None: self._corruptdb)()
    corruptdb = (lambda self = None, corruptdb = None: self._corruptdb = corruptdb)()
    corruptdb_secondary = (lambda self = None: self._corruptdb_secondary)()
    corruptdb_secondary = (lambda self = None, corruptdb_secondary = None: self._corruptdb_secondary = corruptdb_secondary)()
    corruptdb_name = (lambda self = None: self._corruptdb_name)()
    corruptdb_name = (lambda self = None, corruptdb_name = None: self._corruptdb_name = corruptdb_name)()
    
    def check_for_corruptdb(self = None, account = None):
