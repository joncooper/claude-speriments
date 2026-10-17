# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from typing import Dict, Text
from pynt.constants import E_ACCESS_DENIED, E_FILE_NOT_FOUND, E_PATH_NOT_FOUND, FOLDERID_Desktop, FOLDERID_Documents, FOLDERID_Downloads, FOLDERID_Music, FOLDERID_Pictures, FOLDERID_Videos
from pynt.helpers.shell import shell_get_known_folder_path
from  import UserFolderPathKeys, UserFolderPaths
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import convert_to_twos_complement
from dropbox.trace import TRACE

class UserFolderPathsWindows(UserFolderPaths):
    
    def paths_dict(self = None):
        folder_ids = {
            UserFolderPathKeys.DOWNLOADS: FOLDERID_Downloads,
            UserFolderPathKeys.VIDEOS: FOLDERID_Videos,
            UserFolderPathKeys.MUSIC: FOLDERID_Music,
            UserFolderPathKeys.PICTURES: FOLDERID_Pictures,
            UserFolderPathKeys.DESKTOP: FOLDERID_Desktop,
            UserFolderPathKeys.DOCUMENTS: FOLDERID_Documents }
        paths = { }
        for key in folder_ids:
            paths[key] = shell_get_known_folder_path(folder_ids[key])
            except WindowsError:
                e = None
                error_code = convert_to_twos_complement(e.winerror)
                if error_code in (E_PATH_NOT_FOUND, E_FILE_NOT_FOUND):
                    TRACE('!! Path not found for %s folder', key)
                elif error_code == E_ACCESS_DENIED:
                    TRACE('!! Access denied for %s folder', key)
                else:
                    report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)
                e = None
                del e
                continue
                e = None
                del e
            except Exception:
                report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)
                continue
            return paths


