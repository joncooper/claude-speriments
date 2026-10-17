# Source Generated with Decompyle++
# File: office.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import zipfile
from typing import Optional, Text
from AppKit import NSArray, NSError, NSNumber, NSOSStatusErrorDomain, NSPredicate, NSString
from ScriptingBridge import SBApplication
from lib.mac_scripting_bridge import errAENoSuchObject, errAETimeout, four_character, SBSendEvent
from dropbox.components.desktop_components import DesktopComponent
from dropbox.dbexceptions import TimeoutError
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_1, async_queued_method_2, async_queued_method_3
from dropbox.foundation.context.machine import MachineContext
from dropbox.functions import lrumemoized
from dropbox.harmony.mac.accessibility import AccessibilityPlugin
from dropbox.harmony.mac.plugin import MacPlugin
from dropbox.harmony.models.types import ApplicationVersion, MacApplicationVersion
from dropbox.harmony.plugins.base import BasicCoordinatingPlugin, EditorStatusTracker, PluginArgs
from dropbox.mac.internal import autoreleasepool, MacError
from dropbox.repr_utils import easy_repr
from dropbox.trace import TRACE
OFFICE2011 = 14
OFFICE2016 = 15
OFFICE_V16 = 16

class OfficePlugin(BasicCoordinatingPlugin, MacPlugin):
    pass
# WARNING: Decompyle incomplete


class PowerPointPlugin(OfficePlugin):
    APPLICATION_IDENTIFIER = 'com.microsoft.Powerpoint'
    STORMCROW_RULE = 'desktop-harmony-enable-powerpoint'
    supports_version = (lambda version = None: if not isinstance(version, MacApplicationVersion):
FalseNone.get_major_version(version) >= OFFICE2011)()
    
    def _save_as(self = None, source_path = None, destination_path = None, should_close = (False,)):
        destination_predicate_filter = destination_path
        autoreleasepool()
        if OfficePlugin.get_major_version(self._version) == OFFICE2011:
            source_path = self._to_hfs_path(source_path)
            destination_predicate_filter = self._to_hfs_path(destination_predicate_filter)
        destination_path = self._to_hfs_path(destination_path)
        predicate = NSPredicate.predicateWithFormat_('fullName == %@', source_path)
        target_array = self._remote.presentations().filteredArrayUsingPredicate_(predicate)
        target = target_array.allObjects()
        target.setSaved_(False)
        error = target.lastError()
        if isinstance(error, NSError):
            if error.domain() == NSOSStatusErrorDomain and error.code() == errAETimeout:
                raise TimeoutError()
            raise MacError(error)
        destination_wrapped = NSString.stringWithString_(destination_path)
        SBSendEvent(target, 'core', 'save', 'kfil', destination_wrapped)
        error = target.lastError()
        if isinstance(error, NSError):
            if error.domain() == NSOSStatusErrorDomain and error.code() == errAETimeout:
                raise TimeoutError()
            if error.domain() == NSOSStatusErrorDomain and error.code() == errAENoSuchObject:
                raise KeyError()
            raise MacError(error)
        if should_close:
            predicate = NSPredicate.predicateWithFormat_('fullName == %@', destination_predicate_filter)
            target = self._remote.presentations().filteredArrayUsingPredicate_(predicate).allObjects()
            SBSendEvent(target, 'core', 'clos')
        error = target.lastError()
        if isinstance(error, NSError):
            if error.domain() == NSOSStatusErrorDomain and error.code() == errAETimeout:
                raise TimeoutError()
            raise MacError(error)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    reopen = (lambda self = None, source_path = None: autoreleasepool()if OfficePlugin.get_major_version(self._version) == OFFICE2011:
source_path = self._to_hfs_path(source_path)predicate = NSPredicate.predicateWithFormat_('fullName == %@', source_path)target = self._remote.presentations().filteredArrayUsingPredicate_(predicate).allObjects()target.closeSaving_savingIn_(0, 0)error = target.lastError()if isinstance(error, NSError):
if error.domain() == NSOSStatusErrorDomain and error.code() == errAETimeout:
raise TimeoutError()raise MacError(error)path_wrapped = NSString.stringWithString_(source_path)if OfficePlugin.get_major_version(self._version) >= OFFICE2016:
path_wrapped = NSArray.arrayWithArray_([
source_path])SBSendEvent(self._remote, 'aevt', 'odoc', '----', path_wrapped)error = target.lastError()if isinstance(error, NSError):
if error.domain() == NSOSStatusErrorDomain and error.code() == errAETimeout:
raise TimeoutError()raise MacError(error)None(None, None)Nonewith None:
if not None:
pass)()


class ExcelPlugin(OfficePlugin):
    pass
# WARNING: Decompyle incomplete


class WordPlugin(OfficePlugin):
    APPLICATION_IDENTIFIER = 'com.microsoft.Word'
    STORMCROW_RULE = 'desktop-harmony-enable-word'
    supports_version = (lambda version = None: if not isinstance(version, MacApplicationVersion):
FalseNone.get_major_version(version) >= OFFICE2011)()
    unlock = (lambda self = None, path = None: if OfficePlugin.get_major_version(self.version) >= OFFICE_V16:
try:
self._close(path)except KeyError:
TRACE('COORDINATION: Trying to unlock when document no longer open')None)()
    
    def _save_as(self = None, source_path = None, destination_path = None, should_close = (False,)):
        autoreleasepool()
        source_path = self._to_hfs_path(source_path)
        destination_path = self._to_hfs_path(destination_path)
        target = self._remote.documents().objectWithName_(source_path)
        destination_wrapped = NSString.stringWithString_(destination_path)
        SBSendEvent(target, 'core', 'save', 'kfil', destination_wrapped)
        error = target.lastError()
        if isinstance(error, NSError):
            if error.domain() == NSOSStatusErrorDomain and error.code() == errAETimeout:
                raise TimeoutError()
            if error.domain() == NSOSStatusErrorDomain and error.code() == errAENoSuchObject:
                raise KeyError()
            raise MacError(error)
        if should_close:
            target = self._remote.documents().objectWithName_(destination_path)
            no_wrapped = NSNumber.numberWithInt_(four_character('no  '))
            SBSendEvent(target, 'core', 'clos', 'savo', no_wrapped)
            error = target.lastError()
            if isinstance(error, NSError):
                if error.domain() == NSOSStatusErrorDomain and error.code() == errAETimeout:
                    raise TimeoutError()
                raise MacError(error)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _close(self = None, source_path = None):
        autoreleasepool()
        source_path = self._to_hfs_path(source_path)
        target = self._remote.documents().objectWithName_(source_path)
        no_wrapped = NSNumber.numberWithInt_(four_character('no  '))
        SBSendEvent(target, 'core', 'clos', 'savo', no_wrapped)
        error = target.lastError()
        if isinstance(error, NSError):
            if error.domain() == NSOSStatusErrorDomain and error.code() == errAETimeout:
                raise TimeoutError()
            if error.domain() == NSOSStatusErrorDomain and error.code() == errAENoSuchObject:
                raise KeyError()
            raise MacError(error)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    sanity_check_move = (lambda self = None, source_path = None, destination_path = async_queued_method_2: if OfficePlugin.get_major_version(self._version) == OFFICE2011:
TRACE('COORDINATION: Reopening moved document due to Word 2011 bug')try:
self._close(destination_path)self._reopen(destination_path)Noneexcept KeyError:
TRACE('COORDINATION: Old document not open')Noneexcept Exception:
report_exception(severity = Severity.CRITICAL, component = DesktopComponent.HARMONY)NoneNone)()
    reopen = (lambda self = None, source_path = None: self._reopen(source_path))()
    
    def _reopen(self = None, source_path = None):
        autoreleasepool()
        if OfficePlugin.get_major_version(self._version) == OFFICE2011:
            source_path = self._to_hfs_path(source_path)
        path_wrapped = NSString.stringWithString_(source_path)
        true_wrapped = NSNumber.numberWithInt_(1)
        SBSendEvent(self._remote, 'aevt', 'odoc', '5015', path_wrapped, '5835', true_wrapped)
        error = self._remote.lastError()
        if isinstance(error, NSError):
            if error.domain() == NSOSStatusErrorDomain and error.code() == errAETimeout:
                raise TimeoutError()
            raise MacError(error)
        None(None, None)
        return None
        with None:
            if not None:
                pass



class PowerPointAXTrackerPlugin(AccessibilityPlugin, PowerPointPlugin):
    pass


class ExcelAXTrackerPlugin(AccessibilityPlugin, ExcelPlugin):
    pass


class WordAXTrackerPlugin(AccessibilityPlugin, WordPlugin):
    pass


class PowerPointSBTrackerPlugin(EditorStatusTracker, PowerPointPlugin):
    is_saved = (lambda self = None, local_path = None: autoreleasepool()if OfficePlugin.get_major_version(self._version) == OFFICE2011:
local_path = self._to_hfs_path(local_path)predicate = NSPredicate.predicateWithFormat_('fullName == %@', local_path)target_array = self._remote.presentations().filteredArrayUsingPredicate_(predicate)saved_array = target_array.arrayByApplyingSelector_('saved')if saved_array or len(saved_array) != 1:
raise KeyError('presentation ambiguous', saved_array)result = bool(saved_array[0])None(None, None)with None:
if not None, result:
pass)()
    supports_version = (lambda version = None: if not isinstance(version, MacApplicationVersion):
FalseNone.get_major_version(version) >= OFFICE_V16)()


class ExcelSBTrackerPlugin(EditorStatusTracker, ExcelPlugin):
    is_saved = (lambda self = None, local_path = None: autoreleasepool()if OfficePlugin.get_major_version(self._version) == 14:
local_path = self._to_hfs_path(local_path)predicate = NSPredicate.predicateWithFormat_('fullName == %@', local_path)target_array = self._remote.workbooks().filteredArrayUsingPredicate_(predicate)saved_array = target_array.arrayByApplyingSelector_('saved')if saved_array or len(saved_array) != 1:
raise KeyError('workbook ambiguous', saved_array)result = bool(saved_array[0])None(None, None)with None:
if not None, result:
pass)()
    supports_version = (lambda version = None: if not isinstance(version, MacApplicationVersion):
FalseNone.get_major_version(version) >= OFFICE_V16)()


class WordSBTrackerPlugin(EditorStatusTracker, WordPlugin):
    is_saved = (lambda self = None, local_path = None: autoreleasepool()local_path = self._to_hfs_path(local_path)target = self._remote.documents().objectWithName_(local_path)# WARNING: Decompyle incomplete
)()
    supports_version = (lambda version = None: if not isinstance(version, MacApplicationVersion):
Falseint(OfficePlugin.get_major_version(version)) >= OFFICE_V16)()

