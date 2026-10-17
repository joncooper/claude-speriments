# Source Generated with Decompyle++
# File: win.pyc (Python 3.11)

import os
import shutil
import stat
from typing import Any, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.sync_event.report import report_sync_event, SyncEventName
from dropbox.trace import TRACE

class HardlinksFixFailedException(Exception):
    pass


def _convert_hardlinks_to_copies_under_path(account = None, path = None):
    links_fixed = 0
    links_failed = 0
    for dir_path, _, file_names in os.walk(path):
        if '.dropbox.cache' in dir_path:
            continue
        for file_name in file_names:
            if file_name == 'Icon\r':
                continue
            abs_path = os.path.join(dir_path, file_name)
            TRACE('Traversing over path: %r', abs_path)
            if os.path.isdir(abs_path):
                TRACE('!! Path is a directory %r', abs_path)
                continue
            st = os.lstat(abs_path)
            if stat.S_ISLNK(st.st_mode):
                TRACE('Skipping symlink in %r', abs_path)
                continue
            if st.st_nlink > 1:
                TRACE('Found hardlink in %r', abs_path)
                temporary_location = os.path.join(dir_path, file_name + '.hardlink.bak')
                if os.path.exists(temporary_location):
                    raise HardlinksFixFailedException('Backup location is occupied.')
                shutil.copy2(abs_path, temporary_location, follow_symlinks = False)
                os.remove(abs_path)
                shutil.move(temporary_location, abs_path)
                links_fixed += 1
            except Exception:
                e = None
                TRACE('Found exception while traversing over path: %r', abs_path)
                report_exception(severity = Severity.DEBUG, component = DesktopComponent.UNKNOWN)
                report_sync_event(SyncEventName.HARDLINK_TO_COPY_FAILED, account = account, path = abs_path, file_name = file_name, error = str(e))
                e = None
                del e
                continue
                e = None
                del e
            report_sync_event(SyncEventName.TURNED_HARDLINKS_TO_COPIES, account = account, number_of_links_fixed = links_fixed, number_of_links_failed_to_fix = links_failed)
            if links_failed:
                raise HardlinksFixFailedException('Unable to fix {} hardlinks out of {}.'.format(links_failed, links_failed + links_fixed))
            return None


def convert_hardlinks_to_copies_in_dropbox(app, account):
    local_config = app.config_manager.local_config(account)
    path = local_config.config_dict.get('dropbox_path')
    if not path:
        TRACE("!! User hasn't picked their Dropbox location, so we can't fix hardlinks yet.")
        return None
    return _convert_hardlinks_to_copies_under_path(account, path)

