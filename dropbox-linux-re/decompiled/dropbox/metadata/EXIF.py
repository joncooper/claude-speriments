# Source Generated with Decompyle++
# File: EXIF.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import plistlib
import struct
from collections import defaultdict
from typing import Any, cast, Dict, IO, List, Optional, Set, Tuple, Union
import six
from six import iteritems
from six.moves import range
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import make_str

def make_string(seq = None):
    str = b''
    for c in seq:
        if 32 <= c and c < 256:
            str += six.int2byte(c)
        if not str:
            return seq
        return None


def make_string_uc(seq = None):
    seq = seq[8:]
    return make_string(seq)


def int_at_index(buf = None, idx = None):
    return buf[idx]


def byte_at_index(buf = None, idx = None):
    return six.int2byte(buf[idx])

GLOBAL_WHITELIST = (b'ExifOffset', b'EXIF MakerNote', b'InteroperabilityOffset', b'GPSInfo', b'Image Make', b'Thumbnail Compression', b'Thumbnail JPEGInterchangeFormat')
FIELD_TYPES = ((0, b'X', b'Proprietary'), (1, b'B', b'Byte'), (1, b'A', b'ASCII'), (2, b'S', b'Short'), (4, b'L', b'Long'), (8, b'R', b'Ratio'), (1, b'SB', b'Signed Byte'), (1, b'U', b'Undefined'), (2, b'SS', b'Signed Short'), (4, b'SL', b'Signed Long'), (8, b'SR', b'Signed Ratio'))
# WARNING: Decompyle incomplete
