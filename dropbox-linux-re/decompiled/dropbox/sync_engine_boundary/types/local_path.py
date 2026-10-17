# Source Generated with Decompyle++
# File: local_path.pyc (Python 3.11)

from typing import NamedTuple, Union
from dropbox.model.types import FileId, NsId
from dropbox.proto.nucleus.common_api_types_pb2 import LookupByLocalPathReply
from dropbox.shared.server_path import MRCasedServerPath, RRCasedServerPath
from dropbox.sync_engine_boundary.exceptions import NucleusProtoException
from dropbox.sync_engine_boundary.types.shortest_fileid_path import ShortestFileIdPath

class DBXValid(NamedTuple):
    dbx_validity: 'Union[FileId, Exception]' = 'DBXValid'
    from_proto = (lambda dbx_valid = None, root_ns = None: mr_server_path = MRCasedServerPath.from_ns_rel(dbx_valid.mr_server_path.ns_id, dbx_valid.mr_server_path.rel)rr_server_path = RRCasedServerPath.from_ns_rel(root_ns, dbx_valid.rr_server_path.path)if dbx_valid.HasField('tracked'):
dbx_validity = FileId(dbx_valid.tracked.id)elif dbx_valid.HasField('untracked'):
dbx_validity = UntrackedPathException(ShortestFileIdPath.from_proto(dbx_valid.untracked))elif dbx_valid.HasField('ignored_descendant'):
dbx_validity = IgnoredDescendantException(ShortestFileIdPath.from_proto(dbx_valid.ignored_descendant.ignored_root), ShortestFileIdPath.from_proto(dbx_valid.ignored_descendant.ignored_root_parent))elif dbx_valid.HasField('sustained_filesystem_errors'):
dbx_validity = SustainedFilesystemErrorsException(ShortestFileIdPath.from_proto(dbx_valid.sustained_filesystem_errors))else:
dbx_validity = NucleusProtoException(f'''Unexpected dbx_valid_path from Nucleus: {dbx_valid}''')DBXValid(mr_server_path, rr_server_path, dbx_validity))()


class LocalPathProperties(NamedTuple):
    fs_validity: "Union[DBXValid, 'InvalidDropboxPathException', NucleusProtoException]" = 'LocalPathProperties'
    from_proto = (lambda proto = None, root_ns = None: if proto.HasField('fsvalid'):
fsvalid = proto.fsvalidif fsvalid.HasField('inside_dropbox'):
inside_dropbox = proto.fsvalid.inside_dropboxif inside_dropbox.HasField('dbx_valid_path'):
fs_validity = DBXValid.from_proto(proto.fsvalid.inside_dropbox.dbx_valid_path, root_ns)else:
invalid = inside_dropbox.dbx_invalid_pathif invalid.HasField('filename_error'):
fs_validity = InvalidDropboxFilenameException(invalid.filename_error)elif invalid.HasField('unimportant'):
fs_validity = UnimportantDropboxFilenameException()else:
fs_validity = NucleusProtoException(f'''Unexpected dbx_invalid_path from Nucleus: {invalid}''')elif fsvalid.HasField('deleted_file'):
fs_validity = DeletedFileLocationException()elif fsvalid.HasField('in_engine_temp_dir'):
fs_validity = EngineTempDirException()elif fsvalid.HasField('outside_dropbox'):
fs_validity = OutsideDropboxException()else:
fs_validity = NucleusProtoException(f'''Unexpected fsvalid from Nucleus: {fsvalid}''')elif proto.HasField('fsinvalid'):
fs_validity = FSInvalidPathException()else:
fs_validity = NucleusProtoException(f'''Unexpected LookupByLocalPathReply from Nucleus: {proto}''')LocalPathProperties(fs_validity))()
    
    def fileid(self = None):
        if isinstance(self.fs_validity, Exception):
            raise self.fs_validity
        if isinstance(self.fs_validity.dbx_validity, Exception):
            raise self.fs_validity.dbx_validity
        return self.fs_validity.dbx_validity

    
    def is_tracked(self = None):
        
        try:
            self.fileid()
            return True
        except NonSyncingLocalPathException:
            return False


    
    def is_valid(self = None):
        return isinstance(self.fs_validity, DBXValid)

    
    def is_valid_fs_path(self = None):
        return not isinstance(self.fs_validity, FSInvalidPathException)

    
    def is_monitored(self = None):
