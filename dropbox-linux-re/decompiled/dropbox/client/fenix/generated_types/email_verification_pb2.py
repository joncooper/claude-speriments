# Source Generated with Decompyle++
# File: email_verification_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'email_verification.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18email_verification.proto\x12\x13dropbox.meta_engine\x1a\x1bgoogle/protobuf/empty.proto"<\n\nDialogText\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0e\n\x06detail\x18\x03 \x01(\t"\xce\x01\n"ShowEmailVerificationDialogRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x124\n\x0bdialog_text\x18\x02 \x01(\x0b2\x1f.dropbox.meta_engine.DialogText\x12 \n\x18change_email_button_text\x18\x03 \x01(\t\x12 \n\x18resend_email_button_text\x18\x04 \x01(\t\x12\x1a\n\x12cancel_button_text\x18\x05 \x01(\t"j\n\x1dShowSharingErrorDialogRequest\x124\n\x0bdialog_text\x18\x01 \x01(\x0b2\x1f.dropbox.meta_engine.DialogText\x12\x13\n\x0bbutton_text\x18\x02 \x01(\t"w\n\x1dEmailVerificationDialogResult\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12B\n\x06action\x18\x02 \x01(\x0e22.dropbox.meta_engine.EmailVerificationDialogAction*\xe4\x01\n\x1dEmailVerificationDialogAction\x120\n,EMAIL_VERIFICATION_DIALOG_ACTION_UNSPECIFIED\x10\x00\x121\n-EMAIL_VERIFICATION_DIALOG_ACTION_CHANGE_EMAIL\x10\x01\x121\n-EMAIL_VERIFICATION_DIALOG_ACTION_RESEND_EMAIL\x10\x02\x12+\n\'EMAIL_VERIFICATION_DIALOG_ACTION_CANCEL\x10\x032\xe3\x02\n\x14EmailVerificationApi\x12p\n\x1bShowEmailVerificationDialog\x12\x16.google.protobuf.Empty\x1a7.dropbox.meta_engine.ShowEmailVerificationDialogRequest0\x01\x12f\n\x16ShowSharingErrorDialog\x12\x16.google.protobuf.Empty\x1a2.dropbox.meta_engine.ShowSharingErrorDialogRequest0\x01\x12q\n#SubmitEmailVerificationDialogResult\x122.dropbox.meta_engine.EmailVerificationDialogResult\x1a\x16.google.protobuf.Emptyb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'email_verification_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_EMAILVERIFICATIONDIALOGACTION']._serialized_start = 579
    _globals['_EMAILVERIFICATIONDIALOGACTION']._serialized_end = 807
    _globals['_DIALOGTEXT']._serialized_start = 78
    _globals['_DIALOGTEXT']._serialized_end = 138
    _globals['_SHOWEMAILVERIFICATIONDIALOGREQUEST']._serialized_start = 141
    _globals['_SHOWEMAILVERIFICATIONDIALOGREQUEST']._serialized_end = 347
    _globals['_SHOWSHARINGERRORDIALOGREQUEST']._serialized_start = 349
    _globals['_SHOWSHARINGERRORDIALOGREQUEST']._serialized_end = 455
    _globals['_EMAILVERIFICATIONDIALOGRESULT']._serialized_start = 457
    _globals['_EMAILVERIFICATIONDIALOGRESULT']._serialized_end = 576
    _globals['_EMAILVERIFICATIONAPI']._serialized_start = 810
    _globals['_EMAILVERIFICATIONAPI']._serialized_end = 1165
    return None
