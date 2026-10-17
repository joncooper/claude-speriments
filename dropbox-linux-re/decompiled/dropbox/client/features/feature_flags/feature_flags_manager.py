# Source Generated with Decompyle++
# File: feature_flags_manager.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Dict, Iterable, List, Optional
from build_number.features import feature_enabled
from dropbox.client.features.feature_flags.bridge_gen.bridge_interface_feature_flags_manager import FeatureFlagsManagerBridgeInterface, FeatureFlagsManagerObservableMixin
from dropbox.client.features.feature_flags.bridge_gen.feature_flags_data import FeatureFlagsData
from dropbox.client.features.feature_flags.bridge_gen.feature_lookup_result import FeatureLookupResult
from dropbox.client.features.feature_flags.bridge_gen.feature_name import FeatureName
from dropbox.client.features.feature_flags.bridge_gen.variant_feature_name import VariantFeatureName
from dropbox.client.features.feature_flags.bridge_gen.variant_lookup_result import VariantLookupResult
from dropbox.client.features.feature_flags.feature_definitions import FEATURE_DEFINITIONS, VARIANT_DEFINITIONS
from dropbox.client.features.feature_flags.feature_flags import RegularFeature
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future
from dropbox.foundation.raii2.singleton import SingletonActor

class FeatureFlagsManager(FeatureFlagsManagerBridgeInterface, SingletonActor, FeatureFlagsManagerObservableMixin):
    pass
# WARNING: Decompyle incomplete

