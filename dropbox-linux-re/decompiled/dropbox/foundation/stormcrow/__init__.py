# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import abstractmethod
from typing import List, Text
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.signals import Signal

class NoStormcrowDataError(Exception):
    pass
# WARNING: Decompyle incomplete


class MachineStormcrowInterface(Destroyable):
    allows_any_account = (lambda self = None, feature = None, treat_control_as_off = abstractmethod: pass)()
    get_variants_all_accounts = (lambda self = None, feature = None: pass)()
    on_changed = (lambda self = None: pass)()()

