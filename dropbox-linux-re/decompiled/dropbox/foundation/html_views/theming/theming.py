# Source Generated with Decompyle++
# File: theming.pyc (Python 3.11)

from typing import Optional
from build_number.features import feature_enabled
from bridge_gen.bridge_interface_theming import ThemingBridgeInterface
from dropbox.client.theme_manager.theme_manager import get_current_theme_setting
from dropbox.client.theme_manager.types import Theme
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.singleton import MachineSingleton
from dropbox.foundation.environment import debugging_features_are_enabled
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.signals import Signal, StandardSignal
from dropbox.foundation.stormcrow import NoStormcrowDataError
DARK_MODE_STORMCROW = 'desktop-dark-mode'

class Theming(ThemingBridgeInterface, Actor, MachineSingleton):
    pass
# WARNING: Decompyle incomplete

