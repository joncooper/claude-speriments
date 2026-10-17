# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from enum import StrEnum
PROMOTION_NOTIFICATION_HEIGHT = 368
PROMOTION_NOTIFICATION_WIDTH = 383

class TrayPromotionState(StrEnum):
    PENDING = 'pending'
    INELIGIBLE = 'ineligible'


class DialogStopReason(StrEnum):
    SEEN_TRAY = 'seen_tray'
    MAX_ATTEMPTS = 'max_attempts'
    EXISTING_LINKED_USER_SEEN_TRAY = 'existing_linked_user_seen_tray'

TRAY_PROMOTION_STATE_CONFIG_KEY = 'tray_promotion_state'
TRAY_PROMOTION_DIALOG_NEXT_SCHEDULED_TIME = 'tray_promotion_dialog_next_scheduled_time'
TRAY_PROMOTION_ATTEMPTS_PENDING = 'tray_promotion_attempts_pending'
DELAY_TRAY_PROMOTION_SECONDS = 2419200
DEBUG_DELAY_TRAY_PROMOTION_SECONDS = 60
TWO_WEEKS_IN_SECONDS = 1209600
TRAY_PROMOTION_MAX_ATTEMPTS = 3
TRAY_PROMOTION_PIN_DROPBOX_STORMCROW = 'desktop-tray-promotion-prompt'
