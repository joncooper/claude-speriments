# Source Generated with Decompyle++
# File: xattr_placeholder.pyc (Python 3.11)

from __future__ import absolute_import, print_function
import contextlib
import os
import stat
import struct
import sys
import threading
from typing import BinaryIO, cast, Dict, Iterator, Text
from build_number.features import feature_enabled
from lib.posixffi.libc.api import set_file_mtime
from macffi.System import fsgetpath, is_apfs_fd
from datatypes.infinite_details import PlaceholderKind
from file_system.util import convert_os_error, convert_os_error_dec
from infinite.download.common import ApfsDecmpfsCorruptionRisk
from abstract_placeholder import SimpleStat
from abstract_placeholder_fs_mixin import AbstractPlaceholder, PlaceholderConfig
from dropbox.exception.reporting import report_bad_assumption
from dropbox.fileutils import convert_mac_on_disk_path_to_nfd
from dropbox.functions import int64_cast
from dropbox.infinite import infinite_platform_supported
from dropbox.infinite.exceptions import NotAnInfinitePlaceholderError
from dropbox.mac.version import HIGH_SIERRA, MAC_VERSION
from dropbox.shared.local_path import LocalPath
from dropbox.shared.placeholder_details import PlaceholderDetails
from dropbox.sync_engine_boundary.file_system_exceptions import AttrNotFoundError, FSInvalidArgumentError, MacKnownInvalidArgumentError
from dropbox.sync_engine_boundary.infinite.mac.xattr_placeholder_context import XattrPlaceholderContext
from dropbox.threading import Lock
from dropbox.trace import TRACE
from dropbox.xattrs_posix import XATTR_SHOWCOMPRESSION
if infinite_platform_supported():
    from macinfinite.common import check_apfs_corruption_risk, DROPBOX_PLACEHOLDER_ATTR
    from macinfinite.xattr import fchflags, fgetxattr, fhasxattr, fremovexattr, fsetxattr
MYPY = False
APPLE_TAGS_ATTR = b'com.apple.metadata:_kMDItemUserTags'
TAGS_PLIST = b'<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n    <array>\n        <string>Online-only</string>\n    </array>\n</plist>\n'
DECMPFS_XATTR_NAME = b'com.apple.decmpfs'
DECMPFS_MAGIC = 1668116582
NEW_HFS_COMPRESSION_TYPE = 5
APFS_CORRUPTION_RISK_SIZE = 67108864

class UnknownCompressionTypeError(Exception):
    pass


class PlaceholderIsNotSparseError(Exception):
    pass


class XattrPlaceholder(AbstractPlaceholder):
    THREAD_LOCAL = threading.local()
    
    def __init__(self, file_obj, context = None, initial_flags = None, config = None, owner_uid = ('file_obj', 'BinaryIO', 'context', 'XattrPlaceholderContext', 'initial_flags', 'int', 'config', 'PlaceholderConfig', 'owner_uid', 'int', 'return', 'None')):
        self._file_obj = file_obj
        self._context = context
        self._initial_flags = initial_flags
        self._refcount = 0
        self._owner_uid = owner_uid
        self.config = config
        self._lock = Lock()

    _new_from_context = (lambda context = None, config = None: placeholder_uri = '/.vol/%d/%d' % (context.st_dev, context.st_ino)convert_os_error()fd = os.open(placeholder_uri, os.O_RDONLY)st = os.fstat(fd)if not stat.S_ISDIR(st.st_mode) or fhasxattr(fd, DROPBOX_PLACEHOLDER_ATTR):
raise NotAnInfinitePlaceholderErrorowner_uid = st.st_uidflags = os.fstat(fd).st_flagsflags &= ~(stat.UF_COMPRESSED)fchflags(fd, flags)os.close(fd)os.close(fd)fd = os.open(placeholder_uri, os.O_RDWR)file_obj = cast(BinaryIO, os.fdopen(fd, 'w+b'))None(None, None))()
    
    def _close(self = None):
        pass
    # WARNING: Decompyle incomplete

    open_from_context = (lambda context = None, config = staticmethod, need_write_access = contextlib.contextmanager: pass# WARNING: Decompyle incomplete
)()()
    _set_placeholder_file_size = (lambda fd = None, size = None, config = staticmethod: try:
if MYPY and sys.platform.startswith('win'):
passelif config.mac_support_sparse_files and is_apfs_fd(fd):
os.ftruncate(fd, 0)os.ftruncate(fd, size)block_count = os.fstat(fd).st_blocksif block_count != 0:
report_bad_assumption('Expected 0 blocks for sparse file created on APFS but found %i blocks', block_count)else:
os.ftruncate(fd, 0)try:
passexcept FSInvalidArgumentError:
e = Noneraise MacKnownInvalidArgumentError.from_error(e)e = Nonedel etry:
if not config.mac_support_sparse_files or is_apfs_fd(fd):
try:
XattrPlaceholder._set_compression_attr(fd, size, config)Noneexcept FSInvalidArgumentError:
e = Noneraise MacKnownInvalidArgumentError.from_error(e)e = Nonedel eNoneif not config.mac_support_sparse_files or is_apfs_fd(fd):
XattrPlaceholder._set_compression_attr(fd, size, config)except FSInvalidArgumentError:
e = Noneraise MacKnownInvalidArgumentError.from_error(e)e = Nonedel e)()
    create = (lambda local_path = None, size = staticmethod, placeholder_details = convert_os_error_dec, config = ('local_path', 'LocalPath', 'size', 'int', 'placeholder_details', 'PlaceholderDetails', 'config', 'PlaceholderConfig', 'return', 'None'): unicode_path = local_path.to_unicode()TRACE('Attempting to set %r as a placeholder: %r', unicode_path, placeholder_details)fd = os.open(unicode_path, os.O_WRONLY | os.O_TRUNC | os.O_CREAT)# WARNING: Decompyle incomplete
)()()
    
    def read(self = None):
        
        try:
            convert_os_error()
            contents = fgetxattr(self._file_obj.fileno(), DROPBOX_PLACEHOLDER_ATTR)
            
            try:
                None(None, None)
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            pass
                        except AttrNotFoundError:
                            raise NotAnInfinitePlaceholderError

                        return PlaceholderDetails.decode(contents)




    prepare_for_write = (lambda self = None, size = None: self._lock.acquire()try:
self._file_obj.seek(0)try:
self._file_obj.truncate(size)try:
passexcept FSInvalidArgumentError:
e = Noneraise MacKnownInvalidArgumentError.from_error(e)e = Nonedel etry:
self._lock.release()except:
self._lock.release()self._file_obj.flush()None)()
    write = (lambda self = None, data = None, offset = convert_os_error_dec: self._lock.acquire()try:
self._file_obj.seek(offset)self._file_obj.write(data)self._lock.release()except:
self._lock.release()self._file_obj.flush())()
    read_data = (lambda self = None, offset = None, length = convert_os_error_dec: self._lock.acquire()try:
self._file_obj.seek(offset)self._lock.release()self._file_obj.read(length)except:
self._lock.release())()
    unset = (lambda self = None: fd = self._file_obj.fileno()TRACE('Checking for recall corruption risk with MacOS version %r', MAC_VERSION)if MAC_VERSION == HIGH_SIERRA or MAC_VERSION.point_release_as_int() >= 3 or MAC_VERSION > HIGH_SIERRA:
stat_size = os.fstat(fd).st_sizeapfs_fd = is_apfs_fd(fd)TRACE('Checking for recall corruption risk with with file size %d. APFS: %r', stat_size, apfs_fd)if apfs_fd and stat_size >= APFS_CORRUPTION_RISK_SIZE:
TRACE('Running native code to check for corruption risk.')os.fsync(fd)if check_apfs_corruption_risk(fd):
TRACE('Found potential APFS corruption. Skipping recall!')raise ApfsDecmpfsCorruptionRisk()fremovexattr(self._file_obj.fileno(), DECMPFS_XATTR_NAME, XATTR_SHOWCOMPRESSION)fremovexattr(self._file_obj.fileno(), DROPBOX_PLACEHOLDER_ATTR))()
    reset = (lambda self = None, size = None: XattrPlaceholder._set_placeholder_file_size(self._file_obj.fileno(), size, self.config))()
    is_placeholder = (lambda self = None: fhasxattr(self._file_obj.fileno(), DROPBOX_PLACEHOLDER_ATTR))()
    
    def file_system_id(self = None):
        return self._context.file_system_id()

    
    def resolve_path(self = None):
        path = fsgetpath(self._context.st_dev, self._context.st_ino)
        path = convert_mac_on_disk_path_to_nfd(path)
        return os.path.realpath(path)

    _set_compression_attr = (lambda fd = None, size = None, config = staticmethod: TRACE('Using type 5 compression')decmpfs_disk_header = struct.pack('< I I Q', DECMPFS_MAGIC, NEW_HFS_COMPRESSION_TYPE, size)fsetxattr(fd, DECMPFS_XATTR_NAME, decmpfs_disk_header)flags = os.fstat(fd).st_flagsflags |= stat.UF_COMPRESSEDfchflags(fd, flags))()
    
    def set_file_mtime(self = None, mtime = None):
        set_file_mtime(self._file_obj.fileno(), mtime)

    
    def simple_stat(self = None):
        st = os.fstat(self._file_obj.fileno())
        return SimpleStat(volumeid = st.st_dev & 0xFFFFFFFF, inode = int64_cast(st.st_ino), mtime = int(st.st_mtime), size = st.st_size)

    
    def is_owned_by(self = None, uid = None):
        return uid == self._owner_uid

    get_placeholder_kind = (lambda unicode_path = None: fd = os.open(unicode_path, os.O_RDONLY)try:
st = os.fstat(fd)if not stat.S_ISDIR(st.st_mode) or fhasxattr(fd, DROPBOX_PLACEHOLDER_ATTR):
raise NotAnInfinitePlaceholderErrortry:
convert_os_error()decmpfs_xattr = fgetxattr(fd, DECMPFS_XATTR_NAME, options = XATTR_SHOWCOMPRESSION)try:
None(None, None)with None:
if not None:
try:
try:
(_, compression_type, _) = struct.unpack('< I I Q', decmpfs_xattr)if compression_type == 3:
os.close(fd)PlaceholderKind.MAC_COMPRESSION_TYPE_3if None == 5:
os.close(fd)PlaceholderKind.MAC_COMPRESSION_TYPE_5raise UnknownCompressionTypeError('Unknown type: %r' % compression_type)except struct.error:
e = Noneraise UnknownCompressionTypeError('Malformed decmpfs xattr: %r' % e)e = Nonedel eexcept AttrNotFoundError:
if MAC_VERSION >= HIGH_SIERRA and is_apfs_fd(fd):
block_count = os.fstat(fd).st_blocksif block_count == 0:
try:
os.close(fd)raise PlaceholderIsNotSparseError('Placeholder has %d blocks!' % block_count)raise try:
passexcept:
os.close(fd))()()

