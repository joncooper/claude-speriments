# Source Generated with Decompyle++
# File: volumeid_to_persistent_volumeid_map.pyc (Python 3.11)

from __future__ import absolute_import
import itertools
import json
import os
import struct
from typing import Dict, Tuple
from pymac.helpers.disk import get_all_drives, get_volume_uuid
from six import iteritems
from file_cache.constants import UUID_TO_PERSISTENT_VOLUMEID_KEY
from exceptions import FileSystemError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.mac.internal import autoreleasepool
from dropbox.mac.mount_notification_handler import MountNotificationHandler
from dropbox.mac.version import CATALINA, MAC_VERSION
from dropbox.threading import Lock
from dropbox.trace import TRACE

class UUIDToPersistentVolumeIdMap(object):
    ENTRY_TYPE_UUID = 'uuid'
    ENTRY_TYPE_VOLUMEID = 'raw_volumeid'
    ENTRY_TYPE_STR = 'type'
    ENTRY_VALUE_STR = 'value'
    PERSISTENT_VOLUMEID_STR = 'persistent_volumeid'
    
    def __init__(self, sync_engine):
        self.sync_engine = sync_engine

    
    def load_from_file_cache(self = None):
        uuid_to_persistent_volumeid = { }
        raw_volumeid_to_persistent_volumeid = { }
        
        try:
            stored_value = self.sync_engine.get_config_key(UUID_TO_PERSISTENT_VOLUMEID_KEY)
            
            try:
                obj = json.loads(stored_value)
                for entry in obj:
                    entry_type = entry[self.ENTRY_TYPE_STR]
                    value = int(entry[self.ENTRY_VALUE_STR])
                    persistent_vid = int(entry[self.PERSISTENT_VOLUMEID_STR])
                    if entry_type == self.ENTRY_TYPE_UUID:
                        uuid_to_persistent_volumeid[value] = persistent_vid
                        continue
                    if entry_type == self.ENTRY_TYPE_VOLUMEID:
                        raw_volumeid_to_persistent_volumeid[value] = persistent_vid
            except ValueError:
                TRACE("Couldn't parse JSON volume map: %r", stored_value)
                report_exception(severity = Severity.WARN, component = DesktopComponent.SYNC_ENGINE)
            except KeyError:
                TRACE('!! Could not find the uuid_to_persistent_volumeid_key in sync engine config')
            except Exception:
                report_exception(component = DesktopComponent.SYNC_ENGINE)

            TRACE('Current uuid_to_persistent_volumeid(%r), raw_volumeid_to_persistent_volumeid(%r)', uuid_to_persistent_volumeid, raw_volumeid_to_persistent_volumeid)
            return (uuid_to_persistent_volumeid, raw_volumeid_to_persistent_volumeid)


    
    def _create_entry(self, entry_type, value, persistent_vid):
        return {
            self.PERSISTENT_VOLUMEID_STR: persistent_vid,
            self.ENTRY_VALUE_STR: value,
            self.ENTRY_TYPE_STR: entry_type }

    
    def store_in_file_cache(self, uuid_to_persistent_volumeid, raw_volumeid_to_persistent_volumeid):
        list_to_serialize = []
        for uuid, persistent_volumeid in iteritems(uuid_to_persistent_volumeid):
            list_to_serialize.append(self._create_entry(self.ENTRY_TYPE_UUID, uuid, persistent_volumeid))
            for raw_volumeid, persistent_volumeid in iteritems(raw_volumeid_to_persistent_volumeid):
                list_to_serialize.append(self._create_entry(self.ENTRY_TYPE_VOLUMEID, raw_volumeid, persistent_volumeid))
                TRACE('Updating uuid_to_persistent_volumeid map to %r', list_to_serialize)
                self.sync_engine.set_config_key(UUID_TO_PERSISTENT_VOLUMEID_KEY, json.dumps(list_to_serialize))
                return None



class VolumeIdToPersistentVolumeIdMap(object):
    NETWORK_VOLUME_MOUNT_POINTS = set([
        '/Network/Servers',
        '/home',
        '/net'])
    
    def __init__(self, sync_engine):
        self.sync_engine = sync_engine
        self.fs = sync_engine.fs
        self.volumeid_to_persistent_volumeid = { }
        self.missing_volumeids = set()
        autoreleasepool()
        self.volume_change_notifier = MountNotificationHandler()
        self.volume_change_notifier.set_volume_change_handler(self.refresh)
        None(None, None)

    
    def _new_persistent_volumeid(self, persistent_volumeids):
        rand_bytes = os.urandom(8)
        int_value = struct.unpack('!q', rand_bytes)[0]
        if int_value and int_value not in persistent_volumeids:
            return int_value

    _process_single_device = (lambda self, mount_point, volumeid_to_uuid: pass# WARNING: Decompyle incomplete
)()
    
    def lookup_volumeid(self, volumeid):
        persistent_volumeid = self.volumeid_to_persistent_volumeid.get(volumeid)
    # WARNING: Decompyle incomplete

    
    def _get_uuid_to_volumeid_map(self):
        volumeid_to_uuid = { }
        all_drives = { }
        
        try:
            all_drives = get_all_drives()
        except Exception:
            report_exception(component = DesktopComponent.SYNC_ENGINE)

        if '/' not in all_drives:
            all_drives['/'] = None
        for path in all_drives:
            self._process_single_device(path, volumeid_to_uuid)
            return volumeid_to_uuid

    refresh = (lambda self: self._locklocal_volumeid_to_persistent_volumeid = { }volumeid_to_uuid = self._get_uuid_to_volumeid_map()file_cache_map = UUIDToPersistentVolumeIdMap(self.sync_engine)(uuid_to_persistent_volumeid, raw_volumeid_to_persistent_volumeid) = file_cache_map.load_from_file_cache()updated = False# WARNING: Decompyle incomplete
)()

