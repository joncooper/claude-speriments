# Source Generated with Decompyle++
# File: tray_preferences_menu_utils.pyc (Python 3.11)

from typing import Dict, List, Text
from dropbox.client.features.sync_everything.view_model.bridge_gen.bridge_interface_folder_status import FolderStatusBridgeInterface
from dropbox.client.features.sync_everything.view_model.bridge_gen.folder_status_type import FolderStatusType
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.client.ui.common.strings import UI, UIStrings

class BackupDisableDialogFolderStrings(UIStrings):
    DESKTOP = UI('Desktop')
    DOCUMENTS = UI('Documents')
    PICTURES = UI('Pictures')
    MUSIC = UI('Music')
    VIDEOS = UI('Videos')
    MOVIES = UI('Movies')
    SCREENSHOTS = UI('Screenshots')
    DOWNLOADS = UI('Downloads')


def _get_folder_display_name(folder_id = None):
    mapping = {
        'DESKTOP': BackupDisableDialogFolderStrings.DESKTOP,
        'DOCUMENTS': BackupDisableDialogFolderStrings.DOCUMENTS,
        'DOWNLOADS': BackupDisableDialogFolderStrings.DOWNLOADS,
        'PICTURES': BackupDisableDialogFolderStrings.PICTURES,
        'MUSIC': BackupDisableDialogFolderStrings.MUSIC,
        'VIDEOS': BackupDisableDialogFolderStrings.VIDEOS,
        'MOVIES': BackupDisableDialogFolderStrings.MOVIES,
        'SCREENSHOTS': BackupDisableDialogFolderStrings.SCREENSHOTS }
    return mapping.get(folder_id, folder_id)


def check_folder_status(folder_map = None, status = None):
    for folder_id, folder_status in folder_map.items():
        if folder_status.status == status:
            return True
        return False


def folder_has_advisory_error(folder_status = None):
