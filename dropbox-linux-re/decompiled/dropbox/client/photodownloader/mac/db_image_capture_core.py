# Source Generated with Decompyle++
# File: db_image_capture_core.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
import datetime
from abc import ABCMeta, abstractmethod
from typing import Any, Callable, List, NamedTuple, Optional, Text
from six import add_metaclass
DBNSError = <NODE:12>()
DBICCameraFolder = <NODE:12>()
DBICCameraFile = <NODE:12>()
DidReadCallbackType = Callable[([
    bytes,
    DBICCameraFile,
    Optional[DBNSError],
    Any], None)]
DidDownloadCallbackType = Callable[([
    DBICCameraFile,
    Optional[Text],
    Optional[DBNSError],
    Any], None)]
DBICCameraDevice = <NODE:12>()
DBICDeviceBrowser = <NODE:12>()
DBICCameraDeviceDelegate = NamedTuple('DBICCameraDeviceDelegate', [
    ('device_did_become_ready_with_complete_content_catalog', Callable[([
        DBICCameraDevice], None)]),
    ('device_did_become_ready', Callable[([
        DBICCameraDevice], None)]),
    ('device_did_encounter_error', Callable[([
        DBICCameraDevice,
        Optional[DBNSError]], None)]),
    ('device_did_open_session_with_error', Callable[([
        DBICCameraDevice,
        Optional[DBNSError]], None)]),
    ('device_did_close_session_with_error', Callable[([
        DBICCameraDevice,
        Optional[DBNSError]], None)]),
    ('did_remove_device', Callable[([
        DBICCameraDevice], None)])])
DBICDeviceBrowserDelegate = NamedTuple('DBICDeviceBrowserDelegate', [
    ('device_browser_enumerated_local_devices', Callable[([
        DBICDeviceBrowser], None)]),
    ('device_browser_did_add_device_more_coming', Callable[([
        DBICDeviceBrowser,
        DBICCameraDevice,
        bool], None)]),
    ('device_browser_did_remove_device_more_going', Callable[([
        DBICDeviceBrowser,
        DBICCameraDevice,
        bool], None)])])
