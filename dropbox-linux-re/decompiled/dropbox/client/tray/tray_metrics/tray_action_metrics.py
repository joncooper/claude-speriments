# Source Generated with Decompyle++
# File: tray_action_metrics.pyc (Python 3.11)

from enum import Enum
from typing import Dict, Optional
from dropbox.client.tray.tray_metrics.common import TrayMetrics
from dropbox.enum_utils import auto, AutoLowerNameEnum, StrAsPrefixlessValueTrait

class TrayMetricsView(Enum):
    NATIVE_VIEW = 'tray_native'
    LOCAL_VIEW = 'tray_local_view'
    FALLBACK_MENU = 'tray_fallback_menu'
    MENU_FALLBACK_AND_GEAR_MENU = 'tray_fallback_and_gear_menu'
    NOTIFICATION_STICKY = 'tray_notification_sticky'
    NOTIFICATION_LOUD = 'tray_notification_loud'
    MODAL_DIALOG = 'tray_modal_dialog'
    PREFERENCES_DIALOG = 'tray_preferences_dialog'
    NEW_MENU = 'tray_new_menu'
    UNLINKED_VIEW = 'tray_unlinked_view'


class TrayMetricsActionItem(AutoLowerNameEnum):
    UPGRADE = auto()
    OVER_QUOTA = auto()
    NEAR_QUOTA = auto()
    LOUD_NOTIFICATIONS_AUTHORIZATION_OPEN_SETTINGS = auto()
    LOUD_NOTIFICATIONS_AUTHORIZATION_DISMISS = auto()
    LOUD_NOTIFICATIONS_AUTHORIZATION_LEARN_MORE = auto()
    BOTTOM_PROMPT = auto()
    BOTTOM_PROMPT_DISMISS = auto()
    LAUNCH_WEBSITE = auto()
    OPEN_DROPBOX_FOLDER = auto()
    GEAR_MENU = auto()
    TAB_SWITCH_RECENT = auto()
    TAB_SWITCH_NOTIFICATIONS = auto()
    TAB_SWITCH_SYNC = auto()
    OPEN_SEARCH_SHEET = auto()
    OPEN_NOTIFICATIONS_SHEET = auto()
    RESUME = auto()
    PAUSE = auto()
    SYNC_ISSUES_BUTTON = auto()
    SYNC_ISSUES_BOTTOM_BAR_SEEN = auto()
    VIEW_SYNC_ISSUES = auto()
    ADMIN_CONSOLE = auto()
    IMPORTING = auto()
    TURN_OFF_DND = auto()
    PREFERENCES = auto()
    MANAGE_SPACE = auto()
    HELP = auto()
    QUIT = auto()
    SWITCH_DROPBOX_ACCOUNTS = auto()
    SWITCH_TO_ACCOUNT = auto()
    LINK_ACCOUNT = auto()
    SNOOZE_NOTIFICATIONS = auto()
    OPEN_UPGRADE = auto()
    SEND_FEEDBACK = auto()
    SYNC_DASHABORD = auto()
    SIGN_IN = auto()
    HELP_CENTER = auto()
    SNOOZE_SYNC = auto()
    OS_CONSENT = auto()
    TRAY_CONTENT = auto()
    SYNC_VIEW_SEEN_WITH_STUCK_ITEMS = auto()
    MERGED_TRAY_TOOL_TIP_SEEN = auto()
    TOOLTIP_RENDERED = auto()
    TRAY_ICON_RICH_TOOLTIP_SEEN = auto()
    DASH_TOOLTIP_DISMISSED_CLICKED = auto()


class TrayMetricsActionMetric(Enum):
    SHOW = 'tray_action_metric_show'
    NOT_SHOW = 'tray_action_metric_not_show'
    CLICK = 'tray_action_metric_click'


class TrayMetric(AutoLowerNameEnum, StrAsPrefixlessValueTrait):
    TRIGGERED_TRAY = auto()
    SHOWN_TRAY = auto()
    SHOWN_MENU = auto()
    TRAY_SESSION_LENGTH = auto()


class TrayEmbedMetric(AutoLowerNameEnum):
    TRAY_EMBED_TRIGGER = auto()
    TRAY_EMBED_SUCCESS = auto()
    TRAY_EMBED_FAILURE = auto()


class TrayFailureMetric(AutoLowerNameEnum, StrAsPrefixlessValueTrait):
    TRAY_MISSING_POPUP_CONTROLLER = auto()


class TrayActionMetrics:
    log_tray_action = (lambda *: tags = {
'tray_view': tray_view.value,
'tray_item': tray_action_item.value }if additional_tags:
tags.update(additional_tags)TrayMetrics.log_tray_metric_with_tags(tray_action_type.value, tags, 1))()


def get_tray_metrics_action_item(label = None):
    if label == 'view_sync_issues':
        return TrayMetricsActionItem.VIEW_SYNC_ISSUES
    if None == 'admin_console':
        return TrayMetricsActionItem.ADMIN_CONSOLE
    if None == 'importing':
        return TrayMetricsActionItem.IMPORTING
    if None == 'turn_on_notifications':
        return TrayMetricsActionItem.TURN_OFF_DND
    if None == 'preferences':
        return TrayMetricsActionItem.PREFERENCES
    if None == 'manage_space':
        return TrayMetricsActionItem.MANAGE_SPACE
    if None == 'help_center':
        return TrayMetricsActionItem.HELP
    if None == 'quit':
        return TrayMetricsActionItem.QUIT
    if None == 'sign_in':
        return TrayMetricsActionItem.SIGN_IN
    if None == 'switch_dropbox_accounts':
        return TrayMetricsActionItem.SWITCH_DROPBOX_ACCOUNTS
    if None == 'upgrade':
        return TrayMetricsActionItem.UPGRADE
    if None == 'open_upgrade':
        return TrayMetricsActionItem.OPEN_UPGRADE
    if None == 'snooze_notifications':
        return TrayMetricsActionItem.SNOOZE_NOTIFICATIONS
    if None == 'pause':
        return TrayMetricsActionItem.PAUSE
    if None == 'resume':
        return TrayMetricsActionItem.RESUME
    if None == 'snooze_sync':
        return TrayMetricsActionItem.SNOOZE_SYNC
    if None == 'account_switch':
        return TrayMetricsActionItem.SWITCH_TO_ACCOUNT
    if None == 'link_account':
        return TrayMetricsActionItem.LINK_ACCOUNT
    if None == 'link_client':
        return TrayMetricsActionItem.SIGN_IN
    if None == 'os_consent':
        return TrayMetricsActionItem.OS_CONSENT
    if None == 'sendFeedback':
        return TrayMetricsActionItem.SEND_FEEDBACK
    if None == 'sync_issues_button':
        return TrayMetricsActionItem.SYNC_ISSUES_BUTTON
    if None == 'sync_issues_bottom_bar_seen':
        return TrayMetricsActionItem.SYNC_ISSUES_BOTTOM_BAR_SEEN
    if None == 'sync_view_seen_with_stuck_items':
        return TrayMetricsActionItem.SYNC_VIEW_SEEN_WITH_STUCK_ITEMS
    if None == 'merged-tray-tool-tip-seen':
        return TrayMetricsActionItem.MERGED_TRAY_TOOL_TIP_SEEN
    if None == 'merged-tray-tool-tip-rendered':
        return TrayMetricsActionItem.TOOLTIP_RENDERED
    if None == 'tray-icon-rich-tooltip-seen':
        return TrayMetricsActionItem.TRAY_ICON_RICH_TOOLTIP_SEEN
    if None == 'dash-tooltip-dismissed-clicked':
        return TrayMetricsActionItem.DASH_TOOLTIP_DISMISSED_CLICKED
    if None == 'sync_dashboard':
        return TrayMetricsActionItem.SYNC_DASHABORD

