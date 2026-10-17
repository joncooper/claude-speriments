# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
if IS_LINUX:
    from linux import debug_list_drives, listen_to_external_drive_events
    return None
if None:
    from mac import debug_list_drives, listen_to_external_drive_events
    return None
if None:
    from windows import debug_list_drives, listen_to_external_drive_events
    return None
