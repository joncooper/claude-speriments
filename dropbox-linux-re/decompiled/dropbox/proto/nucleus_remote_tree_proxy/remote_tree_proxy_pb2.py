# Source Generated with Decompyle++
# File: remote_tree_proxy_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/nucleus_remote_tree_proxy/remote_tree_proxy.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?dropbox/proto/nucleus_remote_tree_proxy/remote_tree_proxy.proto\x12\x19nucleus_remote_tree_proxy"O\n\x0fRemoteReadError\x12<\n\x04code\x18\x01 \x01(\x0e2..nucleus_remote_tree_proxy.RemoteReadErrorCode"l\n\x11FetchByteRangeReq\x12\x0e\n\x06fileid\x18\x01 \x01(\t\x12\x14\n\x0ccontent_hash\x18\x02 \x01(\x0c\x12\x0e\n\x06offset\x18\x03 \x01(\x04\x12\x0e\n\x06length\x18\x04 \x01(\x04\x12\x11\n\talignment\x18\x05 \x01(\r"\x9a\x01\n\x13FetchByteRangeReply\x12?\n\x05error\x18\x01 \x01(\x0b2..nucleus_remote_tree_proxy.FetchByteRangeErrorH\x00\x128\n\x06served\x18\x02 \x01(\x0b2&.nucleus_remote_tree_proxy.ServedRangeH\x00B\x08\n\x06result"z\n\x0bServedRange\x12\x17\n\x0frange_file_path\x18\x01 \x01(\t\x12\x16\n\x0ealigned_offset\x18\x02 \x01(\x04\x12\x16\n\x0ealigned_length\x18\x03 \x01(\x04\x12\x14\n\x0ccontent_hash\x18\x04 \x01(\x0c\x12\x0c\n\x04data\x18\x05 \x01(\x0c"\x9d\x01\n\x13FetchByteRangeError\x12<\n\x04code\x18\x01 \x01(\x0e2..nucleus_remote_tree_proxy.RemoteReadErrorCode\x12\'\n\x1fstale_revision_new_content_hash\x18\x02 \x01(\x0c\x12\x1f\n\x17stale_revision_new_size\x18\x03 \x01(\x04",\n\x15EnumerateRemoteDirReq\x12\x13\n\x0bdbx_rr_path\x18\x01 \x01(\t"\x9d\x01\n\x17EnumerateRemoteDirReply\x12;\n\x05error\x18\x01 \x01(\x0b2*.nucleus_remote_tree_proxy.RemoteReadErrorH\x00\x12;\n\x07entries\x18\x02 \x01(\x0b2(.nucleus_remote_tree_proxy.RemoteEntriesH\x00B\x08\n\x06result"H\n\rRemoteEntries\x127\n\x07entries\x18\x01 \x03(\x0b2&.nucleus_remote_tree_proxy.RemoteEntry"+\n\x14LookupRemoteEntryReq\x12\x13\n\x0bdbx_rr_path\x18\x01 \x01(\t"\x98\x01\n\x16LookupRemoteEntryReply\x12;\n\x05error\x18\x01 \x01(\x0b2*.nucleus_remote_tree_proxy.RemoteReadErrorH\x00\x127\n\x05found\x18\x02 \x01(\x0b2&.nucleus_remote_tree_proxy.RemoteEntryH\x00B\x08\n\x06result"\xe1\x01\n\x0bRemoteEntry\x12\x10\n\x08filename\x18\x01 \x01(\t\x12\x0e\n\x06fileid\x18\x02 \x01(\t\x128\n\x04type\x18\x03 \x01(\x0e2*.nucleus_remote_tree_proxy.RemoteEntryType\x12\x14\n\x0ccontent_hash\x18\x04 \x01(\x0c\x12\x0c\n\x04size\x18\x05 \x01(\x04\x12\r\n\x05mtime\x18\x06 \x01(\x03\x12C\n\nattributes\x18\x07 \x03(\x0e2/.nucleus_remote_tree_proxy.RemoteEntryAttribute*\x81\x02\n\x13RemoteReadErrorCode\x12\x1d\n\x19REMOTE_READ_ERROR_UNKNOWN\x10\x00\x12\x1f\n\x1bREMOTE_READ_ERROR_NOT_READY\x10\x01\x12\x1f\n\x1bREMOTE_READ_ERROR_NOT_FOUND\x10\x02\x12$\n REMOTE_READ_ERROR_STALE_REVISION\x10\x03\x12"\n\x1eREMOTE_READ_ERROR_INACCESSIBLE\x10\x04\x12\x1f\n\x1bREMOTE_READ_ERROR_TRANSIENT\x10\x05\x12\x1e\n\x1aREMOTE_READ_ERROR_REJECTED\x10\x06*\xab\x01\n\x0fRemoteEntryType\x12\x18\n\x14REMOTE_ENTRY_UNKNOWN\x10\x00\x12\x15\n\x11REMOTE_ENTRY_FILE\x10\x01\x12\x1a\n\x16REMOTE_ENTRY_DIRECTORY\x10\x02\x12\x18\n\x14REMOTE_ENTRY_SYMLINK\x10\x03\x12\x16\n\x12REMOTE_ENTRY_MOUNT\x10\x04\x12\x19\n\x15REMOTE_ENTRY_CLOUDDOC\x10\x05*\x83\x01\n\x14RemoteEntryAttribute\x12"\n\x1eREMOTE_ENTRY_ATTRIBUTE_UNKNOWN\x10\x00\x12$\n REMOTE_ENTRY_ATTRIBUTE_ENCRYPTED\x10\x01\x12!\n\x1dREMOTE_ENTRY_ATTRIBUTE_HIDDEN\x10\x022\xfc\x02\n\x0fRemoteTreeProxy\x12p\n\x0eFetchByteRange\x12,.nucleus_remote_tree_proxy.FetchByteRangeReq\x1a..nucleus_remote_tree_proxy.FetchByteRangeReply"\x00\x12|\n\x12EnumerateRemoteDir\x120.nucleus_remote_tree_proxy.EnumerateRemoteDirReq\x1a2.nucleus_remote_tree_proxy.EnumerateRemoteDirReply"\x00\x12y\n\x11LookupRemoteEntry\x12/.nucleus_remote_tree_proxy.LookupRemoteEntryReq\x1a1.nucleus_remote_tree_proxy.LookupRemoteEntryReply"\x00B\x19\xa2\x02\x16NucleusRemoteTreeProxyb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.nucleus_remote_tree_proxy.remote_tree_proxy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\x16NucleusRemoteTreeProxy'
    _globals['_REMOTEREADERRORCODE']._serialized_start = 1435
    _globals['_REMOTEREADERRORCODE']._serialized_end = 1692
    _globals['_REMOTEENTRYTYPE']._serialized_start = 1695
    _globals['_REMOTEENTRYTYPE']._serialized_end = 1866
    _globals['_REMOTEENTRYATTRIBUTE']._serialized_start = 1869
    _globals['_REMOTEENTRYATTRIBUTE']._serialized_end = 2000
    _globals['_REMOTEREADERROR']._serialized_start = 94
    _globals['_REMOTEREADERROR']._serialized_end = 173
    _globals['_FETCHBYTERANGEREQ']._serialized_start = 175
    _globals['_FETCHBYTERANGEREQ']._serialized_end = 283
    _globals['_FETCHBYTERANGEREPLY']._serialized_start = 286
    _globals['_FETCHBYTERANGEREPLY']._serialized_end = 440
    _globals['_SERVEDRANGE']._serialized_start = 442
    _globals['_SERVEDRANGE']._serialized_end = 564
    _globals['_FETCHBYTERANGEERROR']._serialized_start = 567
    _globals['_FETCHBYTERANGEERROR']._serialized_end = 724
    _globals['_ENUMERATEREMOTEDIRREQ']._serialized_start = 726
    _globals['_ENUMERATEREMOTEDIRREQ']._serialized_end = 770
    _globals['_ENUMERATEREMOTEDIRREPLY']._serialized_start = 773
    _globals['_ENUMERATEREMOTEDIRREPLY']._serialized_end = 930
    _globals['_REMOTEENTRIES']._serialized_start = 932
    _globals['_REMOTEENTRIES']._serialized_end = 1004
    _globals['_LOOKUPREMOTEENTRYREQ']._serialized_start = 1006
    _globals['_LOOKUPREMOTEENTRYREQ']._serialized_end = 1049
    _globals['_LOOKUPREMOTEENTRYREPLY']._serialized_start = 1052
    _globals['_LOOKUPREMOTEENTRYREPLY']._serialized_end = 1204
    _globals['_REMOTEENTRY']._serialized_start = 1207
    _globals['_REMOTEENTRY']._serialized_end = 1432
    _globals['_REMOTETREEPROXY']._serialized_start = 2003
    _globals['_REMOTETREEPROXY']._serialized_end = 2383
    return None
