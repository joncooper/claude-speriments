# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from __future__ import absolute_import
import heapq
import html
import operator
from functools import reduce
from typing import Any, Callable, Dict, Iterable, Iterator, List, Mapping, Optional, Reversible, Set, Text, Tuple, TypeVar, Union
from six import iteritems
from six.moves import filter, map
from dropbox.shared.local_path import LocalPath
from dropbox.shared.quota_info import QuotaEntityData, QuotaInfo
from dropbox.shared.server_path import RRLowerServerPath, ServerPath
AnyPath = TypeVar('AnyPath', Text, LocalPath, ServerPath)
_T = TypeVar('_T')
_S = TypeVar('_S')
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')

class WrapCall(object):
    
    def __init__(self = None, obj = None, new_f = None):
        object.__setattr__(self, '_obj', obj)
        object.__setattr__(self, '_f', new_f)

    
    def __getattr__(self = None, name = None):
        return getattr(self._obj, name)

    
    def __setattr__(self = None, name = None, value = None):
        return setattr(self._obj, name, value)

    
    def __call__(self = None, *n, **kw):
        pass
    # WARNING: Decompyle incomplete



def identity(x = None):
    return x


def const(c = None):
    pass
# WARNING: Decompyle incomplete


class _undefined(object):
    
    def __bool__(self = None):
        raise TypeError('Tried to cast `undefined` to a boolean')

    __nonzero__ = __bool__

undefined = _undefined()

def head(l = None, d = None):
    pass
# WARNING: Decompyle incomplete


def tail(l = None, d = None):
    pass
# WARNING: Decompyle incomplete


class container(object):
    
    def __init__(self, **kw):
        for k, v in iteritems(kw):
            setattr(self, k, v)
            return None

    
    def __repr__(self):
        pass
    # WARNING: Decompyle incomplete



def propagate_none(fn = None, val = None):
    pass
# WARNING: Decompyle incomplete


class RuntimeMixin(object):
    
    def __init__(self, inner):
        self.inner = inner

    
    def __getattr__(self, key):
        return getattr(self.inner, key)

    
    def __enter__(self, *n, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def __exit__(self, *n, **kw):
        pass
    # WARNING: Decompyle incomplete



class OverrideRepr(RuntimeMixin):
    
    def __init__(self, inner, new_repr):
        self.inner = inner
        self.repr = new_repr

    
    def __repr__(self):
        return self.repr



def wrap_tuple(iterable = None):
    return iterable()


def select(needle = None, haystack = None, key = None):
    for item in haystack:
        if key(needle) == key(item):
            
            return None, item
        return None


def find(f = None, iterable = None):
    for item in iterable:
        if f(item):
            
            return None, item
        return None


def safe_navigate(dictionary = None, *keys):
    
    try:
        for key in keys:
            dictionary = dictionary[key]
            return dictionary
            except (KeyError, TypeError):
                return None



def map_maybe(f = None, iterable = None):
    return list(filter((lambda x: x is not None), map(f, iterable)))


def map_keys(f = None, dictionary = None):
    pass
# WARNING: Decompyle incomplete


def merge_sorted(*iterables, **options):
    pass
# WARNING: Decompyle incomplete


def zip_dicts(*dictionaries):
    pass
# WARNING: Decompyle incomplete


def restrict_keys(dictionary = None, *keys):
    pass
# WARNING: Decompyle incomplete


def _parse_quota_block(quota_info_block = None, quota_type = None):
    info_block = quota_info_block[quota_type]
    in_use = info_block['in_use']
    quota = info_block['quota']
    display_quota = info_block.get('display_quota')
    return QuotaEntityData(data_in_use = in_use, sync_quota = quota, display_quota = display_quota)


def get_quota_and_in_use(response_with_quota_info = None):
    if 'quota_info' in response_with_quota_info:
        quota_info_block = response_with_quota_info['quota_info']
        if 'user' in quota_info_block:
            quota_entity_data = _parse_quota_block(quota_info_block, 'user')
            quota = quota_entity_data.sync_quota
            in_use = quota_entity_data.data_in_use
        elif 'team' in quota_info_block:
            quota_entity_data = _parse_quota_block(quota_info_block, 'team')
            quota = quota_entity_data.sync_quota
            in_use = quota_entity_data.data_in_use
        else:
            raise KeyError('user and team both missing from quota-info')
    quota = response_with_quota_info['quota']
    in_use = response_with_quota_info['in_use']
    return (in_use, quota)


def parse_quota_info_from_list(response_with_quota_info = None):
    if 'quota_info' in response_with_quota_info:
        quota_info_block = response_with_quota_info['quota_info']
        if 'total_team' in quota_info_block:
            root_quota_entity_data = _parse_quota_block(quota_info_block, 'user')
            home_quota_entity_data = None
            team_quota_entity_data = _parse_quota_block(quota_info_block, 'total_team')
        elif 'team' in quota_info_block:
            root_quota_entity_data = _parse_quota_block(quota_info_block, 'team')
            if 'user' in quota_info_block:
                home_quota_entity_data = _parse_quota_block(quota_info_block, 'user')
            else:
                home_quota_entity_data = None
            team_quota_entity_data = None
        else:
            root_quota_entity_data = _parse_quota_block(quota_info_block, 'user')
            home_quota_entity_data = None
            team_quota_entity_data = None
    else:
        root_data_in_use = response_with_quota_info['in_use']
        root_quota = response_with_quota_info['quota']
        root_quota_entity_data = QuotaEntityData(data_in_use = root_data_in_use, sync_quota = root_quota)
        home_quota_entity_data = None
        team_quota_entity_data = None
    return QuotaInfo(root_entity_data = root_quota_entity_data, home_entity_data = home_quota_entity_data, team_entity_data = team_quota_entity_data)


def safe_access(obj = None, attr = None):
    if obj:
        return getattr(obj, attr)


def apply_home_change_to_ignore_set(old_ignore_set = None, old_home_path = None, new_root_ns_id = None, new_home_path = ('old_ignore_set', 'Iterable[Text]', 'old_home_path', 'Text', 'new_root_ns_id', 'int', 'new_home_path', 'Text', 'return', 'Set[Text]')):
    if not old_home_path.endswith('/'):
        old_home_path += '/'
    old_home_path = db_lower(old_home_path)
    if not new_home_path.endswith('/'):
        new_home_path += '/'
    new_home_path = db_lower(new_home_path)
    new_ignore_set = set()
    for rr_path in old_ignore_set:
        server_path = RRLowerServerPath(rr_path)
        rel = server_path.rel
        starts_with_old_home_path = rel.startswith(old_home_path)
        if starts_with_old_home_path:
            rel = rel.replace(old_home_path, new_home_path, 1)
        if starts_with_old_home_path or server_path.ns == new_root_ns_id:
            new_ignore_set.add(Text(RRLowerServerPath.from_ns_rel(new_root_ns_id, rel).db_lower()))
        return new_ignore_set


class Closeable(object):
    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, *n, **kw):
        self.close()

    
    def close(self = None):
        raise NotImplementedError



def db_lower(val = None):
    fastpath_db_lower = db_lower
    import fastpath
    return fastpath_db_lower(val)


def format_html(format = None, **kwargs):
    html_escaped_dict = dict()
    for k, v in iteritems(kwargs):
        html_escaped_dict[k] = html.escape(v) if isinstance(v, str) or isinstance(v, Text) else v
        return format % html_escaped_dict


def format_text(format = None, **kwargs):
    return format % kwargs


def merge_dicts(first = None, second = None):
    merged = first.copy()
    merged.update(second)
    return merged

