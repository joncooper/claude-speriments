# Source Generated with Decompyle++
# File: namespace_entity_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/namespace/namespace_entity.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.dropbox/proto/namespace/namespace_entity.proto\x12\tnamespace*\x87\x01\n\x17NamespaceLifecycleState\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x14\n\x10PRE_PROVISIONING\x102\x12\x10\n\x0cPROVISIONING\x10d\x12\x10\n\x0bINITIALIZED\x10\xc8\x01\x12\x0b\n\x06LOCKED\x10\xfa\x01\x12\x18\n\x13PERMANENTLY_DELETED\x10\xac\x02*[\n\x18NamespaceTeamFolderState\x12\n\n\x06ACTIVE\x10\x00\x12\x0c\n\x08ARCHIVED\x10\x01\x12\x17\n\x13ARCHIVE_IN_PROGRESS\x10\x02\x12\x0c\n\x08INACTIVE\x10\x03*\xac\x08\n\x13NamespaceTypeValues\x12\x0b\n\x07ROOT_NS\x10\x00\x12\x11\n\rSHARED_FOLDER\x10\x01\x12\x0f\n\x0bAPP_SANDBOX\x10\x03\x12\n\n\x06HIDDEN\x10\x04\x12\x0f\n\x0bTEAM_FOLDER\x10\x05\x12\x17\n\x13TEAM_SHARED_DROPBOX\x10\x06\x12$\n LEGAL_HOLD_HIDDEN_TEAM_NAMESPACE\x10\x07\x12\x10\n\x0cVAULT_FOLDER\x10\x08\x12\x14\n\x10PASSWORDS_FOLDER\x10\t\x12\x18\n\x14FAMILY_SHARED_FOLDER\x10\n\x12\x1b\n\x17PASSWORDS_SHARED_FOLDER\x10\x0b\x12\x17\n\x0fCOMMERCE_FOLDER\x10\x0c\x1a\x02\x08\x01\x12\x17\n\x13REEL_PROJECT_FOLDER\x10\r\x12\x1e\n\x1aDEPRECATED_BACKUP_SNAPSHOT\x10\x0e\x12\x15\n\x11BACKUP_CONTINUOUS\x10\x0f\x12\x0f\n\x0bBACKUP_ROOT\x10\x10\x12\x14\n\x10COLLECTIONS_ROOT\x10\x11\x12\x15\n\x11COLLECTION_FOLDER\x10\x13\x12(\n$DEPRECATED_CAPTURE_COLLECTION_FOLDER\x10\x14\x12\x14\n\x10TEAM_MEMBER_ROOT\x10\x15\x12.\n*DEPRECATED_VIDEO_SYNTHESIS_DOWNLOAD_FOLDER\x10\x16\x12\x1e\n\x1aDEPRECATED_CLOUD_DATA_ROOT\x10\x17\x12\x1d\n\x19BINDER_BOUND_FILES_FOLDER\x10\x18\x12\x1a\n\x16COLLECTION_TEAM_FOLDER\x10\x19\x12\x11\n\rSTACKS_FOLDER\x10\x1a\x12\x1f\n\x1bMEDIA_PROXY_DOWNLOAD_FOLDER\x10\x1b\x12\x1f\n\x1bVIDEO_EDITOR_PROJECT_FOLDER\x10\x1c\x12\x1e\n\x1aTHIRD_PARTY_CONTENT_FOLDER\x10\x1d\x12\x15\n\x11UD_STARRED_FOLDER\x10\x1e\x12\x1a\n\x16CUSTOM_BRANDING_FOLDER\x10\x1f\x12\x1e\n\x1aREFERENCE_CONTAINER_ANCHOR\x10 \x12\x1f\n\x1bCHAT_SHARING_ANCHORS_FOLDER\x10!\x12\x0c\n\x08RC_STACK\x10"\x12\x12\n\x0eRC_AGENTIC_APP\x10#\x12\x16\n\x12RC_SPACES_V2_SPACE\x10$\x12\x1f\n\x1bRC_SPACES_V2_MEETING_SERIES\x10%\x12\x15\n\x11RC_MEDIA_HUB_LINK\x10&\x12\x18\n\x14RC_MEDIA_HUB_PROJECT\x10\'\x12\x15\n\x11RC_VERSION_BUNDLE\x10(\x12\x13\n\x0fRC_SHARING_LINK\x10)\x12\x16\n\x12RC_SHARING_MEMBERS\x10**?\n\x16APIV2SerializationType\x12\x0b\n\x07RAW_INT\x10\x00\x12\x0b\n\x07PID_INT\x10\x01\x12\x0b\n\x07PID_OID\x10\x02*0\n\nSearchable\x12\t\n\x05NEVER\x10\x00\x12\n\n\x06ALWAYS\x10\x01\x12\x0b\n\x07MOUNTED\x10\x02B8\n\x1bcom.dropbox.proto.namespaceP\x01Z\x17dropbox/proto/namespaceb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.namespace.namespace_entity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.dropbox.proto.namespaceP\x01Z\x17dropbox/proto/namespace'
    _globals['_NAMESPACETYPEVALUES'].values_by_name['COMMERCE_FOLDER']._loaded_options = None
    _globals['_NAMESPACETYPEVALUES'].values_by_name['COMMERCE_FOLDER']._serialized_options = b'\x08\x01'
    _globals['_NAMESPACELIFECYCLESTATE']._serialized_start = 62
    _globals['_NAMESPACELIFECYCLESTATE']._serialized_end = 197
    _globals['_NAMESPACETEAMFOLDERSTATE']._serialized_start = 199
    _globals['_NAMESPACETEAMFOLDERSTATE']._serialized_end = 290
    _globals['_NAMESPACETYPEVALUES']._serialized_start = 293
    _globals['_NAMESPACETYPEVALUES']._serialized_end = 1361
    _globals['_APIV2SERIALIZATIONTYPE']._serialized_start = 1363
    _globals['_APIV2SERIALIZATIONTYPE']._serialized_end = 1426
    _globals['_SEARCHABLE']._serialized_start = 1428
    _globals['_SEARCHABLE']._serialized_end = 1476
    return None
