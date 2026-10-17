# Source Generated with Decompyle++
# File: account_id.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv

class ContainsDbidAnnotation(bb.AnnotationType):
    __slots__ = [
        '_authorize_caller']
    
    def __init__(self, authorize_caller = (True,)):
        self._authorize_caller = authorize_caller

    authorize_caller = (lambda self: self._authorize_caller)()

ROUTES = { }
