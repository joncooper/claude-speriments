# Source Generated with Decompyle++
# File: snooze_time_calc.pyc (Python 3.11)

from datetime import datetime, timedelta
from enum import IntEnum
from dropbox.client.notifications.loud_notifications.local_time_getter import LocalTimeGetter
from dropbox.exception.reporting import report_bad_assumption

class SnoozeTimeInterval(IntEnum):
    UNKNOWN = 0
    THIRTY_MINUTES = 1
    ONE_HOUR = 2
    UNTIL_AFTERNOON = 3
    UNTIL_END_OF_DAY = 4
    UNTIL_TOMORROW = 5
    INDEFINITELY = 6


class SnoozeTimeCalculator:
    calculate_snooze_end_time = (lambda time_interval = None, current_time = None: current_time = current_time.replace(microsecond = 0)if time_interval == SnoozeTimeInterval.THIRTY_MINUTES:
end_time = SnoozeTimeCalculator.calc_end_time(current_time, timedelta(minutes = 30))elif time_interval == SnoozeTimeInterval.ONE_HOUR:
end_time = SnoozeTimeCalculator.calc_end_time(current_time, timedelta(hours = 1))elif time_interval == SnoozeTimeInterval.UNTIL_AFTERNOON:
if current_time.hour >= 13:
report_bad_assumption('Trying to set the snooze time to 1PM even though it is after 1PM')end_time = current_timeelse:
end_time = current_time.replace(hour = 13, minute = 0, second = 0, microsecond = 0)elif time_interval == SnoozeTimeInterval.UNTIL_END_OF_DAY:
if current_time.hour >= 17:
report_bad_assumption('Trying to set the snooze time to 5PM even though it is after 5PM')end_time = current_timeelse:
end_time = current_time.replace(hour = 17, minute = 0, second = 0, microsecond = 0)elif time_interval == SnoozeTimeInterval.UNTIL_TOMORROW:
end_time = SnoozeTimeCalculator.round_to_tomorrow(current_time)else:
report_bad_assumption('Time interval for snoozing is not one of the allowed ones.')end_time = current_timeend_time)()
    calc_end_time = (lambda start_time = None, time_to_snooze = None: start_time + time_to_snooze)()
    round_to_tomorrow = (lambda time_to_round = None: hour = time_to_round.hourif hour >= 2:
time_to_round = time_to_round + timedelta(days = 1)time_to_round = time_to_round.replace(hour = 8, minute = 0, second = 0, microsecond = 0)time_to_round)()

