# Source Generated with Decompyle++
# File: mac.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import fcntl
import os
import plistlib
import pwd
import re
import resource
import shutil
import subprocess
import sys
from typing import Callable, List, Optional, Text, Tuple
from xml.parsers.expat import ExpatError
from apex.context import ApexContext
from apex.metrics import Metric, MetricsReporter
from AppKit import NSRunningApplication, NSURL, NSWorkspace, NSWorkspaceLaunchConfigurationArguments
from CoreServices.LaunchServices import LSRegisterURL
from macffi.CoreFoundation import CFError
from macffi.Security import errAuthorizationCanceled, request_authorization_from_user_and_run
from macffi.System import get_current_task_info
from psutil import NoSuchProcess, Process
from pymac.dlls import preload_dlls
from pymac.helpers.disk import get_mount_point_for_path, get_volume_desc, is_ejectable
from pymac.helpers.shared_file_list import add_path_to_shared_list, get_all_login_matches, remove_path_from_shared_list, SFL_LOGIN
import build_number
from build_number import BUILD_KEY, BuildVersion
from dropbox.client.constants import AppDataPaths
from dropbox.client.constants.mac import get_alt_install_path, get_omaha4_crashpad_usage_stats_folder_path
from dropbox.client.file_permissions.posix import check_and_fix_permissions
from dropbox.client.installer_tag import InstallerTag
from dropbox.client.startup.dmg_starter import decide_dmg_action
from dropbox.client.ui.cocoa.cf_dialog import CFMacDialog
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.client.util import hard_exit
from dropbox.client.util.mac import get_app_path, get_contents_root, get_drives, get_mounted_dmg_paths, is_on_installer, kill_other_instances
from dropbox.components.desktop_components import DesktopComponent
from dropbox.dirtraverse import Directory
from dropbox.event import sanitize_event_extra_dict
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fileutils import loop_delete
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.i18n import trans
from dropbox.mac.helper_installer import install_dropbox_helper_installer, update_helper_installer
from dropbox.mac.internal import autoreleasepool, binaries_ready, find_instances, MacError, post_linked_yet
from dropbox.mac.version import CATALINA, MAC_VERSION
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
METAINSTALLER_BUNDLE_ID = 'com.getdropbox.DropboxMetaInstaller'

def print_shared_list(list_type):
    return f'''print_shared_list({list_type!s}) not implemented'''


def read_version_number(plist_path = None):
    if os.path.exists(plist_path):
        
        try:
            info_file = open(plist_path, 'rb')
            info_plist = plistlib.load(info_file)
            
            try:
                None(None, None)
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            return info_plist['CFBundleVersion'].strip()
                        except (KeyError, ExpatError):
                            return None
                            return None






def check_other_version():
    alt_install_path = get_alt_install_path()
    alt_install_plist_path = os.path.join(alt_install_path, 'Contents', 'Info.plist')
    version = read_version_number(alt_install_plist_path)
    if version:
        TRACE('Current version %s, found version %s in %s', build_number.VERSION, version, alt_install_path)
        
        try:
            other_version = BuildVersion(version)
        except Exception:
            report_exception(severity = Severity.WARN, component = DesktopComponent.INITIALIZATION)
            TRACE('!! Ignoring invalid version %s in %s', version, alt_install_path)
            return None

        if other_version > build_number.dropbox_version:
            return alt_install_path
        return None

LSREGISTER_TOOL_PATH = '/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister'
PLUGINKIT_TOOL_PATH = '/usr/bin/pluginkit'
FP_EXTENSION_PATTERN = re.compile(f'''.*?com\\.getdropbox\\.{BUILD_KEY.lower()}\\.fileprovider\\((.*?)\\)''')

def get_extension_paths(metrics_reporter = None):
    
    try:
        out = subprocess.check_output([
            PLUGINKIT_TOOL_PATH,
            '-mvDA',
            '-p',
            'com.apple.fileprovider-nonui'], timeout = 5).decode('utf-8')
        fp_extensions = out.split('\n')()()
        return fp_extensions
    except subprocess.CalledProcessError:
        e = None
        metrics_reporter.create_stats(Metric('client_mac_startup', 'fix_launch_services_registration/pluginkit_list_failure/event'), {
            'code': str(e.returncode) }).record(1)
        TRACE('Failed to list registered fileprovider extensions: %s', e)
        e = None
        del e
    except subprocess.SubprocessError:
        e = None
        metrics_reporter.create_stats(Metric('client_mac_startup', 'fix_launch_services_registration/pluginkit_list_timeout/event'), { }).record(1)
        TRACE('Timed out when listing registered fileprovider extensions: %s', e)
        e = None
        del e
    except:
        e = None
        del e

    return []


def report_launch_services_registration_result(metrics_reporter, pre_fixup_extension_paths = None, registered = None, unregistered = None, app_path = ('metrics_reporter', 'MetricsReporter', 'pre_fixup_extension_paths', 'List[Tuple[str, str]]', 'registered', 'Optional[Tuple[str, str]]', 'unregistered', 'List[str]', 'app_path', 'str', 'return', 'None')):
    report = report
    import dropbox.event
    extra = {
        'pre_fixup_extension_paths': pre_fixup_extension_paths,
        'registered': registered,
        'unregistered': unregistered,
        'app_path': app_path }
    
    try:
        if registered or unregistered:
            extra['post_fixup_extension_paths'] = get_extension_paths(metrics_reporter)
        report('mac_startup', event_type = 'file_provider_launch_services_fixup', extra = sanitize_event_extra_dict(extra))
        return None
    except Exception:
        report_exception(severity = Severity.WARN, component = DesktopComponent.INITIALIZATION)
        return None



def fix_launch_services_registration_if_necessary(metrics_reporter = None):
    pass
# WARNING: Decompyle incomplete


def get_rss():
    
    try:
        return get_current_task_info().resident_size
    except Exception:
        report_exception(component = DesktopComponent.INITIALIZATION)
        return -1



def install_early_in_boot(client_session_id = None):
    pass


def detect_launch_from_dmg(apex_context = None, installer_tag = None, is_installer = None):
    pass
# WARNING: Decompyle incomplete


def _unmount_dmgs(paths = None):
    to_unmount = []
    for path in paths:
        if os.path.exists(path) or get_app_path().startswith(path):
            continue
        mount_point = get_mount_point_for_path(path)
        if mount_point == '/':
            continue
        if not is_ejectable(mount_point):
            continue
        to_unmount.append(mount_point)
        if not to_unmount:
            return None
        active_installers = list(NSRunningApplication.runningApplicationsWithBundleIdentifier_(METAINSTALLER_BUNDLE_ID))
        for active_installer in active_installers:
            active_installer_proc = Process(pid = active_installer.processIdentifier())
            active_installer_proc.kill()
            active_installer_proc.wait(timeout = 2)
            except NoSuchProcess:
                continue
            except Exception:
                report_exception(severity = Severity.WARN, component = DesktopComponent.INITIALIZATION)
                continue
            TRACE('Going to unmount these paths: %s', to_unmount)
            for mount_point in to_unmount:
                TRACE('about to diskutil eject %s', mount_point)
                subprocess.check_output([
                    '/usr/sbin/diskutil',
                    'eject',
                    mount_point], stderr = subprocess.STDOUT)
                except subprocess.CalledProcessError:
                    cpe = None
                    TRACE('diskutil eject %s failed with "%s"', mount_point, cpe.output)
                    cpe = None
                    del cpe
                    continue
                    cpe = None
                    del cpe
                return None


def _get_permissions_from_user(cmd, argv, auth_text, icon_path = (None, None)):
    output = None
    retval = False
    
    try:
        channel = request_authorization_from_user_and_run(cmd, argv, auth_text = auth_text, icon_path = icon_path)
        retval = True
        if channel:
            
            try:
                output = channel.read()
                
                try:
                    channel.close()
                    
                    try:
                        pass
                    except Exception:
                        report_exception(component = DesktopComponent.INITIALIZATION)
                        
                        try:
                            pass
                        try:
                            channel.close()
                            except Exception:
                                report_exception(component = DesktopComponent.INITIALIZATION)
                            
                            try:
                                pass
                            except CFError:
                                e = None
                                if e.errno != errAuthorizationCanceled:
                                    raise 
                                e = None
                                del e
                            except:
                                e = None
                                del e

                            return (retval, output)







def remove_from_startup_items():
    pass
# WARNING: Decompyle incomplete


def add_to_startup_items():
    if hasattr(sys, 'frozen'):
        app_path = get_app_path()
        if is_on_installer(app_path):
            return False
        if None == get_alt_install_path():
            return False
        
        try:
            matches = get_all_login_matches(f'''{BUILD_KEY!s}.app''', report_exception)
            if matches == [
                app_path]:
                return False
            if None:
                autoreleasepool()
                remove_from_startup_items()
                
                try:
                    None(None, None)
                with None:
                    if not None:
                        
                        try:
                            
                            try:
                                pass
                            except Exception:
                                report_exception(severity = Severity.WARN, component = DesktopComponent.INITIALIZATION)

                            
                            try:
                                autoreleasepool()
                                add_path_to_shared_list(app_path, SFL_LOGIN)
                                
                                try:
                                    None(None, None)
                                with None:
                                    if not None:
                                        
                                        try:
                                            
                                            try:
                                                TRACE('added startup item at %s using add_path_to_shared_list', app_path)
                                            except Exception:
                                                report_exception(severity = Severity.WARN, component = DesktopComponent.INITIALIZATION)
                                                return False

                                            return True
                                            return False








def can_configure_startupitem():
    return True


def reroll_startup_items(local_config):
    TRACE('rerolling startup items')
    
    try:
        if local_config['startupitem']:
            added = add_to_startup_items()
            if added:
                TRACE('Successfully added ourselves as a startup item')
                return None
            TRACE("Startup item preference is on, but we didn't add ourselves")
            return None
        removed = remove_from_startup_items()
        if removed:
            TRACE('Successfully removed ourselves as a startup item')
            return None
        TRACE('Startup item preference is off, but we failed to remove ourselves')
        return None
    except Exception:
        report_exception(component = DesktopComponent.INITIALIZATION)
        return None


needs_shell_touch_on_reindex = False

def cleanup_app_files():
    pass
# WARNING: Decompyle incomplete

is_first_run_update = False

def first_run(is_update, dropbox_name = (False, None)):
    global is_first_run_update
    kill_other_instances()
    is_first_run_update = is_update


def update_and_fix_binaries_if_needed(freshly_linked = None, when_finished = None, metrics_reporter = None):
