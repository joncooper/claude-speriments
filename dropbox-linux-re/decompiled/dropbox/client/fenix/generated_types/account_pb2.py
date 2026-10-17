# Source Generated with Decompyle++
# File: account_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'account.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from  import shared_pb2 as shared__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\raccount.proto\x12\x13dropbox.meta_engine\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0cshared.proto",\n\x14RegisterHostResponse\x12\x14\n\x0craw_response\x18\x01 \x01(\t"\xf7\x02\n\x0fLinkPreferences\x12\x14\n\x0cdropbox_path\x18\x01 \x01(\t\x12\x1c\n\x14directory_ignore_set\x18\x02 \x03(\t\x12\x1b\n\x13open_dropbox_folder\x18\x03 \x01(\x08\x12\x1a\n\x12show_linked_bubble\x18\x04 \x01(\x08\x12"\n\x1acontent_starts_online_only\x18\x05 \x01(\x08\x12%\n\x1dcloud_files_migration_opt_out\x18\x06 \x01(\x08\x12\x1d\n\x15file_provider_opt_out\x18\x07 \x01(\x08\x12\x16\n\x0esync_root_type\x18\x08 \x01(\t\x12\x1d\n\x15sync_root_type_reason\x18\t \x01(\t\x12\x19\n\x11promote_tray_icon\x18\n \x01(\x08\x12\x1e\n\x16root_folder_file_count\x18\x0b \x01(\x05\x12\x1b\n\x13selected_file_count\x18\x0c \x01(\x05"(\n\x12PostLinkSetupFlags\x12\x12\n\nflags_json\x18\x01 \x01(\t"\xd1\x02\n&RegisterLocallyAuthenticatedAccountReq\x12:\n\x07account\x18\x01 \x01(\x0b2).dropbox.meta_engine.AuthenticatedAccount\x12I\n\x16register_host_response\x18\x02 \x01(\x0b2).dropbox.meta_engine.RegisterHostResponse\x12>\n\x10link_preferences\x18\x03 \x01(\x0b2$.dropbox.meta_engine.LinkPreferences\x12F\n\x15post_link_setup_flags\x18\x04 \x01(\x0b2\'.dropbox.meta_engine.PostLinkSetupFlags\x12\x18\n\x10enabled_variants\x18\x05 \x03(\t"\xb2\x01\n)InitializeMinimalAuthenticatedServicesReq\x12:\n\x07account\x18\x01 \x01(\x0b2).dropbox.meta_engine.AuthenticatedAccount\x12I\n\x16register_host_response\x18\x02 \x01(\x0b2).dropbox.meta_engine.RegisterHostResponse"F\n\x14GetAccountForRoleReq\x12.\n\x04role\x18\x01 \x01(\x0e2 .dropbox.meta_engine.AccountRole"T\n\x16GetAccountForRoleReply\x12:\n\x07account\x18\x01 \x01(\x0b2).dropbox.meta_engine.AuthenticatedAccount"\\\n\x1dGetLocallyLinkedAccountsReply\x12;\n\x08accounts\x18\x01 \x03(\x0b2).dropbox.meta_engine.AuthenticatedAccount"_\n GetLocallyLinkedAccountsAllReply\x12;\n\x08accounts\x18\x01 \x03(\x0b2).dropbox.meta_engine.AuthenticatedAccount"j\n\x0bAccountOrId\x12\x14\n\naccount_id\x18\x01 \x01(\tH\x00\x12<\n\x07account\x18\x02 \x01(\x0b2).dropbox.meta_engine.AuthenticatedAccountH\x00B\x07\n\x05value"U\n\x1aGetServerLinkedAccountsReq\x127\n\raccount_or_id\x18\x01 \x01(\x0b2 .dropbox.meta_engine.AccountOrId"\xb3\x01\n\rServerAccount\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\x04\x12\r\n\x05email\x18\x03 \x01(\t\x12\x16\n\x0eemail_verified\x18\x04 \x01(\x08\x12\x14\n\x0cdisplay_name\x18\x05 \x01(\t\x12\x12\n\nfirst_name\x18\x06 \x01(\t\x12\x0c\n\x04role\x18\x07 \x01(\t\x12\x0f\n\x07team_id\x18\x08 \x01(\x04\x12\x11\n\tteam_name\x18\t \x01(\t"T\n\x1cGetServerLinkedAccountsReply\x124\n\x08accounts\x18\x01 \x03(\x0b2".dropbox.meta_engine.ServerAccount"T\n\x19GetQuotaInfoForAccountReq\x127\n\raccount_or_id\x18\x01 \x01(\x0b2 .dropbox.meta_engine.AccountOrId"4\n\tQuotaInfo\x12\x13\n\x0broot_in_use\x18\x01 \x01(\x04\x12\x12\n\nroot_quota\x18\x02 \x01(\x04"L\n\x11GetAppdataPathReq\x127\n\raccount_or_id\x18\x01 \x01(\x0b2 .dropbox.meta_engine.AccountOrId"\x1b\n\x0bAppdataPath\x12\x0c\n\x04path\x18\x01 \x01(\t"o\n\x1eGetAccountLinkedOrFromCacheReq\x127\n\raccount_or_id\x18\x01 \x01(\x0b2 .dropbox.meta_engine.AccountOrId\x12\x14\n\x0cshould_raise\x18\x02 \x01(\x08"^\n GetAccountLinkedOrFromCacheReply\x12:\n\x07account\x18\x01 \x01(\x0b2).dropbox.meta_engine.AuthenticatedAccount"S\n\x15GetActiveAccountReply\x12:\n\x07account\x18\x01 \x01(\x0b2).dropbox.meta_engine.AuthenticatedAccount")\n\x13SetActiveAccountReq\x12\x12\n\naccount_id\x18\x01 \x01(\t")\n\x13GetHomeMountPathReq\x12\x12\n\naccount_id\x18\x01 \x01(\t"\x1d\n\rHomeMountPath\x12\x0c\n\x04path\x18\x01 \x01(\t"1\n HasKnownAccountsLinkedFiredReply\x12\r\n\x05fired\x18\x01 \x01(\x08"$\n\x0eGetPlanInfoReq\x12\x12\n\naccount_id\x18\x01 \x01(\t"A\n\x08PlanInfo\x12\x1b\n\x13has_unlimited_space\x18\x01 \x01(\x08\x12\x18\n\x10is_reseller_user\x18\x02 \x01(\x08"4\n\x1eGetBusinessBasicEligibilityReq\x12\x12\n\naccount_id\x18\x01 \x01(\t"/\n\x18BusinessBasicEligibility\x12\x13\n\x0bis_enrolled\x18\x01 \x01(\x08"\x97\x01\n\x17LocalAccountChangeEvent\x12:\n\x07account\x18\x01 \x01(\x0b2).dropbox.meta_engine.AuthenticatedAccount\x12@\n\x0bchange_type\x18\x02 \x01(\x0e2+.dropbox.meta_engine.LocalAccountChangeType"\x19\n\x17LocalAccountPairedEvent"\x1a\n\x18KnownAccountsLinkedEvent"[\n\x1dTrayActiveAccountChangedEvent\x12:\n\x07account\x18\x01 \x01(\x0b2).dropbox.meta_engine.AuthenticatedAccount"\xb2\x03\n\x0cAccountEvent\x12L\n\x14local_account_change\x18\x01 \x01(\x0b2,.dropbox.meta_engine.LocalAccountChangeEventH\x00\x12L\n\x14local_account_paired\x18\x02 \x01(\x0b2,.dropbox.meta_engine.LocalAccountPairedEventH\x00\x12N\n\x15known_accounts_linked\x18\x03 \x01(\x0b2-.dropbox.meta_engine.KnownAccountsLinkedEventH\x00\x12Y\n\x1btray_active_account_changed\x18\x04 \x01(\x0b22.dropbox.meta_engine.TrayActiveAccountChangedEventH\x00\x12P\n\x18local_account_change_all\x18\x05 \x01(\x0b2,.dropbox.meta_engine.LocalAccountChangeEventH\x00B\t\n\x07payload*\xa6\x01\n\x10AccountEventType\x12"\n\x1eACCOUNT_EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14LOCAL_ACCOUNT_CHANGE\x10\x01\x12\x18\n\x14LOCAL_ACCOUNT_PAIRED\x10\x02\x12\x19\n\x15KNOWN_ACCOUNTS_LINKED\x10\x03\x12\x1f\n\x1bTRAY_ACTIVE_ACCOUNT_CHANGED\x10\x04*]\n\x16LocalAccountChangeType\x12)\n%LOCAL_ACCOUNT_CHANGE_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06LINKED\x10\x01\x12\x0c\n\x08UNLINKED\x10\x022\xcd\r\n\nAccountApi\x12z\n#RegisterLocallyAuthenticatedAccount\x12;.dropbox.meta_engine.RegisterLocallyAuthenticatedAccountReq\x1a\x16.google.protobuf.Empty\x12\x80\x01\n&InitializeMinimalAuthenticatedServices\x12>.dropbox.meta_engine.InitializeMinimalAuthenticatedServicesReq\x1a\x16.google.protobuf.Empty\x12k\n\x11GetAccountForRole\x12).dropbox.meta_engine.GetAccountForRoleReq\x1a+.dropbox.meta_engine.GetAccountForRoleReply\x12f\n\x18GetLocallyLinkedAccounts\x12\x16.google.protobuf.Empty\x1a2.dropbox.meta_engine.GetLocallyLinkedAccountsReply\x12l\n\x1bGetLocallyLinkedAccountsAll\x12\x16.google.protobuf.Empty\x1a5.dropbox.meta_engine.GetLocallyLinkedAccountsAllReply\x12}\n\x17GetServerLinkedAccounts\x12/.dropbox.meta_engine.GetServerLinkedAccountsReq\x1a1.dropbox.meta_engine.GetServerLinkedAccountsReply\x12h\n\x16GetQuotaInfoForAccount\x12..dropbox.meta_engine.GetQuotaInfoForAccountReq\x1a\x1e.dropbox.meta_engine.QuotaInfo\x12Z\n\x0eGetAppdataPath\x12&.dropbox.meta_engine.GetAppdataPathReq\x1a .dropbox.meta_engine.AppdataPath\x12\x89\x01\n\x1bGetAccountLinkedOrFromCache\x123.dropbox.meta_engine.GetAccountLinkedOrFromCacheReq\x1a5.dropbox.meta_engine.GetAccountLinkedOrFromCacheReply\x12V\n\x10GetActiveAccount\x12\x16.google.protobuf.Empty\x1a*.dropbox.meta_engine.GetActiveAccountReply\x12T\n\x10SetActiveAccount\x12(.dropbox.meta_engine.SetActiveAccountReq\x1a\x16.google.protobuf.Empty\x12`\n\x10GetHomeMountPath\x12(.dropbox.meta_engine.GetHomeMountPathReq\x1a".dropbox.meta_engine.HomeMountPath\x12l\n\x1bHasKnownAccountsLinkedFired\x12\x16.google.protobuf.Empty\x1a5.dropbox.meta_engine.HasKnownAccountsLinkedFiredReply\x12Q\n\x0bGetPlanInfo\x12#.dropbox.meta_engine.GetPlanInfoReq\x1a\x1d.dropbox.meta_engine.PlanInfo\x12\x81\x01\n\x1bGetBusinessBasicEligibility\x123.dropbox.meta_engine.GetBusinessBasicEligibilityReq\x1a-.dropbox.meta_engine.BusinessBasicEligibility\x12W\n\x18SubscribeToAccountEvents\x12\x16.google.protobuf.Empty\x1a!.dropbox.meta_engine.AccountEvent0\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'account_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_ACCOUNTEVENTTYPE']._serialized_start = 3537
    _globals['_ACCOUNTEVENTTYPE']._serialized_end = 3703
    _globals['_LOCALACCOUNTCHANGETYPE']._serialized_start = 3705
    _globals['_LOCALACCOUNTCHANGETYPE']._serialized_end = 3798
    _globals['_REGISTERHOSTRESPONSE']._serialized_start = 81
    _globals['_REGISTERHOSTRESPONSE']._serialized_end = 125
    _globals['_LINKPREFERENCES']._serialized_start = 128
    _globals['_LINKPREFERENCES']._serialized_end = 503
    _globals['_POSTLINKSETUPFLAGS']._serialized_start = 505
    _globals['_POSTLINKSETUPFLAGS']._serialized_end = 545
    _globals['_REGISTERLOCALLYAUTHENTICATEDACCOUNTREQ']._serialized_start = 548
    _globals['_REGISTERLOCALLYAUTHENTICATEDACCOUNTREQ']._serialized_end = 885
    _globals['_INITIALIZEMINIMALAUTHENTICATEDSERVICESREQ']._serialized_start = 888
    _globals['_INITIALIZEMINIMALAUTHENTICATEDSERVICESREQ']._serialized_end = 1066
    _globals['_GETACCOUNTFORROLEREQ']._serialized_start = 1068
    _globals['_GETACCOUNTFORROLEREQ']._serialized_end = 1138
    _globals['_GETACCOUNTFORROLEREPLY']._serialized_start = 1140
    _globals['_GETACCOUNTFORROLEREPLY']._serialized_end = 1224
    _globals['_GETLOCALLYLINKEDACCOUNTSREPLY']._serialized_start = 1226
    _globals['_GETLOCALLYLINKEDACCOUNTSREPLY']._serialized_end = 1318
    _globals['_GETLOCALLYLINKEDACCOUNTSALLREPLY']._serialized_start = 1320
    _globals['_GETLOCALLYLINKEDACCOUNTSALLREPLY']._serialized_end = 1415
    _globals['_ACCOUNTORID']._serialized_start = 1417
    _globals['_ACCOUNTORID']._serialized_end = 1523
    _globals['_GETSERVERLINKEDACCOUNTSREQ']._serialized_start = 1525
    _globals['_GETSERVERLINKEDACCOUNTSREQ']._serialized_end = 1610
    _globals['_SERVERACCOUNT']._serialized_start = 1613
    _globals['_SERVERACCOUNT']._serialized_end = 1792
    _globals['_GETSERVERLINKEDACCOUNTSREPLY']._serialized_start = 1794
    _globals['_GETSERVERLINKEDACCOUNTSREPLY']._serialized_end = 1878
    _globals['_GETQUOTAINFOFORACCOUNTREQ']._serialized_start = 1880
    _globals['_GETQUOTAINFOFORACCOUNTREQ']._serialized_end = 1964
    _globals['_QUOTAINFO']._serialized_start = 1966
    _globals['_QUOTAINFO']._serialized_end = 2018
    _globals['_GETAPPDATAPATHREQ']._serialized_start = 2020
    _globals['_GETAPPDATAPATHREQ']._serialized_end = 2096
    _globals['_APPDATAPATH']._serialized_start = 2098
    _globals['_APPDATAPATH']._serialized_end = 2125
    _globals['_GETACCOUNTLINKEDORFROMCACHEREQ']._serialized_start = 2127
    _globals['_GETACCOUNTLINKEDORFROMCACHEREQ']._serialized_end = 2238
    _globals['_GETACCOUNTLINKEDORFROMCACHEREPLY']._serialized_start = 2240
    _globals['_GETACCOUNTLINKEDORFROMCACHEREPLY']._serialized_end = 2334
    _globals['_GETACTIVEACCOUNTREPLY']._serialized_start = 2336
    _globals['_GETACTIVEACCOUNTREPLY']._serialized_end = 2419
    _globals['_SETACTIVEACCOUNTREQ']._serialized_start = 2421
    _globals['_SETACTIVEACCOUNTREQ']._serialized_end = 2462
    _globals['_GETHOMEMOUNTPATHREQ']._serialized_start = 2464
    _globals['_GETHOMEMOUNTPATHREQ']._serialized_end = 2505
    _globals['_HOMEMOUNTPATH']._serialized_start = 2507
    _globals['_HOMEMOUNTPATH']._serialized_end = 2536
    _globals['_HASKNOWNACCOUNTSLINKEDFIREDREPLY']._serialized_start = 2538
    _globals['_HASKNOWNACCOUNTSLINKEDFIREDREPLY']._serialized_end = 2587
    _globals['_GETPLANINFOREQ']._serialized_start = 2589
    _globals['_GETPLANINFOREQ']._serialized_end = 2625
    _globals['_PLANINFO']._serialized_start = 2627
    _globals['_PLANINFO']._serialized_end = 2692
    _globals['_GETBUSINESSBASICELIGIBILITYREQ']._serialized_start = 2694
    _globals['_GETBUSINESSBASICELIGIBILITYREQ']._serialized_end = 2746
    _globals['_BUSINESSBASICELIGIBILITY']._serialized_start = 2748
    _globals['_BUSINESSBASICELIGIBILITY']._serialized_end = 2795
    _globals['_LOCALACCOUNTCHANGEEVENT']._serialized_start = 2798
    _globals['_LOCALACCOUNTCHANGEEVENT']._serialized_end = 2949
    _globals['_LOCALACCOUNTPAIREDEVENT']._serialized_start = 2951
    _globals['_LOCALACCOUNTPAIREDEVENT']._serialized_end = 2976
    _globals['_KNOWNACCOUNTSLINKEDEVENT']._serialized_start = 2978
    _globals['_KNOWNACCOUNTSLINKEDEVENT']._serialized_end = 3004
    _globals['_TRAYACTIVEACCOUNTCHANGEDEVENT']._serialized_start = 3006
    _globals['_TRAYACTIVEACCOUNTCHANGEDEVENT']._serialized_end = 3097
    _globals['_ACCOUNTEVENT']._serialized_start = 3100
    _globals['_ACCOUNTEVENT']._serialized_end = 3534
    _globals['_ACCOUNTAPI']._serialized_start = 3801
    _globals['_ACCOUNTAPI']._serialized_end = 5542
    return None
