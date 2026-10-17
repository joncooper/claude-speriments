# Source Generated with Decompyle++
# File: machine_impl.pyc (Python 3.11)

import errno
import os
from typing import cast, Optional, Text
from apex.metrics import MetricsReporter
from apex.metrics.metrics import MetricsReporterImpl
from client.configuration.wrapper import MachineConfigurationWrapper
from navigation_service import NavigationServiceInterface
from machine import MachineContext
from dropbox.client.configuration.interface import ConfigurationManagerInterface
from dropbox.client.constants import AppDataPaths
from dropbox.client.gandalf import Gandalf
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.foundation.account_manager import AccountManager
from dropbox.foundation.metrics.amp.bridge_gen.bridge_interface_amp_sink import AmpSinkBridgeInterface
from dropbox.foundation.metrics.amp.ts_sink import SamplesSink
from dropbox.foundation.navigation_service.factory import NavigationServiceContext, NavigationServiceFactory
from dropbox.foundation.stormcrow.machine import MachineStormcrow
APEX_METRICS_FEATURE_CONFIG = 'UseApexMetrics'
APEX_METRICS_STORMCROW = 'desktop-apex-metrics-use-rust-lib'

class MachineContextImpl(MachineContext):
    pass
# WARNING: Decompyle incomplete


def _create_directory_if_needed(path = None):
    
    try:
        os.makedirs(path)
        return None
    except OSError:
        e = None
        if e.errno != errno.EEXIST:
            raise 
        e = None
        del e
        return None
        e = None
        del e


