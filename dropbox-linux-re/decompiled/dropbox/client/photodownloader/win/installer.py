# Source Generated with Decompyle++
# File: installer.pyc (Python 3.11)

from typing import Optional
from pynt.constants import KEY_ALL_ACCESS, KEY_READ, KEY_WOW64_64KEY
from pynt.helpers.registry import create_registry_key, delete_registry_tree, delete_regkey_if_empty, hkey_to_str, read_registry_value, registry_key, safe_delete_regkey, safe_delete_regvalue, set_registry_value
from six.moves import range
from six.moves.winreg import HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, REG_SZ, SetValue
from build_number import assert_full_msix_no_registry_writes, BUILD_KEY
from dropbox.client.photodownloader import use_photouploader
from dropbox.client.photodownloader.win.autoplay_defaults import set_old_default_autoplay
from dropbox.client.photodownloader.win.autoplay_event_handler import AutoplayEventHandler
from dropbox.client.photodownloader.win.constants import AUTOPLAY_KEY, DROPBOX_AUTOPLAY_CLSID, DROPBOX_AUTOPLAY_HANDLER_NAME, DROPBOX_AUTOPLAY_PROGID, DROPBOX_AUTOPLAY_VERNO, VOLUME_EVENTS
from dropbox.client.util.win import get_executable
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.i18n import trans
from dropbox.trace import TRACE
from dropbox.win32.internal import is_admin
from dropbox.win32.version import WINDOWS_VERSION
PHOTOUPLOADER_REGKEY = 'Software\\Classes\\%s\\CurVer' % DROPBOX_AUTOPLAY_PROGID

def is_photo_uploader_installed_per_machine_or_user(per_machine = None):
    
    try:
        root_key = HKEY_LOCAL_MACHINE if per_machine else HKEY_CURRENT_USER
        verno = _get_regclass_version(root_key, PHOTOUPLOADER_REGKEY, KEY_READ | KEY_WOW64_64KEY)
        if verno:
            TRACE('Installed Dropbox.AutoplayEventHandler is version %d, current version %d', verno, DROPBOX_AUTOPLAY_VERNO)
        return verno == DROPBOX_AUTOPLAY_VERNO
    except Exception:
        report_exception(severity = Severity.WARN, component = DesktopComponent.SYNC_EVERYTHING)

    return False


def install_photo_uploader_per_machine_or_user(per_machine = None, force = None, exe_path = None):
    if not use_photouploader():
        TRACE('!! Photo uploads not supported on this version of Windows: %r', WINDOWS_VERSION)
        return None
    installed = is_photo_uploader_installed_per_machine_or_user(per_machine)
    TRACE('winver: %r, is admin: %r, photo feature already installed: %r, per-machine: %r', WINDOWS_VERSION, is_admin(), installed, per_machine)
    if not installed and force:
        TRACE('Photouploader is already installed')
        return None
    TRACE('Installing photo uploader')
# WARNING: Decompyle incomplete

uninstall_photo_uploader_per_machine_or_user = (lambda per_machine = None: if not use_photouploader():
None_remove_omaha_photo_uploader_regkeys(per_machine))()

def _install_photo_uploader(per_machine = None, exe_path = None):
    TRACE('Installing photouploader, per-machine: %r', per_machine)
    _remove_omaha_photo_uploader_regkeys(per_machine)
    root_key = HKEY_LOCAL_MACHINE if per_machine else HKEY_CURRENT_USER
    _register_class(root_key, AutoplayEventHandler, DROPBOX_AUTOPLAY_CLSID, DROPBOX_AUTOPLAY_PROGID, DROPBOX_AUTOPLAY_VERNO, 'Dropbox Autoplay COM Server', '"%s" /autoplay' % exe_path)
    _register_drop_target(root_key, DROPBOX_AUTOPLAY_CLSID, DROPBOX_AUTOPLAY_PROGID)
    _add_autoplay_regkeys(root_key, DROPBOX_AUTOPLAY_HANDLER_NAME, DROPBOX_AUTOPLAY_PROGID, exe_path, set_default_selection_for_user = not per_machine)
    _add_wpd_regkeys(root_key, DROPBOX_AUTOPLAY_HANDLER_NAME)

_remove_omaha_photo_uploader_regkeys = (lambda per_machine = None: root_key = HKEY_LOCAL_MACHINE if per_machine else HKEY_CURRENT_USER_unregister_class(root_key, DROPBOX_AUTOPLAY_CLSID, DROPBOX_AUTOPLAY_PROGID, DROPBOX_AUTOPLAY_VERNO)_remove_autoplay_regkeys(hk_which = root_key, handler_name = DROPBOX_AUTOPLAY_HANDLER_NAME, delete_all_the_keys = True)if not per_machine:
try:
TRACE('Removing all Dropbox autoplay default entries')set_old_default_autoplay(old_handlers = { })Noneexcept Exception:
report_exception(severity = Severity.WARN, component = DesktopComponent.SYNC_EVERYTHING)NoneNone)()

def _get_regclass_version(hkey_which = None, curver_key = None, perms = None):
    pass
# WARNING: Decompyle incomplete


def _register_class(hkey, cls, co_clsid, co_progid = None, co_verno = None, co_desc = None, server_path = (KEY_ALL_ACCESS | KEY_WOW64_64KEY,), permissions = ('return', 'None')):
    root = 'Software\\Classes'
    entries = [
        ('\\CLSID\\%s' % co_clsid, co_desc),
        ('\\CLSID\\%s\\LocalServer32' % co_clsid, server_path),
        ('\\CLSID\\%s\\ProgID' % co_clsid, '%s.%d' % (co_progid, co_verno)),
        ('\\CLSID\\%s\\Typelib' % co_clsid, cls._reg_typelib_[0]),
        ('\\CLSID\\%s\\VersionIndependentProgID' % co_clsid, co_progid),
        ('\\%s.%d' % (co_progid, co_verno), co_desc),
        ('\\%s.%d\\CLSID' % (co_progid, co_verno), co_clsid),
        ('\\%s' % co_progid, co_desc),
        ('\\%s\\CLSID' % co_progid, co_clsid),
        ('\\%s\\CurVer' % co_progid, '%s.%d' % (co_progid, co_verno))]
    for reg_key, reg_value in entries:
        full_key = f'''{root!s}{reg_key!s}'''
        TRACE('Creating value [%s\\%s] %s', hkey_to_str(hkey), full_key, reg_value)
        (key, _, _) = create_registry_key(hkey, full_key, permissions)
        assert_full_msix_no_registry_writes()
        if not key or set_registry_value(key, '', REG_SZ, reg_value):
            raise Exception('Registry error: failed to register the %s class' % co_progid)
        None(None, None)
    with None:
        if not None:
            pass
    continue

_unregister_class = (lambda hkey = None, clsid = None, progid = handle_exceptions, verno = (KEY_ALL_ACCESS | KEY_WOW64_64KEY,), permission = ('return', 'None'): pass# WARNING: Decompyle incomplete
)()
DROPBOX_INVOKE_VERB = 'import'

def _register_drop_target(hkey = None, co_clsid = None, co_progid = None):
    key_name = f'''Software\\Classes\\{co_progid!s}\\shell\\{DROPBOX_INVOKE_VERB!s}\\DropTarget'''
    (key, _, _) = create_registry_key(hkey, key_name, permission = KEY_ALL_ACCESS | KEY_WOW64_64KEY)
    assert_full_msix_no_registry_writes()
    value_name = 'CLSID'
    TRACE('Setting value %s %s to %r', key_name, value_name, co_clsid)
    if not key or set_registry_value(key, value_name, REG_SZ, co_clsid):
        raise Exception('Registry error: failed to register %s for DropTarget' % co_progid)
    None(None, None)
    return None
    with None:
        if not None:
            pass

WPD_EVENTS = ('Function\\{23F05BBC-15DE-4C2A-A55B-A9AF5CE412EF}', 'Source\\{9261B03C-3D78-4519-85E3-02C5E1F50BB9}', 'Source\\{EF2107D5-A52A-4243-A26B-62D4176D7603}')

def _add_autoplay_regkeys(hk_which = None, handler_name = None, progid = None, binary = (True,), set_default_selection_for_user = ('return', 'None')):
    for event_name in VOLUME_EVENTS:
        keyname = f'''{AUTOPLAY_KEY!s}\\EventHandlers\\{event_name!s}'''
        TRACE('Adding %r %r %r', hkey_to_str(hk_which), keyname, handler_name)
        (pynt_key, _, _) = create_registry_key(hk_which, keyname, permission = KEY_ALL_ACCESS | KEY_WOW64_64KEY)
        assert_full_msix_no_registry_writes()
        if not pynt_key or set_registry_value(pynt_key, handler_name, REG_SZ, ''):
            raise Exception('Registry error: Failed to add Dropbox as autoplay handler for %s' % event_name)
        None(None, None)
    with None:
        if not None:
            pass
    continue
    if set_default_selection_for_user:
        root = 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\AutoplayHandlers\\EventHandlersDefaultSelection'
        for event in VOLUME_EVENTS:
            TRACE('Creating value %r %r', f'''{root!s}\\{event!s}''', handler_name)
            SetValue(HKEY_CURRENT_USER, f'''{root!s}\\{event!s}''', REG_SZ, handler_name)
            keyname = f'''{AUTOPLAY_KEY!s}\\Handlers\\{handler_name!s}'''
            TRACE('Populating %r %r', hkey_to_str(hk_which), keyname)
            (pynt_key, _, _) = create_registry_key(hk_which, keyname, permission = KEY_ALL_ACCESS | KEY_WOW64_64KEY)
            assert_full_msix_no_registry_writes()
            if not pynt_key:
                raise Exception('Registry error: Failed to create %s' % keyname)
            autoplay_action_label = trans('Import photos and videos')
            values = [
                ('Action', autoplay_action_label),
                ('DefaultIcon', binary),
                ('Provider', BUILD_KEY),
                ('ProgID', progid),
                ('InvokeProgId', progid),
                ('InvokeVerb', DROPBOX_INVOKE_VERB)]
            for valuename, value in values:
                if not set_registry_value(pynt_key, valuename, REG_SZ, value):
                    raise Exception('Registry error: Failed to populate Dropbox AutoplayHandler key')
                None(None, None)
                return None
                with None:
                    if not None:
                        pass


def _add_wpd_regkeys(hk_which = None, handler_name = None):
    for event_guid in WPD_EVENTS:
        keyname = f'''{AUTOPLAY_KEY!s}\\EventHandlers\\WPD\\{event_guid!s}'''
        (pynt_key, _, _) = create_registry_key(hk_which, keyname, permission = KEY_ALL_ACCESS | KEY_WOW64_64KEY)
        assert_full_msix_no_registry_writes()
        TRACE('Adding %r %r %r', hkey_to_str(hk_which), keyname, handler_name)
        if not pynt_key or set_registry_value(pynt_key, handler_name, REG_SZ, ''):
            raise Exception('Registry error: Failed to register Dropbox for WPD events')
        None(None, None)
    with None:
        if not None:
            pass
    continue


def _remove_autoplay_regkeys(hk_which = None, handler_name = None, delete_all_the_keys = None):
    for event_name in VOLUME_EVENTS:
        safe_delete_regvalue(hk_which, f'''{AUTOPLAY_KEY!s}\\EventHandlers\\{event_name!s}''', handler_name, delete_key = delete_all_the_keys, permission = KEY_ALL_ACCESS | KEY_WOW64_64KEY)
        for event_guid in WPD_EVENTS:
            safe_delete_regvalue(hk_which, f'''{AUTOPLAY_KEY!s}\\EventHandlers\\WPD\\{event_guid!s}''', handler_name, delete_key = delete_all_the_keys, permission = KEY_ALL_ACCESS | KEY_WOW64_64KEY)
            keyname = f'''{AUTOPLAY_KEY!s}\\Handlers\\{handler_name!s}'''
            TRACE('Removing %r %r', hkey_to_str(hk_which), keyname)
            delete_registry_tree(hk_which, keyname, permission = KEY_ALL_ACCESS | KEY_WOW64_64KEY)
            if delete_all_the_keys:
                wpd_event_keys = [
                    '%s\\EventHandlers\\WPD\\Function' % AUTOPLAY_KEY,
                    '%s\\EventHandlers\\WPD\\Source' % AUTOPLAY_KEY,
                    '%s\\EventHandlers\\WPD' % AUTOPLAY_KEY,
                    '%s\\EventHandlers' % AUTOPLAY_KEY]
                for wpd_event_key in wpd_event_keys:
                    TRACE('Cleaning up if empty: %r %r', hkey_to_str(hk_which), wpd_event_key)
                    safe_delete_regkey(hk_which, wpd_event_key, permission = KEY_ALL_ACCESS | KEY_WOW64_64KEY)
                    keyname = '%s\\Handlers' % AUTOPLAY_KEY
                    TRACE('Cleaning up if empty: %r %r', hkey_to_str(hk_which), keyname)
                    delete_regkey_if_empty(key = hk_which, subkey = keyname, permission = KEY_ALL_ACCESS | KEY_WOW64_64KEY)
                    return None
                    return None

