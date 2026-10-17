# Source Generated with Decompyle++
# File: sync_engine_status.pyc (Python 3.11)

from typing import Optional
from dropbox.client.status.interface import DownloadStatus, HashStatus, SyncEngineStatus, UploadStatus
from dropbox.client.ui.common.progress import ACTION_DOWNLOADING, ACTION_INDEXING, ACTION_UPLOADING, get_summary_label, get_transfer_status_label
from dropbox.sync_engine_boundary.transfer_status import TransferStatusSnapshot

def get_sync_engine_status(combined_hash = None, combined_upload = None, combined_download = None, *, lansync, initial_hash, includes_backup, percent_complete):
    if not combined_hash and combined_upload or combined_download:
        return None
    (hash_status_str, hash_files, hash_remaining) = get_transfer_status_label(ACTION_INDEXING, combined_hash)
    (upload_status_str, upload_files, upload_remaining) = get_transfer_status_label(ACTION_UPLOADING, combined_upload)
    (download_status_str, download_files, download_remaining) = get_transfer_status_label(ACTION_DOWNLOADING, combined_download, lansync)
    if not hash_status_str and upload_status_str and download_status_str:
        return None
    summary = get_summary_label(seconds = (hash_remaining, upload_remaining, download_remaining), files = (hash_files, upload_files, download_files), last_filenames = (combined_hash.last_filename if hash_files else None, combined_upload.last_filename if upload_files else None, combined_download.last_filename if download_files else None))
    hash_status = None
    if hash_status_str:
        hash_status = HashStatus(label = hash_status_str)
    upload_status = None
    if upload_status_str:
        upload_status = UploadStatus(label = upload_status_str)
    download_status = None
    if not download_status_str and initial_hash:
        download_status = DownloadStatus(label = download_status_str)
    return SyncEngineStatus(summary = summary, hash_snapshot = combined_hash, hash_status = hash_status, upload_snapshot = combined_upload, upload_status = upload_status, download_snapshot = combined_download, download_status = download_status, percent_complete = percent_complete)

