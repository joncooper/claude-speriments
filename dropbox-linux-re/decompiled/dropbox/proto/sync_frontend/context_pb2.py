# Source Generated with Decompyle++
# File: context_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/sync_frontend/context.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rpc_core import service_extensions_pb2 as dropbox_dot_proto_dot_rpc__core_dot_service__extensions__pb2
from dropbox.proto.isotope_server import sync_frontend_pb2 as dropbox_dot_proto_dot_isotope__server_dot_sync__frontend__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)dropbox/proto/sync_frontend/context.proto\x12\rsync_frontend\x1a/dropbox/proto/rpc_core/service_extensions.proto\x1a0dropbox/proto/isotope_server/sync_frontend.proto"\xeb\x02\n\x0eRequestContext\x12\x10\n\x08host_key\x18\x01 \x01(\t\x127\n\x08run_type\x18\x02 \x01(\x0e2%.sync_frontend.RequestContext.RunType\x12\x10\n\x08build_no\x18\x03 \x01(\t\x12\x1c\n\x14sync_engine_build_no\x18\x04 \x01(\t\x12F\n\x17isotope_request_context\x18\x05 \x01(\x0b2%.isotope_server.IsotopeRequestContext"\x95\x01\n\x07RunType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04USER\x10\x01\x12\x14\n\x10INTEGRATION_TEST\x10\x02\x12+\n\'INTEGRATION_TEST_FORCE_FETCH_PROPERTIES\x10\x04\x12\x0f\n\x0bBACKUP_USER\x10\x06\x12\x13\n\x0fMULTI_ROOT_USER\x10\x07"\x04\x08\x05\x10\x05"\x04\x08\x03\x10\x03"\x94\x07\n\x0fResponseContext\x125\n\x06status\x18\x01 \x01(\x0e2%.sync_frontend.ResponseContext.Status"\xc9\x06\n\x06Status\x12\x18\n\x07UNKNOWN\x10\x00\x1a\x0b\xba\xb5\x18\x07UNKNOWN\x12\x13\n\x07SUCCESS\x10\x01\x1a\x06\xba\xb5\x18\x02OK\x12%\n\x0cAUTH_INVALID\x10\x02\x1a\x13\xba\xb5\x18\x0fUNAUTHENTICATED\x12$\n\x0fTRANSIENT_ERROR\x10\x03\x1a\x0f\xba\xb5\x18\x0bUNAVAILABLE\x12\x1a\n\x0eCURSOR_INVALID\x10\x04\x1a\x06\xba\xb5\x18\x02OK\x12,\n\x11DEPRECATED_CLIENT\x10\x05\x1a\x15\xba\xb5\x18\x11PERMISSION_DENIED\x12)\n\x0fINVALID_REQUEST\x10\x07\x1a\x14\xba\xb5\x18\x10INVALID_ARGUMENT\x12<\n CDM_CONVERSION_IN_PROGRESS_ERROR\x10\x08\x1a\x16\xba\xb5\x18\x12RESOURCE_EXHAUSTED\x12\x1c\n\tCANCELLED\x10\n\x1a\r\xba\xb5\x18\tCANCELLED\x12.\n\x12RESOURCE_EXHAUSTED\x10\x0b\x1a\x16\xba\xb5\x18\x12RESOURCE_EXHAUSTED\x12$\n\x0fMIGRATION_ERROR\x10\x0c\x1a\x0f\xba\xb5\x18\x0bUNAVAILABLE\x12\x1a\n\x08INTERNAL\x10\r\x1a\x0c\xba\xb5\x18\x08INTERNAL\x12,\n\x11PERMISSION_DENIED\x10\x0e\x1a\x15\xba\xb5\x18\x11PERMISSION_DENIED\x120\n\x13FAILED_PRECONDITION\x10\x0f\x1a\x17\xba\xb5\x18\x13FAILED_PRECONDITION\x12!\n\x15CDM_RELOCATION_NEEDED\x10\x10\x1a\x06\xba\xb5\x18\x02OK\x121\n\x1cDEPENDENCY_DEADLINE_EXCEEDED\x10\x11\x1a\x0f\xba\xb5\x18\x0bUNAVAILABLE\x12H\n+ISOTOPE_MISMATCHED_CLIENT_VALIDATION_FIELDS\x10\x12\x1a\x17\xba\xb5\x18\x13FAILED_PRECONDITION\x12*\n\x15CYPRESS_RPCS_DISABLED\x10\x13\x1a\x0f\xba\xb5\x18\x0bUNAVAILABLE\x12B\n\'OVER_QUOTA_DELETION_GENERATION_MISMATCH\x10\x14\x1a\x15\xba\xb5\x18\x11PERMISSION_DENIED\x1a\x04\xb0\xb5\x18\x01"\x04\x08\x06\x10\x06"\x04\x08\t\x10\tB\x1dZ\x1bdropbox/proto/sync_frontendb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.sync_frontend.context_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1bdropbox/proto/sync_frontend'
    _globals['_RESPONSECONTEXT_STATUS']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS']._serialized_options = b'\xb0\xb5\x18\x01'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['UNKNOWN']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['UNKNOWN']._serialized_options = b'\xba\xb5\x18\x07UNKNOWN'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['SUCCESS']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['SUCCESS']._serialized_options = b'\xba\xb5\x18\x02OK'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['AUTH_INVALID']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['AUTH_INVALID']._serialized_options = b'\xba\xb5\x18\x0fUNAUTHENTICATED'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['TRANSIENT_ERROR']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['TRANSIENT_ERROR']._serialized_options = b'\xba\xb5\x18\x0bUNAVAILABLE'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['CURSOR_INVALID']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['CURSOR_INVALID']._serialized_options = b'\xba\xb5\x18\x02OK'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['DEPRECATED_CLIENT']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['DEPRECATED_CLIENT']._serialized_options = b'\xba\xb5\x18\x11PERMISSION_DENIED'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['INVALID_REQUEST']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['INVALID_REQUEST']._serialized_options = b'\xba\xb5\x18\x10INVALID_ARGUMENT'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['CDM_CONVERSION_IN_PROGRESS_ERROR']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['CDM_CONVERSION_IN_PROGRESS_ERROR']._serialized_options = b'\xba\xb5\x18\x12RESOURCE_EXHAUSTED'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['CANCELLED']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['CANCELLED']._serialized_options = b'\xba\xb5\x18\tCANCELLED'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['RESOURCE_EXHAUSTED']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['RESOURCE_EXHAUSTED']._serialized_options = b'\xba\xb5\x18\x12RESOURCE_EXHAUSTED'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['MIGRATION_ERROR']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['MIGRATION_ERROR']._serialized_options = b'\xba\xb5\x18\x0bUNAVAILABLE'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['INTERNAL']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['INTERNAL']._serialized_options = b'\xba\xb5\x18\x08INTERNAL'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['PERMISSION_DENIED']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['PERMISSION_DENIED']._serialized_options = b'\xba\xb5\x18\x11PERMISSION_DENIED'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['FAILED_PRECONDITION']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['FAILED_PRECONDITION']._serialized_options = b'\xba\xb5\x18\x13FAILED_PRECONDITION'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['CDM_RELOCATION_NEEDED']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['CDM_RELOCATION_NEEDED']._serialized_options = b'\xba\xb5\x18\x02OK'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['DEPENDENCY_DEADLINE_EXCEEDED']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['DEPENDENCY_DEADLINE_EXCEEDED']._serialized_options = b'\xba\xb5\x18\x0bUNAVAILABLE'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['ISOTOPE_MISMATCHED_CLIENT_VALIDATION_FIELDS']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['ISOTOPE_MISMATCHED_CLIENT_VALIDATION_FIELDS']._serialized_options = b'\xba\xb5\x18\x13FAILED_PRECONDITION'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['CYPRESS_RPCS_DISABLED']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['CYPRESS_RPCS_DISABLED']._serialized_options = b'\xba\xb5\x18\x0bUNAVAILABLE'
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['OVER_QUOTA_DELETION_GENERATION_MISMATCH']._loaded_options = None
    _globals['_RESPONSECONTEXT_STATUS'].values_by_name['OVER_QUOTA_DELETION_GENERATION_MISMATCH']._serialized_options = b'\xba\xb5\x18\x11PERMISSION_DENIED'
    _globals['_REQUESTCONTEXT']._serialized_start = 160
    _globals['_REQUESTCONTEXT']._serialized_end = 523
    _globals['_REQUESTCONTEXT_RUNTYPE']._serialized_start = 374
    _globals['_REQUESTCONTEXT_RUNTYPE']._serialized_end = 523
    _globals['_RESPONSECONTEXT']._serialized_start = 526
    _globals['_RESPONSECONTEXT']._serialized_end = 1442
    _globals['_RESPONSECONTEXT_STATUS']._serialized_start = 601
    _globals['_RESPONSECONTEXT_STATUS']._serialized_end = 1442
    return None
