# Source Generated with Decompyle++
# File: sync_engine_status_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/nucleus/sync_engine_status.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from dropbox.proto.nucleus import network_state_pb2 as dropbox_dot_proto_dot_nucleus_dot_network__state__pb2
from dropbox.proto.nucleus import sync_epoch_pb2 as dropbox_dot_proto_dot_nucleus_dot_sync__epoch__pb2
from dropbox.proto.nucleus import sync_failures_pb2 as dropbox_dot_proto_dot_nucleus_dot_sync__failures__pb2
from dropbox.proto.nucleus import types_pb2 as dropbox_dot_proto_dot_nucleus_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.dropbox/proto/nucleus/sync_engine_status.proto\x12\x07nucleus\x1a\x1bgoogle/protobuf/empty.proto\x1a#dropbox/proto/rust/extensions.proto\x1a)dropbox/proto/nucleus/network_state.proto\x1a&dropbox/proto/nucleus/sync_epoch.proto\x1a)dropbox/proto/nucleus/sync_failures.proto\x1a!dropbox/proto/nucleus/types.proto"\xd8\x01\n\x13NetworkConnectivity\x122\n\x10engine_connected\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12:\n\x13engine_disconnected\x18\x02 \x01(\x0e2\x1b.nucleus.NetworkFailureKindH\x00\x12A\n\x1aignored_connection_failure\x18\x03 \x01(\x0e2\x1b.nucleus.NetworkFailureKindH\x00B\x0e\n\x06status\x12\x04\x88\xb5\x18\x00"\xa7\x02\n\x0eStatusSnapshot\x12\x18\n\nfile_count\x18\x01 \x01(\x04B\x04\xc0\xb5\x18\x00\x12\x1d\n\x0fbytes_remaining\x18\x02 \x01(\x04B\x04\xc0\xb5\x18\x00\x12\x1e\n\x10speed_kb_per_sec\x18\x03 \x01(\x01B\x04\xc0\xb5\x18\x00\x12\x1f\n\x11speed_ops_per_sec\x18\x04 \x01(\x01B\x04\xc0\xb5\x18\x00\x125\n\nbottleneck\x18\x05 \x01(\x0e2\x1b.nucleus.ProgressBottleneckB\x04\xc0\xb5\x18\x00\x12\x1f\n\x12time_remaining_sec\x18\x06 \x01(\x01H\x00\x88\x01\x01\x12\x1a\n\rlast_filename\x18\x07 \x01(\tH\x01\x88\x01\x01B\x15\n\x13_time_remaining_secB\x10\n\x0e_last_filename"\x9b\x03\n\x0cSyncEstimate\x122\n\x0bhash_status\x18\x01 \x01(\x0b2\x17.nucleus.StatusSnapshotB\x04\xc0\xb5\x18\x00\x124\n\rupload_status\x18\x02 \x01(\x0b2\x17.nucleus.StatusSnapshotB\x04\xc0\xb5\x18\x00\x126\n\x0fdownload_status\x18\x03 \x01(\x0b2\x17.nucleus.StatusSnapshotB\x04\xc0\xb5\x18\x00\x12(\n\x1aoverall_time_remaining_sec\x18\x04 \x01(\x01B\x04\xc0\xb5\x18\x00\x12%\n\x17overall_files_remaining\x18\x05 \x01(\x04B\x04\xc0\xb5\x18\x00\x12"\n\x15overall_last_filename\x18\x06 \x01(\tH\x00\x88\x01\x01\x12&\n\nsync_epoch\x18\x07 \x01(\x0b2\x12.nucleus.SyncEpoch\x12\x1d\n\x10percent_complete\x18\x08 \x01(\x02H\x01\x88\x01\x01B\x18\n\x16_overall_last_filenameB\x13\n\x11_percent_complete"\xbb\x02\n\nSyncIssues\x127\n\x0fsample_failures\x18\x01 \x03(\x0b2\x18.nucleus.SyncFailureTypeB\x04\xc0\xb5\x18\x00\x12\x1f\n\x11total_sync_issues\x18\x02 \x01(\x04B\x04\xc0\xb5\x18\x00\x12:\n\x0fnumber_failures\x18\x03 \x01(\x0b2\x1b.nucleus.NumberSyncFailuresB\x04\xc0\xb5\x18\x00\x12?\n\x0eprogress_state\x18\x04 \x01(\x0e2!.nucleus.SyncIssues.ProgressStateB\x04\xc0\xb5\x18\x00"V\n\rProgressState\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nPROCEEDING\x10\x01\x12\x13\n\x0fPARTIALLY_STUCK\x10\x02\x12\r\n\tALL_STUCK\x10\x03\x1a\x04\x90\xb5\x18\x01"\xf0\x01\n\x0cFileProgress\x12%\n\x06fileid\x18\x01 \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00\x12&\n\nlocal_path\x18\x02 \x01(\x0b2\x12.nucleus.LocalPath\x12\x16\n\tfile_name\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x08progress\x18\x04 \x01(\x04\x12+\n\x08job_type\x18\x05 \x01(\x0e2\x19.nucleus.SyncQueueJobType\x12\x17\n\x0fcompleted_bytes\x18\x06 \x01(\x04\x12\x13\n\x0btotal_bytes\x18\x07 \x01(\x04B\x0c\n\n_file_name"n\n\tSyncQueue\x121\n\x0cactive_tasks\x18\x01 \x03(\x0b2\x15.nucleus.FileProgressB\x04\xc0\xb5\x18\x00\x12.\n\x0fcompleted_tasks\x18\x02 \x03(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00"\xd7\x02\n\x10SyncEngineStatus\x12=\n\x13overall_sync_status\x18\x01 \x01(\x0e2\x1a.nucleus.OverallSyncStatusB\x04\xc0\xb5\x18\x00\x12@\n\x14network_connectivity\x18\x02 \x01(\x0b2\x1c.nucleus.NetworkConnectivityB\x04\xc0\xb5\x18\x00\x12\x1f\n\x11is_low_disk_space\x18\x03 \x01(\x08B\x04\xc0\xb5\x18\x00\x12\x1b\n\ris_over_quota\x18\x04 \x01(\x08B\x04\xc0\xb5\x18\x00\x12,\n\rsync_estimate\x18\x06 \x01(\x0b2\x15.nucleus.SyncEstimate\x12.\n\x0bsync_issues\x18\x07 \x01(\x0b2\x13.nucleus.SyncIssuesB\x04\xc0\xb5\x18\x00\x12&\n\nsync_queue\x18\x08 \x01(\x0b2\x12.nucleus.SyncQueue*\xb2\x01\n\x11OverallSyncStatus\x12\x17\n\x13UNKNOWN_SYNC_STATUS\x10\x00\x12\x0c\n\x08STARTING\x10\x01\x12\x0b\n\x07SYNCING\x10\x02\x12\n\n\x06SYNCED\x10\x03\x12\x0c\n\x08INDEXING\x10\x04\x12\x0b\n\x07LISTING\x10\x05\x12\x11\n\rREASSOCIATING\x10\x06\x12\n\n\x06PAUSED\x10\x07\x12\r\n\tMIGRATING\x10\x08\x12\x0e\n\nFP_CUTOVER\x10\t\x1a\x04\x90\xb5\x18\x01*2\n\x12ProgressBottleneck\x12\x0c\n\x08OPS_RATE\x10\x00\x12\x0e\n\nBYTES_RATE\x10\x01*H\n\x10SyncQueueJobType\x12\x14\n\x10UNKNOWN_JOB_TYPE\x10\x00\x12\n\n\x06UPLOAD\x10\x01\x12\x0c\n\x08DOWNLOAD\x10\x02\x1a\x04\x90\xb5\x18\x01B\x0c\xa2\x02\tNucleusSEb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.nucleus.sync_engine_status_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\tNucleusSE'
    _globals['_OVERALLSYNCSTATUS']._loaded_options = None
    _globals['_OVERALLSYNCSTATUS']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_SYNCQUEUEJOBTYPE']._loaded_options = None
    _globals['_SYNCQUEUEJOBTYPE']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_NETWORKCONNECTIVITY'].oneofs_by_name['status']._loaded_options = None
    _globals['_NETWORKCONNECTIVITY'].oneofs_by_name['status']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_STATUSSNAPSHOT'].fields_by_name['file_count']._loaded_options = None
    _globals['_STATUSSNAPSHOT'].fields_by_name['file_count']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_STATUSSNAPSHOT'].fields_by_name['bytes_remaining']._loaded_options = None
    _globals['_STATUSSNAPSHOT'].fields_by_name['bytes_remaining']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_STATUSSNAPSHOT'].fields_by_name['speed_kb_per_sec']._loaded_options = None
    _globals['_STATUSSNAPSHOT'].fields_by_name['speed_kb_per_sec']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_STATUSSNAPSHOT'].fields_by_name['speed_ops_per_sec']._loaded_options = None
    _globals['_STATUSSNAPSHOT'].fields_by_name['speed_ops_per_sec']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_STATUSSNAPSHOT'].fields_by_name['bottleneck']._loaded_options = None
    _globals['_STATUSSNAPSHOT'].fields_by_name['bottleneck']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCESTIMATE'].fields_by_name['hash_status']._loaded_options = None
    _globals['_SYNCESTIMATE'].fields_by_name['hash_status']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCESTIMATE'].fields_by_name['upload_status']._loaded_options = None
    _globals['_SYNCESTIMATE'].fields_by_name['upload_status']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCESTIMATE'].fields_by_name['download_status']._loaded_options = None
    _globals['_SYNCESTIMATE'].fields_by_name['download_status']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCESTIMATE'].fields_by_name['overall_time_remaining_sec']._loaded_options = None
    _globals['_SYNCESTIMATE'].fields_by_name['overall_time_remaining_sec']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCESTIMATE'].fields_by_name['overall_files_remaining']._loaded_options = None
    _globals['_SYNCESTIMATE'].fields_by_name['overall_files_remaining']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCISSUES_PROGRESSSTATE']._loaded_options = None
    _globals['_SYNCISSUES_PROGRESSSTATE']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_SYNCISSUES'].fields_by_name['sample_failures']._loaded_options = None
    _globals['_SYNCISSUES'].fields_by_name['sample_failures']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCISSUES'].fields_by_name['total_sync_issues']._loaded_options = None
    _globals['_SYNCISSUES'].fields_by_name['total_sync_issues']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCISSUES'].fields_by_name['number_failures']._loaded_options = None
    _globals['_SYNCISSUES'].fields_by_name['number_failures']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCISSUES'].fields_by_name['progress_state']._loaded_options = None
    _globals['_SYNCISSUES'].fields_by_name['progress_state']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_FILEPROGRESS'].fields_by_name['fileid']._loaded_options = None
    _globals['_FILEPROGRESS'].fields_by_name['fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCQUEUE'].fields_by_name['active_tasks']._loaded_options = None
    _globals['_SYNCQUEUE'].fields_by_name['active_tasks']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCQUEUE'].fields_by_name['completed_tasks']._loaded_options = None
    _globals['_SYNCQUEUE'].fields_by_name['completed_tasks']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCENGINESTATUS'].fields_by_name['overall_sync_status']._loaded_options = None
    _globals['_SYNCENGINESTATUS'].fields_by_name['overall_sync_status']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCENGINESTATUS'].fields_by_name['network_connectivity']._loaded_options = None
    _globals['_SYNCENGINESTATUS'].fields_by_name['network_connectivity']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCENGINESTATUS'].fields_by_name['is_low_disk_space']._loaded_options = None
    _globals['_SYNCENGINESTATUS'].fields_by_name['is_low_disk_space']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCENGINESTATUS'].fields_by_name['is_over_quota']._loaded_options = None
    _globals['_SYNCENGINESTATUS'].fields_by_name['is_over_quota']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCENGINESTATUS'].fields_by_name['sync_issues']._loaded_options = None
    _globals['_SYNCENGINESTATUS'].fields_by_name['sync_issues']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_OVERALLSYNCSTATUS']._serialized_start = 2237
    _globals['_OVERALLSYNCSTATUS']._serialized_end = 2415
    _globals['_PROGRESSBOTTLENECK']._serialized_start = 2417
    _globals['_PROGRESSBOTTLENECK']._serialized_end = 2467
    _globals['_SYNCQUEUEJOBTYPE']._serialized_start = 2469
    _globals['_SYNCQUEUEJOBTYPE']._serialized_end = 2541
    _globals['_NETWORKCONNECTIVITY']._serialized_start = 287
    _globals['_NETWORKCONNECTIVITY']._serialized_end = 503
    _globals['_STATUSSNAPSHOT']._serialized_start = 506
    _globals['_STATUSSNAPSHOT']._serialized_end = 801
    _globals['_SYNCESTIMATE']._serialized_start = 804
    _globals['_SYNCESTIMATE']._serialized_end = 1215
    _globals['_SYNCISSUES']._serialized_start = 1218
    _globals['_SYNCISSUES']._serialized_end = 1533
    _globals['_SYNCISSUES_PROGRESSSTATE']._serialized_start = 1447
    _globals['_SYNCISSUES_PROGRESSSTATE']._serialized_end = 1533
    _globals['_FILEPROGRESS']._serialized_start = 1536
    _globals['_FILEPROGRESS']._serialized_end = 1776
    _globals['_SYNCQUEUE']._serialized_start = 1778
    _globals['_SYNCQUEUE']._serialized_end = 1888
    _globals['_SYNCENGINESTATUS']._serialized_start = 1891
    _globals['_SYNCENGINESTATUS']._serialized_end = 2234
    return None
