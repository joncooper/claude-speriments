# Source Generated with Decompyle++
# File: backup_bolt.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import device_sync
from dropbox.api.v2.datatypes import external_drive_backup
from dropbox.api.v2.datatypes import files

class ClientBoltEvent(bb.Union):
    pass
# WARNING: Decompyle incomplete

ClientBoltEvent_validator = bv.Union(ClientBoltEvent)

class BoltEvent(ClientBoltEvent):
    pass
# WARNING: Decompyle incomplete

BoltEvent_validator = bv.Union(BoltEvent)

class ComputerBackupUpdatedDisplayName(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ComputerBackupUpdatedDisplayName_validator = bv.Struct(ComputerBackupUpdatedDisplayName)

class ComputerBackupUpdatedDisplayNameV2(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ComputerBackupUpdatedDisplayNameV2_validator = bv.Struct(ComputerBackupUpdatedDisplayNameV2)

class ExternalDriveBackupUpdatedDisplayName(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ExternalDriveBackupUpdatedDisplayName_validator = bv.Struct(ExternalDriveBackupUpdatedDisplayName)

class GetBoltDataResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetBoltDataResult_validator = bv.Struct(GetBoltDataResult)

class PublishToBoltArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PublishToBoltArg_validator = bv.Struct(PublishToBoltArg)
ClientBoltEvent._cb_updated_display_name_validator = ComputerBackupUpdatedDisplayName_validator
ClientBoltEvent._cb_updated_display_name_v2_validator = ComputerBackupUpdatedDisplayNameV2_validator
ClientBoltEvent._edb_updated_display_name_validator = ExternalDriveBackupUpdatedDisplayName_validator
ClientBoltEvent._other_validator = bv.Void()
ClientBoltEvent._tagmap = {
    'cb_updated_display_name': ClientBoltEvent._cb_updated_display_name_validator,
    'cb_updated_display_name_v2': ClientBoltEvent._cb_updated_display_name_v2_validator,
    'edb_updated_display_name': ClientBoltEvent._edb_updated_display_name_validator,
    'other': ClientBoltEvent._other_validator }
ClientBoltEvent.other = ClientBoltEvent('other')
BoltEvent._cb_updated_validator = device_sync.BackupInfo_validator
BoltEvent._edb_updated_validator = external_drive_backup.ExternalDriveEntry_validator
BoltEvent._tagmap = {
    'cb_updated': BoltEvent._cb_updated_validator,
    'edb_updated': BoltEvent._edb_updated_validator }
BoltEvent._tagmap.update(ClientBoltEvent._tagmap)
ComputerBackupUpdatedDisplayName.device_id.validator = device_sync.DeviceId_validator
ComputerBackupUpdatedDisplayName.display_name.validator = bv.String()
ComputerBackupUpdatedDisplayName.display_name.validator._redact = bv.BlotRedactor(None)
ComputerBackupUpdatedDisplayName._all_field_names_ = set([
    'device_id',
    'display_name'])
ComputerBackupUpdatedDisplayName._all_fields_ = [
    ('device_id', ComputerBackupUpdatedDisplayName.device_id.validator),
    ('display_name', ComputerBackupUpdatedDisplayName.display_name.validator)]
ComputerBackupUpdatedDisplayNameV2.computer_backup_id.validator = files.FileId_validator
ComputerBackupUpdatedDisplayNameV2.display_name.validator = bv.String()
ComputerBackupUpdatedDisplayNameV2.display_name.validator._redact = bv.BlotRedactor(None)
ComputerBackupUpdatedDisplayNameV2._all_field_names_ = set([
    'computer_backup_id',
    'display_name'])
ComputerBackupUpdatedDisplayNameV2._all_fields_ = [
    ('computer_backup_id', ComputerBackupUpdatedDisplayNameV2.computer_backup_id.validator),
    ('display_name', ComputerBackupUpdatedDisplayNameV2.display_name.validator)]
ExternalDriveBackupUpdatedDisplayName.anchor_fileid.validator = files.FileId_validator
ExternalDriveBackupUpdatedDisplayName.display_name.validator = bv.String()
ExternalDriveBackupUpdatedDisplayName.display_name.validator._redact = bv.BlotRedactor(None)
ExternalDriveBackupUpdatedDisplayName._all_field_names_ = set([
    'anchor_fileid',
    'display_name'])
ExternalDriveBackupUpdatedDisplayName._all_fields_ = [
    ('anchor_fileid', ExternalDriveBackupUpdatedDisplayName.anchor_fileid.validator),
    ('display_name', ExternalDriveBackupUpdatedDisplayName.display_name.validator)]
GetBoltDataResult.app_id.validator = bv.String()
GetBoltDataResult.app_id.validator._redact = bv.BlotRedactor(None)
GetBoltDataResult.unique_id.validator = bv.String()
GetBoltDataResult.unique_id.validator._redact = bv.BlotRedactor(None)
GetBoltDataResult.token.validator = bv.String()
GetBoltDataResult.token.validator._redact = bv.BlotRedactor(None)
GetBoltDataResult.revision.validator = bv.String()
GetBoltDataResult.revision.validator._redact = bv.BlotRedactor(None)
GetBoltDataResult._all_field_names_ = set([
    'app_id',
    'unique_id',
    'token',
    'revision'])
GetBoltDataResult._all_fields_ = [
    ('app_id', GetBoltDataResult.app_id.validator),
    ('unique_id', GetBoltDataResult.unique_id.validator),
    ('token', GetBoltDataResult.token.validator),
    ('revision', GetBoltDataResult.revision.validator)]
PublishToBoltArg.event.validator = ClientBoltEvent_validator
PublishToBoltArg._all_field_names_ = set([
    'event'])
PublishToBoltArg._all_fields_ = [
    ('event', PublishToBoltArg.event.validator)]
# WARNING: Decompyle incomplete
