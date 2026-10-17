# Source Generated with Decompyle++
# File: migration.pyc (Python 3.11)

from __future__ import absolute_import, annotations, division, print_function
from enum import Enum
from typing import Any, MutableMapping, Text, TYPE_CHECKING
from dropbox.proto.nucleus.fsw_generated_pb2 import ALLOW_MOVE_FILE_OR_FLAT_FOLDER_OUT_OF_TSD, ALLOW_MOVE_NS_OUT_OF_TSD, ALLOW_MOVE_TO_FORBID_NON_TEAM_SHARING, ALLOW_MOVE_TO_FORBID_SHARING_WHEN_OWNER_ACL_ONLY, CDM_ONBOARDING_COPY, CDM_ONBOARDING_CREATE, CDM_ONBOARDING_MOVE, CLOUD_DOCS_COPY_TO_IGNORED, CLOUD_DOCS_CREATE, CLOUD_DOCS_MOVE_TO_TRASH2, CLOUD_DOCS_MOVE_TO_TRASH_INACCESSIBLE, CLOUD_DOCS_MOVE_TO_TRASH_INACCESSIBLE2, CONFIDENTIAL_COPY, CONFIDENTIAL_MOVE, DEVICE_FOLDER_CONTENT_MOVE_TO_TRASH, DEVICE_FOLDER_CONTENT_MOVE_TO_TRASH_INACCESSIBLE, MOVE_SF_TO_TF_NON_OWNER_CONFIRMATION, RESTORATIONS_1, RESTORATIONS_1_AND_3_INACCESSIBLE, RESTORATIONS_2, RESTORATIONS_3, RESTORATIONS_4, RESTORATIONS_5, RESTORATIONS_5_INACCESSIBLE, RESTORATIONS_6A, RESTORATIONS_6A_EXAMPLE, RESTORATIONS_6B, SHARED_FOLDER_NESTING_IMPLICIT_SHARE_ON_MOVE, SMART_SYNC_MOVE_TO_TRASH_INACCESSIBLE, SuspendableRule, TEAM_MEMBER_FOLDER_COPY, WARNING_TMR_MOVE_OUT_OF_TEAM_SPACE
from dropbox.sync_root.gating import file_provider_supported
from dropbox.trace import TRACE
if TYPE_CHECKING:
    from dropbox.client.configuration.manager import ConfigurationManager

class SuspendableRuleName(Enum):
    restorations_1 = 'restorations_1'
    restorations_2 = 'restorations_2'
    restorations_3 = 'restorations_3'
    restorations_4 = 'restorations_4'
    restorations_5 = 'restorations_5'
    restorations_6a = 'restorations_6a'
    restorations_6b = 'restorations_6b'
    restorations_1_and_3_inaccessible = 'restorations_1_and_3_inaccessible'
    restorations_5_inaccessible = 'restorations_5_inaccessible'
    confidential_copy = 'confidential_copy'
    confidential_move = 'confidential_move'
    smart_sync_move_to_trash_inaccessible = 'smart_sync_move_to_trash_inaccessible'
    cloud_docs_move_to_trash_inaccessible = 'cloud_docs_move_to_trash_inaccessible'
    cloud_docs_move_to_trash = 'cloud_docs_move_to_trash'
    cloud_docs_create = 'cloud_docs_create'
    device_folder_content_move_to_trash = 'device_folder_content_move_to_trash'
    device_folder_content_move_to_trash_inaccessible = 'device_folder_content_move_to_trash_inaccessible'
    cloud_docs_copy_to_ignored = 'cloud_docs_copy_to_ignored'
    allow_move_file_or_flat_folder_out_of_tsd = 'allow_move_file_or_flat_folder_out_of_tsd'
    allow_move_ns_out_of_tsd = 'allow_move_ns_out_of_tsd'
    allow_move_to_forbid_non_team_sharing = 'allow_move_to_forbid_non_team_sharing'
    allow_move_to_forbid_sharing_when_owner_acl_only = 'allow_move_to_forbid_sharing_when_owner_acl_only'
    move_sf_to_tf_non_owner_confirmation = 'move_sf_to_tf_non_owner_confirmation'
    cdm_onboarding_move = 'cdm_onboarding_move'
    cdm_onboarding_create = 'cdm_onboarding_create'
    cdm_onboarding_copy = 'cdm_onboarding_copy'
    team_member_folder_copy = 'team_member_folder_copy'
    shared_folder_nesting_implicit_share_on_move = 'shared_folder_nesting_implicit_share_on_move'
    warning_tmr_move_out_of_team_space = 'warning_tmr_move_out_of_team_space'
    from_proto = (lambda proto = None: pass# WARNING: Decompyle incomplete
)()


class FSWSuppressionSettings:
    CONFIG_DICT_KEY_FOR_FSW_SUPPRESSION_SETTINGS = 'FSWSuppressionSettings'
    
    def __init__(self = None, config_manager = None):
        self._config_manager = config_manager
        rule_state_dict = self._get_settings_config()
        TRACE('Initialized FSWSuppressionSettings: %r', rule_state_dict)
        self.migrate()

    
    def suppress_rule(self = None, rule_name = None):
        rule_state_dict = self._get_settings_config()
        rule_state_dict[rule_name.value] = True
        self._config_manager.local_config(None).config_dict[FSWSuppressionSettings.CONFIG_DICT_KEY_FOR_FSW_SUPPRESSION_SETTINGS] = rule_state_dict
        TRACE('suppress_rule: %r', rule_name)

    
    def reset_all_suppressions(self = None):
        rule_state_dict = { }
        self._config_manager.local_config(None).config_dict[FSWSuppressionSettings.CONFIG_DICT_KEY_FOR_FSW_SUPPRESSION_SETTINGS] = rule_state_dict
        if file_provider_supported():
            fp_reset_fsw_suppressions = fp_reset_fsw_suppressions
            import dropbox.sync_root.fp_helpers
            fp_reset_fsw_suppressions()
        TRACE('reset_all_suppressions: %r', rule_state_dict)

    
    def is_rule_suppressed(self = None, rule_name = None):
        if self._is_rule_suppressed_new_style(rule_name):
            return True
        return None._is_rule_suppressed_old_style(rule_name)

    
    def _is_rule_suppressed_new_style(self = None, rule_name = None):
        return self._get_settings_config().get(rule_name.value, False)

    
    def _get_settings_config(self = None):
        return self._config_manager.local_config(None).config_dict.get(FSWSuppressionSettings.CONFIG_DICT_KEY_FOR_FSW_SUPPRESSION_SETTINGS, { })

    
    def _get_old_sec_rule_config(self = None, rule_dict_key = None):
        return self._config_manager.local_config(None).config_dict.get(rule_dict_key, { })

    
    def _is_rule_suppressed_old_style(self = None, rule_name = None):
        pass
    # WARNING: Decompyle incomplete

    
    def migrate(self = None):
        for rule_name in SuspendableRuleName:
            if not self._is_rule_suppressed_old_style(rule_name) and self._is_rule_suppressed_new_style(rule_name):
                TRACE('Migrating rule %r', rule_name)
                self.suppress_rule(rule_name)
            return None


