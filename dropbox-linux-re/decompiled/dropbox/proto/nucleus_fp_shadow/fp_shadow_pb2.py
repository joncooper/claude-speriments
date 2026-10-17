# Source Generated with Decompyle++
# File: fp_shadow_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/nucleus_fp_shadow/fp_shadow.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.nucleus import published_event_pb2 as dropbox_dot_proto_dot_nucleus_dot_published__event__pb2
from dropbox.proto.nucleus import sync_engine_pb2 as dropbox_dot_proto_dot_nucleus_dot_sync__engine__pb2
from dropbox.proto.sync_frontend import remote_command_pb2 as dropbox_dot_proto_dot_sync__frontend_dot_remote__command__pb2
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/dropbox/proto/nucleus_fp_shadow/fp_shadow.proto\x12\x11nucleus_fp_shadow\x1a+dropbox/proto/nucleus/published_event.proto\x1a\'dropbox/proto/nucleus/sync_engine.proto\x1a0dropbox/proto/sync_frontend/remote_command.proto\x1a#dropbox/proto/rust/extensions.proto\x1a\x1bgoogle/protobuf/empty.proto"\x94\x01\n\x10CloneFileRequest\x12(\n\x06fileid\x18\x01 \x01(\x0cB\x18\xa2\xb5\x18\x14::sync_types::FileId\x12\x15\n\rabs_dest_path\x18\x02 \x01(\t\x12?\n\tblocklist\x18\x03 \x03(\x0cB,\xa2\xb5\x18(::obfuscation::WithObfuscation<[u8; 32]>"T\n\x11CloneFileResponse\x125\n\x05error\x18\x01 \x01(\x0e2!.nucleus_fp_shadow.CloneFileErrorH\x00\x88\x01\x01B\x08\n\x06_error"\x1e\n\x0bEchoRequest\x12\x0f\n\x07message\x18\x01 \x01(\t"\x1f\n\x0cEchoResponse\x12\x0f\n\x07message\x18\x01 \x01(\t"\x1e\n\x1cGetMountedCanopyStateRequest"j\n\x1dGetMountedCanopyStateResponse\x12I\n\x14mounted_canopy_state\x18\x01 \x01(\x0b2%.nucleus_fp_shadow.MountedCanopyStateB\x04\xc0\xb5\x18\x00"_\n\x15ShadowHydrationPolicy\x12(\n\x06fileid\x18\x01 \x01(\x0cB\x18\xa2\xb5\x18\x14::sync_types::FileId\x12\x1c\n\x14fp_downloads_eagerly\x18\x02 \x01(\x08"\xca\x02\n$PrepareShadowEngineForCutoverRequest\x12I\n\x14mounted_canopy_state\x18\x01 \x01(\x0b2%.nucleus_fp_shadow.MountedCanopyStateB\x04\xc0\xb5\x18\x00\x12!\n\x13mounted_list_cursor\x18\x02 \x01(\x0cB\x04\xc0\xb5\x18\x00\x12_\n\x0crequest_type\x18\x03 \x01(\x0e2C.nucleus_fp_shadow.PrepareShadowEngineForCutoverRequest.RequestTypeB\x04\xc0\xb5\x18\x00"S\n\x0bRequestType\x12\n\n\x06Dryrun\x10\x00\x12\x18\n\x14DryrunNotFullySynced\x10\x01\x12\x0b\n\x07Cutover\x10\x02\x12\x11\n\rCutoverResume\x10\x03"\xc1\x01\n\x12MountedCanopyState\x12D\n\x12hydration_policies\x18\x01 \x03(\x0b2(.nucleus_fp_shadow.ShadowHydrationPolicy\x12,\n\nhidden_set\x18\x02 \x03(\x0cB\x18\xa2\xb5\x18\x14::sync_types::FileId\x127\n\x15device_anchor_fileids\x18\x03 \x03(\x0cB\x18\xa2\xb5\x18\x14::sync_types::FileId"\xc1\x01\n%PrepareShadowEngineForCutoverResponse\x12@\n\x02ok\x18\x01 \x01(\x0b22.nucleus_fp_shadow.PrepareShadowEngineForCutoverOkH\x00\x12F\n\x05error\x18\x02 \x01(\x0b25.nucleus_fp_shadow.PrepareShadowEngineForCutoverErrorH\x00B\x0e\n\x06result\x12\x04\x88\xb5\x18\x00"E\n\x1fPrepareShadowEngineForCutoverOk\x12"\n\x14shadow_database_path\x18\x01 \x01(\tB\x04\xc0\xb5\x18\x00"\x96\x01\n"PrepareShadowEngineForCutoverError\x12S\n\nerror_kind\x18\x01 \x01(\x0e29.nucleus_fp_shadow.PrepareShadowEngineForCutoverErrorKindB\x04\xc0\xb5\x18\x00\x12\x1b\n\rerror_message\x18\x02 \x01(\tB\x04\xc0\xb5\x18\x00"\xbe\x01\n\rPollFpDfcArgs\x12:\n\x11localized_strings\x18\x01 \x01(\x0b2\x19.nucleus.LocalizedStringsB\x04\xc0\xb5\x18\x00\x12\x16\n\x08dfc_root\x18\x02 \x01(\tB\x04\xc0\xb5\x18\x00\x12\x15\n\x07fp_root\x18\x03 \x01(\tB\x04\xc0\xb5\x18\x00\x12\x1d\n\x0ffp_home_ns_root\x18\x04 \x01(\tB\x04\xc0\xb5\x18\x00\x12#\n\x15dfc_database_location\x18\x05 \x01(\tB\x04\xc0\xb5\x18\x00"\xa6\x07\n\x11PollFpDfcResponse\x121\n\tsucceeded\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyB\x04\xc0\xb5\x18\x00H\x00\x12G\n\x06failed\x18\x02 \x01(\x0b2/.nucleus_fp_shadow.PollFpDfcResponse.DfcFailureB\x04\xc0\xb5\x18\x00H\x00\x12=\n\x07metrics\x18\x03 \x01(\x0b2,.nucleus_fp_shadow.PollFpDfcResponse.Metrics\x12\x17\n\x0felapsed_time_us\x18\x04 \x01(\x04\x1a\x8b\x01\n\x07Metrics\x12$\n\x16num_items_to_resurrect\x18\x01 \x01(\x04B\x04\xc0\xb5\x18\x00\x12\x16\n\x08dfc_size\x18\x02 \x01(\x04B\x04\xc0\xb5\x18\x00\x12\x1d\n\x0fdfc_size_bucket\x18\x03 \x01(\tB\x04\xc0\xb5\x18\x00\x12#\n\x15serialized_perf_stats\x18\x04 \x01(\tB\x04\xc0\xb5\x18\x00\x1a\xfd\x02\n\x14ResurrectionFailures\x12x\n\x15resurrection_failures\x18\x01 \x03(\x0b2S.nucleus_fp_shadow.PollFpDfcResponse.ResurrectionFailures.ResurrectionFailuresEntryB\x04\xc0\xb5\x18\x00\x12t\n\x14error_counts_by_type\x18\x02 \x03(\x0b2P.nucleus_fp_shadow.PollFpDfcResponse.ResurrectionFailures.ErrorCountsByTypeEntryB\x04\xc0\xb5\x18\x00\x1a;\n\x19ResurrectionFailuresEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a8\n\x16ErrorCountsByTypeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x028\x01\x1a\x9e\x01\n\nDfcFailure\x12`\n\x15resurrection_failures\x18\x01 \x01(\x0b29.nucleus_fp_shadow.PollFpDfcResponse.ResurrectionFailuresB\x04\xc0\xb5\x18\x00H\x00\x12\x1d\n\rfailure_error\x18\x02 \x01(\tB\x04\xc0\xb5\x18\x00H\x00B\x0f\n\x07failure\x12\x04\x88\xb5\x18\x00B\x0e\n\x06result\x12\x04\x88\xb5\x18\x00":\n\x1dGetMountedEngineStatusRequest\x12\x19\n\x11include_dbxignore\x18\x01 \x01(\x08"~\n\x1eGetMountedEngineStatusResponse\x12\x16\n\tis_paused\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x1a\n\x12dbxignore_contents\x18\x02 \x01(\x0c\x12\x1a\n\x12dbxignore_filename\x18\x03 \x01(\tB\x0c\n\n_is_paused"C\n\x16MaterializationRequest\x12)\n\x07fileids\x18\x01 \x03(\x0cB\x18\xa2\xb5\x18\x14::sync_types::FileId"7\n\x17MaterializationResponse\x12\x12\n\x05error\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_error"#\n\x11ItemLookupRequest\x12\x0e\n\x06itemid\x18\x01 \x01(\x04"4\n\x12ItemLookupResponse\x12\x13\n\x06fileid\x18\x01 \x01(\tH\x00\x88\x01\x01B\t\n\x07_fileid"J\n\x16UpdateDbxIgnoreRequest\x12\x1e\n\x16new_dbxignore_contents\x18\x01 \x01(\x0c\x12\x10\n\x08filename\x18\x02 \x01(\t"w\n\x19ResolveDumpMethodResponse\x129\n\x06method\x18\x01 \x01(\x0b2\'.nucleus.FileProviderDumpRequestedEventH\x00\x12\x0f\n\x05error\x18\x02 \x01(\tH\x00B\x0e\n\x06result\x12\x04\x88\xb5\x18\x00"*\n\x12RequestDumpRequest\x12\x14\n\x06reason\x18\x01 \x01(\tB\x04\xc0\xb5\x18\x00*\xdd\x01\n\x0eCloneFileError\x12\x10\n\x0cFileNotFound\x10\x00\x12\x0c\n\x08NotAFile\x10\x01\x12\x15\n\x11BlocklistMismatch\x10\x02\x12\x12\n\x0eNoAbsolutePath\x10\x03\x12\x0e\n\nCopyFailed\x10\x04\x12\x14\n\x10BlocklistMissing\x10\x05\x12\x1e\n\x1aBlocklistMismatchAfterCopy\x10\x06\x12\r\n\tHashError\x10\x07\x12\x10\n\x0cHashMismatch\x10\x08\x12\x19\n\x15UnexpectedPlaceholder\x10\t*\xab\x02\n&PrepareShadowEngineForCutoverErrorKind\x12 \n\x1cUpdateHydrationPoliciesError\x10\x00\x12$\n ShadowCursorDeserializationError\x10\x01\x12%\n!MountedCursorDeserializationError\x10\x02\x12\x17\n\x13CursorMismatchError\x10\x03\x12\x1b\n\x17CopyShadowDatabaseError\x10\x04\x12\x12\n\x0eNotFullySynced\x10\x05\x12\x0e\n\nPauseError\x10\x06\x12&\n"ShadowCursorChangedAfterPauseError\x10\x07\x12\x10\n\x0cFailedResume\x10\x082\xef\x08\n\x08FPShadow\x12I\n\x04Echo\x12\x1e.nucleus_fp_shadow.EchoRequest\x1a\x1f.nucleus_fp_shadow.EchoResponse"\x00\x12X\n\tCloneFile\x12#.nucleus_fp_shadow.CloneFileRequest\x1a$.nucleus_fp_shadow.CloneFileResponse"\x00\x12|\n\x15GetMountedCanopyState\x12/.nucleus_fp_shadow.GetMountedCanopyStateRequest\x1a0.nucleus_fp_shadow.GetMountedCanopyStateResponse"\x00\x12\x94\x01\n\x1dPrepareShadowEngineForCutover\x127.nucleus_fp_shadow.PrepareShadowEngineForCutoverRequest\x1a8.nucleus_fp_shadow.PrepareShadowEngineForCutoverResponse"\x00\x12\x7f\n\x16GetMountedEngineStatus\x120.nucleus_fp_shadow.GetMountedEngineStatusRequest\x1a1.nucleus_fp_shadow.GetMountedEngineStatusResponse"\x00\x12q\n\x16RequestMaterialization\x12).nucleus_fp_shadow.MaterializationRequest\x1a*.nucleus_fp_shadow.MaterializationResponse"\x00\x12[\n\nItemLookup\x12$.nucleus_fp_shadow.ItemLookupRequest\x1a%.nucleus_fp_shadow.ItemLookupResponse"\x00\x12V\n\x0fUpdateDbxIgnore\x12).nucleus_fp_shadow.UpdateDbxIgnoreRequest\x1a\x16.google.protobuf.Empty"\x00\x12C\n\x0fCancelMigration\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty"\x00\x12k\n\x11ResolveDumpMethod\x12&.sync_frontend.FileProviderDumpRequest\x1a,.nucleus_fp_shadow.ResolveDumpMethodResponse"\x00\x12N\n\x0bRequestDump\x12%.nucleus_fp_shadow.RequestDumpRequest\x1a\x16.google.protobuf.Empty"\x00B\x10\xa2\x02\rNucleusShadowb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.nucleus_fp_shadow.fp_shadow_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\rNucleusShadow'
    _globals['_CLONEFILEREQUEST'].fields_by_name['fileid']._loaded_options = None
    _globals['_CLONEFILEREQUEST'].fields_by_name['fileid']._serialized_options = b'\xa2\xb5\x18\x14::sync_types::FileId'
    _globals['_CLONEFILEREQUEST'].fields_by_name['blocklist']._loaded_options = None
    _globals['_CLONEFILEREQUEST'].fields_by_name['blocklist']._serialized_options = b'\xa2\xb5\x18(::obfuscation::WithObfuscation<[u8; 32]>'
    _globals['_GETMOUNTEDCANOPYSTATERESPONSE'].fields_by_name['mounted_canopy_state']._loaded_options = None
    _globals['_GETMOUNTEDCANOPYSTATERESPONSE'].fields_by_name['mounted_canopy_state']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SHADOWHYDRATIONPOLICY'].fields_by_name['fileid']._loaded_options = None
    _globals['_SHADOWHYDRATIONPOLICY'].fields_by_name['fileid']._serialized_options = b'\xa2\xb5\x18\x14::sync_types::FileId'
    _globals['_PREPARESHADOWENGINEFORCUTOVERREQUEST'].fields_by_name['mounted_canopy_state']._loaded_options = None
    _globals['_PREPARESHADOWENGINEFORCUTOVERREQUEST'].fields_by_name['mounted_canopy_state']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_PREPARESHADOWENGINEFORCUTOVERREQUEST'].fields_by_name['mounted_list_cursor']._loaded_options = None
    _globals['_PREPARESHADOWENGINEFORCUTOVERREQUEST'].fields_by_name['mounted_list_cursor']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_PREPARESHADOWENGINEFORCUTOVERREQUEST'].fields_by_name['request_type']._loaded_options = None
    _globals['_PREPARESHADOWENGINEFORCUTOVERREQUEST'].fields_by_name['request_type']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_MOUNTEDCANOPYSTATE'].fields_by_name['hidden_set']._loaded_options = None
    _globals['_MOUNTEDCANOPYSTATE'].fields_by_name['hidden_set']._serialized_options = b'\xa2\xb5\x18\x14::sync_types::FileId'
    _globals['_MOUNTEDCANOPYSTATE'].fields_by_name['device_anchor_fileids']._loaded_options = None
    _globals['_MOUNTEDCANOPYSTATE'].fields_by_name['device_anchor_fileids']._serialized_options = b'\xa2\xb5\x18\x14::sync_types::FileId'
    _globals['_PREPARESHADOWENGINEFORCUTOVERRESPONSE'].oneofs_by_name['result']._loaded_options = None
    _globals['_PREPARESHADOWENGINEFORCUTOVERRESPONSE'].oneofs_by_name['result']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_PREPARESHADOWENGINEFORCUTOVEROK'].fields_by_name['shadow_database_path']._loaded_options = None
    _globals['_PREPARESHADOWENGINEFORCUTOVEROK'].fields_by_name['shadow_database_path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_PREPARESHADOWENGINEFORCUTOVERERROR'].fields_by_name['error_kind']._loaded_options = None
    _globals['_PREPARESHADOWENGINEFORCUTOVERERROR'].fields_by_name['error_kind']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_PREPARESHADOWENGINEFORCUTOVERERROR'].fields_by_name['error_message']._loaded_options = None
    _globals['_PREPARESHADOWENGINEFORCUTOVERERROR'].fields_by_name['error_message']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_POLLFPDFCARGS'].fields_by_name['localized_strings']._loaded_options = None
    _globals['_POLLFPDFCARGS'].fields_by_name['localized_strings']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_POLLFPDFCARGS'].fields_by_name['dfc_root']._loaded_options = None
    _globals['_POLLFPDFCARGS'].fields_by_name['dfc_root']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_POLLFPDFCARGS'].fields_by_name['fp_root']._loaded_options = None
    _globals['_POLLFPDFCARGS'].fields_by_name['fp_root']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_POLLFPDFCARGS'].fields_by_name['fp_home_ns_root']._loaded_options = None
    _globals['_POLLFPDFCARGS'].fields_by_name['fp_home_ns_root']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_POLLFPDFCARGS'].fields_by_name['dfc_database_location']._loaded_options = None
    _globals['_POLLFPDFCARGS'].fields_by_name['dfc_database_location']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_POLLFPDFCRESPONSE_METRICS'].fields_by_name['num_items_to_resurrect']._loaded_options = None
    _globals['_POLLFPDFCRESPONSE_METRICS'].fields_by_name['num_items_to_resurrect']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_POLLFPDFCRESPONSE_METRICS'].fields_by_name['dfc_size']._loaded_options = None
    _globals['_POLLFPDFCRESPONSE_METRICS'].fields_by_name['dfc_size']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_POLLFPDFCRESPONSE_METRICS'].fields_by_name['dfc_size_bucket']._loaded_options = None
    _globals['_POLLFPDFCRESPONSE_METRICS'].fields_by_name['dfc_size_bucket']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_POLLFPDFCRESPONSE_METRICS'].fields_by_name['serialized_perf_stats']._loaded_options = None
    _globals['_POLLFPDFCRESPONSE_METRICS'].fields_by_name['serialized_perf_stats']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_POLLFPDFCRESPONSE_RESURRECTIONFAILURES_RESURRECTIONFAILURESENTRY']._loaded_options = None
    _globals['_POLLFPDFCRESPONSE_RESURRECTIONFAILURES_RESURRECTIONFAILURESENTRY']._serialized_options = b'8\x01'
    _globals['_POLLFPDFCRESPONSE_RESURRECTIONFAILURES_ERRORCOUNTSBYTYPEENTRY']._loaded_options = None
    _globals['_POLLFPDFCRESPONSE_RESURRECTIONFAILURES_ERRORCOUNTSBYTYPEENTRY']._serialized_options = b'8\x01'
    _globals['_POLLFPDFCRESPONSE_RESURRECTIONFAILURES'].fields_by_name['resurrection_failures']._loaded_options = None
    _globals['_POLLFPDFCRESPONSE_RESURRECTIONFAILURES'].fields_by_name['resurrection_failures']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_POLLFPDFCRESPONSE_RESURRECTIONFAILURES'].fields_by_name['error_counts_by_type']._loaded_options = None
    _globals['_POLLFPDFCRESPONSE_RESURRECTIONFAILURES'].fields_by_name['error_counts_by_type']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_POLLFPDFCRESPONSE_DFCFAILURE'].oneofs_by_name['failure']._loaded_options = None
    _globals['_POLLFPDFCRESPONSE_DFCFAILURE'].oneofs_by_name['failure']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_POLLFPDFCRESPONSE_DFCFAILURE'].fields_by_name['resurrection_failures']._loaded_options = None
    _globals['_POLLFPDFCRESPONSE_DFCFAILURE'].fields_by_name['resurrection_failures']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_POLLFPDFCRESPONSE_DFCFAILURE'].fields_by_name['failure_error']._loaded_options = None
    _globals['_POLLFPDFCRESPONSE_DFCFAILURE'].fields_by_name['failure_error']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_POLLFPDFCRESPONSE'].oneofs_by_name['result']._loaded_options = None
    _globals['_POLLFPDFCRESPONSE'].oneofs_by_name['result']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_POLLFPDFCRESPONSE'].fields_by_name['succeeded']._loaded_options = None
    _globals['_POLLFPDFCRESPONSE'].fields_by_name['succeeded']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_POLLFPDFCRESPONSE'].fields_by_name['failed']._loaded_options = None
    _globals['_POLLFPDFCRESPONSE'].fields_by_name['failed']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_MATERIALIZATIONREQUEST'].fields_by_name['fileids']._loaded_options = None
    _globals['_MATERIALIZATIONREQUEST'].fields_by_name['fileids']._serialized_options = b'\xa2\xb5\x18\x14::sync_types::FileId'
    _globals['_RESOLVEDUMPMETHODRESPONSE'].oneofs_by_name['result']._loaded_options = None
    _globals['_RESOLVEDUMPMETHODRESPONSE'].oneofs_by_name['result']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_REQUESTDUMPREQUEST'].fields_by_name['reason']._loaded_options = None
    _globals['_REQUESTDUMPREQUEST'].fields_by_name['reason']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_CLONEFILEERROR']._serialized_start = 3537
    _globals['_CLONEFILEERROR']._serialized_end = 3758
    _globals['_PREPARESHADOWENGINEFORCUTOVERERRORKIND']._serialized_start = 3761
    _globals['_PREPARESHADOWENGINEFORCUTOVERERRORKIND']._serialized_end = 4060
    _globals['_CLONEFILEREQUEST']._serialized_start = 273
    _globals['_CLONEFILEREQUEST']._serialized_end = 421
    _globals['_CLONEFILERESPONSE']._serialized_start = 423
    _globals['_CLONEFILERESPONSE']._serialized_end = 507
    _globals['_ECHOREQUEST']._serialized_start = 509
    _globals['_ECHOREQUEST']._serialized_end = 539
    _globals['_ECHORESPONSE']._serialized_start = 541
    _globals['_ECHORESPONSE']._serialized_end = 572
    _globals['_GETMOUNTEDCANOPYSTATEREQUEST']._serialized_start = 574
    _globals['_GETMOUNTEDCANOPYSTATEREQUEST']._serialized_end = 604
    _globals['_GETMOUNTEDCANOPYSTATERESPONSE']._serialized_start = 606
    _globals['_GETMOUNTEDCANOPYSTATERESPONSE']._serialized_end = 712
    _globals['_SHADOWHYDRATIONPOLICY']._serialized_start = 714
    _globals['_SHADOWHYDRATIONPOLICY']._serialized_end = 809
    _globals['_PREPARESHADOWENGINEFORCUTOVERREQUEST']._serialized_start = 812
    _globals['_PREPARESHADOWENGINEFORCUTOVERREQUEST']._serialized_end = 1142
    _globals['_PREPARESHADOWENGINEFORCUTOVERREQUEST_REQUESTTYPE']._serialized_start = 1059
    _globals['_PREPARESHADOWENGINEFORCUTOVERREQUEST_REQUESTTYPE']._serialized_end = 1142
    _globals['_MOUNTEDCANOPYSTATE']._serialized_start = 1145
    _globals['_MOUNTEDCANOPYSTATE']._serialized_end = 1338
    _globals['_PREPARESHADOWENGINEFORCUTOVERRESPONSE']._serialized_start = 1341
    _globals['_PREPARESHADOWENGINEFORCUTOVERRESPONSE']._serialized_end = 1534
    _globals['_PREPARESHADOWENGINEFORCUTOVEROK']._serialized_start = 1536
    _globals['_PREPARESHADOWENGINEFORCUTOVEROK']._serialized_end = 1605
    _globals['_PREPARESHADOWENGINEFORCUTOVERERROR']._serialized_start = 1608
    _globals['_PREPARESHADOWENGINEFORCUTOVERERROR']._serialized_end = 1758
    _globals['_POLLFPDFCARGS']._serialized_start = 1761
    _globals['_POLLFPDFCARGS']._serialized_end = 1951
    _globals['_POLLFPDFCRESPONSE']._serialized_start = 1954
    _globals['_POLLFPDFCRESPONSE']._serialized_end = 2888
    _globals['_POLLFPDFCRESPONSE_METRICS']._serialized_start = 2188
    _globals['_POLLFPDFCRESPONSE_METRICS']._serialized_end = 2327
    _globals['_POLLFPDFCRESPONSE_RESURRECTIONFAILURES']._serialized_start = 2330
    _globals['_POLLFPDFCRESPONSE_RESURRECTIONFAILURES']._serialized_end = 2711
    _globals['_POLLFPDFCRESPONSE_RESURRECTIONFAILURES_RESURRECTIONFAILURESENTRY']._serialized_start = 2594
    _globals['_POLLFPDFCRESPONSE_RESURRECTIONFAILURES_RESURRECTIONFAILURESENTRY']._serialized_end = 2653
    _globals['_POLLFPDFCRESPONSE_RESURRECTIONFAILURES_ERRORCOUNTSBYTYPEENTRY']._serialized_start = 2655
    _globals['_POLLFPDFCRESPONSE_RESURRECTIONFAILURES_ERRORCOUNTSBYTYPEENTRY']._serialized_end = 2711
    _globals['_POLLFPDFCRESPONSE_DFCFAILURE']._serialized_start = 2714
    _globals['_POLLFPDFCRESPONSE_DFCFAILURE']._serialized_end = 2872
    _globals['_GETMOUNTEDENGINESTATUSREQUEST']._serialized_start = 2890
    _globals['_GETMOUNTEDENGINESTATUSREQUEST']._serialized_end = 2948
    _globals['_GETMOUNTEDENGINESTATUSRESPONSE']._serialized_start = 2950
    _globals['_GETMOUNTEDENGINESTATUSRESPONSE']._serialized_end = 3076
    _globals['_MATERIALIZATIONREQUEST']._serialized_start = 3078
    _globals['_MATERIALIZATIONREQUEST']._serialized_end = 3145
    _globals['_MATERIALIZATIONRESPONSE']._serialized_start = 3147
    _globals['_MATERIALIZATIONRESPONSE']._serialized_end = 3202
    _globals['_ITEMLOOKUPREQUEST']._serialized_start = 3204
    _globals['_ITEMLOOKUPREQUEST']._serialized_end = 3239
    _globals['_ITEMLOOKUPRESPONSE']._serialized_start = 3241
    _globals['_ITEMLOOKUPRESPONSE']._serialized_end = 3293
    _globals['_UPDATEDBXIGNOREREQUEST']._serialized_start = 3295
    _globals['_UPDATEDBXIGNOREREQUEST']._serialized_end = 3369
    _globals['_RESOLVEDUMPMETHODRESPONSE']._serialized_start = 3371
    _globals['_RESOLVEDUMPMETHODRESPONSE']._serialized_end = 3490
    _globals['_REQUESTDUMPREQUEST']._serialized_start = 3492
    _globals['_REQUESTDUMPREQUEST']._serialized_end = 3534
    _globals['_FPSHADOW']._serialized_start = 4063
    _globals['_FPSHADOW']._serialized_end = 5198
    return None
