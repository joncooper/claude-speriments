# Source Generated with Decompyle++
# File: posix.pyc (Python 3.11)

from __future__ import absolute_import
import os
import stat
import sys
import tempfile
from functools import partial
from re import match
from typing import Callable, Optional, Text
from dropbox.client.system_authorization import request_authorization_from_user_and_run
from dropbox.client.util import get_contents_root
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.fastwalk_bridge import fastwalk
from dropbox.fileutils import check_perms
from dropbox.functions import EitherStr, make_unicode
from dropbox.gui import message_sender, spawn_thread_with_name
from dropbox.i18n import safe_activate_translation, trans
from dropbox.platform import IS_MAC
from dropbox.sync_engine_boundary.constants import FixPermissionStatus
from dropbox.trace import TRACE
MYPY = False
fileprovider_fix_ownership_in_a_thread = (lambda path = None: fileprovider_fix_ownership(path))()

def fileprovider_fix_ownership(path = None):
    permission_fixer_path = os.path.join(get_contents_root(), 'MacOS', 'permission_fixer')
    safe_activate_translation()
    msg = trans('Dropbox needs to change permissions for the Folder: %(folder_name)s') % {
        'folder_name': path }
    if MYPY and sys.platform.startswith('win'):
        uid = 0
    else:
        uid = os.getuid()
    f = request_authorization_from_user_and_run(permission_fixer_path, [
        path,
        str(uid)], msg + '\n\n')
    if f:
        
        try:
            TRACE('FP Permission Fix for %r: %r', path, f.read())
            
            try:
                f.close()
                TRACE('Successfully fixed FP permissions')
                return None
            except Exception:
                report_exception(component = DesktopComponent.SYNC_ENGINE)
                return None
                f.close()
                TRACE('Successfully fixed FP permissions')
                except Exception:
                    report_exception(component = DesktopComponent.SYNC_ENGINE)
                return None




def fix_perm_on_directory(path = None, required_perms = None, recursive = None, msg = ('rwX', False, None)):
    temp_file = tempfile.NamedTemporaryFile()
    if MYPY and sys.platform.startswith('win'):
        uid = 0
    else:
        uid = os.getuid()
    temp_file.write(('#!/bin/bash\nchown -h %(rec_opts)s %(uid)s "%(rootdir)s"\nchmod %(opts)s %(rec_opts)s u+%(perms)s "%(rootdir)s"\necho Done' % dict(uid = uid, rootdir = path, pid = os.getpid(), perms = required_perms, opts = '-h' if not IS_MAC and recursive else '', rec_opts = '-R' if recursive else '')).encode(sys.getfilesystemencoding()))
    temp_file.flush()
    safe_activate_translation()
    if not msg:
        msg = trans('Dropbox needs to change permissions for the Folder: %(folder_name)s') % {
            'folder_name': path }
    f = request_authorization_from_user_and_run('/bin/sh', [
        temp_file.name], msg + '\n\n')
    if f:
        TRACE('Permission Fix for %r: %r', path, f.read())
        f.close()
    else:
        except Exception:
            report_exception(component = DesktopComponent.FILE_LOCKING)
        except Exception:
            report_exception(component = DesktopComponent.FILE_LOCKING)
        None(None, None)
        return None
    with None:
        if not None:
            pass


def _check_perms_for_one_path(path, required_perms):
    required_perms = os.R_OK | os.W_OK
    if os.access(path, required_perms):
        
        try:
            mode = os.lstat(path)[stat.ST_MODE]
        except OSError:
            return False

        if mode & stat.S_IRUSR and mode & stat.S_IWUSR:
            return True
        return None
    return False


def fix_perms_without_prompt_if_needed(path = None, validate_perms = None, required_perms = None):
    path = make_unicode(path)
    if not os.access(path, os.F_OK):
        return FixPermissionStatus.NOTEXIST
    if validate_perms(path, required_perms):
        return FixPermissionStatus.NOTNEEDED
    
    try:
        _do_fix_perms(required_perms, path)
    except Exception:
        TRACE('Failed to fix permission for: %r', path)

    if validate_perms(path, required_perms):
        return FixPermissionStatus.SUCCESS
    return None.FAILED


def _fix_perms(path, validate_perms, required_perms, follow_symlinks = (check_perms, 'rwX', False)):
    pass
# WARNING: Decompyle incomplete


def check_and_fix_permissions(path = None):
    
    try:
        if check_perms(path, first_time = True, follow_symlinks = True):
            return True
        validate_fn = partial(check_perms, follow_symlinks = True)
        return _fix_perms(path, validate_perms = validate_fn, follow_symlinks = True)
    except Exception:
        report_exception(component = DesktopComponent.FILE_LOCKING)
        return False


fix_whole_dropbox_permissions_in_a_thread = (lambda root_mount_path = None: fix_whole_dropbox_permissions(root_mount_path))()

def fix_whole_dropbox_permissions(root_mount_path = None):
    pass
# WARNING: Decompyle incomplete


def _do_fix_perms(mod_str, path):
    lstat_res = os.lstat(path)
    if IS_MAC:
        cur_flags = lstat_res.st_flags
        new_flags = cur_flags
        if new_flags & stat.UF_IMMUTABLE:
            new_flags = new_flags - stat.UF_IMMUTABLE
        if new_flags & stat.UF_APPEND:
            new_flags = new_flags - stat.UF_APPEND
        if new_flags != cur_flags:
            os.chflags(path, new_flags)
    newmode = lstat_res[stat.ST_MODE]
    mode = lstat_res[stat.ST_MODE]
    for char in mod_str:
        if char == 'r':
            newmode |= stat.S_IRUSR
            continue
        if char == 'w':
            newmode |= stat.S_IWUSR
            continue
        if char == 'x':
            newmode |= stat.S_IXUSR
            continue
        if char == 'X':
            if stat.S_ISDIR(mode) and mode & stat.S_IXGRP or mode & stat.S_IXOTH:
                newmode |= stat.S_IXUSR
        if newmode != mode:
            os.chmod(path, newmode)
            return None
        return None


def show_perms(path = None):
    permission_list = [
        'S_IRUSR',
        'S_IWUSR',
        'S_IXUSR',
        'S_IRGRP',
        'S_IWGRP',
        'S_IXGRP',
        'S_IROTH',
        'S_IWOTH',
        'S_IXOTH']
    perm_values = 'rwx'
    rv = '-'
    
    try:
        mode = os.stat(path).st_mode
    except Exception:
        return 'unable to read permissions'

    if stat.S_ISDIR(mode):
        rv = 'd'
    for i, perm_name in enumerate(permission_list):
        perm_value = getattr(stat, perm_name)
        if perm_value & mode == perm_value:
            rv += perm_values[i % 3]
            continue
        rv += '-'
        return rv

