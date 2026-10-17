# Source Generated with Decompyle++
# File: rosf_strategy.pyc (Python 3.11)

from typing import Optional
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.client.ui.sync_engine_ui.notification_generator import NotificationGenerator
from dropbox.shared.local_path import LocalPath

class ROSFStrategy:
    
    def __init__(self = None, notif_generator = None):
        self._notif_generator = notif_generator
        self.will_flush_rosf = False
        self.num_rosf_files = 0
        self.last_rosf_local_path = None

    
    def aggregate_rosf_bubble(self = None, num_files_updated = None, last_file_changed = None):
        last_file_changed = self, self.num_rosf_files += num_files_updated, .num_rosf_files
        if not self.will_flush_rosf:
            self.will_flush_rosf = True
            delay = max(self._notif_generator.last_bubble_time_remaining, 1)
            on_ui_thread(f = self._flush_rosf_bubble, delay = delay, debounce = True)()
            return None

    
    def _flush_rosf_bubble(self = None):
        pass
    # WARNING: Decompyle incomplete


