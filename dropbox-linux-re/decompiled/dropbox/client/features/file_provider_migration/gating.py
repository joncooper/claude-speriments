# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from datetime import datetime, timezone
from build_number.features import feature_enabled
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.configuration.interface import ConfigurationManagerInterface, LocalConfigurationInterface
from dropbox.client.features.file_provider_migration.constants import FILE_PROVIDER_OPT_OUT_DURING_SIGN_IN_CONFIG_KEY
from dropbox.client.features.file_provider_migration.file_provider_migration_logger import FileProviderMigrationEvent, FileProviderMigrationLogger
from dropbox.platform import IS_MAC

def platform_supports_file_provider_migration():
    if not IS_MAC:
        return False
    MAC_VERSION = MAC_VERSION
    MONTEREY = MONTEREY
    import dropbox.mac.version
    return MAC_VERSION >= MONTEREY


def has_unsupported_multi_team_accounts(account_manager = None):
    if feature_enabled('multi-team-accounts-prod'):
        pass
    return len(account_manager.linked_accounts_all) > len(account_manager.linked_accounts)


def should_initialize_fp_migration_root_converter(config_manager = None):
    if platform_supports_file_provider_migration():
        ReadOnlyStateMachine = ReadOnlyStateMachine
        import dropbox.client.features.file_provider_migration.state_machine
        return ReadOnlyStateMachine.should_attempt_root_conversion(config_manager)


def mark_fp_opt_out(account = None, local_config = None):
    FileProviderMigrationLogger.report_event(account, FileProviderMigrationEvent.OPTED_OUT_DURING_SIGN_IN, None)
    local_config.config_dict[FILE_PROVIDER_OPT_OUT_DURING_SIGN_IN_CONFIG_KEY] = datetime.now(timezone.utc)

