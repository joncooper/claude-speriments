# Source Generated with Decompyle++
# File: disk_space_threshold.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Dict, NamedTuple, Text
from dropbox.sync_engine_boundary.constants import MIN_FREE_FRACTION, MIN_FREE_SPACE
BYTES_IN_MB = 1048576
BYTES_IN_GB = 1073741824
LOW_FREE_SPACE = MIN_FREE_SPACE + 1500 * BYTES_IN_MB
LOW_FREE_FRACTION = 1.5 * MIN_FREE_FRACTION
ACCOUNT_SUBFOLDER_SIZE_SELSYNC_TRIGGER_FRACTION = 0.05

def DiskSpaceThreshold():
    '''DiskSpaceThreshold'''
    min_space_mb = (lambda self = None: int(round(float(self.min_space_bytes) / BYTES_IN_MB)))()
    low_space_gb = (lambda self = None: int(round(float(self.low_space_bytes) / BYTES_IN_GB)))()
    
    def to_format_dict(self = None):
        return {
            'min_space_mb': self.min_space_mb,
            'low_space_gb': self.low_space_gb }

    default = (lambda : DiskSpaceThreshold(MIN_FREE_SPACE, LOW_FREE_SPACE, 0))()

DiskSpaceThreshold = <NODE:27>(DiskSpaceThreshold, 'DiskSpaceThreshold', NamedTuple('DiskSpaceThreshold', [
    ('min_space_bytes', int),
    ('low_space_bytes', int),
    ('selsync_size', int)]))
