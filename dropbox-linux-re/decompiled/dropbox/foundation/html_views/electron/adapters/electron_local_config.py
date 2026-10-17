# Source Generated with Decompyle++
# File: electron_local_config.pyc (Python 3.11)

from datetime import datetime
from typing import Any, Callable, Dict, List, NamedTuple, Optional
from build_number.features import feature_enabled
from dropbox.client.configuration.context_aware_config_dict import ContextAwareConfigDict
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.configuration.wrapper import LocalConfigurationWrapper
from dropbox.client.fenix.utils import fenix_api
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures.basic import Future, ResolvedFuture
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict, JSONish
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.trace import TRACE

class UnserializableConfigValueException(Exception):
    pass

CustomSerializer = NamedTuple('CustomSerializer', [
    ('to_jsonish', Callable[([
        Any], JSONish)]),
    ('from_jsonish', Callable[([
        JSONish], Any)])])

class ElectronLocalConfigAdapter(Destroyable):
    pass
# WARNING: Decompyle incomplete

