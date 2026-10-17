# Source Generated with Decompyle++
# File: notification_config.pyc (Python 3.11)

from datetime import datetime, timedelta, timezone
from typing import List, Optional
from dropbox.client.lib.stormcrow.constants import VARIANT_OFF
VARIANT_INDEFINITELY_DISMISS = 'INDEFINITELY_DISMISS'
VARIANT_CANNOT_DISMISS = 'CANNOT_DISMISS'
VARIANT_7_DAYS = '7_DAYS'
VARIANT_28_DAYS = '28_DAYS'

def can_show_notification(variant = None, last_dismissed_time = None):
    if variant == VARIANT_CANNOT_DISMISS:
        return True
    if None == VARIANT_INDEFINITELY_DISMISS:
        return last_dismissed_time is None
    variant_to_time = {
        VARIANT_28_DAYS: timedelta(days = 28),
        None: timedelta(days = 7) }
    if variant not in variant_to_time:
        return False
# WARNING: Decompyle incomplete


def get_dismiss_config(variants = None):
    if len(variants) == 1:
        return variants[0]
    variant_priority_order = [
        None,
        VARIANT_28_DAYS,
        VARIANT_7_DAYS,
        VARIANT_OFF,
        VARIANT_INDEFINITELY_DISMISS]
    for variant in variant_priority_order:
        if variant in variants:
            
            return None, variant
        return VARIANT_OFF

