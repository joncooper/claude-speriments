# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from contextlib import contextmanager
from typing import Any, cast, Dict, Iterator, Optional, Type, TypeVar
from weakref import WeakKeyDictionary
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.raii2._shared_impl.base import SuperDestroyable
from dropbox.foundation.raii2.arc import Arc, Weak
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.threading import Lock
__all__ = [
    'Singleton',
    'SingletonActor']
_SI = TypeVar('_SI', bound = '_SingletonImpl')

class _SingletonImpl(SuperDestroyable):
    _SingletonImpl__memo: "Dict[Type['_SingletonImpl'], WeakKeyDictionary['_SingletonImpl', Weak[SuperDestroyable]]]" = { }
    _SingletonImpl__memo_lock = Lock()
    _SingletonImpl__instance_locks: "Dict[Type['_SingletonImpl'], Lock]" = { }
    from_context = (lambda cls = None, context = None: pass# WARNING: Decompyle incomplete
)()
    _singleton_instances = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()()

MYPY = False

class Singleton(_SingletonImpl, Destroyable):
    pass
# WARNING: Decompyle incomplete


class SingletonActor(_SingletonImpl, Actor):
    pass
# WARNING: Decompyle incomplete

