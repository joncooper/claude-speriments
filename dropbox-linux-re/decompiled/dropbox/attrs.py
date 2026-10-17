# Source Generated with Decompyle++
# File: attrs.pyc (Python 3.11)

from __future__ import absolute_import
import base64
import itertools
import json
import os
import zlib
from io import BytesIO
from typing import AbstractSet, Any, Callable, cast, Dict, IO, List, Mapping, Optional, Set, Text, Tuple, Type, Union
import six
from six import iteritems, iterkeys
from dropbox.client_api.hashing import BetterDropboxHasher, DROPBOX_MAX_BLOCK_SIZE, split_blocklist
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.functions import EitherStr, frozendict, make_bytes, make_unicode
from dropbox.shared.util import safe_navigate
from dropbox.threading import Lock
from dropbox.trace import is_debugging, TRACE
BLOCKABLE_INLINE_CUT_OFF = 0
BLOCKABLE_DEFAULT = 1
BLOCKABLE_BLOCKLIST_IF_TOO_LARGE = 1
BLOCKABLE_BLOCKLIST_ALWAYS = 2
FILE_TAG_PLAT = 'dropbox_tag'
FILE_TAG_GID_V3_ATTR = 'file_tag_gid_v3'
SERVER_FILEID_PLAT = 'dropbox_file_id'
SERVER_FILEID_KEY = 'file_id_rev'
DROPBOX_MUTE_PLAT = 'dropbox_mute'
DROPBOX_MUTE_KEY_ATTR = 'mute_key'
DROPBOX_MUTE_ATTR = 'mute'
DROPBOX_SYMLINK_PLAT = 'dropbox'
AttrPlatDictValueDict = Dict[(Text, Union[(str, Text, int)])]
AttrPlatDict = Dict[(Text, AttrPlatDictValueDict)]
AttrDict = Dict[(Text, AttrPlatDict)]

class CorruptedAttributeError(Exception):
    pass


class ChangingAttributeError(Exception):
    pass


class AllowAllWhitelist(object):
    
    def __getitem__(self = None, key = None):
        return AllowAllWhitelist()

    
    def __contains__(self = None, key = None):
        return True



def mute_attr_set(attrs = None):
    pass
# WARNING: Decompyle incomplete


def get_attrs_blocklist(attr = None):
    l = []
# WARNING: Decompyle incomplete


def is_attrs_subset(attrs_a = None, attrs_b = None):
    for plat_key, plat_dict in iteritems(attrs_a.attr_dict):
        attrs_b_plat_dict = attrs_b.attr_dict[plat_key]
        for attr_key, attr_value in iteritems(plat_dict):
            attrs_b_attr_value = attrs_b_plat_dict[attr_key]
            if attrs_b_attr_value != attr_value:
                return False
            except KeyError:
                return False
            except KeyError:
                return False
            return True


def unserialize_attr_dict(buf = None):
    if buf:
        return json.loads(make_unicode(zlib.decompress(buf)))


def serialize_attr_dict(attr = None, data_plats = None, only = None, extra_attrs = (None, None, None)):
    pass
# WARNING: Decompyle incomplete


def serialize_attr_dict_only(attr_dict = None, only = None, extra_attrs = None):
    buf = dict(attr_dict)
# WARNING: Decompyle incomplete


def attr_dict_filter_whitelist(attrs_dict = None, whitelist = None):
    pass
# WARNING: Decompyle incomplete


def convert_attr_data(raw_attr_fh = None, max_inline_attr_size = None, block_handler = None, blockable = (None, None, BLOCKABLE_DEFAULT)):
    raw_attr_fh.seek(0, os.SEEK_END)
    attr_length = raw_attr_fh.tell()
    raw_attr_fh.seek(0, os.SEEK_SET)
# WARNING: Decompyle incomplete


def dropboxize_raw_attrs_dict(attrs_dict = None, whitelist = None, max_inline_attr_size = None, block_handler = (None, 4096, None)):
    new_dict = { }
# WARNING: Decompyle incomplete


def _split_metadata_key(full_key = None):
    
    try:
        (key, num) = full_key.split(',')
        return key
    except ValueError:
        pass

    return full_key


def attr_dict_from_whitelist(attr_handle = None, _platform = None, whitelist = None, max_inline_attr_size = (None, 4096, None), block_handler = ('attr_handle', 'Dict[Text, Union[Text, bytes]]', '_platform', 'Text', 'whitelist', 'Optional[AttrDict]', 'max_inline_attr_size', 'int', 'block_handler', 'Optional[Callable[[bytes, bytes], None]]', 'return', 'AttrPlatDict')):
    return dropboxize_raw_attrs_dict({
        _platform: attr_handle }, whitelist = whitelist, max_inline_attr_size = max_inline_attr_size, block_handler = block_handler).get(_platform, frozendict())


def get_attr_data(attr_data = None, get_contents = None):
    pass
# WARNING: Decompyle incomplete


def convert_attr_dict(dict_constructor = None, attr_dict = None):
    pass
# WARNING: Decompyle incomplete


def make_frozen_attr_dict(attr_dict = None):
    return convert_attr_dict(frozendict, attr_dict)


def unfreeze_attr_dict(frozen_attr_dict = None):
    return convert_attr_dict(dict, frozen_attr_dict)


def has_file_tag_gid_v3(attrs = None):
    return safe_navigate(attrs.attr_dict, FILE_TAG_PLAT, FILE_TAG_GID_V3_ATTR)


def copy_key_if_exists_in_both(from_attrs = None, to_attrs = None, platform = None, key = ('from_attrs', 'Attributes', 'to_attrs', 'Attributes', 'platform', 'Text', 'key', 'Text', 'return', 'Attributes')):
    if from_attrs.lookup_key(platform, key) and to_attrs.lookup_key(platform, key):
        new_attr_dict = dict(to_attrs.attr_dict)
        plat_dict = dict(new_attr_dict[platform])
        plat_dict[key] = from_attrs.attr_dict[platform][key]
        new_attr_dict[platform] = plat_dict
        return to_attrs.copy(attr_dict = new_attr_dict)


def copy_file_tag_gid_v3(from_attrs = None, to_attrs = None):
    return copy_key_if_exists_in_both(from_attrs, to_attrs, FILE_TAG_PLAT, FILE_TAG_GID_V3_ATTR)


def copy_server_fileid(from_attrs = None, to_attrs = None):
    return copy_key_if_exists_in_both(from_attrs, to_attrs, SERVER_FILEID_PLAT, SERVER_FILEID_KEY)

UNDERIVABLE_ATTRS = {
    'dropbox_mute': set([
        'mute',
        'mute_key']) }

def filter_underivable_attrs(attrs = None):
    pass
# WARNING: Decompyle incomplete


class Attributes(object):
    __slots__ = ('data_plats', 'attr_dict')
    singleton_lock = Lock()
    singletons: 'Dict[str, Attributes]' = { }
    
    def __init__(self = None, attr_dict = None, data_plats = None):
        if not hasattr(self, 'attr_dict'):
            self.attr_dict = make_frozen_attr_dict(attr_dict)
        if not hasattr(self, 'data_plats'):
            self.data_plats = frozenset(data_plats)
            return None

    __singleton = (lambda cls, key, attr_dict, data_plats: pass# WARNING: Decompyle incomplete
)()
    
    def __new__(cls, attr_dict, data_plats = (frozendict(), frozenset())):
        if not attr_dict and data_plats:
            return cls.__singleton(cls, attr_dict, data_plats)
        if not None:
            data_plats = frozenset(data_plats)
            return cls.__singleton(data_plats, attr_dict, data_plats)
        return None.__new__(cls)

    
    def __repr__(self = None):
        return f'''Attributes({self.attr_dict!r},{self.data_plats!r})'''

    
    def __eq__(self = None, other = None):
