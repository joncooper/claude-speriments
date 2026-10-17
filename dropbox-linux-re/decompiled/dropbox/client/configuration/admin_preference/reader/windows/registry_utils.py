# Source Generated with Decompyle++
# File: registry_utils.pyc (Python 3.11)

import abc
import datetime
from typing import Any, Optional
import six
from dropbox.platform import IS_WINDOWS
if IS_WINDOWS:
    from pynt.helpers.registry import HKEY_CURRENT_USER, read_registry_value, registry_key
NUMBER_OF_RETRIES_TO_READ_REGISTRY = 3

class RegistryReader:
    LAST_ERROR_TIME_FOR_ACCESSING_REGISTRY = datetime.datetime.now()
    DELAY_BEFORE_READING_REGISTRY_AGAIN = None
    read = (lambda cls, key_path, value_name: raise NotImplementedError())()
    _query_registry = (lambda cls, key_path, value_name: if not IS_WINDOWS:
raise ValueError('Invalid platform')for retry in range(NUMBER_OF_RETRIES_TO_READ_REGISTRY):
hkey = registry_key(HKEY_CURRENT_USER, key_path)None(None, None)None, read_registry_value(hkey, value_name), with None:
if not None:
passexcept Exception:
if retry - 1 == NUMBER_OF_RETRIES_TO_READ_REGISTRY:
raise None = Nonedel excontinueex = Nonedel exNone)()
    reset_registry_change_event = (lambda cls, registry_main_path, registry_change_event: import win32apiimport win32conif cls.DELAY_BEFORE_READING_REGISTRY_AGAIN and datetime.datetime.now() - cls.LAST_ERROR_TIME_FOR_ACCESSING_REGISTRY < cls.DELAY_BEFORE_READING_REGISTRY_AGAIN:
Falsetry:
registry_to_watch = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, registry_main_path, 0, win32con.KEY_READ)win32api.RegNotifyChangeKeyValue(registry_to_watch, True, win32api.REG_NOTIFY_CHANGE_LAST_SET, registry_change_event, True)except Exception:
cls.LAST_ERROR_TIME_FOR_ACCESSING_REGISTRY = datetime.datetime.now()cls.DELAY_BEFORE_READING_REGISTRY_AGAIN = datetime.timedelta(seconds = 10)FalseTrue)()


def SimpleRegistryReader():
    '''SimpleRegistryReader'''
    read = (lambda cls, key_name, value_name: cls._query_registry(key_name, value_name))()

SimpleRegistryReader = <NODE:27>(SimpleRegistryReader, 'SimpleRegistryReader', six.with_metaclass(abc.ABCMeta, RegistryReader))
