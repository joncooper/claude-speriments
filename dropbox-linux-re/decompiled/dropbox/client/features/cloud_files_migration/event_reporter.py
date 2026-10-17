# Source Generated with Decompyle++
# File: event_reporter.pyc (Python 3.11)

from enum import StrEnum
from typing import Dict, Optional
from dropbox.event import report
CLOUD_FILES_CONVERSION_EVENTS = 'cloud-files-conversion-events'

class CloudFilesConversionEventType(StrEnum):
    CONVERSION_SUCCEEDED = 'conversion_succeeded'
    CONVERSION_FAILED = 'conversion_failed'


class CloudFilesConversionEventInfo:
    
    def __init__(self, root_mount_path = None, error_string = None, error = None, exc_traceback = ('root_mount_path', 'str', 'error_string', 'str', 'error', 'int', 'exc_traceback', 'str')):
        self.root_mount_path = root_mount_path
        self.error_string = error_string
        self.error = error
        self.exc_traceback = exc_traceback

    
    def as_dict(self = None):
        return {
            'error_string': self.error_string,
            'error': self.error,
            'exc_traceback': self.exc_traceback,
            'root_mount_path': self.root_mount_path }



def report_cloud_files_conversion_event(event_type = None, error_info = None):
    report(CLOUD_FILES_CONVERSION_EVENTS, True, event_type = event_type, extra = error_info.as_dict() if error_info else None)

