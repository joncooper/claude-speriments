# Source Generated with Decompyle++
# File: ordered_set.pyc (Python 3.11)

from collections.abc import MutableSet
from typing import Optional, Any, Dict, Generic, Hashable, Iterable, Iterator, List, TypeVar
_SetType = TypeVar('_SetType', bound = Hashable)
_LinkedListEntry = List[Any]

def OrderedSet():
    '''OrderedSet'''
    
    def __init__(self = None, iterable = None):
        self.end = []
        end = []
        end += [
            None,
            end,
            end]
        self.map = { }
    # WARNING: Decompyle incomplete

    
    def __len__(self = None):
        return len(self.map)

    
    def __contains__(self = None, key = None):
        return key in self.map

    
    def add(self = None, key = None):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = [
                key,
                curr,
                end]
            end[1] = [
                key,
                curr,
                end]
            self.map[key] = [
                key,
                curr,
                end]
            return None

    
    def discard(self = None, key = None):
        if key in self.map:
            (key, prev, next) = self.map.pop(key)
            prev[2] = next
            next[1] = prev
            return None

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __reversed__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def pop(self = None, last = None):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    
    def __repr__(self = None):
        if not self:
            return f'''{self.__class__.__name__!s}()'''
        return f'''{None.__class__.__name__!s}({list(self)!r})'''

    
    def __eq__(self = None, other = None):
