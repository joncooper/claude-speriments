# Source Generated with Decompyle++
# File: bubble_context.pyc (Python 3.11)

from typing import Any, Callable, MutableMapping, Optional
from dropbox.client.notifications.loud_notifications.events import BubbleClickInfo, report_click_bubble
from dropbox.client.notifications.loud_notifications.types import BubbleContextRef
from dropbox.functions import lrudict
from dropbox.repr_utils import easy_repr
from dropbox.threading import Lock
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotificationType

class BubbleCallback:
    __slots__ = [
        'f',
        'loud_notification_type']
    
    def __init__(self = None, f = None, loud_notif_type = None):
        self.f = f
        self.loud_notification_type = loud_notif_type

    
    def __repr__(self = None):
        return f'''BubbleCallback({self.f!r}, {self.loud_notification_type!s})'''

    
    def thunk(self = None, arg = None):
        pass
    # WARNING: Decompyle incomplete



class BubbleContext:
    
    def __init__(self = None, expire_by_lru = None):
        if expire_by_lru:
            self.click_context_map = lrudict(cache_size = 100)
        else:
            self.click_context_map = { }
        self.next_click_context_ref = 0
        self.lock = Lock()

    
    def __repr__(self = None):
        return easy_repr(self, 'click_context_map', 'next_click_context_ref')

    
    def clear(self = None):
        self.click_context_map.clear()

    
    def make_func_context_ref(self = None, f = None, loud_notif_type = None):
        return self.make_context_ref(BubbleCallback(f, loud_notif_type))

    
    def make_context_ref(self = None, context = None):
        self.lock
        cr = BubbleContextRef(self.next_click_context_ref)
        context = self, self.next_click_context_ref %= 65536, .next_click_context_ref
        None(None, None)

    
    def is_valid_context_ref(self = None, cr = None):
        return cr in self.click_context_map

    
    def get_context_ref(self = None, cr = None):
        self.lock
        None(None, None)
        return 
        except KeyError:
            TRACE("Couldn't find %r in %r", cr, self.click_context_map)
            raise 
        with None:
            if not None:
                pass

    
    def thunk_and_expire_context_ref(self = None, click_info = None, context_ref = None, arg = (None, True), report_click = ('click_info', 'BubbleClickInfo', 'context_ref', 'BubbleContextRef', 'arg', 'Optional[Any]', 'report_click', 'bool', 'return', 'None')):
        context = self.get_context_ref(context_ref)
        loud_notification_type = context.loud_notification_type
    # WARNING: Decompyle incomplete

    
    def expire_context_ref(self = None, cr = None):
        pass
    # WARNING: Decompyle incomplete


