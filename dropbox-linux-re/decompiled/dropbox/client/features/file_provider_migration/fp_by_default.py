# Source Generated with Decompyle++
# File: fp_by_default.pyc (Python 3.11)

from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.preferences import FP_DOWNGRADE
from dropbox.sync_root.gating import file_provider_supported
from dropbox.sync_root.helpers import fp_get_valid_domain_id_from_unlink_cookie

def _fp_did_downgrade(local_config = None):
    if local_config.unlink_cookie:
        return local_config.unlink_cookie.get(FP_DOWNGRADE, False)


def force_start_on_fp(account = None, local_config = None):
    if not file_provider_supported():
        return False
    domain_id = fp_get_valid_domain_id_from_unlink_cookie(account, local_config)
    if not domain_id:
        return False
    domain_exists = domain_exists
    import dropbox.sync_root.handlers.macos.file_provider
    return domain_exists(domain_id)


def force_start_on_mounted(account_manager = None, account = None, local_config = None):
    if _fp_did_downgrade(local_config):
        return True
    mounted_root_path = None.get_valid_path_in_unlink_cookie(account, local_config)
    return mounted_root_path is not None

