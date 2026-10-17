# Source Generated with Decompyle++
# File: persist.pyc (Python 3.11)

from build_number.platform import IS_MAC, IS_WINDOWS
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.trace import TRACE
if IS_MAC:
    from Foundation import NSUserDefaults
if IS_WINDOWS:
    from pynt.constants import KEY_ALL_ACCESS, KEY_WOW64_32KEY, REG_DWORD
    from pynt.helpers.registry import create_registry_key, safe_delete_regvalue, set_registry_value
    from six.moves.winreg import HKEY_CURRENT_USER
    from dropbox.win32.win_cache import DROPBOX_REG_KEY
DISABLE_GPU_KEY = 'electron_disable_gpu'

def set_gpu_disabled(disabled = None):
    if IS_MAC:
        
        try:
            defaults = NSUserDefaults.standardUserDefaults()
            if disabled:
                TRACE('Setting disable gpu key for Electron...')
                defaults.setObject_forKey_(True, DISABLE_GPU_KEY)
            else:
                TRACE('Removing disable gpu key for Electron...')
                defaults.removeObjectForKey_(DISABLE_GPU_KEY)
            defaults.synchronize()
            return None
        except Exception:
            TRACE('Unable to set disable gpu user default for Electron...')
            report_exception(severity = Severity.WARN, component = DesktopComponent.ELECTRON)
            return None
            if disabled:
                TRACE('Setting disable gpu flag for Electron...')
                
                try:
                    (key, _, _) = create_registry_key(HKEY_CURRENT_USER, DROPBOX_REG_KEY, permission = KEY_ALL_ACCESS | KEY_WOW64_32KEY, restrict_to_current_user = False)
                    if key:
                        set_registry_value(key, DISABLE_GPU_KEY, REG_DWORD, 1)
                        
                        try:
                            None(None, None)
                        with None:
                            if not None:
                                
                                try:
                                    
                                    try:
                                        return None
                                        return None
                                    except Exception:
                                        TRACE('Unable to set disable gpu registry flag for Electron...')
                                        report_exception(severity = Severity.WARN, component = DesktopComponent.ELECTRON)
                                        return None
                                        TRACE('Removing disable gpu flag for Electron...')
                                        
                                        try:
                                            safe_delete_regvalue(HKEY_CURRENT_USER, DROPBOX_REG_KEY, DISABLE_GPU_KEY, delete_key = True, permission = KEY_ALL_ACCESS | KEY_WOW64_32KEY)
                                            return None
                                        except Exception:
                                            TRACE('Unable to remove disable gpu registry flag for Electron...')
                                            report_exception(severity = Severity.WARN, component = DesktopComponent.ELECTRON)
                                            return None







