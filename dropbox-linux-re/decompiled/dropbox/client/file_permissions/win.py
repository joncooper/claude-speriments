# Source Generated with Decompyle++
# File: win.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import stat
from typing import Text
import ntsecuritycon
import win32api
import win32con
import win32security
import winerror
from six.moves import range
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.sync_engine_boundary.client_lib.windows_path_util import nt_escape_and_convert_to_unicode
from dropbox.sync_engine_boundary.constants import FixPermissionStatus
from dropbox.trace import TRACE

def _check_perms_for_one_path(path, required_perms, raw_user_sid, permissions = (None, None)):
    pass
# WARNING: Decompyle incomplete


def _fix_access_bits_helper(escaped_path, required_perms):
    
    try:
        access_bits = 0
        required_perms_lower = required_perms.lower()
        if 'r' in required_perms_lower:
            access_bits += stat.S_IREAD
        if 'w' in required_perms_lower:
            access_bits += stat.S_IWRITE
        if 'x' in required_perms_lower:
            access_bits += stat.S_IXUSR
        os.chmod(escaped_path, access_bits)
        return None
    except OSError:
        e = None
        TRACE('_fix_access_bits_helper: os.chmod failed with error %r %r -- ignoring', e.errno, e)
        e = None
        del e
        return None
        e = None
        del e



def fix_perms_without_prompt_if_needed(path, validate_perms, required_perms = (_check_perms_for_one_path, 'rwX')):
    escaped_path = nt_escape_and_convert_to_unicode(path)
    required_perms_orig = required_perms
    if not os.access(escaped_path, os.F_OK):
        return FixPermissionStatus.NOTEXIST
    if None == 'rwX':
        if os.path.isdir(escaped_path):
            required_perms = AccessControlEntry.RWX_DIR_PERMISSION_LIST
        else:
            required_perms = AccessControlEntry.RWX_FILE_PERMISSION_LIST
    _fix_access_bits_helper(escaped_path, required_perms_orig)
    permissions = WinPermissions(escaped_path)
# WARNING: Decompyle incomplete


class WinPermissions(object):
    
    def __init__(self, path):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        rv = f'''<{self.__class__.__name__!s} path= {self.path!r}\n'''
        if not self.ace_list:
            rv += 'unable to read permissions'
        for ace in self.ace_list:
            rv += '%r\n' % ace
            rv += '>'
            return rv

    
    def get_ace(self, raw_sid, ace_type):
        for ace in self.ace_list:
            if ace.raw_sid == raw_sid and ace.ace_type == ace_type:
                
                return None, ace
            return None

    
    def get_ace_index(self, raw_sid, ace_type):
        for i, ace in enumerate(self.ace_list):
            if ace.raw_sid == raw_sid and ace.ace_type == ace_type:
                
                return None, i
            return None

    
    def remove_access_denied_ace_for_sid(self, raw_sid):
        access_denied_index = self.get_ace_index(raw_sid, 'ACCESS_DENIED_ACE_TYPE')
    # WARNING: Decompyle incomplete

    
    def has_access_allowed_ace_for_sid(self, raw_sid):
        return self.get_ace(raw_sid, 'ACCESS_ALLOWED_ACE_TYPE') is not None

    
    def add_access_allowed_ace_for_sid_from_parent(self, raw_sid):
        parent = os.path.dirname(self.path)
        parent_permissions = WinPermissions(parent)
        parent_access_allowed_ace = parent_permissions.get_ace(raw_sid, 'ACCESS_ALLOWED_ACE_TYPE')
    # WARNING: Decompyle incomplete

    
    def has_permissions_in_list(self, raw_sid, perm_list):
        access_denied_ace = self.get_ace(raw_sid, 'ACCESS_DENIED_ACE_TYPE')
        access_allowed_ace = self.get_ace(raw_sid, 'ACCESS_ALLOWED_ACE_TYPE')
    # WARNING: Decompyle incomplete

    
    def save(self):
        self.sd.SetSecurityDescriptorDacl(1, self.dacl, 0)
        win32security.SetFileSecurity(self.path, win32security.DACL_SECURITY_INFORMATION, self.sd)



class AccessControlEntry(object):
    ACE_TYPES = [
        'ACCESS_ALLOWED_ACE_TYPE',
        'ACCESS_DENIED_ACE_TYPE',
        'SYSTEM_AUDIT_ACE_TYPE',
        'SYSTEM_ALARM_ACE_TYPE']
    ACE_FLAGS = [
        'OBJECT_INHERIT_ACE',
        'CONTAINER_INHERIT_ACE',
        'NO_PROPAGATE_INHERIT_ACE',
        'INHERIT_ONLY_ACE',
        'SUCCESSFUL_ACCESS_ACE_FLAG',
        'FAILED_ACCESS_ACE_FLAG']
    PERMISSION_LIST_FILE = [
        'DELETE',
        'READ_CONTROL',
        'WRITE_DAC',
        'WRITE_OWNER',
        'SYNCHRONIZE',
        'FILE_GENERIC_READ',
        'FILE_GENERIC_WRITE',
        'FILE_GENERIC_EXECUTE',
        'FILE_DELETE_CHILD']
    PERMISSION_LIST_DIR = [
        'DELETE',
        'READ_CONTROL',
        'WRITE_DAC',
        'WRITE_OWNER',
        'SYNCHRONIZE',
        'FILE_ADD_SUBDIRECTORY',
        'FILE_ADD_FILE',
        'FILE_DELETE_CHILD',
        'FILE_LIST_DIRECTORY',
        'FILE_TRAVERSE',
        'FILE_READ_ATTRIBUTES',
        'FILE_WRITE_ATTRIBUTES',
        'FILE_READ_EA',
        'FILE_WRITE_EA']
    PERMISSION_LIST_DIR_INHERIT = [
        'DELETE',
        'READ_CONTROL',
        'WRITE_DAC',
        'WRITE_OWNER',
        'SYNCHRONIZE',
        'GENERIC_READ',
        'GENERIC_WRITE',
        'GENERIC_EXECUTE',
        'GENERIC_ALL']
    RWX_DIR_PERMISSION_LIST = [
        'DELETE',
        'READ_CONTROL',
        'FILE_ADD_SUBDIRECTORY',
        'FILE_ADD_FILE',
        'FILE_LIST_DIRECTORY',
        'FILE_TRAVERSE',
        'FILE_READ_ATTRIBUTES',
        'FILE_WRITE_ATTRIBUTES',
        'FILE_READ_EA',
        'FILE_WRITE_EA']
    RWX_FILE_PERMISSION_LIST = [
        'DELETE',
        'READ_CONTROL']
    
    def __init__(self, raw_ace, is_file, name = ('ACE',)):
        self.name = name
        self.raw_ace = raw_ace
        self.raw_type = raw_ace[0][0]
        self.raw_flags = raw_ace[0][1]
        self.raw_mask = raw_ace[1]
        self.raw_sid = raw_ace[2]
        self.ace_type = ''
        self.flags = []
        self.sid = None
        self.permissions = []
        self._set_ace_type()
        self._set_flags()
        self._set_sid()
        if not is_file:
            self.permission_list = self.PERMISSION_LIST_DIR
            if self.has_flag('OBJECT_INHERIT_ACE') and self.has_flag('INHERIT_ONLY_ACE'):
                self.permission_list = self.PERMISSION_LIST_DIR_INHERIT
            else:
                self.permission_list = self.PERMISSION_LIST_FILE
        self._set_permissions()

    
    def all_permissions_in_list(self, perm_list):
        pass
    # WARNING: Decompyle incomplete

    
    def any_permission_in_list(self, perm_list):
        pass
    # WARNING: Decompyle incomplete

    
    def has_flag(self, flag_name):
        return flag_name in self.flags

    
    def has_permission(self, perm_name):
        return perm_name in self.permissions

    
    def _set_ace_type(self):
        for t in self.ACE_TYPES:
            if getattr(ntsecuritycon, t) == self.raw_type:
                self.ace_type = t
                return None
            return None

    
    def _set_flags(self):
        for flag_name in self.ACE_FLAGS:
            flag_value = getattr(ntsecuritycon, flag_name)
        except AttributeError:
            continue
        if flag_value & self.raw_flags == flag_value:
            self.flags.append(flag_name)
        continue

    
    def _set_permissions(self):
        self.calc_mask = 0
        for perm_name in self.permission_list:
            perm_value = getattr(ntsecuritycon, perm_name)
        except AttributeError:
            continue
        if perm_value & self.raw_mask == perm_value:
            self.permissions.append(perm_name)
            self.calc_mask = self.calc_mask | perm_value
        continue

    
    def _set_sid(self):
        
        try:
            self.pretty_sid = win32security.LookupAccountSid(None, self.raw_sid)
            return None
        except win32api.error:
            e = None
            self.pretty_sid = self.raw_sid
            if e.winerror == winerror.ERROR_NONE_MAPPED:
                pass
            else:
                report_exception(component = DesktopComponent.FILE_LOCKING)
                e = None
                del e
                return None
            e = None
            del e
            return None
            e = None
            del e


    
    def __repr__(self):
        repr_vars = (self.__class__.__name__, self.pretty_sid, self.ace_type, hex(self.raw_flags), self.flags, hex(self.raw_mask), hex(self.calc_mask), self.permissions)
        return '<%s sid=%s, type=%s, flags(hex, list)=%s %s, permissions(read, calculated, list)=%s %s %s>' % repr_vars



def show_perms(path = None):
    return str(WinPermissions(path))

