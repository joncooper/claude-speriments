# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional
from dropbox.exception.reporting import report_bad_assumption
from dropbox.sync_engine_boundary.types.local_props import DBXIconType
from dropbox.sync_engine_boundary.types.location_props import LocationProperties

class FolderTag(object):
    __module__ = __name__
    __qualname__ = 'FolderTag'
    CAMERA_UPLOADS = 'camerauploads'
    DROPBOX = 'dropbox'
    SANDBOX = 'sandbox'
    SHARED = 'shared'
    SHARED_READ_ONLY = 'shared_read_only'
    SHARED_VIEW_NAME_ONLY = 'shared_view_name_only'
    TEAM_FOLDER = 'team_folder'
    TEAM_FOLDER_READ_ONLY = 'team_folder_read_only'
    TEAM_MEMBER_FOLDER = 'team_member_folder'
    STANDARD_FOLDER = 'folder'
    DEVICE_FOLDER_MAC = 'device_folder_mac'
    DEVICE_FOLDER_WIN = 'device_folder_win'
    DEVICE_FOLDER_GENERIC = 'device_folder_generic'
    DEVICE_FOLDER_DESKTOP = 'device_folder_desktop'
    DEVICE_FOLDER_DOCUMENTS = 'device_folder_documents'
    DEVICE_FOLDER_DOWNLOADS = 'device_folder_downloads'
    DEVICE_FOLDER_PICTURES = 'device_folder_pictures'
    DEVICE_FOLDER_MUSIC = 'device_folder_music'
    DEVICE_FOLDER_VIDEOS = 'device_folder_videos'
    VAULT = 'vault'
    FAMILY_SHARED_FOLDER = 'family_shared_folder'
    ENCRYPTED_TEAM_FOLDER = 'encrypted_team_folder'
    ALL_TAGS = {
        CAMERA_UPLOADS,
        DROPBOX,
        SANDBOX,
        SHARED,
        SHARED_READ_ONLY,
        SHARED_VIEW_NAME_ONLY,
        TEAM_FOLDER,
        TEAM_FOLDER_READ_ONLY,
        TEAM_MEMBER_FOLDER,
        ENCRYPTED_TEAM_FOLDER}
    ALL_READ_ONLY_TAGS = {
        SHARED_READ_ONLY,
        SHARED_VIEW_NAME_ONLY,
        TEAM_FOLDER_READ_ONLY}
    SERVER_ICON_MAPPING = {
        'folder_user': SHARED,
        'folder_team': TEAM_FOLDER,
        'folder_team_locked': TEAM_FOLDER_READ_ONLY,
        'folder_user_locked': SHARED_READ_ONLY,
        'folder': STANDARD_FOLDER,
        'folder_team_member': TEAM_MEMBER_FOLDER,
        'folder_user_no_access': SHARED_VIEW_NAME_ONLY,
        'folder_app': SANDBOX,
        'folder_camera': CAMERA_UPLOADS }
# WARNING: Decompyle incomplete

