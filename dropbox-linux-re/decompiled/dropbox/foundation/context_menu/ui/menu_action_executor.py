# Source Generated with Decompyle++
# File: menu_action_executor.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Callable, Dict, List, Optional, Text
from bridge_gen.bridge_interface_menu_action_executor import MenuActionExecutorBridgeInterface
from dropbox.client.ui.common.uikit import on_ui_thread_future
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.signals import Signal, StandardSignal
from dropbox.threading import Lock

class MenuActionExecutor(Destroyable, MenuActionExecutorBridgeInterface):
    pass
# WARNING: Decompyle incomplete


def action_to_selector(action = None):
    if action.isalpha():
        return action + ':'


def selector_to_action(selector = None):
    if selector and selector.endswith(':') and selector[:-1].isalpha():
        return selector[:-1]

