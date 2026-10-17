# Source Generated with Decompyle++
# File: indexing_attributes.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, Dict, Optional, Text
from six import iteritems

class IndexingAttributes(object):
    
    def __init__(self = None, **kw):
        if 'type' in kw:
            self.type = kw['type']
        if 'size' in kw:
            self.size = kw['size']
        if 'size_on_disk' in kw:
            self.size_on_disk = kw['size_on_disk']
        if 'ctime' in kw:
            self.ctime = kw['ctime']
        if 'mtime' in kw:
            self.mtime = kw['mtime']
        if 'atime' in kw:
            self.atime = kw['atime']
        if 'posix_mode' in kw:
            self.posix_mode = kw['posix_mode']
        if 'posix_gid' in kw:
            self.posix_gid = kw['posix_gid']
        if 'posix_uid' in kw:
            self.posix_uid = kw['posix_uid']
        if 'posix_nlink' in kw:
            self.posix_nlink = kw['posix_nlink']
        if 'posix_symlink_target' in kw:
            self.posix_symlink_target = kw['posix_symlink_target']
        if 'is_read_only' in kw:
            self.is_read_only = kw['is_read_only']
        if 'volumeid' in kw:
            self.volumeid = kw['volumeid']
        if 'inode' in kw:
            self.inode = kw['inode']
        if 'machineid_attr' in kw:
            self.machineid_attr = kw['machineid_attr']
        if 'has_stable_inodes' in kw:
            self.has_stable_inodes = kw['has_stable_inodes']
        if 'children' in kw:
            self.children = kw['children']
        if 'stringlock' in kw:
            self.stringlock = kw['stringlock']
        if 'stringio' in kw:
            self.stringio = kw['stringio']
        if 'attrs' in kw:
            self.attrs = kw['attrs']
        if 'symdata' in kw:
            self.symdata = kw['symdata']
        if 'infinite_details' in kw:
            self.infinite_details = kw['infinite_details']
        if 'stubfolder_details' in kw:
            self.stubfolder_details = kw['stubfolder_details']
        if 'reparse_tag' in kw:
            self.reparse_tag = kw['reparse_tag']
        if 'name' in kw:
            self.name = kw['name']
            return None

    
    def copy(self = None):
        fields = self.__dict__
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        fields = self.__dict__
        return ','.join % (lambda .0: pass# WARNING: Decompyle incomplete
)(iteritems(fields)())


