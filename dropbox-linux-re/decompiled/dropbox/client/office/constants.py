# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum
OFFICE_ADDIN_DEFAULT_ON_VARIANT = 'DEFAULT_ENABLED'
STORMCROW_FEATURE_OFFICE_ADDIN = 'desktop-native-office-addin'
CONFIG_KEY_ADDIN_IS_FIRST_SET = 'office_addin_default_set'
CONFIG_KEY_USER_INTERACTED_WITH_ADDIN_SETTINGS = 'office_addin_user_has_set'

class OfficeAddInMetrics:
    SET_REGISTRY_ATTEMPT = 'set_registry_attempt'
    SET_REGISTRY_SUCCESS = 'set_registry_success'
    REGISTRY_DISABLED = 'registry_disabled'
    REGISTRY_MALFORMED = 'registry_malformed'
    ADDIN_ENABLED = 'addin_enabled'
    ADDIN_DISABLED = 'addin_disabled'
    PREFERENCES_UPDATED = 'preferences_updated'
    DIALOG_DISPLAYED = 'dialog_displayed'
    DIALOG_ACCEPTED = 'dialog_accept_clicked'
    DIALOG_DENIED = 'dialog_deny_clicked'


class RegistryCheckValues(Enum):
    NotRegistered = 0
    Registered = 1
    Malformed = 2
    Disabled = 3


class AdminSetting(Enum):
    Unknown = 0
    Allowed = 1
    Disallowed = 2


class OfficeAddInFailureReason(Enum, int):
    AdminSettingUnknown = 0
    AdminSettingDisabled = 1
    DisabledInApp = 2


class OfficeAddInPolicy:
    Enabled = 'enabled'
    Disabled = 'disabled'

