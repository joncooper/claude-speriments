# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import configparser
import functools
import glob
import os
import shutil
from enum import IntEnum
from typing import List, NamedTuple, Optional, Text, Tuple
import win32api
import winerror
from comtypes import COMError
from comtypes.client import CreateObject
from comtypes.persist import IPersistFile
from comtypes.shelllink import ShellLink
from pynt.constants import CSIDL_COMMON_PROGRAMS, CSIDL_PROGRAMS
from winffi.kernel32.api import FILE_ATTRIBUTE_HIDDEN, GetFileAttributesW, SetFileAttributesW
from build_number import BUILD_KEY, is_frozen
from dropbox.client.background_worker import on_background_thread
from dropbox.client.gandalf import Gandalf
from dropbox.client.installer_tag import InstallerTag
from dropbox.client.util.win import get_executable, get_long_path
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.exception_decorators import handle_exceptions, handle_exceptions_ex_1
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.trace import TRACE
from dropbox.win32.com_helper import uses_com
from dropbox.win32.internal import create_shortcut, get_user_folder_path, is_admin
from dropbox.win32.version import WIN10, WINDOWS_VERSION

class StartMenuStatus(IntEnum):
    UNKNOWN_FAILURE = 1
    PARENT_FOLDER_MISSING = 2
    PARENT_FOLDER_HIDDEN = 3
    SHORTCUT_MISSING = 4
    SHORTCUT_HIDDEN = 5
    APPMODELID_MISSING = 6

ShortcutValidityInfo = NamedTuple('ShortcutValidityInfo', [
    ('is_ok', bool),
    ('most_probable_path', Optional[Text]),
    ('is_common_folder', Optional[bool]),
    ('errors', List[StartMenuStatus])])
ShortcutInfo = NamedTuple('ShortcutInfo', [
    ('path', Optional[Text]),
    ('arguments', Optional[Text])])
get_shortcut_info = (lambda shortcut_path = None, ignore_exception = None: if not os.path.exists(shortcut_path):
ShortcutInfo(None, None)try:
shortcut = CreateObject(ShellLink)persist_file = shortcut.QueryInterface(IPersistFile)STGM_READ = 0ret = persist_file.Load(shortcut_path, STGM_READ)if ret:
TRACE('!! Could not load shortcut at %r (return code: %d)', shortcut_path, ret)ShortcutInfo(None, None)target_path = Noneraw_path = shortcut.GetPath()if raw_path:
target_path = win32api.GetLongPathNameW(raw_path)ShortcutInfo(path = target_path, arguments = shortcut.GetArguments())except win32api.error:
e = Noneif ignore_exception and e.winerror != winerror.ERROR_PATH_NOT_FOUND and e.winerror != winerror.ERROR_FILE_NOT_FOUND:
report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)if e.winerror == winerror.ERROR_FILE_NOT_FOUND:
TRACE('!! The system cannot find the file specified')del eNoneNone = del eexcept Exception:
e = Noneif isinstance(e, COMError) and e.hresult == -2147467259:
report_exception(severity = Severity.TRACE, component = DesktopComponent.UNKNOWN)else:
report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)del eNoneNone = del e)()

def is_app_shortcut_valid(shortcut_path = None, ignore_exception = None):
    if not os.path.exists(shortcut_path):
        return False
    
    try:
        target_path = get_shortcut_info(shortcut_path, ignore_exception).path
        if not target_path:
            return False
        norm_target_path = None.path.normpath(target_path).lower()
        norm_dropbox_executable = os.path.normpath(get_long_path(get_executable())).lower()
        return norm_target_path == norm_dropbox_executable
    except Exception:
        report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)
        return False



def _pick_best_startmenu_shortcut(shortcuts = None):
    valid_shortcut = (lambda .0: pass# WARNING: Decompyle incomplete
)(shortcuts(), None)
    if valid_shortcut:
        return valid_shortcut
    
    def _select_startmenu_error(shortcut_a = None, shortcut_b = None):
        a_errors = shortcut_a.errors
        b_errors = shortcut_b.errors
        if StartMenuStatus.PARENT_FOLDER_MISSING in a_errors:
            if StartMenuStatus.PARENT_FOLDER_MISSING not in b_errors:
                return shortcut_b
            return None
        if None.PARENT_FOLDER_MISSING in b_errors:
            return shortcut_a
        if None.SHORTCUT_MISSING in a_errors:
            if StartMenuStatus.SHORTCUT_MISSING not in b_errors:
                return shortcut_b
        if StartMenuStatus.SHORTCUT_MISSING in b_errors:
            return shortcut_a
        if None.APPMODELID_MISSING in a_errors:
            if StartMenuStatus.APPMODELID_MISSING not in b_errors:
                return shortcut_b
        if StartMenuStatus.APPMODELID_MISSING in b_errors:
            return shortcut_a
        if None.SHORTCUT_HIDDEN in a_errors:
            if StartMenuStatus.SHORTCUT_HIDDEN not in b_errors:
                return shortcut_b
        if StartMenuStatus.SHORTCUT_HIDDEN in b_errors:
            return shortcut_a
        if None.PARENT_FOLDER_HIDDEN in a_errors:
            if StartMenuStatus.PARENT_FOLDER_HIDDEN not in b_errors:
                return shortcut_b
        if StartMenuStatus.PARENT_FOLDER_HIDDEN in b_errors:
            return shortcut_a
        if None.is_common_folder and shortcut_a.is_common_folder:
            return shortcut_b

    filtered_shortcuts = shortcuts()
    if len(filtered_shortcuts):
        return functools.reduce(_select_startmenu_error, filtered_shortcuts)
    return shortcuts[0] if len(shortcuts) else ShortcutValidityInfo(False, None, None, [
        StartMenuStatus.UNKNOWN_FAILURE])

_check_startmenu_specific = (lambda is_common_folder = None: if WINDOWS_VERSION.version_number() < WIN10.version_number():
Noneis_valid_shortcut_for_toasts = is_valid_shortcut_for_toastsimport windisplaytoast.apidropbox_start_menu_folder = _get_startmenu_dropbox_folder(is_common_folder)if not os.path.exists(dropbox_start_menu_folder):
ShortcutValidityInfo(False, None, is_common_folder, [
StartMenuStatus.PARENT_FOLDER_MISSING])is_parent_hidden = Noneif GetFileAttributesW(dropbox_start_menu_folder) & FILE_ATTRIBUTE_HIDDEN == FILE_ATTRIBUTE_HIDDEN:
is_parent_hidden = Trueall_shortcuts = glob.iglob(os.path.join(dropbox_start_menu_folder, '*.lnk'))shortcuts = all_shortcuts()if not shortcuts:
reasons = [
StartMenuStatus.SHORTCUT_MISSING]if is_parent_hidden:
reasons.append(StartMenuStatus.PARENT_FOLDER_HIDDEN)ShortcutValidityInfo(False, None, is_common_folder, reasons)
def shortcuts_possible(.0):
pass# WARNING: Decompyle incomplete
for shortcut in shortcuts:
reasons = [
StartMenuStatus.PARENT_FOLDER_HIDDEN] if is_parent_hidden else []if not is_valid_shortcut_for_toasts(shortcut):
reasons.append(StartMenuStatus.APPMODELID_MISSING)if GetFileAttributesW(shortcut) & FILE_ATTRIBUTE_HIDDEN == FILE_ATTRIBUTE_HIDDEN:
reasons.append(StartMenuStatus.SHORTCUT_HIDDEN)if not reasons:
None, ShortcutValidityInfo(True, shortcut, is_common_folder, [])None.append(ShortcutValidityInfo(False, shortcut, is_common_folder, reasons))_pick_best_startmenu_shortcut(shortcuts_possible))()()

def check_startmenu():
    state_user = _check_startmenu_specific(False)
    state_for_fix = state_for_check
    if not state_for_check.is_common_folder and is_admin():
        state_for_fix = state_user
    return (state_for_check, state_for_fix)


def _get_startmenu_dropbox_folder(per_machine = None):
    startmenu_folder_id = CSIDL_COMMON_PROGRAMS if per_machine else CSIDL_PROGRAMS
    dropbox_startmenu = os.path.join(get_user_folder_path(startmenu_folder_id), BUILD_KEY)
    return dropbox_startmenu

setup_shortcuts = (lambda per_machine = None, inst_dir = None: remove_all_start_menu_shortcuts()TRACE('Setup start menu shortcut')dropbox_startmenu = _get_startmenu_dropbox_folder(per_machine)os.makedirs(dropbox_startmenu)lnk_path = f'''{dropbox_startmenu!s}\\{BUILD_KEY!s}.lnk'''try:
setup_dropbox_link_shortcut(dropbox_startmenu)except Exception:
report_exception(severity = Severity.TRACE, component = DesktopComponent.UNKNOWN)exe_path = os.path.join(inst_dir, '%s.exe' % BUILD_KEY)try:
setup_dropbox_app_shortcut(lnk_path, exe_path)Noneexcept Exception:
report_exception(severity = Severity.TRACE, component = DesktopComponent.UNKNOWN)None)()
setup_dropbox_app_shortcut = (lambda lnk_path = None, exe_path = None: create_shortcut(lnk_path, exe_path, arguments = '/home', working_directory = os.path.dirname(exe_path))if WINDOWS_VERSION.version_number() >= WIN10.version_number():
set_shortcut_properties = set_shortcut_propertiesimport windisplaytoast.apiset_shortcut_properties(lnk_path)None)()

def setup_dropbox_link_shortcut(dropbox_startmenu = None):
    TRACE('Setting up dropbox.com shortcut')
    config = configparser.ConfigParser()
    config.add_section('InternetShortcut')
    config.set('InternetShortcut', 'URL', 'https://www.dropbox.com')
    configfile = open(os.path.join(dropbox_startmenu, '%s Website.URL' % BUILD_KEY), 'w')
    config.write(configfile)
    None(None, None)
    return None
    with None:
        if not None:
            pass

remove_all_start_menu_shortcuts = (lambda : for per_machine in (True, False):
remove_start_menu_shortcuts(per_machine)None)()
remove_start_menu_shortcuts = (lambda per_machine = None: startmenu_folder = _get_startmenu_dropbox_folder(per_machine)shutil.rmtree(startmenu_folder, ignore_errors = True))()

def _fix_shortcut(dropbox_exe = None, shortcut_path = None):
    
    try:
        if not WINDOWS_VERSION.version_number() < WIN10.version_number() or os.path.exists(dropbox_exe):
            return None
        dropbox_startmenu_path = None.path.dirname(shortcut_path)
        if os.path.exists(dropbox_startmenu_path):
            attributes = GetFileAttributesW(dropbox_startmenu_path)
            if attributes & FILE_ATTRIBUTE_HIDDEN == FILE_ATTRIBUTE_HIDDEN:
                SetFileAttributesW(dropbox_startmenu_path, attributes & ~FILE_ATTRIBUTE_HIDDEN)
            else:
                os.makedirs(dropbox_startmenu_path)
        setup_dropbox_app_shortcut(shortcut_path, dropbox_exe)
        if os.path.exists(shortcut_path):
            attributes = GetFileAttributesW(shortcut_path)
            if attributes & FILE_ATTRIBUTE_HIDDEN == FILE_ATTRIBUTE_HIDDEN:
                SetFileAttributesW(shortcut_path, attributes & ~FILE_ATTRIBUTE_HIDDEN)
                return None
            return None
        return None
    except Exception:
        report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)
        return None



def ensure_startmenu_shortcut_for_toasts():
    (state_for_check, state_for_fix) = check_startmenu()
    if state_for_check.is_ok:
        return state_for_check
    dropbox_exe = get_executable()
# WARNING: Decompyle incomplete


def _report_state(state = None):
    if state.is_ok:
        return None
    'win10-startmenu-shortcut-broken'(state.is_common_folder, is_common_folder = (lambda .0: [ int(error) for error in .0 ]), errors = state.errors())

check_and_fix_startmenu_shortcut_in_background = (lambda gandalf: check_and_fix_startmenu_shortcut(gandalf))()
check_and_fix_startmenu_shortcut = (lambda gandalf = None: pass# WARNING: Decompyle incomplete
)()

def is_allowed_create_desktop_shortcut_at_install(is_primary_account = None, installer_tag = None, hades_deal_redeemed = None):
    if hades_deal_redeemed:
        TRACE('Hades deal redeemed, not creating shortcut on Desktop.')
        return False
    import hashlib
    blacklist_dealcodes = [
        '31cd23ea59358b730937e6c10577e0d6d1132cef',
        '47d8c358cdd6db743483051de6d5e8cfcd6691e9',
        '48e16860873543e3b322d23804e7891367231897',
        '2aa5efc2f2c22470fa1b74fa5d80257a16919b44',
        'e3c10e6ec1d4c2c685d4a86053d176f64189fd25',
        'ccd19928ed479b92e561ade45ca8a42dd9175ef4',
        'f0a3ee285c852d9988e5f2cd80fc740987a96f88',
        '82fdcc5452715274d7e76f1d10303376fc5d633c',
        '6276fda1572ff57616167ca1457dc20530137fcc',
        '9b9708a2507031a4b8c7f0baf60a17b0847ca959',
        'ef425dbeb1527fea34e56203226343910e858d81',
        '89dd7c0ebe61d48fe29c3810cbb93d5e81e7507f',
        '42b794745d4a1c447a0408fd5ba1db22c08ac9f2',
        '915e6cd43176481dc4cdba2716edcb1feb248858',
        'f19a6d3bf1481e07b1b496b2bf3f9736a58a9e2a',
        '9f64f44ac73582550e387d5fb33260c29ed689db',
        'f6c9e54bb366811e6b5178a0c4ace2aad205bab6',
        'ff1262b42221230fb1bc741435cba0aa05a445fd',
        '67415296eb9081f267757a99be738bd742cf62ac',
        '631a7cc71c6e692e6ee4379e3974ec16ffd59ebc',
        '259432471d11822edd010b288105751c9c5d1db8',
        'a1f2a02a3f4ca8532166cd578918adf04ea39da0',
        'f60ac66e1411c15cca95ea36f6a145e0f4a5dea2',
        '946e025ab9491eae6ca9f19f4c73ee5436057009',
        'c528182b1f66c38678b251b6f09d7ef51d91bfd7',
        'a19a1074aaa971b6833248c64306bedc5266b5a5',
        '0d47be9b4402e31b2c0191c1c1c1aa9046286a19',
        'adf419b0567061e0e9c3d35c30249fffbbf99e9a',
        'db0a9981dec5c3cec8e2be69bdcbc20c520dc1fd',
        '1d23f23e56b465029349b014537b6aceb96ffb39',
        '846addcfdc9daaa1d26aefd54daa2a1931097760',
        'cb3568587eafa6921d0bab3aca73828af6020745',
        '4e0d6f88dffae77a99040f2d3375bc22d3b98f38',
        '8a029caa02925552d5c07a32b1694b5157e69827',
        'd00ee25729fb563856a508322f19b4ccb9fe37a1',
        '958731e59127e81773f8f67bc25e4a08dffbff68',
        'a6bcbcbe038149f41a94a85908f18d1d7aa52a35',
        '5c885701917f4e297d70d9c090a70054e09343e2']
    if not not is_primary_account:
        if not installer_tag is None:
            if not installer_tag.command_line_dealcode is None:
                pass
    return hashlib.sha1(installer_tag.command_line_dealcode.encode('UTF-8')).hexdigest() not in blacklist_dealcodes

