# Source Generated with Decompyle++
# File: debug_tracing.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import ast
import inspect
from pprint import pformat
from typing import Any
from six.moves import map, range, zip
import build_number
from dropbox.trace import TRACE

def dlog(*args, **options):
    pass
# WARNING: Decompyle incomplete


class UnparseError(Exception):
    pass


def unparse_ast_node(node = None):
    if isinstance(node, ast.Name):
        return node.id
# WARNING: Decompyle incomplete

