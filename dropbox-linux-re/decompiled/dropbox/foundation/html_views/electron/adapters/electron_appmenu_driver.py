# Source Generated with Decompyle++
# File: electron_appmenu_driver.pyc (Python 3.11)

from typing import Any, Dict, List, Text
from apex.metrics import MetricsReporter
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.i18n import trans
from dropbox.trace import TRACE

class ElectronAppMenuDriver(Destroyable):
    pass
# WARNING: Decompyle incomplete


def get_appmenu_translations_internal(requested_phrases = None):
    appmenu_translations = { }
    for phrase in requested_phrases:
        translation = trans(phrase)
        appmenu_translations[phrase] = translation
        TRACE('Failed to get translation for: %s', phrase)
        raise 
        return appmenu_translations

