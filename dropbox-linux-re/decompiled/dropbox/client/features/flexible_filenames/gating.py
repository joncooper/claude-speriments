# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.flexible_filenames.consts import FFN_VARIANT_STORMCROW, FlexibleFileNameStickyVariant
from dropbox.client.gandalf import Gandalf
from dropbox.proto.nucleus.sync_engine_pb2 import FlexibleFilenamesConfig
__DEFAULT_FLEXIBLE_FILENAMES_RULES = FlexibleFilenamesConfig.Rules.OFF
__FLEXIBLE_FILENAMES_CONFIG_KEY = 'flexible_filenames_rules'
__FLEXIBLE_FILENAMES_DEFAULT_CONFIG_KEY = 'flexible_filenames_rules_default'

def get_flexible_filenames_on_variant(gandalf = None, account = None):
    variant_str = gandalf.get_variant(FFN_VARIANT_STORMCROW, account)
# WARNING: Decompyle incomplete


def get_flexible_filenames_rules(local_config = None):
    current_rules = local_config.config_dict.get(__FLEXIBLE_FILENAMES_CONFIG_KEY)
# WARNING: Decompyle incomplete


def save_flexible_filenames_rules_default(local_config = None, rules = None):
    local_config.config_dict[__FLEXIBLE_FILENAMES_DEFAULT_CONFIG_KEY] = rules


def save_flexible_filenames_rules(local_config = None, rules = None):
    local_config.config_dict[__FLEXIBLE_FILENAMES_CONFIG_KEY] = rules

