# Source Generated with Decompyle++
# File: tray_lifetime_adapter.pyc (Python 3.11)

from typing import Any, Callable, Optional, TypeVar
from dropbox.enum_utils import auto, AutoNameEnum
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.signals.event import EventSignal
from dropbox.functions import classproperty
from dropbox.threading import Lock
_T = TypeVar('_T')
_D = TypeVar('_D', bound = Destroyable)

class TrayLifetimeAdapter(Destroyable):
    pass
# WARNING: Decompyle incomplete


class _TrayLifetimeMixinState(AutoNameEnum):
    APPMODEL_NOT_INITIALIZED = auto()
    APPMODEL_INITIALIZED = auto()
    APPMODEL_DESTROYING = auto()
    OBJECT_DESTROYED = auto()


class _TrayDestroyableOwner(Destroyable):
    pass
# WARNING: Decompyle incomplete


class TrayLifetimeMixin:
    pass
# WARNING: Decompyle incomplete

