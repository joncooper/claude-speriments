# Source Generated with Decompyle++
# File: bridge_examples.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import random as insecure_random
from typing import Dict, List, Optional, Text
from bridge_gen.basic_record import BasicRecord
from bridge_gen.bridge_interface_bridge_test_class_with_props import BridgeTestClassWithPropsBridgeInterface, BridgeTestClassWithPropsObservableMixin
from bridge_gen.bridge_interface_bridge_test_static import BridgeTestStaticBridgeInterface
from bridge_gen.bridge_interface_bridge_test_types import BridgeTestTypesBridgeInterface
from bridge_gen.bridge_interface_grab_fruit_results_vm import GrabFruitResultsVMBridgeInterface
from bridge_gen.bridge_interface_imported_class import ImportedClassBridgeInterface
from bridge_gen.bridge_interface_python_doubler import PythonDoublerBridgeInterface
from bridge_gen.bridge_interface_static_constructor_test import StaticConstructorTestBridgeInterface
from bridge_gen.fruit_type import FruitType
from bridge_gen.nested_record import NestedRecord
from bridge_gen.record_with_enum import RecordWithEnum
from bridge_gen.record_with_list_of_records import RecordWithListOfRecords
from bridge_gen.record_with_optional_fields import RecordWithOptionalFields
from bridge_gen.secondary_record import SecondaryRecord
from bridge_gen.traffic_light_colors import TrafficLightColors
from dropbox.client.features.api_v2.api_v2 import ApiV2ClientUntyped
from dropbox.client.features.local_view_basic_example.view_model.bridge_gen.types import ComplexType, ImportedType, OtherImportedType
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_1
from dropbox.foundation.context.bridge_gen.bridge_interface_user_context import UserContextBridgeInterface
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import typed_exc_info
from dropbox.foundation.futures import CancelledFuture, FailedFuture, Future, ResolvedFuture
from dropbox.foundation.futures.sleep import sleep_async
from dropbox.foundation.html_views.bridge.bridge_registration import bridge_class
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.signals import Signal, StandardSignal
from dropbox.trace import TRACE

class ImportedClass(ImportedClassBridgeInterface):
    
    def __init__(self = None, value = None):
        self._some_value = value

    some_value = (lambda self = None: self._some_value)()


class PythonDoubler(PythonDoublerBridgeInterface):
    
    def __init__(self = None, prefix = None):
        self._prefix = prefix

    
    def foo(self = None, value = None):
        msg = '[{}]{}.foo()={}'.format(id(self), self._prefix, value * 2)
        TRACE('%r', msg)
        return msg



class StaticBridgeClass(BridgeTestStaticBridgeInterface):
    static_foo = (lambda message = None: TRACE('StaticBridgeClass.static_foo(%r)', message))()
    raise_exception = (lambda message = None: raise Exception(message))()
    cancelled_future = (lambda : CancelledFuture())()


class StaticConstructorBridgeTest(StaticConstructorTestBridgeInterface):
    
    def __init__(self = None, prefix = None):
        self._prefix = prefix

    static_constructor = (lambda prefix = None: TRACE('StaticConstructorBridgeTest.static_constructor()')StaticConstructorBridgeTest(prefix))()
    
    def instance_foo(self = None, message = None):
        TRACE('StaticConstructorBridgeTest[%r][%r].instance_foo(%r)', id(self), self._prefix, message)



class SimpleBridgeTypes(BridgeTestTypesBridgeInterface, Destroyable):
    pass
# WARNING: Decompyle incomplete

GrabAppleResultsVM = <NODE:12>()
GrabOrangesResultVM = <NODE:12>()

class BridgeTestClassWithProps(BridgeTestClassWithPropsBridgeInterface, Actor, BridgeTestClassWithPropsObservableMixin):
    pass
# WARNING: Decompyle incomplete

