# Source Generated with Decompyle++
# File: host_driver.pyc (Python 3.11)

import json
from abc import abstractmethod, abstractproperty
from typing import Dict, NamedTuple, Optional
from apex.context import ApexContext
from apex.util import system_architecture
from build_number import BUILDID, dropbox_version, is_frozen, is_full_msix, is_store_managed
from build_number.features import get_feature_state
from dropbox.client.constants import DROPBOX_API_APP_KEY, DROPBOX_API_APP_SECRET
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import exception_cpu_family
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.html_views.bridge.pipe_interface import JavaScriptBridgePipeInterface
from dropbox.foundation.html_views.common.content_metadata import StandaloneHtmlContentMetadata
from dropbox.foundation.html_views.common.content_source import ContentSource
from dropbox.foundation.html_views.common.debug import html_view_debugging_features_enabled
from dropbox.foundation.html_views.common.navigation_rules import get_server_view_navigation_prefs, LOCAL_VIEW_NAVIGATION_PREFS, LOCAL_VIEW_NAVIGATION_PREFS_DEBUG
from dropbox.foundation.html_views.common.view import ViewType
from dropbox.foundation.html_views.electron.adapters.electron_metrics_reporter import ElectronMetricsReporter
from dropbox.foundation.html_views.electron.bridge import ElectronBridgePipe
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.html_views.electron.managed_electron_view import ManagedElectronView, ManagedElectronViewDefinition, ManagedElectronViewError, ManagedElectronViewResult, MEVSpawnFailure, MEVSpawnSuccess
from dropbox.foundation.platform_version import PLATFORM_VERSION
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.gui import assert_not_on_main_thread
from dropbox.platform import platform
from dropbox.threading import Lock
from dropbox.trace import TRACE
ElectronProperties = NamedTuple('ElectronProperties', [
    ('productName', str),
    ('productVersion', str),
    ('electronVersion', str),
    ('chromeVersion', str)])

class ElectronHostDriverInterface(Destroyable):
    ipc = (lambda self = None: pass)()
    get_electron_properties = (lambda self = None: pass)()
    ping = (lambda self = None: pass)()
    create_embeddable_view = (lambda self, serialized_top_level_params = None, use_isolated_session = None, view_type = abstractmethod, user_agent = ('serialized_top_level_params', 'str', 'use_isolated_session', 'bool', 'view_type', 'ViewType', 'user_agent', 'str', 'return', 'Future[int]'): pass)()
    load_web_contents = (lambda self = None, web_contents_id = None, url = abstractmethod, headers = ('web_contents_id', 'int', 'url', 'str', 'headers', 'Optional[JSONDict]', 'return', 'None'): pass)()
    initialize_window_from_metadata = (lambda self = None, web_contents_id = None, metadata = abstractmethod: pass)()
    create_bridge_pipe = (lambda self = None, web_contents_id = None: pass)()
    signal_web_contents_view_destroyed = (lambda self = None, web_contents_id = None: pass)()
    dropbox_quitting = (lambda self = None: pass)()
    destroy_electron_views = (lambda self = None: pass)()


class ElectronHostDriver(ElectronHostDriverInterface):
    pass
# WARNING: Decompyle incomplete

