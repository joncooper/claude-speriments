# Source Generated with Decompyle++
# File: interface.pyc (Python 3.11)

from abc import abstractmethod, abstractproperty
from typing import Generic, Text, TypeVar
from dropbox.client.ui.common.uikit import FrameworkProps
from dropbox.foundation.html_views.common.embeddable_mixin import EmbeddableViewMixin
from dropbox.foundation.html_views.common.interface import HtmlViewAffinityGroup
from dropbox.foundation.performance import PerfSession
_EV = TypeVar('_EV', bound = EmbeddableViewMixin)

def LocalViewFactoryInterface():
    '''LocalViewFactoryInterface'''
    framework_props = (lambda self = None: pass)()
    create_embeddable = (lambda self = None, perf_session = None, affinity_group = abstractmethod, view_id = ('perf_session', 'PerfSession', 'affinity_group', 'HtmlViewAffinityGroup', 'view_id', 'Text', 'return', '_EV'): pass)()

LocalViewFactoryInterface = <NODE:27>(LocalViewFactoryInterface, 'LocalViewFactoryInterface', Generic[_EV])
