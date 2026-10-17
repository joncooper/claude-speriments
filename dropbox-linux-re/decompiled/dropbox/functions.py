# Source Generated with Decompyle++
# File: functions.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import base64
import collections
import collections.abc as collections
import datetime
import functools
import hashlib
import itertools
import json
import math
import os
import platform
import random as insecure_random
import re
import sys
import threading
import time
from collections import OrderedDict
from collections.abc import MutableMapping
from contextlib import suppress
from typing import AbstractSet, Any, AnyStr, Callable, cast, DefaultDict, Dict, Generic, Iterable, Iterator, KeysView, List, Mapping, Match, Optional, Sequence, SupportsInt, Text, Tuple, TypeVar, Union, ValuesView
import six
from six import iteritems
from six.moves import filterfalse, zip
from six.moves.queue import Empty, Queue
from dropbox.client.cloud_docs.extension_constants import LOGGING_WHITELISTED_EXTS
from dropbox.platform import IS_MAC, IS_WINDOWS
if IS_MAC:
    from macffi.System import sysctl
MYPY = False
if MYPY:
    from dropbox.client.installer_tag import InstallerTag
    from dropbox.shared.local_path import LocalPath
MYPY = False
_T = TypeVar('_T')
_S = TypeVar('_S')
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')
_UCS4_PYTHON = len('ð €') == 1
EitherStr = Union[(bytes, Text)]
_SURROGATE_PAIR_EXPR = re.compile('[í €-í¿¿]')
_SURROGATE_PAIR_EXPR_WIDE = re.compile('[ð€€-ô¿¿]') if _UCS4_PYTHON else _SURROGATE_PAIR_EXPR

def cmp(left = None, right = None):
    return (left > right) - (left < right)


def make_unicode(buf = None, encoding = None, errors = None):
    pass
# WARNING: Decompyle incomplete


def make_bytes(buf = None, encoding = None, errors = None):
    if isinstance(buf, bytes):
        return buf
    return None.encode(encoding if encoding else 'utf-8', errors)


def make_str(buf = None, encoding = None, errors = None):
    return make_unicode(buf, encoding, errors)


def is_four_byte_unicode(t = None):
