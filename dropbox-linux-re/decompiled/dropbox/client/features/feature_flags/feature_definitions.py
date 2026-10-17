# Source Generated with Decompyle++
# File: feature_definitions.pyc (Python 3.11)

from typing import Mapping, Union
from dropbox.client.features.feature_flags.bridge_gen.feature_name import FeatureName
from dropbox.client.features.feature_flags.bridge_gen.variant_feature_name import VariantFeatureName
from dropbox.client.features.feature_flags.feature_flags import CustomFeature, RegularFeature, VariantFeature
from dropbox.client.features.file_locking.constants import DESKTOP_FILE_LOCKING_STORMCROW
from dropbox.client.features.file_locking.file_locking_controller import FileLockingAccessor
from dropbox.client.features.sync_error.feature import SyncErrorsFeature
from dropbox.client.features.sync_everything.gating import BackupAppFeature
from dropbox.foundation.context.user import UserContext

def check_basic_filelocking_enabled(context = None):
    return FileLockingAccessor.context_menu_supported(context.account)


def check_filelocking_locking_enabled(context = None):
