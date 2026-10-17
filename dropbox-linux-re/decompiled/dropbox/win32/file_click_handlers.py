# Source Generated with Decompyle++
# File: file_click_handlers.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Optional, Text, Tuple
from build_number import assert_full_msix_no_registry_writes
from pynt.constants import KEY_ALL_ACCESS, KEY_WOW64_32KEY, KEY_WOW64_64KEY
from pynt.helpers.general import FormattedWindowsError
from pynt.helpers.registry import create_registry_key, delete_registry_tree, delete_registry_value, registry_key, safe_read_registry_value, set_registry_value
from six.moves.winreg import HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, REG_SZ
from dropbox.install_type.win import WINDOWS_CLASSES_KEY
from dropbox.trace import TRACE

def install_file_click_handler(exe_path, extension, handler_name = None, type_description = None, icon_path = None, is_alternative = (False, HKEY_LOCAL_MACHINE), hive = ('exe_path', 'Text', 'extension', 'Text', 'handler_name', 'Text', 'type_description', 'Text', 'icon_path', 'Text', 'is_alternative', 'bool', 'hive', 'int', 'return', 'None')):
    TRACE('Installing %s click handler', handler_name)
    entries = _entries_for_install(exe_path, extension, handler_name, type_description, icon_path, is_alternative)
# WARNING: Decompyle incomplete


def uninstall_file_click_handler(extension = None, handler_name = None, is_alternative = None, hive = (False, HKEY_LOCAL_MACHINE)):
    TRACE('Uninstalling %s click handler', handler_name)
    entries = _entries_for_uninstall(extension, handler_name, is_alternative)
# WARNING: Decompyle incomplete


def validate_file_click_handler_installation(exe_path, extension, handler_name = None, type_description = None, icon_path = None, is_alternative = (False, HKEY_LOCAL_MACHINE), hive = ('exe_path', 'Text', 'extension', 'Text', 'handler_name', 'Text', 'type_description', 'Text', 'icon_path', 'Text', 'is_alternative', 'bool', 'hive', 'int', 'return', 'bool')):
    entries = _entries_for_install(exe_path, extension, handler_name, type_description, icon_path, is_alternative)
# WARNING: Decompyle incomplete


def _entries_for_install(exe_path, extension, handler_name = None, type_description = None, icon_path = None, is_alternative = ('exe_path', 'Text', 'extension', 'Text', 'handler_name', 'Text', 'type_description', 'Text', 'icon_path', 'Text', 'is_alternative', 'bool', 'return', 'Tuple[Tuple[Text, Optional[Text], int, Text], ...]')):
    handler_key = 'Dropbox.' + handler_name
    extension_path = WINDOWS_CLASSES_KEY + '\\' + extension
    handler_path = WINDOWS_CLASSES_KEY + '\\' + handler_key
    return ((extension_path + '\\OpenWithProgids', handler_key, REG_SZ, '') if is_alternative else (extension_path, None, REG_SZ, handler_key), (handler_path, None, REG_SZ, type_description), (handler_path + '\\DefaultIcon', None, REG_SZ, icon_path), (handler_path + '\\shell\\Open\\Command', None, REG_SZ, '"%s" /openext "%%1" %%*' % exe_path))


def _entries_for_uninstall(extension = None, handler_name = None, is_alternative = None):
    handler_key = 'Dropbox.' + handler_name
    extension_path = WINDOWS_CLASSES_KEY + '\\' + extension
    handler_path = WINDOWS_CLASSES_KEY + '\\' + handler_key
    return ((extension_path + '\\OpenWithProgids', handler_key) if is_alternative else (extension_path, None), (handler_path, None))

