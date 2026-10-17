# Source Generated with Decompyle++
# File: continue_setup_wizard_nonce_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/pap/events/onboard/continue_setup_wizard_nonce.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.pap import options_pb2 as dropbox_dot_proto_dot_pap_dot_options__pb2
from dropbox.proto.pap import event_state_pb2 as dropbox_dot_proto_dot_pap_dot_event__state__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<dropbox/pap/events/onboard/continue_setup_wizard_nonce.proto\x12\x12pap.events.onboard\x1a\x1fdropbox/proto/pap/options.proto\x1a#dropbox/proto/pap/event_state.proto"\xa2\x02\n\x19Continue_SetupWizardNonce\x12\x16\n\x0eaction_surface\x18\x01 \x01(\t\x12N\n\x0bevent_class\x18\xcd\x08 \x01(\x0e28.pap.events.onboard.Continue_SetupWizardNonce.EventClass\x12%\n\x0bevent_state\x18\xce\x08 \x01(\x0e2\x0f.pap.EventState\x12\x1c\n\x14setup_wizard_version\x18\x02 \x01(\t\x12\x1b\n\x13validation_trace_id\x18\x03 \x01(\t"\x19\n\nEventClass\x12\x0b\n\x07ONBOARD\x10\x00: \xca>\x08continue\xd2>\x12setup_wizard_nonceB\x1cZ\x1adropbox/pap/events/onboardb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.pap.events.onboard.continue_setup_wizard_nonce_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1adropbox/pap/events/onboard'
    _globals['_CONTINUE_SETUPWIZARDNONCE']._loaded_options = None
    _globals['_CONTINUE_SETUPWIZARDNONCE']._serialized_options = b'\xca>\x08continue\xd2>\x12setup_wizard_nonce'
    _globals['_CONTINUE_SETUPWIZARDNONCE']._serialized_start = 155
    _globals['_CONTINUE_SETUPWIZARDNONCE']._serialized_end = 445
    _globals['_CONTINUE_SETUPWIZARDNONCE_EVENTCLASS']._serialized_start = 386
    _globals['_CONTINUE_SETUPWIZARDNONCE_EVENTCLASS']._serialized_end = 411
    return None
