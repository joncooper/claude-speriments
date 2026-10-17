# Source Generated with Decompyle++
# File: xattr_stub_folder_fs_mixin.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import errno
import os
import stat
from file_system.exceptions import create_not_a_directory_error, create_permission_denied_error
from file_system.util import convert_os_error, convert_os_error_dec
from stub_folder_fs_mixin import StubFolderFileSystemMixinInterface
from dropbox.infinite import infinite_platform_supported
from dropbox.infinite.exceptions import NotAStubFolderError
from dropbox.shared.local_path import LocalPath
from dropbox.shared.stub_folder_details import StubFolderDetails
from dropbox.sync_engine_boundary.file_system_exceptions import AttrNotFoundError, FileNotFoundError
from dropbox.trace import TRACE
if infinite_platform_supported():
    from macinfinite.common import DROPBOX_PLACEHOLDER_ATTR
    from macinfinite.xattr import fgetxattr, fhasxattr, fremovexattr, fsetxattr

class XattrStubFolderFileSystemMixinInterface(StubFolderFileSystemMixinInterface):
    
    def is_infinite_stub_folder(self = None, local_path = None):
        
        try:
            convert_os_error()
            fd = os.open(local_path.to_unicode(), os.O_RDONLY)
            if fhasxattr(fd, DROPBOX_PLACEHOLDER_ATTR) and stat.S_ISDIR(os.fstat(fd).st_mode):
                os.close(fd)
                
                try:
                    None(None, None)
                    return True
                    os.close(fd)
                try:
                    None(None, None)
                with None:
                    if not None:
                        
                        try:
                            
                            try:
                                return False
                            except FileNotFoundError:
                                return False





    set_stub_folder_by_path = (lambda self = None, local_path = None, stub_folder_details = convert_os_error_dec: TRACE('Attempting to set a stubfolder at path %r', local_path)unicode_path = local_path.to_unicode()fd = os.open(unicode_path, os.O_RDONLY)try:
st = os.fstat(fd)if not stat.S_ISDIR(st.st_mode):
raise create_not_a_directory_error(local_path)try:
placeholder_data = stub_folder_details.encode()fsetxattr(fd, DROPBOX_PLACEHOLDER_ATTR, placeholder_data)try:
passexcept OSError:
e = Noneif e.errno == errno.EPERM:
raise create_permission_denied_error(local_path)raise e = Nonedel etry:
os.close(fd)Noneexcept:
os.close(fd))()
    unset_stub_folder_by_path = (lambda self = None, local_path = None: TRACE('Attempting to unset a stubfolder at path %r', local_path)unicode_path = local_path.to_unicode()fd = os.open(unicode_path, os.O_RDONLY)try:
st = os.fstat(fd)if not stat.S_ISDIR(st.st_mode):
raise create_not_a_directory_error(local_path)try:
fremovexattr(fd, DROPBOX_PLACEHOLDER_ATTR)try:
passexcept OSError:
e = Noneif e.errno == errno.EPERM:
raise create_permission_denied_error(local_path)raise e = Nonedel etry:
os.close(fd)Noneexcept:
os.close(fd))()
    
    def read_stub_folder_by_path(self = None, local_path = None):
        
        try:
            convert_os_error()
            fd = os.open(local_path.to_unicode(), os.O_RDONLY)
            st = os.fstat(fd)
            if not stat.S_ISDIR(st.st_mode):
                raise NotAStubFolderError
            contents = fgetxattr(fd, DROPBOX_PLACEHOLDER_ATTR)
            os.close(fd)
            
            try:
                None(None, None)
                return 
                os.close(fd)
                with None:
                    if not None:
                        
                        try:
                            
                            try:
                                None, StubFolderDetails.decode(contents)
                                return None
                            except AttrNotFoundError:
                                raise NotAStubFolderError






