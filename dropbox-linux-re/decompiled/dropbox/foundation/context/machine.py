# Source Generated with Decompyle++
# File: machine.pyc (Python 3.11)

from abc import abstractmethod
from typing import Optional
from client.configuration.wrapper import MachineConfigurationWrapper
from navigation_service import NavigationServiceInterface
from bridge_gen.bridge_interface_machine_context import MachineContextBridgeInterface
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.foundation.account_manager import AccountManager
from dropbox.foundation.context import Context
from dropbox.foundation.metrics.amp.bridge_gen.bridge_interface_amp_sink import AmpSinkBridgeInterface
from dropbox.foundation.stormcrow.machine import MachineStormcrow
MYPY = False
if MYPY:
    from dropbox.foundation.navigation_service.factory import NavigationServiceContext
APEX_METRICS_FEATURE_CONFIG = 'UseApexMetrics'
APEX_METRICS_STORMCROW = 'desktop-apex-metrics-use-rust-lib'

class MachineContext(MachineContextBridgeInterface, Context):
    account_manager = (lambda self = None: pass)()()
    primary_account_config = (lambda self = None: pass)()()
    stormcrow = (lambda self = None: pass)()()
    connection = (lambda self = None: pass)()()
    amp_metrics_sink = (lambda self = None: pass)()()
    navigation_service = (lambda self = None: pass)()()
    navigation_service_context = (lambda self = None: pass)()()

