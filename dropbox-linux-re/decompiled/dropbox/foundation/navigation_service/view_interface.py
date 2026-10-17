# Source Generated with Decompyle++
# File: view_interface.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import abstractmethod, abstractproperty
from typing import Callable, NamedTuple, Optional, Text
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.futures import Future
from dropbox.foundation.raii2 import Destroyable
MYPY = False
if MYPY:
    from dropbox.foundation.html_views.common.bridge_gen.view_close_reason import ViewCloseReason
StandaloneViewIdentifier = NamedTuple('StandaloneViewIdentifier', [
    ('content_identifier', Text),
    ('window_id', Optional[Text]),
    ('component', DesktopComponent)])
PRE_CONTENT_VIEW_ID = StandaloneViewIdentifier(content_identifier = 'sentinel id for views that have not yet loaded content', window_id = None, component = DesktopComponent.HTML_VIEWS)

class ViewInterface(Destroyable):
    close = (lambda self = None, close_reason = None: pass)()
    add_closed_handler = (lambda self = None, callback = None: pass)()
    foreground = (lambda self = None: pass)()
    render_offscreen = (lambda self = None: pass)()
    is_visible = (lambda self = None: pass)()
    is_foreground = (lambda self = None: pass)()

