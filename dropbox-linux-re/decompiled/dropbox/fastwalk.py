# Source Generated with Decompyle++
# File: fastwalk.pyc (Python 3.11)

from __future__ import absolute_import
import collections
import errno
import functools
import itertools
import operator
import sys
from typing import Iterator, Text
from dropbox.assertions import assert_
from dropbox.components.desktop_components import DesktopComponent
from dropbox.dirtraverse.common import DirectoryModifiedError
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import run_iterable_in_c
from dropbox.platform import IS_WINDOWS
from dropbox.shared.util import identity
from dropbox.sync_engine_boundary.file_system_constants import FILE_TYPE_DIRECTORY, FILE_TYPE_POSIX_SYMLINK, FILE_TYPE_UNKNOWN
from dropbox.trace import TRACE
if IS_WINDOWS:
    from dropbox.win32.internal import is_junction_point

def is_cyclic(pelt, new_pstat):
    pass
# WARNING: Decompyle incomplete


def is_file_not_found_exception(e):
