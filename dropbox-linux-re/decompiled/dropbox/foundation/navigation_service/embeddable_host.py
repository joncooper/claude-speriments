# Source Generated with Decompyle++
# File: embeddable_host.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import abstractmethod
from typing import Callable, Generic, Optional, TypeVar
from view_interface import StandaloneViewIdentifier
from dropbox.foundation.futures import Future, ResolvedFuture
_V = TypeVar('_V')

def EmbeddableViewHost():
    '''EmbeddableViewHost'''
    extract_view = (lambda self = None, view_id = None: pass)()
    embed_view = (lambda self = None, view_id = None, view = abstractmethod: pass)()
    get_view = (lambda self = None, view_id = None: pass)()
    bring_view_to_front = (lambda self = None, view_id = None: pass)()
    foreground_window = (lambda self = None: pass)()
    
    def close_views(self = None):
        return ResolvedFuture(None)

    transfer_view_from_to = (lambda from_host = None, to_host = None, view_id = staticmethod: view = from_host.extract_view(view_id)to_host.embed_view(view_id, view))()

EmbeddableViewHost = <NODE:27>(EmbeddableViewHost, 'EmbeddableViewHost', Generic[_V])

def EmbeddableViewHostRouter():
    '''EmbeddableViewHostRouter'''
    
    def __init__(self, extract_view_func, embed_view_func = None, bring_to_front_func = None, foreground_window_func = None, get_view_func = (None, None), close_views_func = ('extract_view_func', 'Callable[[StandaloneViewIdentifier], Optional[_V]]', 'embed_view_func', 'Callable[[StandaloneViewIdentifier, Optional[_V]], None]', 'bring_to_front_func', 'Callable[[StandaloneViewIdentifier], bool]', 'foreground_window_func', 'Callable[[], None]', 'get_view_func', 'Optional[Callable[[StandaloneViewIdentifier], Optional[_V]]]', 'close_views_func', 'Optional[Callable[[], Future[None]]]', 'return', 'None')):
        self._extract_view_func = extract_view_func
        self._embed_view_func = embed_view_func
        self._get_view_func = get_view_func
        self._bring_to_front_func = bring_to_front_func
        self._foreground_window_func = foreground_window_func
        self._close_views_func = close_views_func

    
    def extract_view(self = None, view_id = None):
        return self._extract_view_func(view_id)

    
    def embed_view(self = None, view_id = None, view = None):
        self._embed_view_func(view_id, view)

    
    def get_view(self = None, view_id = None):
        return self._get_view_func(view_id) if self._get_view_func else None

    
    def bring_view_to_front(self = None, view_id = None):
        return self._bring_to_front_func(view_id)

    
    def foreground_window(self = None):
        self._foreground_window_func()

    
    def close_views(self = None):
        if self._close_views_func:
            return self._close_views_func()
        return ResolvedFuture(None)


EmbeddableViewHostRouter = <NODE:27>(EmbeddableViewHostRouter, 'EmbeddableViewHostRouter', EmbeddableViewHost[_V])
