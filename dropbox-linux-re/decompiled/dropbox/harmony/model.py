# Source Generated with Decompyle++
# File: model.pyc (Python 3.11)

import time
from typing import DefaultDict, Dict, NamedTuple, Optional, Text, Union
from weakref import ref, WeakSet, WeakValueDictionary
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.ui.common.mvc import ObservableModel, ObservableProperty
from dropbox.repr_utils import easy_repr
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRLowerServerPath
ConflictedCopyInfo = NamedTuple('ConflictedCopyInfo', [
    ('original_local_path', Optional[Text]),
    ('original_uid', Optional[int]),
    ('original_ts', Union[(int, float)]),
    ('original_fileid', Optional[bytes])])

class HarmonyWindow(ObservableModel):
    document = ObservableProperty(None)
    dirty = ObservableProperty(None)
    dirty_ts = ObservableProperty(None)
    document_update = ObservableProperty(None)
    __slots__ = ('wid', 'pid', 'aid', 'plugin', 'hidden', 'preferences')
    
    def __init__(self, plugin, wid, pid, aid):
        self.wid = wid
        self.pid = pid
        self.aid = aid
        self.hidden = False
        self.preferences = dict()
        if plugin:
            self.plugin = ref(plugin)
            return None

    
    def reset_dirty(self):
        self.dirty = None
        self.dirty_ts = None

    
    def mark_dirty(self, dirty):
        if dirty:
            if not self.dirty:
                self.dirty_ts = time.time()
            else:
                self.dirty_ts = None
        self.dirty = dirty

    
    def __repr__(self):
        return easy_repr(self, 'wid', 'pid', 'document')



class HarmonyDocument(ObservableModel):
    conflicted_copy_local_path = ObservableProperty(None)
    __slots__ = ('windows', 'uid', 'local_path', 'server_path', 'account', 'read_only', 'mount_path', 'original_local_path', 'last_known_shmodel_link', 'last_viewer_count')
    
    def __init__(self, local_path = None, server_path = None, mount_path = None, account = ('local_path', 'Optional[Text]', 'server_path', 'MRLowerServerPath', 'mount_path', 'Optional[MRLowerServerPath]', 'account', 'Optional[AccountInterface]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return easy_repr(self, 'uid', 'local_path', 'server_path', 'account')

    
    def __eq__(self, other):
