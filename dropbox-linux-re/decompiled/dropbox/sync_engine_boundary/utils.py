# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional
from dropbox.assertions import assert_
from dropbox.sync_engine_boundary.constants import NamespaceProperty, NamespacePropertySet, SyncEngineGeneration

class NamespacePropertyUtils(NamespaceProperty):
    has_property = (lambda cls = None, property_to_test = None, ns_properties = classmethod: pass# WARNING: Decompyle incomplete
)()
    can_mount_shared_folders = (lambda cls = None, ns_properties = None: cls.has_property(cls.CAN_MOUNT_SHARED_FOLDERS, ns_properties))()
    is_team_shared_folder = (lambda cls = None, ns_properties = None: cls.has_property(cls.IS_TEAM_SHARED_FOLDER, ns_properties))()
    is_in_team_folder = (lambda cls = None, ns_properties = None: cls.has_property(cls.IN_TEAM_FOLDER, ns_properties))()
    is_confidential = (lambda cls = None, ns_properties = None: cls.has_property(cls.IS_CONFIDENTIAL, ns_properties))()
    can_create_confidential_folder = (lambda cls = None, ns_properties = None: not cls.has_property(cls.DISALLOW_CONFIDENTIAL_CREATION, ns_properties))()
    only_owner_can_update_acl = (lambda cls = None, ns_properties = None: cls.has_property(cls.ONLY_OWNER_CAN_UPDATE_ACL, ns_properties))()
    forbid_non_team_sharing = (lambda cls = None, ns_properties = None: cls.has_property(cls.FORBID_NON_TEAM_SHARING, ns_properties))()
    is_user_on_same_team_as_owner = (lambda cls = None, ns_properties = None: cls.has_property(cls.IS_USER_ON_SAME_TEAM_AS_OWNER, ns_properties))()


def backup_mode_args_to_engine_generation():
    return SyncEngineGeneration.NUCLEUS

