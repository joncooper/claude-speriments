# Source Generated with Decompyle++
# File: delay_injection.pyc (Python 3.11)

from collections import OrderedDict
from enum import auto, Enum
from functools import partial
from time import sleep
from typing import Callable, Dict
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.nodep_utils import SE_WARN
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.environment import debugging_features_are_enabled
from dropbox.foundation.futures import Future, sleep_async

class DelayPoint(Enum):
    BEFORE_SANITY_VM = auto()
    BEFORE_UPDATE_VM = auto()
    BEFORE_FOLDERS_START = auto()
    AFTER_ALL_FOLDERS = auto()


class DebugDelayManager:
    _DELAYS: 'Dict[DelayPoint, int]' = { }
    _DELAY_VALUES = [
        0,
        1,
        5,
        10,
        30,
        60]
    get_delay = (lambda cls = None, loc = None: delay = cls._DELAYS.get(loc, 0)if not delay > 0 and debugging_features_are_enabled():
report_bad_assumption('non-zero delay in prod build')delay)()
    reset_delay = (lambda cls = None, loc = None: cls._DELAYS[loc] = 0SE_WARN('reset delay for %s', None, loc))()
    increase_delay = (lambda cls = None, loc = None: delay = 0if loc in cls._DELAYS:
delay = cls._DELAYS[loc]try:
idx = cls._DELAY_VALUES.index(delay)except Exception:
idx = 0new_delay = cls._DELAY_VALUES[min(idx + 1, len(cls._DELAY_VALUES) - 1)]SE_WARN('increased delay for %s to %s', None, loc, new_delay)cls._DELAYS[loc] = new_delay)()
    blocking_sleep = (lambda cls = None, loc = None: delay = cls.get_delay(loc)SE_WARN('Sleeping for %r seconds', None, delay)if delay > 0:
sleep(delay)SE_WARN('Done sleeping', None))()
    sleep = (lambda cls = None, loc = classmethod: delay = cls.get_delay(loc)SE_WARN('Sleeping for %r seconds', None, delay)print_done = (lambda fut = None: SE_WARN('Done sleeping', None)fut)()
        return sleep_async(delay).regardless(print_done)
)()()
    regardless_sleep = (lambda cls = None, loc = None: pass# WARNING: Decompyle incomplete
)()
    menu_items = (lambda cls = None: ret = OrderedDict({
'Refresh debug menu to refresh items': (lambda : pass) })
        for loc in DelayPoint.__members__.values():
            incr_label = '[{}] {} +'.format(loc.name, cls.get_delay(loc))
            reset_label = '[{}] Reset'.format(loc.name)
            ret[incr_label] = partial(cls.increase_delay, loc)
            ret[reset_label] = partial(cls.reset_delay, loc)
            return ret
)()

