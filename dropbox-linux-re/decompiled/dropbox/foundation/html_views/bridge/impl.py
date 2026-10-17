# Source Generated with Decompyle++
# File: impl.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import json
import sys
import time
import traceback
from typing import Any, Callable, Dict, List, Optional, Text, TypeVar
from weakref import WeakKeyDictionary
from six import iteritems, iterkeys
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exceptions import PythonBridgeError
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.exception_info import OptExcInfo, typed_exc_info
from dropbox.foundation.exception_info.bridge_gen.bridge_interface_exception_handle import ExceptionHandleBridgeInterface
from dropbox.foundation.futures import CancelledFuture, CancelledFutureException, Future, ResolvedFuture
from dropbox.foundation.html_views.bridge import BRIDGE_EXCEPTION_UNCAUGHT, BridgeInstanceId, BridgeInstanceToken
from dropbox.foundation.html_views.bridge.bridge_registration import BRIDGE_CLASSES, BRIDGE_RECORDS
from dropbox.foundation.html_views.bridge.errors import BridgeClassNotFoundException, BridgeInstanceNotFoundException, BridgeMethodNotFoundException, BridgeSignalNotFoundException, merge_bridged_stacks
from dropbox.foundation.html_views.bridge.interface import ViewBridgeSerializable
from dropbox.foundation.html_views.bridge.response import BridgeResultPayload
from dropbox.foundation.html_views.bridge.timed_bridge_call_tracker import TimedBridgeCallTracker
from dropbox.foundation.html_views.common.bridge_gen.bridge_call_checkpoint import BridgeCallCheckpoint
from dropbox.foundation.html_views.common.threading import LatencySensitiveBridgeFuture
from dropbox.foundation.reporting import report_app_framework_event
from dropbox.foundation.runtime import ExitCode, panic_with_report
from dropbox.foundation.signals import Signal, SignalConnection
from dropbox.threading import Lock
from dropbox.trace import TRACE

class MarshalledInstanceTrackerAlreadyCleanedUpError(Exception):
    pass


def json_box_records(obj = None):
    if obj.__class__.__name__ in BRIDGE_RECORDS:
        return obj.__class__.box(obj)
    raise TypeError(repr(obj) + ' is not JSON serializable')


def json_unbox_records(dct = None):
    cls = BRIDGE_RECORDS.get(dct.get('__type__'))
    if cls:
        return cls.unbox(dct)


class _InstanceIdGenerator(object):
    
    def __init__(self = None):
        self._InstanceIdGenerator__instance_id_counter = 0
        self._InstanceIdGenerator__instance_id_counter_lock = Lock()

    
    def get_id(self = None):
        self._InstanceIdGenerator__instance_id_counter_lock
        None(None, None)
        return 
        with None:
            if not self, self._InstanceIdGenerator__instance_id_counter += 1, ._InstanceIdGenerator__instance_id_counter, BridgeInstanceId(Text(self._InstanceIdGenerator__instance_id_counter)):
                pass



class MarshalledInstanceTracker(object):
    
    def __init__(self = None):
        self._MarshalledInstanceTracker__instance_lock = Lock()
        self._id_generator = _InstanceIdGenerator()
        self._instance_ids = WeakKeyDictionary()
        self._instances = { }
        self._instance_metadata = WeakKeyDictionary()
        self._is_destroyed = False

    
    def instance_table_size_for_test(self = None):
        self._MarshalledInstanceTracker__instance_lock
        None(None, None)
        return 
        with None:
            if not None, len(self._instances):
                pass

    
    def cleanup(self = None):
        self._MarshalledInstanceTracker__instance_lock
        (_, metadata) = self._instance_metadata.popitem()

    
    def track_instance(self = None, instance = None):
        self._MarshalledInstanceTracker__instance_lock
        if self._is_destroyed:
            raise MarshalledInstanceTrackerAlreadyCleanedUpError('Cannot call track_instance where instance tracker has already been destroyed')
        if instance not in self._instance_ids:
            instance_id = self._id_generator.get_id()
            self._instance_ids[instance] = instance_id
            self._instances[instance_id] = instance
            None(None, None)
            return 
        None(None, None)
        return 
        with None:
            if not None, None._instance_ids[instance]:
                pass

    
    def stop_tracking_instance(self = None, instance = None):
        self._MarshalledInstanceTracker__instance_lock
        if instance in self._instance_ids:
            instance_id = self._instance_ids.pop(instance)
            del self._instances[instance_id]
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def lookup_instance(self = None, instance_id = None):
        self._MarshalledInstanceTracker__instance_lock
        None(None, None)
        return 
        with None:
            if not None, self._instances.get(instance_id, None):
                pass

    
    def get_instance_metadata(self = None, instance = None):
        self._MarshalledInstanceTracker__instance_lock
        None(None, None)
        return 
        with None:
            if not None, self._instance_metadata.get(instance, None):
                pass

    
    def update_instance_meta(self = None, instance = None, updater = None):
        self._MarshalledInstanceTracker__instance_lock
        if self._is_destroyed:
            raise MarshalledInstanceTrackerAlreadyCleanedUpError('Cannot call update_instance_meta where instance tracker has already been destroyed')
        old_meta = self._instance_metadata.get(instance, None)
        new_meta = updater(old_meta)
        if new_meta != old_meta:
            self._instance_metadata[instance] = new_meta
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def delete_instance_meta(self = None, instance = None):
        self._MarshalledInstanceTracker__instance_lock
        if instance in self._instance_metadata:
            del self._instance_metadata[instance]
        None(None, None)
        return None
        with None:
            if not None:
                pass



class _ProjectedExceptionHandle(ExceptionHandleBridgeInterface):
    
    def __init__(self, exc_info = None, js_stack = None, instance_tracker = None, component = ('exc_info', 'OptExcInfo', 'js_stack', 'Text', 'instance_tracker', 'MarshalledInstanceTracker', 'component', 'DesktopComponent', 'return', 'None')):
        self._exc_info = exc_info
        self._js_stack = js_stack
        self._instance_tracker = instance_tracker
        self._component = component

    
    def _dispose(self = None):
        self._instance_tracker.stop_tracking_instance(self)
        del self._instance_tracker
        del self._exc_info

    exception_type = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    args = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def was_not_handled(self = None):
        pass
    # WARNING: Decompyle incomplete



def _is_signal(pyobj = None):
    return isinstance(pyobj, Signal)


def _is_future(pyobj = None):
    return isinstance(pyobj, Future)


def _is_primitive(value = None):
    if not value is None:
        pass
    return isinstance(value, (str, int, float, bool))


def _is_bridge_class(pyobj = None):
    return type(pyobj).__name__ in BRIDGE_CLASSES


def _is_bridge_instance_type(pyobj = None):
