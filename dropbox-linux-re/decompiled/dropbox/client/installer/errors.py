# Source Generated with Decompyle++
# File: errors.pyc (Python 3.11)

from enum import IntEnum, unique
from dropbox.client.ui.common.strings import UI, UIStrings

class InstallerStrings(UIStrings):
    unknown_error = UI('Installation failed. Please remove any files in %(inst_dir)s and try again after restarting your computer.')
    failed_to_kill_old_processes_error = UI('Installation cannot proceed because another instance of Dropbox is already running. Quit any running Dropbox processes, then run the installer again.')
    disk_full_error = UI('Installation failed because your local hard drive is full. Run Disk Cleanup to free at least 1 gigabyte of space, then run the installer again.')
    permission_error = UI('Installation failed. The installer was denied permission to write to the target directory. Please remove any files in %(inst_dir)s and try again.')
    store_managed_install_error = UI('Installation cannot proceed because the Microsoft Store version of Dropbox is currently installed.')
    failed_to_remove_store_managed_install_error = UI('Couldn’t uninstall the Microsoft Store version of Dropbox. To try again, go to the Programs section of your control panel.')

InstallerErrorCode = <NODE:12>()
