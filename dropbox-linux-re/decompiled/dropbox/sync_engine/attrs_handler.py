# Source Generated with Decompyle++
# File: attrs_handler.pyc (Python 3.11)

from __future__ import absolute_import
import base64
import errno
import itertools
import zlib
from contextlib import contextmanager
from typing import Any, Callable, Dict, FrozenSet, Iterator, Optional, Set, Text, Tuple
from six import iteritems, itervalues
from exceptions import UnreconstructableError
from file_system.exceptions import AttrsModifiedError, FileNotFoundError, NotADirectoryError, PermissionDeniedError
from sync_engine_util import AttributeMergeError
from dropbox.fsutil import fsutil
from dropbox.attrs import AttrDict, Attributes, BLOCKABLE_DEFAULT, convert_attr_data, get_attr_data, serialize_attr_dict, serialize_attr_dict_only, unfreeze_attr_dict, unserialize_attr_dict
from dropbox.client_api.hashing import DROPBOX_MAX_BLOCK_SIZE, split_blocklist
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fileutils import loop_delete, safe_chdir
from dropbox.functions import frozendict, make_bytes, retry, RetryException
from dropbox.infinite import infinite_stubfolders_enabled
from dropbox.platform import IS_MAC
from dropbox.shared.util import safe_navigate
from dropbox.trace import TRACE, trace_stack, WARNING
if IS_MAC:
    from dropbox.mac.finderinfo import FINDER_INFO_BLOB_BYTE_SIZE, MacFinderInfoHelper
MYPY = False
if MYPY:
    from file_system.abstract_attributes_handle import AbstractAttributesHandle
    from file_system.abstract_file_system import AbstractFileSystem as FileSystem
    from dropbox.functions import EitherStr
    from dropbox.shared.local_path import LocalPath
_DROPBOX_SAFE_ATTR_FILE = '.dropbox.attr'
AttrsWhitelist = Dict[(str, Dict[(str, Dict[(str, Any)])])]
BlockHandler = Optional[Callable[([
    bytes,
    bytes], None)]]

def _dir_safe_filename(local_path):
    return local_path.join(_DROPBOX_SAFE_ATTR_FILE)


def _safe_open_file(fs, local_path, mode):
    
    try:
        return fs.open(_dir_safe_filename(local_path), mode)
    except IOError:
        e = None
        if e.errno == errno.ENAMETOOLONG:
            safe_chdir(local_path)
            None(None, None)
            del e
            return None
        with None:
            if not None:
                pass
        raise 
        None = None
        del e



def dir_safe_read_attributes(fs, local_path):
    f = _safe_open_file(fs, local_path, 'r')
    None(None, None)
    return 
    with None:
        if not None, Attributes.unmarshal(f.read()):
            pass


def dir_safe_write_attributes(fs, attr, local_path):
    attr_file = _dir_safe_filename(local_path)
# WARNING: Decompyle incomplete

read_preserved_attributes = (lambda attr_handle, local_path = (None,): pass# WARNING: Decompyle incomplete
)()
_read_preserved_attributes = (lambda attr_handle = None, local_path = contextmanager: MAX_ERROR_DATA_LENGTH = 1024try:
preserved_attr_handle = attr_handle.open_preserved('r')except Exception:
e = Noneif fsutil.is_file_not_found_exception(e):
del eNoneNone = Nonedel etry:
buf = preserved_attr_handle.read()unserialized_dict = unserialize_attr_dict(buf)try:
preserved_attr_handle.close()unserialized_dictexcept zlib.error:
e = Noneerr_data = buf if len(buf) < MAX_ERROR_DATA_LENGTH else buf[MAX_ERROR_DATA_LENGTH:]trace_stack()TRACE('attr_decompress_failed: data=%s, data_len=%s, error=%s, local_path=%r', base64.b64encode(err_data), len(buf), repr(e), local_path)raise RetryException(inner = e)e = Nonedel eexcept Exception:
report_exception(component = DesktopComponent.SYNC_ENGINE)try:
preserved_attr_handle.close()Nonetry:
passexcept:
preserved_attr_handle.close())()

class AttrsNotSupportedException(Exception):
    pass

open_attributes_handle_context = (lambda fs = None, local_path = None, open_dir_handle = contextmanager: pass# WARNING: Decompyle incomplete
)()

def _read_single_platform(attr_handle, plat, whitelist, block_handler, max_inline_attr_size):
    pass
# WARNING: Decompyle incomplete


def _read_preserved_attrs_dict(unserialized_dict, whitelist, extra_preserved_whitelist):
    attr_dict = { }
# WARNING: Decompyle incomplete


def read_attributes(attr_handle, local_path, block_handler = None, whitelist = None, max_inline_attr_size = None, read_preserved = (None, None, None, None, True, None), extra_preserved_whitelist = ('attr_handle', 'AbstractAttributesHandle', 'local_path', 'Optional[LocalPath]', 'block_handler', 'Optional[BlockHandler]', 'whitelist', 'Optional[AttrsWhitelist]', 'max_inline_attr_size', 'Optional[int]', 'read_preserved', 'bool', 'extra_preserved_whitelist', 'Optional[AttrsWhitelist]', 'return', 'Attributes')):
    attr_dict = { }
    data_plats = set()
    if read_preserved:
        unserialized_dict = read_preserved_attributes(attr_handle, local_path)
        if unserialized_dict:
            preserved_dict = _read_preserved_attrs_dict(unserialized_dict, whitelist, extra_preserved_whitelist)
            if preserved_dict:
                attr_dict.update(preserved_dict)
        None(None, None)
    else:
        with None:
            if not None:
                pass
# WARNING: Decompyle incomplete


def fix_finderinfo_icon_bit_conflict(fs = None, attr_handle = None, data = None):
    if IS_MAC and len(data) == FINDER_INFO_BLOB_BYTE_SIZE and fsutil.is_directory(fs, attr_handle.path):
        
        try:
            local_xattr = MacFinderInfoHelper.load_or_create_finderinfo_xattr(fs, attr_handle.path)
            local_bit_enabled = MacFinderInfoHelper.is_finderinfo_custom_icon_enabled(local_xattr)
            remote_bit_enabled = MacFinderInfoHelper.is_finderinfo_custom_icon_enabled(data)
            if local_bit_enabled == remote_bit_enabled:
                return data
            data = MacFinderInfoHelper.change_icon_bit_in_xattr(data, local_bit_enabled)
        except PermissionDeniedError:
            pass
        except Exception:
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.SYNC_ENGINE)

        return data


def is_attrs_unsupported_exception(exc = None):
