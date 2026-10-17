# Source Generated with Decompyle++
# File: honeypot.pyc (Python 3.11)

import errno
import os
import shutil
from typing import Any, List, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.shared.local_path import LocalPath
from dropbox.shared.placeholder_details import PlaceholderDetails
from dropbox.sync_engine_boundary.file_system_exceptions import FileSystemError
from dropbox.trace import TRACE
HONEYPOT_FILE_EXTENSIONS: 'List[Text]' = [
    'aep',
    'dmg',
    'doc',
    'inf',
    'jpeg',
    'lnk',
    'm4a',
    'mpg',
    'py',
    'tmp',
    'url',
    'wav',
    'xlsx',
    'xml',
    'zip']
if IS_WINDOWS:
    HONEYPOT_FILE_EXTENSIONS += []
elif IS_MAC:
    HONEYPOT_FILE_EXTENSIONS += []
elif IS_LINUX:
    HONEYPOT_FILE_EXTENSIONS += []
FileSystem = Any

def create_honeypot_placeholder_files(account = None, fs = None):
    honeypot_path = honeypot_container_path(account, fs)
# WARNING: Decompyle incomplete


def _create_single_honeypot_placeholder(account = None, fs = None, placeholder_path = None):
    placeholder_details = PlaceholderDetails(ns = -1, sjid = -1, user_id = account.uid, fileid = b'i', fileid_rev = 1)
    
    try:
        if fs.is_infinite_placeholder(placeholder_path):
            return None
    except FileSystemError:
        e = None
        TRACE('!! Error checking a honeypot placeholder; proceeding with recreation %r', e)
        e = None
        del e
    except:
        e = None
        del e

    
    try:
        os.unlink(placeholder_path.to_unicode())
    except OSError:
        e = None
        if e.errno == errno.ENOENT:
            pass
        e = None
        del e
    except:
        e = None
        del e

    
    try:
        fs.create_infinite_placeholder(placeholder_path, 1024, placeholder_details)
        return None
    except FileSystemError:
        e = None
        TRACE('!! Cannot create honeypot placeholder file %r', e)
        e = None
        del e
        return None
        e = None
        del e



def is_path_in_honeypot(account = None, fs = None, path = None):
