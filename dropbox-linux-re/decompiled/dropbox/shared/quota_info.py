# Source Generated with Decompyle++
# File: quota_info.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional, Tuple

class QuotaEntityData:
    
    def __init__(self = None, *, data_in_use, sync_quota, display_quota):
        self._data_in_use = data_in_use
        self._sync_quota = sync_quota
        self._display_quota = display_quota

    
    def __str__(self = None):
        quota_entity_data_str = f'''quota: {self.sync_quota!r} (display: {self.display_quota!r}), in_use: {self.data_in_use!r}, '''
        return quota_entity_data_str

    
    def __eq__(self = None, other = None):
