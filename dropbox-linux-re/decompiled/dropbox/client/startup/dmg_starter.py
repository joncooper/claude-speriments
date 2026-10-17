# Source Generated with Decompyle++
# File: dmg_starter.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import filecmp
import os
import subprocess
from typing import Callable, Dict, List, Optional, Text, Tuple
from apex.context import ApexContext
from AppKit import NSWorkspace
from pymac.helpers.shared_file_list import get_all_login_matches
from build_number import BUILD_KEY
from dropbox.client.installer_tag import InstallerTag
from dropbox.client.util.mac import get_user_agent_dict, is_in_trash, is_on_installer
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.foundation.futures.basic import allow_blocking_on_main_thread
from dropbox.functions import make_unicode, random_string
from dropbox.i18n import safe_activate_translation, trans
from dropbox.mac.internal import autoreleasepool
from dropbox.mac.version import MAC_VERSION
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info

def find_previous_installation():
    if not get_all_login_matches:
        return None
    matches = get_all_login_matches(f'''{BUILD_KEY!s}.app''', report_exception)
    for match in reversed(matches):
        if not os.path.exists(match) and is_in_trash(match):
            
            return None, os.path.dirname(match)
        return None


class InstallerReport(object):
    
    def __init__(self = None, apex_context = None, installer_tag = None, install_type = ('apex_context', 'ApexContext', 'installer_tag', 'InstallerTag', 'install_type', 'Text', 'return', 'None')):
        self.installer_tag = installer_tag
        self.install_type = install_type
        self.conn = None
        
        try:
            DropboxConnection = DropboxConnection
            import dropbox.client_api.dropbox_connection
            self.conn = DropboxConnection(hosts = dropbox_url_info.api_hosts, user_agent_dict = get_user_agent_dict(), legacy_usage_skip_metrics = True, apex_context = apex_context)
            return None
        except Exception:
            report_exception(component = DesktopComponent.INITIALIZATION)
            self.conn = None
            return None


    report = (lambda installer_report = None, event_name = None, extra = staticmethod: if not installer_report or installer_report.conn:
Nonetry:
allow_blocking_on_main_thread()installer_report.conn.report_installer_funnel(event_name, MAC_VERSION.version_string(), installer_report.installer_tag, installer_report.install_type, extra = extra)try:
None(None, None)Nonewith None:
if not None:
try:
try:
Noneexcept Exception:
report_exception(component = DesktopComponent.INITIALIZATION)None)()


def can_remove_target_app(app_target = None):
    if not os.path.exists(app_target):
        return True
    for dirpath, dirnames, filenames in os.walk(app_target):
        for dirname in dirnames:
            if not os.access(os.path.join(dirpath, dirname), os.W_OK | os.X_OK):
                return False
            for filename in filenames:
                if not os.access(os.path.join(dirpath, filename), os.W_OK):
                    return False
                return True


def is_elevation_required(app_target = None):
    if os.path.exists(app_target):
        return not can_remove_target_app(app_target)
    parent_dir = None.path.dirname(app_target)
    return not os.access(parent_dir, os.W_OK | os.X_OK)


def decide_dmg_action(apex_context, curr_instance_path, default_app_folder_path, alt_install_path = None, give_us_permissions_cb = None, kill_other_instances = None, is_installer = (None, False, None), installer_tag = ('apex_context', 'ApexContext', 'curr_instance_path', 'Text', 'default_app_folder_path', 'Text', 'alt_install_path', 'Text', 'give_us_permissions_cb', 'Callable[[Text, List[Text], Text, Optional[Text]], Tuple[int, bytes]]', 'kill_other_instances', 'Optional[Callable[[], bool]]', 'is_installer', 'bool', 'installer_tag', 'Optional[InstallerTag]', 'return', 'Optional[List[Text]]')):
    TRACE('starting decide_dmg_action %s, %s, %s, %s, %s', curr_instance_path, default_app_folder_path, alt_install_path, give_us_permissions_cb, kill_other_instances)
    curr_instance_path = curr_instance_path.rstrip('/')
    if not is_installer:
        return None
# WARNING: Decompyle incomplete


def _plist_identical(d1 = None, d2 = None):
    p1 = os.path.join(d1, 'Contents', 'Info.plist')
    p2 = os.path.join(d2, 'Contents', 'Info.plist')
    if not os.path.exists(p1) or os.path.exists(p2):
        return False
    
    try:
        return filecmp.cmp(p1, p2, shallow = False)
    except EnvironmentError:
        return False


