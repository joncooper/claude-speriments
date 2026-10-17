# Source Generated with Decompyle++
# File: singleton.pyc (Python 3.11)

from typing import cast, Type, TypeVar, Union
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.singleton import Singleton
_M = TypeVar('_M', bound = 'MachineSingleton')

class MachineSingleton(Singleton):
    pass
# WARNING: Decompyle incomplete

_U = TypeVar('_U', bound = 'UserSingleton')

class UserSingleton(Singleton):
    pass
# WARNING: Decompyle incomplete

_G = TypeVar('_G', bound = 'GlobalSingleton')

class _Token:
    pass


class GlobalSingleton(Singleton):
    pass
# WARNING: Decompyle incomplete

