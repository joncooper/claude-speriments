# Source Generated with Decompyle++
# File: registrar_win.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from itertools import islice
from typing import Any, Iterable, List, Optional, Text, Tuple
from pynt.constants import KEY_WOW64_32KEY, REG_SZ, REG_VALUE_TYPE, WOW64_ACCESS_TYPE
from registrar import URLSchemeRegistrar
from dropbox.client.util import hard_exit
from dropbox.exception.reporting import report_assertion_error
from dropbox.exception.severity import Severity
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronIpc
from dropbox.foundation.runtime import ExitCode
from dropbox.install_type.win import WINDOWS_CLASSES_KEY
from dropbox.trace import TRACE
from dropbox.win32.copy_data import CopyDataId, create_unique_copy_data_window, destroy_copy_data_window
URL_SCHEME_WND_CLASS = 'DropboxUrlScheme'
URL_SCHEME_ARG_PREFIX_FROM_REGISTRY = 'custom-url+'

class WindowsURLSchemeRegistrar(URLSchemeRegistrar):
    pass
# WARNING: Decompyle incomplete


def sanitize_custom_url_input_args(argv = None):
    for index, arg in enumerate(argv):
        if arg.startswith(URL_SCHEME_ARG_PREFIX_FROM_REGISTRY):
            prefix_length = len(URL_SCHEME_ARG_PREFIX_FROM_REGISTRY)
            new_argv = list(islice(argv, index))
            new_argv.append(arg[prefix_length:])
            
            return None, new_argv
        return argv


def url_scheme_registry_entries(exe_path = None, scheme_name = None, icon_path = None):
    base_key_name = WINDOWS_CLASSES_KEY + '\\' + scheme_name
    return [
        (base_key_name, '', REG_SZ, KEY_WOW64_32KEY, 'URL:%s protocol' % scheme_name),
        (base_key_name, 'URL Protocol', REG_SZ, KEY_WOW64_32KEY, ''),
        (base_key_name + '\\DefaultIcon', '', REG_SZ, KEY_WOW64_32KEY, icon_path),
        (base_key_name + '\\shell', '', REG_SZ, KEY_WOW64_32KEY, ''),
        (base_key_name + '\\shell\\Open', '', REG_SZ, KEY_WOW64_32KEY, ''),
        (base_key_name + '\\shell\\Open\\Command', '', REG_SZ, KEY_WOW64_32KEY, '"{}" "{}%1"'.format(exe_path, URL_SCHEME_ARG_PREFIX_FROM_REGISTRY))]

