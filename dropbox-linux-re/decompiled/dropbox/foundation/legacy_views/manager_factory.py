# Source Generated with Decompyle++
# File: manager_factory.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.foundation.context import Context
from dropbox.foundation.navigation_service.interface import NavigationServiceInterface
from dropbox.foundation.navigation_service.view_manager_interface import ViewManagerInterface
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter

class LegacyViewManagerFactory(object):
    create = (lambda context = None, navigation_service = None, legacy_ui_kit = staticmethod, sync_engine_adapter = ('context', 'Context', 'navigation_service', 'NavigationServiceInterface', 'legacy_ui_kit', 'BaseUIKit', 'sync_engine_adapter', 'SyncEngineAdapter', 'return', 'ViewManagerInterface'): LegacyViewManager = LegacyViewManagerimport managerLegacyViewManager(context, navigation_service, legacy_ui_kit, sync_engine_adapter))()

