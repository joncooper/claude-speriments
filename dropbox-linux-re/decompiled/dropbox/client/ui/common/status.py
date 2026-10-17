# Source Generated with Decompyle++
# File: status.pyc (Python 3.11)

from __future__ import absolute_import
from dropbox.client.ui.common.strings import UI, UIStrings

class StatusStrings(UIStrings):
    connecting = UI('Connecting...')
    initializing = UI('Starting...')
    pausing = UI('Pausing...')
    moving = UI('Moving Dropbox...')
    importing = UI('Importing photos...', mac = UI('Importing photos...'))
    paused = UI('Syncing paused')
    waiting_for_link = UI('Waiting to be linked to a Dropbox account...')
    low_disk_space = UI("Can't sync (not enough free disk space)")
    updating = UI('Upgrading Dropbox...')
    cant_mount_dropbox = UI("Can't access Dropbox folder")
    cant_unmount_namespace = UI("Can't sync (close all Dropbox files)")
    cant_watch_dropbox = UI("Can't monitor Dropbox folder (Click to fix)")
    reindexing = UI('Indexing...')
    listing = UI('Syncing...')
    migrating = UI('Upgrading database...')
    migrating_sync_engine = UI('Performing one-time update...')
    starting = UI('Starting...')
    selsync = UI('Applying selective sync settings...')
    no_root_permission = UI("Can't sync")
    nil = UI('Up to date')
    rearranging = UI('Updating Dropbox account...')
    connecting_engine = UI('Connecting components...')
    encrypted_folder_enrollment_blocking = UI('Waiting for access to encrypted folders...')
    encrypted_folder_enrollment_non_blocking = UI('Requesting access to encrypted folders...')
    error = UI('')
    syncing_with_errors = UI('')
    files_blocked_by_over_quota = UI('')
    overquota = UI('')
    badge_tooltip_singular = UI('You have {count} unread notification')
    badge_tooltip_plural = UI('You have {count} unread notifications')


class BackupStatusStrings(UIStrings):
    paused = UI('File sync and backups paused')
    low_disk_space = UI("Can't sync or backup (not enough free disk space)")
    listing = UI('Updating files...')
    no_root_permission = UI("Can't update files")

