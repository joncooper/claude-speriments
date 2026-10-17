# Source Generated with Decompyle++
# File: sync_engine_util.pyc (Python 3.11)

from __future__ import absolute_import
import fnmatch
import os
import re
from constants import IGNORED_FILES, UNWATCHED_FILE_PATTERNS
from dropbox.client_api.hashing import is_valid_blocklist
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.functions import is_four_byte_unicode
from dropbox.nfcdetector import is_nfc
from dropbox.platform import IS_WINDOWS
from dropbox.shared.util import db_lower
from dropbox.sync_engine_boundary.exceptions import BlockContentsBadDataError, BlockContentsError, BlockContentsNotFoundError, SyncEngineStoppedError
from dropbox.sync_engine_boundary.sync_engine_util.interface import SyncEngineUtilInterface

class AttributeMergeError(Exception):
    pass


class ConflictedPathInfo(object):
    
    def __init__(self):
        self.local_path = None



def add_sig_and_check(hashes_to_prune, sigstore, sha1_digest, s):
    pass

_UNWATCHED_RE = UNWATCHED_FILE_PATTERNS()
_TEMP_RE = list(_UNWATCHED_RE)
if IS_WINDOWS:
    _TEMP_RE.append(re.compile('^[0-9a-fA-F]{8}$'))
    _TEMP_RE.append(re.compile('^sw[0-9]{4}$'))
_TEMP_RE.append(re.compile('^(A|a)bleton(T|t)mp-[0-9]{4}$'))
_TEMP_RE.append(re.compile('^.*\\.(tmp|TMP)$'))

def is_temp_file(filename):
    pass
# WARNING: Decompyle incomplete


def update_temp_regex(regex_list):
    global _TEMP_RE
    
    try:
        temp_file_re_list = list(_UNWATCHED_RE)
        for rex in regex_list:
            temp_file_re_list.append(re.compile(rex))
            _TEMP_RE = temp_file_re_list
            return None
            except re.error:
                report_exception(component = DesktopComponent.SYNC_ENGINE)
                return None



def is_watched_filename(filename, isdir = (False,)):
    pass
# WARNING: Decompyle incomplete


def is_malformed_entry(server_path, blocklist):
