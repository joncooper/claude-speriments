# Source Generated with Decompyle++
# File: nucleus_cdm_relocation.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import NamedTuple, Optional, Text, Tuple
from google.protobuf.empty_pb2 import Empty as EmptyPb
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.model.types import FileId, NsId
from dropbox.proto.nucleus.cdm_relocation_pb2 import CdmJoin, NucleusCdmRelocationArgs
RelocationParameters = NamedTuple('RelocationParameters', [
    ('pre_relocate_root_ns_id', NsId),
    ('pre_relocate_root_ns_fileid', FileId),
    ('post_relocate_root_ns_id', NsId),
    ('team_join', Optional[Tuple[(Text, FileId)]])])

class NucleusCdmRelocationMigration:
    NUCLEUS_IN_PROGRESS_KEY = 'nucleus_cdm_migration_in_progress'
    write_relocation_parameters = (lambda cls = None, config = None, relocation_parameters = classmethod: relocation_args = Noneif relocation_parameters.team_join:
(home_path, home_fileid) = relocation_parameters.team_joinrelocation_args = NucleusCdmRelocationArgs(pre_relocate_root_ns_id = relocation_parameters.pre_relocate_root_ns_id, pre_relocate_root_ns_fileid = relocation_parameters.pre_relocate_root_ns_fileid, post_relocate_root_ns_id = relocation_parameters.post_relocate_root_ns_id, team_join = CdmJoin(post_relocate_home_ns_path = home_path, post_relocate_home_fileid = home_fileid))else:
relocation_args = NucleusCdmRelocationArgs(pre_relocate_root_ns_id = relocation_parameters.pre_relocate_root_ns_id, pre_relocate_root_ns_fileid = relocation_parameters.pre_relocate_root_ns_fileid, post_relocate_root_ns_id = relocation_parameters.post_relocate_root_ns_id, team_leave = EmptyPb())# WARNING: Decompyle incomplete
)()
    get_relocation_parameters = (lambda cls = None, config = None: serialized_string = config.config_dict.get(cls.NUCLEUS_IN_PROGRESS_KEY)if not serialized_string:
Nonerelocation_args = NucleusCdmRelocationArgs()relocation_args.ParseFromString(serialized_string)if relocation_args.HasField('team_join'):
RelocationParameters(pre_relocate_root_ns_id = NsId(relocation_args.pre_relocate_root_ns_id), pre_relocate_root_ns_fileid = FileId(relocation_args.pre_relocate_root_ns_fileid), post_relocate_root_ns_id = NsId(relocation_args.post_relocate_root_ns_id), team_join = (Text(relocation_args.team_join.post_relocate_home_ns_path), FileId(relocation_args.team_join.post_relocate_home_fileid)))RelocationParameters(pre_relocate_root_ns_id = NsId(relocation_args.pre_relocate_root_ns_id), pre_relocate_root_ns_fileid = FileId(relocation_args.pre_relocate_root_ns_fileid), post_relocate_root_ns_id = NsId(relocation_args.post_relocate_root_ns_id), team_join = None))()
    clear_relocation_parameters = (lambda cls = None, config = None: del config.config_dict[cls.NUCLEUS_IN_PROGRESS_KEY])()

