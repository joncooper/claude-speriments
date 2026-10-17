# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import NamedTuple, Optional, Text, Union
from dropbox.model.types import FileId
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRLowerServerPath
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.trace import redact_pii
ApplicationID = Text
ProcessID = int
WindowID = int
MacApplicationVersion = Text
WinApplicationVersion = int
ApplicationVersion = Union[(MacApplicationVersion, WinApplicationVersion)]
_ApplicationDetails = NamedTuple('_ApplicationDetails', [
    ('aid', ApplicationID),
    ('version', ApplicationVersion),
    ('long_version', Text),
    ('pid', ProcessID),
    ('application_path', Optional[Text]),
    ('supports_coauthoring', bool)])

class ApplicationDetails(_ApplicationDetails):
    
    def __repr__(self = None):
        return self.__class__.__name__ + f'''(aid={self.aid}, version={self.version}, long_version={self.long_version}, pid={self.pid}, application_path={redact_pii(self.application_path)}, supports_coauthoring={self.supports_coauthoring})'''


WindowDetails = NamedTuple('WindowDetails', [
    ('app_details', ApplicationDetails),
    ('wid', Optional[WindowID])])
_WindowFile = NamedTuple('_WindowFile', [
    ('window_details', WindowDetails),
    ('local_path', Optional[LocalPath])])

class WindowFile(_WindowFile):
    
    def __repr__(self = None):
        return self.__class__.__name__ + f'''(window_details={self.window_details!r}, local_path={redact_pii(self.local_path)!r})'''


DocumentSessionID = NamedTuple('DocumentSessionID', [
    ('server_path', MRLowerServerPath),
    ('file_id', FileId),
    ('window_details', WindowDetails)])

class DocumentSession(object):
    
    def __init__(self, server_path = None, file_id = None, window_file = None, location_props = ('server_path', 'MRLowerServerPath', 'file_id', 'FileId', 'window_file', 'WindowFile', 'location_props', 'LocationProperties', 'return', 'None')):
        self._server_path = server_path
        self._file_id = file_id
        self._window_file = window_file
        self._location_props = location_props
        self._id = DocumentSessionID(server_path = self._server_path, file_id = self._file_id, window_details = self._window_file.window_details)
        local_path = self._window_file.local_path
    # WARNING: Decompyle incomplete

    id = (lambda self = None: self._id)()
    server_path = (lambda self = None: self._server_path)()
    file_id = (lambda self = None: self._file_id)()
    canonical_local_path = (lambda self = None: self._canon_local_path)()
    location_properties = (lambda self = None: self._location_props)()
    window_file = (lambda self = None: self._window_file)()
    window_file = (lambda self = None, window_file = None: pass# WARNING: Decompyle incomplete
)()
    
    def __repr__(self = None):
        return self.__class__.__name__ + f'''(id={self.id!r}, window_file={self.window_file!r}, local_path={self.window_file.local_path!r}, canonical_local_path={self.canonical_local_path!r})'''


