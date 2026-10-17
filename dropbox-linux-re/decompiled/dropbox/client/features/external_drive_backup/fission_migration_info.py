# Source Generated with Decompyle++
# File: fission_migration_info.pyc (Python 3.11)

from enum import auto, Enum
from typing import Dict, Optional
from uuid import UUID
from dropbox.api.v2.datatypes.external_drive_backup import SeamlessFissionMigrationStateEnum
from dropbox.model.types import FileId
from dropbox.repr_utils import easy_repr

class FissionMigrationStatus(Enum):
    NOT_MIGRATED = auto()
    BROKEN = auto()
    ERROR_STATE_ON_BREAK_ATTEMPT = auto()
    MIGRATED = auto()


class FissionMigrationInfo:
    
    def __init__(self = None, migration_status = None, fileid = None, drive_capcity = ('migration_status', 'FissionMigrationStatus', 'fileid', 'FileId', 'drive_capcity', 'Optional[int]', 'return', 'None')):
        self.migration_status = migration_status
        self.fileid = fileid
        self.drive_capcity = drive_capcity

    
    def __repr__(self = None):
        return easy_repr(self, 'drive_capcity', 'fileid', 'migration_status')



class FissionPostMigrationChoice(Enum):
    KEEP_BOTH = auto()
    DELETE = auto()


class SeamlessFissionMigrationState(Enum):
    UNKNOWN = 0
    NOT_MIGRATED = 1
    MIGRATION_STARTED = 2
    SETUP_MIGRATION_COMPLETE = 3
    FISSION_PAUSED_ANCHOR_CREATED = 4
    FISSION_MOVE_STARTED = 5
    FISSION_COPY_STARTED = 6
    FISSION_UNPAUSED_ANCHOR = 12
    FSS_ANCHOR_BREAK_COMPLETE = 7
    FSS_ANCHOR_DELETE_COMPLETE = 8
    FISSION_MOVE_COMPLETE = 9
    FISSION_COPY_COMPLETE = 10
    MIGRATION_COMPLETE = 11
    ABORTED = 13
    ABORTED_BROKEN = 14
    BASIC_MIGRATION_STARTED = 15
    BASIC_MIGRATION_FSS_ANCHOR_BREAK_COMPLETE = 16
    BASIC_MIGRATION_MIGRATION_COMPLETE = 17
    state_order = (lambda : pass# WARNING: Decompyle incomplete
)()
    from_local_to_api = (lambda cls = None, backup_state = None: if backup_state == SeamlessFissionMigrationState.UNKNOWN:
SeamlessFissionMigrationStateEnum.unknownif None == SeamlessFissionMigrationState.NOT_MIGRATED:
SeamlessFissionMigrationStateEnum.not_migratedif None == SeamlessFissionMigrationState.MIGRATION_STARTED:
SeamlessFissionMigrationStateEnum.migration_startedif None == SeamlessFissionMigrationState.SETUP_MIGRATION_COMPLETE:
SeamlessFissionMigrationStateEnum.setup_migration_completeif None == SeamlessFissionMigrationState.FISSION_PAUSED_ANCHOR_CREATED:
SeamlessFissionMigrationStateEnum.fission_paused_anchor_createdif None == SeamlessFissionMigrationState.FISSION_MOVE_STARTED:
SeamlessFissionMigrationStateEnum.fission_move_startedif None == SeamlessFissionMigrationState.FISSION_COPY_STARTED:
SeamlessFissionMigrationStateEnum.fission_copy_startedif None == SeamlessFissionMigrationState.FISSION_UNPAUSED_ANCHOR:
SeamlessFissionMigrationStateEnum.fission_unpaused_anchorif None == SeamlessFissionMigrationState.FSS_ANCHOR_BREAK_COMPLETE:
SeamlessFissionMigrationStateEnum.fss_anchor_break_completeif None == SeamlessFissionMigrationState.FSS_ANCHOR_DELETE_COMPLETE:
SeamlessFissionMigrationStateEnum.fss_anchor_delete_completeif None == SeamlessFissionMigrationState.FISSION_MOVE_COMPLETE:
SeamlessFissionMigrationStateEnum.fission_move_completeif None == SeamlessFissionMigrationState.FISSION_COPY_COMPLETE:
SeamlessFissionMigrationStateEnum.fission_copy_completeif None == SeamlessFissionMigrationState.MIGRATION_COMPLETE:
SeamlessFissionMigrationStateEnum.migration_completeif None == SeamlessFissionMigrationState.ABORTED:
SeamlessFissionMigrationStateEnum.abortedif None == SeamlessFissionMigrationState.ABORTED_BROKEN:
SeamlessFissionMigrationStateEnum.aborted_brokenif None == SeamlessFissionMigrationState.BASIC_MIGRATION_STARTED:
SeamlessFissionMigrationStateEnum.basic_migration_startedif None == SeamlessFissionMigrationState.BASIC_MIGRATION_FSS_ANCHOR_BREAK_COMPLETE:
SeamlessFissionMigrationStateEnum.basic_migration_fss_anchor_break_completeif None == SeamlessFissionMigrationState.BASIC_MIGRATION_MIGRATION_COMPLETE:
SeamlessFissionMigrationStateEnum.basic_migration_migration_completeNone.unknown)()
    from_api_to_local = (lambda cls = None, backup_state = None: if backup_state == SeamlessFissionMigrationStateEnum.unknown:
SeamlessFissionMigrationState.UNKNOWNif None == SeamlessFissionMigrationStateEnum.not_migrated:
SeamlessFissionMigrationState.NOT_MIGRATEDif None == SeamlessFissionMigrationStateEnum.migration_started:
SeamlessFissionMigrationState.MIGRATION_STARTEDif None == SeamlessFissionMigrationStateEnum.setup_migration_complete:
SeamlessFissionMigrationState.SETUP_MIGRATION_COMPLETEif None == SeamlessFissionMigrationStateEnum.fission_paused_anchor_created:
SeamlessFissionMigrationState.FISSION_PAUSED_ANCHOR_CREATEDif None == SeamlessFissionMigrationStateEnum.fission_move_started:
SeamlessFissionMigrationState.FISSION_MOVE_STARTEDif None == SeamlessFissionMigrationStateEnum.fission_copy_started:
SeamlessFissionMigrationState.FISSION_COPY_STARTEDif None == SeamlessFissionMigrationStateEnum.fission_unpaused_anchor:
SeamlessFissionMigrationState.FISSION_UNPAUSED_ANCHORif None == SeamlessFissionMigrationStateEnum.fss_anchor_break_complete:
SeamlessFissionMigrationState.FSS_ANCHOR_BREAK_COMPLETEif None == SeamlessFissionMigrationStateEnum.fss_anchor_delete_complete:
SeamlessFissionMigrationState.FSS_ANCHOR_DELETE_COMPLETEif None == SeamlessFissionMigrationStateEnum.fission_move_complete:
SeamlessFissionMigrationState.FISSION_MOVE_COMPLETEif None == SeamlessFissionMigrationStateEnum.fission_copy_complete:
SeamlessFissionMigrationState.FISSION_COPY_COMPLETEif None == SeamlessFissionMigrationStateEnum.migration_complete:
SeamlessFissionMigrationState.MIGRATION_COMPLETEif None == SeamlessFissionMigrationStateEnum.aborted:
SeamlessFissionMigrationState.ABORTEDif None == SeamlessFissionMigrationStateEnum.aborted_broken:
SeamlessFissionMigrationState.ABORTED_BROKENif None == SeamlessFissionMigrationStateEnum.basic_migration_started:
SeamlessFissionMigrationState.BASIC_MIGRATION_STARTEDif None == SeamlessFissionMigrationStateEnum.basic_migration_fss_anchor_break_complete:
SeamlessFissionMigrationState.BASIC_MIGRATION_FSS_ANCHOR_BREAK_COMPLETEif None == SeamlessFissionMigrationStateEnum.basic_migration_migration_complete:
SeamlessFissionMigrationState.BASIC_MIGRATION_MIGRATION_COMPLETENone.UNKNOWN)()
    
    def __lt__(self = None, other = None):
        our_index = self.state_order()[self]
        other_index = self.state_order()[other]
        return our_index < other_index

    
    def __gt__(self = None, other = None):
        our_index = self.state_order()[self]
        other_index = self.state_order()[other]
        return our_index > other_index

    
    def __le__(self = None, other = None):
        if self.value == other.value:
            return True
        return None.__lt__(other)

    
    def __ge__(self = None, other = None):
        if self.value == other.value:
            return True
        return None.__gt__(other)

    
    def is_migration_started(self = None):
        return self > SeamlessFissionMigrationState.NOT_MIGRATED

    
    def is_after_move_started(self = None):
        return self >= SeamlessFissionMigrationState.FISSION_MOVE_STARTED

    
    def is_before_move_started(self = None):
        return self < SeamlessFissionMigrationState.FISSION_MOVE_STARTED

    
    def is_in_finalized_state(self = None):
        return self in (SeamlessFissionMigrationState.MIGRATION_COMPLETE, SeamlessFissionMigrationState.ABORTED, SeamlessFissionMigrationState.ABORTED_BROKEN, SeamlessFissionMigrationState.BASIC_MIGRATION_MIGRATION_COMPLETE)

    
    def is_migration_started_but_before_move(self = None):
        return self in (SeamlessFissionMigrationState.MIGRATION_STARTED, SeamlessFissionMigrationState.SETUP_MIGRATION_COMPLETE, SeamlessFissionMigrationState.FISSION_PAUSED_ANCHOR_CREATED)

    
    def is_in_basic_migration_flow(self = None):
        return self in (SeamlessFissionMigrationState.BASIC_MIGRATION_STARTED, SeamlessFissionMigrationState.BASIC_MIGRATION_FSS_ANCHOR_BREAK_COMPLETE, SeamlessFissionMigrationState.BASIC_MIGRATION_MIGRATION_COMPLETE)

    
    def is_eligible_for_basic_migration(self = None):
