# Source Generated with Decompyle++
# File: fanotify_manager.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import subprocess
import sys
import tempfile
import textwrap
from hashlib import sha256
from typing import Any, BinaryIO, List, Optional, Text
from build_number import dropbox_version
from lib.linuxinfinite.fanotify_listener_version import CURRENT_LISTENER_HASH, CURRENT_LISTENER_SIZE
from dropbox.client.system_authorization import request_authorization_from_user_and_run
from dropbox.i18n import safe_activate_translation
from dropbox.infinite import InfiniteReleaseChannel
from dropbox.infinite.blacklist import InfiniteModuleBlacklist
from dropbox.infinite.kernel_component_manager import KernelComponentManager
from dropbox.infinite.pager import PagerNotLoadedError
from dropbox.trace import TRACE
MYPY = False
if MYPY and sys.platform.startswith('win'):
    _listener_locations_uid = 0
else:
    _listener_locations_uid = os.getuid()
LISTENER_LOCATIONS = [
    '/var/lib/dropbox/%(build_key)s_%(uid)s' % dict(uid = _listener_locations_uid, build_key = dropbox_version.key)]

def find_dropbox_dist_path():
    path = os.path.abspath(__file__)
# WARNING: Decompyle incomplete


def hash_file(f = None):
    hasher = sha256()
    file_contents = f.read(4096)
    if not file_contents:
        pass
    else:
        hasher.update(file_contents)
    return hasher.hexdigest()


def hash_path(path = None):
    f = open(path, 'rb')
    None(None, None)
    return 
    with None:
        if not None, hash_file(f):
            pass


def is_current_listener(path = None):
    st = os.stat(path)
    if st.st_size != CURRENT_LISTENER_SIZE:
        return False
    if hash_path(path) != CURRENT_LISTENER_HASH:
        return False


def get_listeners_installed():
    listener_paths = []
    for path in LISTENER_LOCATIONS:
        infinite_path = os.path.join(path, 'dropbox-infinite')
        if os.access(infinite_path, os.R_OK | os.X_OK):
            listener_paths.append(infinite_path)
        return listener_paths


def get_current_listener_path():
    listener_paths = get_listeners_installed()
    for path in listener_paths:
        if is_current_listener(path):
            
            return None, path
        return None


def is_current_listener_installed():
    for path in get_listeners_installed():
        if is_current_listener(path):
            return True
        return False


class FanotifyManager(KernelComponentManager):
    try_install = True
    
    def __init__(self = None, release_channel = None):
        self._release_channel = release_channel

    
    def enable_kernel_components_if_needed(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def disable_kernel_components_if_needed(self = None):
        pass

    
    def log_kernel_memory_usage(self = None):
        pass

    _kernel_components_compatible = (lambda module_blacklist = None: True)()
    
    def is_running(self = None):
        return False

    
    def is_installed(self = None):
        return False

    
    def report_kernel_components_status(self = None):
        pass

    
    def on_quit(self = None, *n, **kw):
        pass

    install_fanotify_listener = (lambda cls = None: if not cls.try_install:
raise PagerNotLoadedError('Installation already failed --- not retrying.')if MYPY and sys.platform.startswith('win'):
our_listener_dir = ''our_tgz = ''# WARNING: Decompyle incomplete
)()

