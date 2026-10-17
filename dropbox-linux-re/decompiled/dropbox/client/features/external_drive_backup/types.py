# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from dataclasses import dataclass
from enum import auto, Enum
from typing import Callable, List, NamedTuple, Optional, Tuple
from dropbox.client.features.external_drive_backup.constants import BROKEN_ERROR_STATES
from dropbox.client.features.external_drive_backup.fission_migration_info import SeamlessFissionMigrationInfo, SeamlessFissionMigrationState
from dropbox.model.types import FileId
from dropbox.repr_utils import easy_repr
from dropbox.sync_engine_boundary.types import DeviceAnchorInfo, DeviceAnchorState, ErredDeviceAnchorInfo

class SeparatedAnchorsByState:
    
    def __init__(self = None, erred_device_anchors = None, valid_device_anchors = None, is_fission_engine = ('erred_device_anchors', 'List[ErredDeviceAnchorInfo]', 'valid_device_anchors', 'List[DeviceAnchorInfo]', 'is_fission_engine', 'bool', 'return', 'None')):
        self._erred_device_anchors = erred_device_anchors
        self._valid_device_anchors = valid_device_anchors
        self.is_fission_engine = is_fission_engine
        self._non_broken_device_anchors = None
        self._broken_device_anchors = None

    generate_empty_fission_response = (lambda : SeparatedAnchorsByState(valid_device_anchors = [], erred_device_anchors = [], is_fission_engine = True))()
    generate_empty_fss_response = (lambda : SeparatedAnchorsByState(valid_device_anchors = [], erred_device_anchors = [], is_fission_engine = False))()
    valid_device_anchors = (lambda self = None: self._valid_device_anchors)()
    erred_device_anchors = (lambda self = None: self._erred_device_anchors)()
    non_broken_device_anchors = (lambda self = None: if not self._non_broken_device_anchors:
self._non_broken_device_anchors = self._compute_nonbroken_anchors(self._valid_device_anchors)self._non_broken_device_anchors)()
    broken_device_anchors = (lambda self = None: if not self._broken_device_anchors:
self._broken_device_anchors = self._compute_broken_anchors(self._valid_device_anchors)self._broken_device_anchors)()
    
    def get_all_anchors(self = None):
        return self.broken_device_anchors + self.non_broken_device_anchors

    
    def get_drive_info_from_uuid(self = None, uuid = None):
        for anchor_info in self.non_broken_device_anchors:
            if anchor_info.target_uuid == uuid:
                
                return None, anchor_info
            for None in self.broken_device_anchors:
                if anchor_info.target_uuid == uuid:
                    
                    return None, anchor_info
                return None

    
    def __repr__(self = None):
        return easy_repr(self, 'valid_device_anchors', 'erred_device_anchors')

    _compute_broken_anchors = (lambda valid_anchors = None: broken_device_anchors = valid_anchors()broken_device_anchors)()
    _compute_nonbroken_anchors = (lambda valid_anchors = None: non_broken_device_anchors = valid_anchors()non_broken_device_anchors)()


class SeparatedAnchorsByEngineAndState(NamedTuple):
    fission_device_anchors: 'SeparatedAnchorsByState' = 'SeparatedAnchorsByEngineAndState'
    generate_empty_response = (lambda : SeparatedAnchorsByEngineAndState(fss_device_anchors = SeparatedAnchorsByState.generate_empty_fss_response(), fission_device_anchors = SeparatedAnchorsByState.generate_empty_fission_response()))()
    
    def _search_with_preference(self = None, search_predicate = None):
        for fiz_valid in self.get_fission_non_broken():
            if search_predicate(fiz_valid):
                
                return None, (fiz_valid, False)
            for None in self.get_fss_non_broken():
                if search_predicate(fss_valid):
                    
                    return None, (fss_valid, True)
                for None in self.get_fission_broken():
                    if search_predicate(fiz_broken):
                        
                        return None, (fiz_broken, False)
                    for None in self.get_fss_broken():
                        if search_predicate(fss_broken):
                            
                            return None, (fss_broken, True)
                        return (None, False)

    
    def _search_with_preference_by_uuid(self = None, drive_uuid = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _search_with_preference_by_fileid(self = None, fileid = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_fission_non_broken(self = None):
        return self.fission_device_anchors.non_broken_device_anchors

    
    def get_fission_valid(self = None):
        return self.fission_device_anchors.valid_device_anchors

    
    def get_fission_broken(self = None):
        return self.fission_device_anchors.broken_device_anchors

    
    def get_fission_erred(self = None):
        return self.fission_device_anchors.erred_device_anchors

    
    def get_all_valid_fission(self = None):
        return self.fission_device_anchors.non_broken_device_anchors + self.fission_device_anchors.broken_device_anchors

    
    def do_any_valid_fission_anchors_exist(self = None):
        return len(self.fission_device_anchors.valid_device_anchors) > 0

    
    def do_any_erred_fission_anchors_exist(self = None):
        return len(self.fission_device_anchors.erred_device_anchors) > 0

    
    def do_any_fission_anchors_exist(self = None):
