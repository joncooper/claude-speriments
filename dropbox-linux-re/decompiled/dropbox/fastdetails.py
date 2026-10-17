# Source Generated with Decompyle++
# File: fastdetails.pyc (Python 3.11)

from __future__ import absolute_import
from six import iteritems, itervalues

class FastDetails(object):
    __attrs__ = ('server_path', 'blocklist', 'parent_blocklist', 'attrs', 'parent_attrs', 'size', 'mtime', 'sjid', 'dir', 'ctime', 'timestamp', 'user_id', 'host_id', 'mount_request', 'machineid_volumeid', 'machineid_inode', 'machineid_attr', 'fileid', 'fileid_rev', 'parent_fileid', 'parent_fileid_rev')
    __slots__ = __attrs__ + ('__internal_dict',)
    
    def __init__(self, *args, **kw):
        self.__internal_setattr('_FastDetails__internal_dict', None)
        optional_attrs = [
            'host_id',
            'ctime',
            'timestamp',
            'user_id']
        for attr in optional_attrs:
            self.__internal_setattr(attr, None)
            for k, v in iteritems(kw):
                if k == '__internal_dict':
                    continue
                self.__internal_setattr(k, v)
                return None

    
    def __iter__(self, include_none = (True,)):
        pass
    # WARNING: Decompyle incomplete

    EMPTY_DICT = { }
    
    def __eq__(self, other):
        for k in FastDetails.__attrs__:
            if getattr(self, k, None) != getattr(other, k, None):
                return False
            if not self._FastDetails__internal_dict:
                d1 = self.EMPTY_DICT
                if not other._FastDetails__internal_dict:
                    d2 = self.EMPTY_DICT
                    
                    def len_wo_none(d):
                        return (lambda .0: pass# WARNING: Decompyle incomplete
)(itervalues(d)())

                    if len_wo_none(d1) != len_wo_none(d2):
                        return False
                    for k, v in iteritems(d1):
                        if d2.get(k) != v:
                            return False
                        return True

    
    def __ne__(self, other):
        return not self.__eq__(other)

    
    def __hash__(self):
        return hash(frozenset(self.__iter__(include_none = False)))

    
    def copy(self, exclude = ((),), **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def __setattr__(self, k, v):
        raise TypeError(f'''{type(self).__name__!r} object does not support setting attributes''')

    
    def __internal_setattr(self, k, v):
        pass
    # WARNING: Decompyle incomplete

    
    def __getattribute__(self, k):
        return object.__getattribute__(self, k)

    
    def __getattr__(self, k):
        
        try:
            return self._FastDetails__internal_dict[k]
        except (KeyError, TypeError):
            raise AttributeError(f'''{type(self).__name__!r} object has no attribute {k!r}''')


    
    def to_dict(self):
        return self._FastDetails__internal_dict

    
    def __repr__(self):
        return ', '.join % (lambda .0: pass# WARNING: Decompyle incomplete
)(self())


