# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals

class InfinitePlaceholderDecodeError(Exception):
    pass


class NotAnInfinitePlaceholderError(Exception):
    pass


class NucleusPlaceholderError(InfinitePlaceholderDecodeError):
    
    def __init__(self, user_id):
        self.user_id = user_id



class StubFolderDecodeError(Exception):
    pass


class NotAStubFolderError(Exception):
    pass

