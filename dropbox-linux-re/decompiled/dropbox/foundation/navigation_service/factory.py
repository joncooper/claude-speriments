# Source Generated with Decompyle++
# File: factory.pyc (Python 3.11)

from abc import abstractmethod
from typing import Optional
from navigation_service import NavigationService
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.html_views.electron.adapters._impl import ElectronIpcAdapters
from dropbox.foundation.raii2 import Destroyable

class NavigationServiceContext(Destroyable):
    navigation_service = (lambda self = None: pass)()()
    ipc_adapters = (lambda self = None: pass)()()


class NavigationServiceFactory:
    create = (lambda self = None, machine_context = None: pass)()

