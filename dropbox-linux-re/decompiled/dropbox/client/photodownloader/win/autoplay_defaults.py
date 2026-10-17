# Source Generated with Decompyle++
# File: autoplay_defaults.pyc (Python 3.11)

from __future__ import absolute_import
import os
from pprint import pformat
from pynt.constants import KEY_ALL_ACCESS, KEY_READ, KEY_WOW64_64KEY
from pynt.helpers.registry import create_registry_key, delete_registry_tree, enum_registry_subkeys, enum_registry_subkeys_as_keys, enum_registry_values, REG_SZ, registry_key, safe_read_registry_value, set_registry_value
from six import iteritems
from six.moves.winreg import HKEY_CURRENT_USER as HKCU
from dropbox.client.photodownloader.win.constants import AUTOPLAY_KEY, DROPBOX_AUTOPLAY_HANDLER_NAME, OLD_VOLUME_EVENT_DEFAULTS, VOLUME_EVENT_DEFAULTS, VOLUME_EVENTS, WIN8_VOLUME_EVENT_DEFAULTS
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.trace import TRACE
AUTOPLAY_DEFAULTS_KEY = os.path.join(AUTOPLAY_KEY, 'UserChosenExecuteHandlers')
AUTOPLAY_KNOWNDEVICES_KEY = os.path.join(AUTOPLAY_KEY, 'KnownDevices')
IMAGING_DEVICE_CLSGUID = '{6bdd1fc6-810f-11d0-bec7-08002be2092f}'
MASS_STORAGE_CLSGUID = '{10497b1b-ba51-44e5-8318-a65c837b6661}'
GUID_DEVINTERFACE_WPD1 = '{6ac27878-a6fa-4155-ba85-f98f491d4f33}'
GUID_DEVINTERFACE_WPD2 = '{f33fdc04-d1ac-4e8e-9a30-19bbd4b108ae}'
IMAGING_INTERFACES = (IMAGING_DEVICE_CLSGUID, MASS_STORAGE_CLSGUID, GUID_DEVINTERFACE_WPD1, GUID_DEVINTERFACE_WPD2)
DROPBOX_AUTOPLAY_HANDLERS = (DROPBOX_AUTOPLAY_HANDLER_NAME,)

def change_autoplay_default(event, handler):
    chosen_handlers_key = os.path.join(AUTOPLAY_DEFAULTS_KEY, event)
    (key, _, _) = create_registry_key(HKCU, chosen_handlers_key)
    set_registry_value(key, '', REG_SZ, handler)
    None(None, None)
    return None
    with None:
        if not None:
            pass


def get_device_name(device_id):
    name = device_id
    dev = registry_key(HKCU, os.path.join(AUTOPLAY_KNOWNDEVICES_KEY, device_id))
    if dev:
        name = safe_read_registry_value(dev, 'Label')
    None(None, None)


def get_single_default_win7(event_name, device_name = (None,)):
    defaults_key = registry_key(HKCU, AUTOPLAY_DEFAULTS_KEY)
# WARNING: Decompyle incomplete


def get_autoplay_defaults():
    defaults = get_autoplay_defaults_xp()
    defaults.update(get_autoplay_defaults_win7())
    return defaults


def get_autoplay_defaults_xp():
    ret = { }
    
    try:
        defaults_key = registry_key(HKCU, AUTOPLAY_DEFAULTS_KEY)
        if defaults_key:
            for subkey in enum_registry_values(defaults_key):
                if subkey:
                    name = subkey.split('+')[-1]
                    value = safe_read_registry_value(defaults_key, subkey)
                    if value:
                        ret[subkey] = (name, value)
                
                try:
                    None(None, None)
                with None:
                    if not None:
                        
                        try:
                            
                            try:
                                pass
                            except Exception:
                                report_exception(component = DesktopComponent.SYNC_EVERYTHING)

                            return ret





def get_autoplay_defaults_win7(only_check_these_keys = (None,)):
    ret = { }
    
    try:
        defaults_key = registry_key(HKCU, AUTOPLAY_DEFAULTS_KEY)
        if not defaults_key:
            
            try:
                None(None, None)
                return 
                for subkey_name, subkey in enum_registry_subkeys_as_keys(defaults_key):
                    ret.update(_check_one_key(subkey, subkey_name, only_check_these_keys))
                    for subsubkey_name, subsubkey in enum_registry_subkeys_as_keys(subkey):
                        subsubkey_name = os.path.join(subkey_name, subsubkey_name)
                        ret.update(_check_one_key(subsubkey, subsubkey_name, only_check_these_keys))
                        
                        try:
                            None(None, None)
                        with None:
                            if not None, ret:
                                
                                try:
                                    
                                    try:
                                        pass
                                    except Exception:
                                        report_exception(component = DesktopComponent.SYNC_EVERYTHING)

                                    return ret






def _check_one_key(key, key_name, only_check_these_keys):
    ret = { }
# WARNING: Decompyle incomplete


def is_imaging_device(device_key):
    interfaces_key = registry_key(device_key, 'KnownInterfaces')
    if interfaces_key:
        for interface in enum_registry_values(interfaces_key):
            clsguid = interface.lower().split('#')[-1]
            if clsguid in IMAGING_INTERFACES:
                None(None, None)
                return True
            None(None, None)
        with None:
            if not None:
                pass
    return False

set_dropbox_default_autoplay = (lambda : events = list(VOLUME_EVENT_DEFAULTS)for device_id, device_name in known_imaging_devices():
TRACE('Setting Dropbox as the default handler for %r', device_name)events.append(device_id)set_default_by_event(events)events)()

def known_imaging_devices():
    pass
# WARNING: Decompyle incomplete


def set_default_by_event(events):
    autoplay_handler = DROPBOX_AUTOPLAY_HANDLER_NAME
    for event in events:
        keyname = os.path.join(AUTOPLAY_DEFAULTS_KEY, event)
        (event_key, _, _) = create_registry_key(HKCU, keyname, permission = KEY_ALL_ACCESS)
        if not event_key:
            raise Exception('Registry error: failed to create key %s', keyname)
        if not set_registry_value(event_key, None, REG_SZ, autoplay_handler):
            raise Exception(f'''Registry error: could not set default property of {keyname!s} to {autoplay_handler!s}''')
        TRACE('Set default autoplay handler of %s to %s', event, autoplay_handler)
        None(None, None)
    with None:
        if not None:
            pass
    continue
    except Exception:
        report_exception(component = DesktopComponent.SYNC_EVERYTHING)
        continue

set_old_default_autoplay = (lambda old_handlers, device = (None,): events = []if device:
TRACE('Resetting autoplay default for single device: %r', device.id)event = device.formatted_device_id()events.append((event, os.path.join(AUTOPLAY_DEFAULTS_KEY, event)))else:
try:
defaults_key = registry_key(HKCU, AUTOPLAY_DEFAULTS_KEY, permission = KEY_ALL_ACCESS)if defaults_key:
for event in enum_registry_subkeys(defaults_key):
events.append((event, os.path.join(AUTOPLAY_DEFAULTS_KEY, event)))try:
None(None, None)with None:
if not None:
try:
try:
passexcept Exception:
report_exception(component = DesktopComponent.SYNC_EVERYTHING)if events:
reset_devices(events, old_handlers)NoneNone)()

def reset_devices(events, old_handlers):
    pass
# WARNING: Decompyle incomplete


def any_volume_defaults_are_dropbox():
    for event in VOLUME_EVENTS:
        keyname = os.path.join(AUTOPLAY_DEFAULTS_KEY, event)
        event_key = registry_key(HKCU, keyname, permission = KEY_READ | KEY_WOW64_64KEY)
        if not event_key:
            None(None, None)
            continue
        cur_handler = safe_read_registry_value(event_key, None)
        if cur_handler in DROPBOX_AUTOPLAY_HANDLERS:
            TRACE('any_volume_defaults_are_dropbox: Handler for %s is %r. Returning True!', event, cur_handler)
            None(None, None)
            return True
        None(None, None)
    with None:
        if not None:
            pass
    continue
    except Exception:
        report_exception(component = DesktopComponent.SYNC_EVERYTHING)
        continue
    defaults_key = registry_key(HKCU, AUTOPLAY_DEFAULTS_KEY)
    if not defaults_key:
        None(None, None)
        return False
    for subkey in enum_registry_values(defaults_key):
        if not subkey:
            continue
        name = subkey.split('+')[-1]
        if name in VOLUME_EVENTS:
            cur_handler = safe_read_registry_value(defaults_key, subkey)
            if cur_handler in DROPBOX_AUTOPLAY_HANDLERS:
                TRACE('any_volume_defaults_are_dropbox: Handler for %s is %r. Returning True!', subkey, cur_handler)
                None(None, None)
                return True
            None(None, None)
        else:
            with None:
                if not None:
                    pass
    return False


def update_autoplay_defaults(previously_set_defaults):
    TRACE('PHOTOUPLOADER: Previously set defaults=%s', pformat(previously_set_defaults))
    previously_set_defaults = set(previously_set_defaults) if previously_set_defaults else set()
    new_defaults = []
    old_defaults = { }
    for device_id, device_name in known_imaging_devices():
        if device_id in previously_set_defaults:
            continue
        TRACE('PHOTOUPLOADER: Found new camera %r id %r', device_name, device_id)
        new_defaults.append(device_id)
        current_default = get_single_default_win7(device_id, device_name)
        if current_default:
            old_defaults[device_id] = current_default
        new_win8_defaults = set(WIN8_VOLUME_EVENT_DEFAULTS) - previously_set_defaults
        old_defaults.update(get_autoplay_defaults_win7(only_check_these_keys = new_win8_defaults))
        new_defaults.extend(new_win8_defaults)
        TRACE("PHOTOUPLOADER: Found autoplay defaults we haven't overwritten: %s, old settings: %s", pformat(new_defaults), pformat(old_defaults))
        set_default_by_event(new_defaults)
        new_defaults.extend(list(set(OLD_VOLUME_EVENT_DEFAULTS) - previously_set_defaults))
        return (old_defaults, new_defaults)


def any_defaults_are_dropbox():
    defaults = get_autoplay_defaults()
    defaults_they_cant_change = set(VOLUME_EVENTS).difference(set(VOLUME_EVENT_DEFAULTS))
    for event_name, default_handler in iteritems(defaults):
        if default_handler in DROPBOX_AUTOPLAY_HANDLERS and event not in defaults_they_cant_change:
            return True
        return False

