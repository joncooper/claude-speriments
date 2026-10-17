# Source Generated with Decompyle++
# File: open_file_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/pap/events/filesystem_item_actions/open_file.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.pap import options_pb2 as dropbox_dot_proto_dot_pap_dot_options__pb2
from dropbox.pap.events.enums import desktop_open_origin_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_desktop__open__origin__pb2
from dropbox.pap.events.enums import file_category_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_file__category__pb2
from dropbox.pap.events.enums import file_type_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_file__type__pb2
from dropbox.pap.events.enums import tray_variant_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_tray__variant__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:dropbox/pap/events/filesystem_item_actions/open_file.proto\x12"pap.events.filesystem_item_actions\x1a\x1fdropbox/proto/pap/options.proto\x1a2dropbox/pap/events/enums/desktop_open_origin.proto\x1a,dropbox/pap/events/enums/file_category.proto\x1a(dropbox/pap/events/enums/file_type.proto\x1a+dropbox/pap/events/enums/tray_variant.proto"\xf7\x04\n\tOpen_File\x12\x16\n\x0eaction_surface\x18\x01 \x01(\t\x12N\n\x0bevent_class\x18\xcd\x08 \x01(\x0e28.pap.events.filesystem_item_actions.Open_File.EventClass\x12\x16\n\x0epath_extension\x18\x02 \x01(\t\x12I\n\x13desktop_open_origin\x18\x03 \x01(\x0e2,.enums.desktop_open_origin.DesktopOpenOrigin\x12\x16\n\x0efile_extension\x18\x04 \x01(\t\x128\n\rfile_category\x18\x05 \x01(\x0e2!.enums.file_category.FileCategory\x12,\n\tfile_type\x18\x06 \x01(\x0e2\x19.enums.file_type.FileType\x12\x11\n\tupload_id\x18\x07 \x01(\t\x12\x13\n\x0bfile_obj_id\x18\x08 \x01(\t\x12\x14\n\x0cis_encrypted\x18\t \x01(\x08\x12\x1a\n\x12content_identifier\x18\n \x01(\t\x12\x11\n\tfile_size\x18\x0b \x01(\x03\x12\x15\n\rupload_method\x18\x0c \x01(\t\x125\n\x0ctray_variant\x18\r \x01(\x0e2\x1f.enums.tray_variant.TrayVariant\x12\x16\n\x0eaction_element\x18\x0e \x01(\t\x12\x11\n\tis_shared\x18\x0f \x01(\x08")\n\nEventClass\x12\x1b\n\x17FILESYSTEM_ITEM_ACTIONS\x10\x00:\x0e\xca>\x04open\xd2>\x04fileB,Z*dropbox/pap/events/filesystem_item_actionsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.pap.events.filesystem_item_actions.open_file_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z*dropbox/pap/events/filesystem_item_actions'
    _globals['_OPEN_FILE']._loaded_options = None
    _globals['_OPEN_FILE']._serialized_options = b'\xca>\x04open\xd2>\x04file'
    _globals['_OPEN_FILE']._serialized_start = 317
    _globals['_OPEN_FILE']._serialized_end = 948
    _globals['_OPEN_FILE_EVENTCLASS']._serialized_start = 891
    _globals['_OPEN_FILE_EVENTCLASS']._serialized_end = 932
    return None
