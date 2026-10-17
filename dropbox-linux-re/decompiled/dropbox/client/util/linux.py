# Source Generated with Decompyle++
# File: linux.pyc (Python 3.11)

from __future__ import absolute_import, print_function
import collections
import errno
import fcntl
import functools
import os
import platform
import re
import signal
import struct
import subprocess
import sys
import time
from typing import Any, Dict, Iterable, Iterator, List, Optional, Text, Tuple
import psutil
from apex.auto_updater import get_updater_id
from six import iteritems
from six.moves import range
from build_number import BUILD_KEY, is_frozen
from dropbox.fsutil import fsutil
from dropbox.client.cli import get_existing_control_thread
from dropbox.client.notifications.loud_notifications.types import BubbleContextRef
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.runtime import Interpreter
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.functions import make_bytes, make_unicode, natural_sort_cmp as natural_basename_sort_cmp, synchronized
from dropbox.linux.internal import executable
from dropbox.threading import Lock
from dropbox.trace import TRACE
from dropbox.xattrs import xattr
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
PROC_NAME = BUILD_KEY.lower()
PROC_NAME_PY3 = PROC_NAME + '_py3'

def get_fs_type(path = None):
    pass
# WARNING: Decompyle incomplete


def copy_text_to_clipboard_external(text):
    control_thread = get_existing_control_thread()
# WARNING: Decompyle incomplete


def get_text_from_clipboard_external():
    pass


def hard_exit_unwatched(exit_code = None):
    pass
# WARNING: Decompyle incomplete


def raise_application():
    pass


def running_dropbox_instances():
    return running_instances([
        PROC_NAME,
        PROC_NAME_PY3])


def running_instances(process_names = None):
    pass
# WARNING: Decompyle incomplete


def get_clean_env():
    env = dict(os.environ)
    env['PATH'] = '/sbin:/bin'
    return env


def get_drives():
    
    try:
        output = subprocess.Popen([
            'mount',
            '-v'], stdout = subprocess.PIPE, env = get_clean_env()).communicate()[0]
        lines = output.split(b'\n')()
        return lines()
    except Exception:
        report_exception(component = DesktopComponent.UNKNOWN)
        return 



def kill_other_instances():
    success = True
    for pid in running_dropbox_instances():
        TRACE('Killing %s', pid)
        os.kill(pid, signal.SIGKILL)
        except Exception:
            success = False
            report_exception(component = DesktopComponent.UNKNOWN)
            continue
        return success


def clear_fs_bits(full_path):
    pass

_main_pid = os.getpid()

def _save_env_vars(names):
    if os.getpid() == _main_pid:
        report_bad_assumption('Modifying the environment in a multithreaded process is unsafe!', full_stack = True)
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(names())


def _restore_env_vars(saved_vars):
    if os.getpid() == _main_pid:
        report_bad_assumption('Modifying the environment in a multithreaded process is unsafe!', full_stack = True)
# WARNING: Decompyle incomplete


def using_old_ld_library_path(func):
    pass
# WARNING: Decompyle incomplete


def _preexec_fn_lose_child():
    
    try:
        os.setsid()
    except Exception:
        report_exception(component = DesktopComponent.UNKNOWN)

    if os.fork():
        os._exit(0)
        return None


def _start_process(cmd):
    env = os.environ.copy()
    old_path = env.pop('OLD_LD_LIBRARY_PATH', None)
# WARNING: Decompyle incomplete


def launch_app(full_path):
    
    try:
        subprocess.check_output([
            'xdg-open',
            full_path], stderr = subprocess.STDOUT, close_fds = True)
        return None
    except subprocess.CalledProcessError:
        e = None
        raise IOError(e.returncode, e.output)
        e = None
        del e



def app_for_file(full_path = None):
    
    try:
        filetype = subprocess.check_output([
            'xdg-mime',
            'query',
            'filetype',
            full_path]).strip()
        if not filetype:
            return None
        app_name = subprocess.check_output([
            'xdg-mime',
            'query',
            'default',
            filetype], universal_newlines = True).strip()
        if not app_name:
            return None
        return None
    except subprocess.CalledProcessError:
        return None



def app_display_name_for_file(full_path = None):
    pass


def is_dir(full_path):
    return os.path.isdir(full_path)


def show_folder(full_path = None):
    launch_folder(full_path)


def launch_folder(full_path = None, force_foreground = None, cleanup = None):
    _start_process([
        'xdg-open',
        full_path])


def _nautilus_cmd():
    use_no_desktop_flag = True
    lsb_out = subprocess.check_output([
        'lsb_release',
        '-ds'])
    if lsb_out.startswith(b'Ubuntu 19'):
        use_no_desktop_flag = False
    else:
        proc = subprocess.Popen([
            'nautilus',
            '--version'], stdout = subprocess.PIPE)
        (stdout, _) = proc.communicate()
        raw_version = stdout.strip()
        match = re.match(b'.*nautilus.*(\\d+).(\\d+).(\\d+)', raw_version)
        if match:
            version = (int(match.group(1)), int(match.group(2)), int(match.group(3)))
            if version >= (3, 21, 92):
                use_no_desktop_flag = False
            else:
                TRACE("Can't parse `nautilus --version`, defaulting to using the --no-desktop flag: %s", raw_version)
    return [
        'nautilus',
        '--no-desktop'] if use_no_desktop_flag else [
        'nautilus']


def highlight_file(local_path = None, hwnd = None):
    
    try:
        cmd = _nautilus_cmd() + [
            '--select',
            local_path]
        _start_process(cmd)
        return None
    except OSError:
        _start_process([
            'dolphin',
            '--select',
            local_path])
        return None
        except OSError:
            _start_process([
                'xdg-open',
                os.path.dirname(local_path)])
            return None



def highlight_files(folder, local_paths):
    launch_folder(folder)

bubble_last_key_and_ctx: 'Optional[Tuple[Text, Any]]' = None
bubblelock = Lock()

def bubble_external(app = None, message = None, caption = None, ctx_ref = (None,)):
    pass
# WARNING: Decompyle incomplete


def refresh_tray_menu_external(menu):
    control_thread = get_existing_control_thread()
# WARNING: Decompyle incomplete


def change_state_external(new_state):
    control_thread = get_existing_control_thread()
# WARNING: Decompyle incomplete


def get_platform_info():
    
    try:
        return list(platform.uname())
    except Exception:
        report_exception(component = DesktopComponent.UNKNOWN)
        return 



def enable_p2p_default():
    return True


def fs_supports_attrs(directory):
    
    try:
        x = xattr.from_path(directory)
        
        try:
            x['user.myxattr']
            return True
        except KeyError:
            
            try:
                return True
                except OSError:
                    e = None
                    if e.errno == errno.EOPNOTSUPP:
                        
                        try:
                            e = None
                            del e
                            return False
                            raise 
                            e = None
                            del e
                            
                            try:
                                pass
                            except Exception:
                                report_exception(component = DesktopComponent.UNKNOWN)

                            return False






def launch_new_dropbox(opts = None, wait = None, timeout = None):
    TRACE('Launching second Dropbox process with args %r', opts)
    argv = executable(opts)
    p = subprocess.Popen(argv)
    if wait:
        TRACE('Waiting for second Dropbox process to finish')
        p.communicate(timeout = timeout)
    return p


def restart_unwatched(opts = None):
    argv = executable(opts)
    
    try:
        if MYPY and sys.platform.startswith('win'):
            MAXFD = 0
        else:
            MAXFD = os.sysconf('SC_OPEN_MAX')
    except Exception:
        MAXFD = 256

    for i in range(3, MAXFD):
        fcntl.fcntl(i, fcntl.F_SETFD, 1)
        except Exception:
            continue
        if not is_frozen():
            maybe_detach_debugger = maybe_detach_debugger
            import dropbox.client.debugger
            maybe_detach_debugger()
    os.execv(argv[0], argv)


def launch_newer_version(path = None):
    dropbox_exe = make_bytes(os.path.join(path, 'dropboxd'))
    cmd = (lambda .0: [ make_bytes(b) for b in .0 ]) + sys.argv[1:]()
    TRACE('launching newer version from alt path. Command: %s', cmd)
    
    try:
        force_flush = force_flush
        import dropbox.client.high_trace
        force_flush()
    except Exception:
        report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)

    subprocess.check_call(cmd, close_fds = True, cwd = '/')


def set_hidden_and_read_only(path):
    pass


def get_free_space(folder):
    st = os.statvfs(folder)
    return st.f_bfree * st.f_bsize


def get_executable():
    return sys.executable


def get_install_dir():
    exe = get_executable()
    if is_frozen() and 'python' in os.path.basename(exe):
        repo_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
        return os.path.abspath(os.path.join(repo_root, 'build', 'Debug'))
    return None.path.dirname(exe)


def get_contents_root():
    return get_install_dir()


def get_repo_root_unfrozen():
    pass
# WARNING: Decompyle incomplete


def get_sanitized_executable_path():
    if not is_frozen():
        return 'dev'
    home_dir = None.path.expanduser('~/')
    if get_contents_root().startswith(home_dir):
        return 'home'


def clean_tray():
    pass


def get_user_agent_dict():
    return {
        'platform': 'Linux',
        'version': platform.release(),
        'architecture': 'x64' if struct.calcsize('P') * 8 == 64 else 'i32' }


def check_move_blocked(paths = None, destination = None):
    return 0


def move_files(paths = None, destination = None, fs = None):
    files_moved = { }
    total_file_size = 0
    for path in paths:
        dest = os.path.join(destination, os.path.basename(path))
        fsutil.safe_move(fs, fs.make_path(path), fs.make_path(dest))
        files_moved[path] = dest
        total_file_size += os.path.getsize(dest)
        except OSError:
            report_exception(component = DesktopComponent.UNKNOWN)
            continue
        return (files_moved, total_file_size)


def create_hidden_symlink(link_name, source):
    status = fsutil.CreateHiddenSymlinkStatus
    
    try:
        os.symlink(source, link_name)
        return status.HIDDEN_FILE_FAILED
    except OSError:
        e = None
        TRACE('symlink creation failed with error code %r', e.errno)
        del e
        return None
        None = 
        del e



def get_update_manager_id():
    return get_updater_id()


def get_update_manager_logs(load_contents = (False,)):
    return []

Library = collections.namedtuple('Library', [
    'full_path',
    'system',
    'base',
    'version1',
    'version2',
    'version_full'])

def _parse_library_path(lib):
    homedir = os.path.expanduser('~')
    if len(homedir) < 3 or homedir in frozenset({'/', '/lib', '/usr', '/usr/lib'}):
        homedir = None
    if not '.dropbox-dist/dropbox-lnx.' in lib:
        if not 'client-dropbox-python/dropbox-python' in lib:
            if homedir:
                system = not lib.startswith(homedir)
                if not system:
                    lib = re.sub('^.*/\\.dropbox-dist/dropbox-lnx\\.x86(?:_64)?-\\d+\\.\\d+\\.\\d+', 'DROPBOX_DIST_DIR', lib)
                    if homedir:
                        lib = re.sub('^{}'.format(homedir), 'USER_HOME_DIR', lib)
    base = None
    version_full = None
    dash = None
    dot = None
    if system:
        base = os.path.split(lib)[-1]
        match = re.match('(?P<base>.*?)(?P<dash>-[\\d\\.]+)?\\.so(?P<dot>\\.[\\d\\.]+)?$', base)
        if match:
            base = match.group('base') + '.so'
            dash = match.group('dash')
            if dash:
                dash = dash[1:]
            dot = match.group('dot')
            if dot:
                dot = dot[1:]
            version_full = None
            if dash or dot:
                version_full = (lambda .0: pass# WARNING: Decompyle incomplete
)((dash, dot)())
    return Library(full_path = lib, system = system, base = base, version1 = dash, version2 = dot, version_full = version_full)


def get_loaded_libraries():
    raw_libs = set()
    inp = open('/proc/{}/maps'.format(os.getpid()))
    for line in inp:
        if '.so' in line:
            split_line = line.strip().split(None, 6)
            if len(split_line) == 6:
                raw_libs.add(split_line[-1])
        None(None, None)
    with None:
        if not None:
            pass
    return raw_libs()


def switch_sidebar_link(dropbox_folder, ignore_missing, remove_only, old_dropbox_folder, windows_skip_desktop_shortcut = (False, False, None, False)):
    pass


def get_volume_info(path = None):
    raise NotImplementedError('get_volume_info is not implemented on linux')

