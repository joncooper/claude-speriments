# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from dropbox.client.features.home_feed.shared.util.network_request_handling import RateLimitSettings
from dropbox.foundation.stormcrow.user import UserStormcrow
from dropbox.foundation.stormcrow.utils import get_variant_as_int
DESKTOP_ASSISTANT_MAX_BOLT_REQUESTS_IN_5_MIN = 'desktop-assistant-max-bolt-requests-in-5-min'
DEFAULT_MAX_BOLT_REQUESTS_PER_5_MINS_INTERVAL = 1
ABSOLUTE_MAX_REQUESTS_PER_5_MINS_INTERVAL = 10
FIVE_MINUTES_IN_SECONDS = 300
NOTIFICATION_CLEANOUT_INTERVAL_STORMCROW = 'desktop-assistant-notification-cleanout-interval'
OVERQUOTA_REDESIGN_STORMCROW = 'desktop-overquota-redesign-variant'
DESKTOP_TRAY_OQ_FOOTER_KILLSWITCH = 'desktop-sync-overquota-footer-killswitch'
OVERQUOTA_STICKY_FORCE_ENABLE = 'desktop-overquota-sticky-force-enable'
OVERQUOTA_PREVENTED_STICKY_KILLSWITCH = 'desktop-overquota-prevented-sticky-killswitch'

def _get_rate_limit_settings(user_stormcrow = None, requests_5_min_stormcrow_name = None, default_max_requests_5_mins = None):
    stormcrow_value = get_variant_as_int(user_stormcrow, requests_5_min_stormcrow_name, default_max_requests_5_mins, True)
    runs_per_5_mins = min(ABSOLUTE_MAX_REQUESTS_PER_5_MINS_INTERVAL, stormcrow_value)
    return RateLimitSettings(time_window = FIVE_MINUTES_IN_SECONDS, runs_per_window = runs_per_5_mins)


def get_bolt_rate_limit_settings(user_stormcrow = None):
    return _get_rate_limit_settings(user_stormcrow, DESKTOP_ASSISTANT_MAX_BOLT_REQUESTS_IN_5_MIN, DEFAULT_MAX_BOLT_REQUESTS_PER_5_MINS_INTERVAL)

