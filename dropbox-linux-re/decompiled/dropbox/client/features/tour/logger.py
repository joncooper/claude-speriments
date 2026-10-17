# Source Generated with Decompyle++
# File: logger.pyc (Python 3.11)

from enum import StrEnum, unique
from typing import Any, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.tour.ui.bridge_gen.tour_variant import TourVariant
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.exception.reporting import report_bad_assumption
TourLoggingEvent = <NODE:12>()

def _report_event(account = None, event = None, tour_type = unique, **extra_dict):
    pass
# WARNING: Decompyle incomplete


class DesktopTourLogger:
    report_tour_launched = (lambda account = None, tour_type = None: _report_event(account = account, event = TourLoggingEvent.TOUR_LAUNCHED, tour_type = tour_type))()
    report_user_progressed_to_stage = (lambda account = None, stage = None, tour_type = staticmethod: _report_event(account = account, event = TourLoggingEvent.USER_PROGRESSED_TO_STAGE, tour_type = tour_type, extra = {
'stage': stage }))()
    report_user_completed_tour = (lambda account = None, tour_type = None: _report_event(account = account, event = TourLoggingEvent.USER_COMPLETED_TOUR, tour_type = tour_type))()

