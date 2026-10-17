# Source Generated with Decompyle++
# File: app_model.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional, Type
from apex.metrics import MetricsReporter
from dropbox.client.authentication.interface import AccountManagerInterface as LegacyAccountManagerInterface
from dropbox.client.configuration.manager import ConfigurationManager
from dropbox.client.gandalf import Gandalf
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.fileevents import FileEvents
from dropbox.foundation.account_manager import AccountManager
from dropbox.foundation.account_manager.impl import AccountManagerImpl
from dropbox.foundation.account_manager.user_anchor_interface import UserAnchorInterface
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.app_model.machine_anchor_interface import MachineAnchorInterface
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.machine_impl import MachineContextImpl
from dropbox.foundation.html_views.electron.host_driver import ElectronHostDriver
from dropbox.foundation.navigation_service.factory import NavigationServiceFactory
from dropbox.foundation.navigation_service.navigation_service import NavigationService
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.metrics.reporter import PeriodicMetricsReporter
MYPY = False
if MYPY:
    from dropbox.client.session_metadata.interface import LegacySessionMetadata

class ApplicationModel(Destroyable):
    pass
# WARNING: Decompyle incomplete

