# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import os
from typing import Optional
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.trace import TRACE
if IS_WINDOWS:
    import pywintypes
    from win32api import RegOpenKeyEx, RegQueryValueEx
    from win32con import HKEY_LOCAL_MACHINE, KEY_READ, KEY_WOW64_64KEY, REG_SZ
elif IS_MAC:
    from Foundation import NSUserDefaults

def cert_pinning_disabled():
    nts_team_id = nts_team_id_preference()
    is_disabled = nts_team_id is not None
    if is_disabled:
        TRACE('Certificate pinning disabled: (nts_team_id: %s)' % nts_team_id)
    return is_disabled

NTS_TEAM_ID_PREF_KEY = 'NtsTeamId'

def nts_team_id_preference():
    if IS_WINDOWS:
        
        try:
            key = RegOpenKeyEx(HKEY_LOCAL_MACHINE, 'SOFTWARE\\Dropbox', 0, KEY_READ | KEY_WOW64_64KEY)
            (value, value_type) = RegQueryValueEx(key, NTS_TEAM_ID_PREF_KEY)
            team_id = value if value_type == REG_SZ else None
        except pywintypes.error:
            return None
            if IS_MAC:
                suite_name = '/Library/Preferences/com.getdropbox.dropbox.plist'
                defaults = NSUserDefaults.alloc().initWithSuiteName_(suite_name)
                team_id = defaults.stringForKey_(NTS_TEAM_ID_PREF_KEY)
            elif IS_LINUX:
                preference_file = '/etc/dbx/' + NTS_TEAM_ID_PREF_KEY
                if os.path.exists(preference_file):
                    nts_file = open(preference_file, 'r')
                    team_id = nts_file.read()
                    None(None, None)
                else:
                    with None:
                        if not None:
                            pass
            else:
                return None
            return None

        if not team_id:
            return None
        
        try:
            return int(team_id)
        except ValueError:
            return None


