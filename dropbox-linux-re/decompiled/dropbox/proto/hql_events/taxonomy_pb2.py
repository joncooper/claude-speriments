# Source Generated with Decompyle++
# File: taxonomy_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/hql_events/taxonomy.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'dropbox/proto/hql_events/taxonomy.proto\x12\nhql_events"\xf4\x03\n\x0eTaxonomyAction"\xe1\x03\n\x06Action\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\t\n\x05START\x10\x01\x12\x0e\n\nFOREGROUND\x10\x02\x12\t\n\x05SHOWN\x10\x03\x12\t\n\x05HOVER\x10\x04\x12\n\n\x06SCROLL\x10\x05\x12\n\n\x06SEARCH\x10\x06\x12\n\n\x06SELECT\x10\x07\x12\x07\n\x03PIN\x10\x08\x12\t\n\x05UNPIN\x10\t\x12\x08\n\x04MOVE\x10\n\x12\n\n\x06RENAME\x10\x0b\x12\x08\n\x04COPY\x10\x0c\x12\n\n\x06DELETE\x10\r\x12\x08\n\x04OPEN\x10\x0e\x12\n\n\x06CREATE\x10\x0f\x12\x13\n\x0fVERSION_HISTORY\x10\x10\x12\x0c\n\x08DOWNLOAD\x10\x11\x12\x0c\n\x08TRANSFER\x10\x12\x12\x0b\n\x07COMMENT\x10\x13\x12\x08\n\x04STAR\x10\x14\x12\n\n\x06UNSTAR\x10\x15\x12\n\n\x06UPLOAD\x10\x16\x12\x0b\n\x07REQUEST\x10\x17\x12\x12\n\x0eREWIND_HISTORY\x10\x18\x12\t\n\x05SHARE\x10\x19\x12\x08\n\x04EDIT\x10\x1a\x12\x0b\n\x07PREVIEW\x10\x1b\x12\x0c\n\x08INITIATE\x10\x1c\x12\x08\n\x04FAIL\x10\x1d\x12\x0b\n\x07SUCCEED\x10\x1e\x12\x0b\n\x07ATTEMPT\x10\x1f\x12\x1c\n\x18PREVIEW_RENDER_SUCCEEDED\x10 \x12\x0b\n\x07DISMISS\x10!\x12\r\n\tHEARTBEAT\x10"\x12\x0c\n\x08CONTINUE\x10#"_\n\rTaxonomyClass"N\n\tClassName\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x11\n\rSEE_AND_CLICK\x10\x01\x12\x10\n\x0cFILE_ACTIONS\x10\x02\x12\x0b\n\x07FEATURE\x10\x03">\n\x10TaxonomySubclass"*\n\x0cSubclassName\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\t\n\x05SHARE\x10\x01"\x82\x01\n\x12TaxonomyAppSurface"l\n\nAppSurface\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x19\n\x15DESKTOP_COLLAB_BROWSE\x10\x01\x12\x10\n\x0cDESKTOP_TRAY\x10\x02\x12\x07\n\x03WEB\x10\x03\x12\n\n\x06NATIVE\x10\x04\x12\x0b\n\x07HARMONY\x10\x05"\x94\x0b\n\x15TaxonomyActionSurface"\xfa\n\n\rActionSurface\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x10\n\x0cSIGN_IN_PAGE\x10\x01\x12\x14\n\x10SIGN_IN_DBX_PAGE\x10\x02\x12\x18\n\x14SIGN_IN_GOOGLE_MODAL\x10\x03\x12%\n!INTERSTITIAL_GOOGLE_ACCOUNTS_PAGE\x10\x04\x12\x0f\n\x0bSIGNUP_PAGE\x10\x05\x12\x0e\n\nSTART_MENU\x10\x06\x12\x0e\n\nSTART_DOCK\x10\x07\x12\r\n\tTRAY_ICON\x10\x08\x12\x15\n\x11NOTIFICATIONS_TAB\x10\t\x12\x0e\n\nRECENT_TAB\x10\n\x12\x0f\n\x0bFOR_YOU_TAB\x10\x0b\x12\x16\n\x12RECENT_YOU_SUB_TAB\x10\x0c\x12\x17\n\x13RECENT_TEAM_SUB_TAB\x10\r\x12\x17\n\x13CALENDAR_EVENT_MENU\x10\x0e\x12\x11\n\rSHARING_MODAL\x10\x0f\x12\x0b\n\x07TOP_BAR\x10\x10\x12\x10\n\x0cFOR_YOU_TABS\x10\x11\x12\x12\n\x0eSEARCH_RESULTS\x10\x12\x12\x17\n\x13TOP_BAR_CREATE_MENU\x10\x13\x12\r\n\tTRAY_MENU\x10\x14\x12\x0f\n\x0bCENTER_PANE\x10\x15\x12\x1c\n\x18PLUS_CANCEL_SURVEY_MODAL\x10\x16\x12\x10\n\x0cPROFILE_MENU\x10\x17\x12\x12\n\x0eBROWSER_WINDOW\x10\x18\x12\x0e\n\nRIGHT_PANE\x10\x19\x12\x18\n\x14CENTER_PANE_PLAN_TAB\x10\x1a\x12\x1b\n\x17CENTER_PANE_GENERAL_TAB\x10\x1b\x12\x1b\n\x17CENTER_PANE_BILLING_TAB\x10\x1c\x12\x16\n\x12CENTER_PANE_PERSON\x10\x1d\x12\x17\n\x13CENTER_PANE_STARRED\x10\x1e\x12#\n\x1fCENTER_PANE_CREATE_CONTEXT_MENU\x10\x1f\x12!\n\x1dCENTER_PANE_VIEW_CONTEXT_MENU\x10 \x12\r\n\tLEFT_PANE\x10!\x12!\n\x1dRIGHT_PANE_SHARE_CONTEXT_MENU\x10"\x12\x0c\n\x08APP_ICON\x10#\x12\x15\n\x11RIGHT_PANE_PERSON\x10$\x12\x1b\n\x17RIGHT_PANE_CONTEXT_MENU\x10%\x12 \n\x1cRIGHT_PANE_OPEN_CONTEXT_MENU\x10&\x12\x14\n\x10APPLICATION_MENU\x10\'\x12\x1e\n\x1aCAROUSEL_ONBOARDING_WINDOW\x10(\x12\x16\n\x12CONNECT_APP_WINDOW\x10)\x12\x16\n\x12ONBOARDING_TOOLTIP\x10*\x12\x1f\n\x1bRIGHT_PANE_PIN_CONTEXT_MENU\x10+\x12\x17\n\x13SPACE_EXAMPLE_MODAL\x10,\x12\x1c\n\x18TEAM_CANCEL_SURVEY_MODAL\x10-\x12\x0e\n\nMOVE_MODAL\x10.\x12\x18\n\x14ACCOUNT_CONTEXT_MENU\x10/\x12\x0e\n\nBOTTOM_BAR\x100\x12\x0e\n\nSYNC_QUEUE\x101\x12\x15\n\x11PLAN_CHANGE_MODAL\x102\x12\x18\n\x14MAGIC_PAIRING_WINDOW\x103\x12\x10\n\x0cCONTEXT_MENU\x104\x12\x0c\n\x08SNACKBAR\x105\x12\x17\n\x13FILE_SYSTEM_WARNING\x106\x12\x0e\n\nSCREENSHOT\x107\x12\x14\n\x10SCREEN_RECORDING\x108\x12\x12\n\x0eREEL_HOME_PAGE\x109\x12\x13\n\x0fREEL_VIDEO_PAGE\x10:\x12\x18\n\x14ESSENTIAL_SETUP_PAGE\x10@"\x04\x08;\x10;"\x04\x08<\x10<"\x04\x08=\x10="\x04\x08>\x10>"\x04\x08?\x10?B:\n\x1ccom.dropbox.proto.hql_eventsP\x01Z\x18dropbox/proto/hql_eventsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.hql_events.taxonomy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.dropbox.proto.hql_eventsP\x01Z\x18dropbox/proto/hql_events'
    _globals['_TAXONOMYACTION']._serialized_start = 56
    _globals['_TAXONOMYACTION']._serialized_end = 556
    _globals['_TAXONOMYACTION_ACTION']._serialized_start = 75
    _globals['_TAXONOMYACTION_ACTION']._serialized_end = 556
    _globals['_TAXONOMYCLASS']._serialized_start = 558
    _globals['_TAXONOMYCLASS']._serialized_end = 653
    _globals['_TAXONOMYCLASS_CLASSNAME']._serialized_start = 575
    _globals['_TAXONOMYCLASS_CLASSNAME']._serialized_end = 653
    _globals['_TAXONOMYSUBCLASS']._serialized_start = 655
    _globals['_TAXONOMYSUBCLASS']._serialized_end = 717
    _globals['_TAXONOMYSUBCLASS_SUBCLASSNAME']._serialized_start = 675
    _globals['_TAXONOMYSUBCLASS_SUBCLASSNAME']._serialized_end = 717
    _globals['_TAXONOMYAPPSURFACE']._serialized_start = 720
    _globals['_TAXONOMYAPPSURFACE']._serialized_end = 850
    _globals['_TAXONOMYAPPSURFACE_APPSURFACE']._serialized_start = 742
    _globals['_TAXONOMYAPPSURFACE_APPSURFACE']._serialized_end = 850
    _globals['_TAXONOMYACTIONSURFACE']._serialized_start = 853
    _globals['_TAXONOMYACTIONSURFACE']._serialized_end = 2281
    _globals['_TAXONOMYACTIONSURFACE_ACTIONSURFACE']._serialized_start = 879
    _globals['_TAXONOMYACTIONSURFACE_ACTIONSURFACE']._serialized_end = 2281
    return None
