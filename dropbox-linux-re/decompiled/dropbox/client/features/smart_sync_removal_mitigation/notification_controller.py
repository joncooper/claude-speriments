# Source Generated with Decompyle++
# File: notification_controller.pyc (Python 3.11)

from typing import Dict
from helpers import ss_removal_mitigation_degraded_placeholders_enabled
from logging.ss_removal_mitigation_logger import SSRemovalMitigationLogger
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import ConfigurationManagerInterface, LocalConfigurationInterface
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.smart_sync_removal_mitigation.helpers import SS_REMOVAL_MITIGATION_DP_STICKY_ACKNOWLEDGED_CONFIG_KEY
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.legacy_notifications import SSRemovalMitigationDegradedPlaceholdersStickyNotification
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.context.machine import AccountManager
from dropbox.infinite.constants import InfiniteState
from dropbox.url_info import DropboxURLInfo

class SSRemovalMitigationDegradedPlaceholdersStrings(UIStrings):
    title = UI('Trouble opening files?')
    message = UI('Right now, some apps on your Mac might have trouble opening online-only files.')
    learn_more = UI('Learn more')
    got_it = UI('Got it')


class SmartSyncRemovalMitigationNotifier(Actor):
    pass
# WARNING: Decompyle incomplete

