# Source Generated with Decompyle++
# File: bidl_gen_test.pyc (Python 3.11)

'''Module for bidl generation regression tests.'''
from __future__ import absolute_import, division, print_function
from typing import List, Optional
from dropbox.client.features.bidl_gen_test.bridge_gen.bridge_interface_class_with_raw_return_type import ClassWithRawReturnTypeBridgeInterface, ClassWithRawReturnTypeObservableMixin
from dropbox.client.features.bidl_gen_test.bridge_gen.other_record import OtherRecord
from dropbox.client.features.bidl_gen_test.bridge_gen.record_with_raw_field import RecordWithRawField
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.signals import Signal

class RawTestClass(ClassWithRawReturnTypeBridgeInterface, Destroyable, ClassWithRawReturnTypeObservableMixin):
    pass
# WARNING: Decompyle incomplete

