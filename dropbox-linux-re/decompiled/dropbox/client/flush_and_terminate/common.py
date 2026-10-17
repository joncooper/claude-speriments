# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import time
from typing import Optional
from build_number import VERSION
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.flush_and_terminate import FlushAndTerminateHandler
from dropbox.client.flush_and_terminate.constants import FLUSH_AND_TERMINATE, FLUSH_AND_TERMINATE_EXIT_REASON
from dropbox.client.shutdown_blocker import ShutdownBlockerInterface
from dropbox.client.updatemanager.base import get_user_engagement_wait_time
from dropbox.client.util import hard_exit
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.trace import TRACE

class FlushAndTerminateHandlerCommon(FlushAndTerminateHandler):
    FORCED_UPDATE_TIMEOUT_SECONDS = 120
    
    def __init__(self = None):
        self.shutdown_blocker = None
        self.config = None
        self.timeout = None

    
    def set_shutdown_blocker(self = None, shutdown_blocker = None):
        self.shutdown_blocker = shutdown_blocker

    
    def set_config(self = None, config = None):
        self.config = config

    
    def _update_config(self = None):
        if not self.config:
            return None
        
        try:
            self.config.config_dict['last_updatemanager'] = VERSION
            return None
        except Exception:
            report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)
            return None


    
    def _try_to_exit(self = None, installer_timeout = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _shutdown_blockers_allow_shutdown(self = None, installer_timeout = None):
        pass
    # WARNING: Decompyle incomplete


