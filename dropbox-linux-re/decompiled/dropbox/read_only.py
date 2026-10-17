# Source Generated with Decompyle++
# File: read_only.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional, Any, Callable, Set
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.fastwalk import fastwalk_with_exception_handling
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.file_system_exceptions import FileNotFoundError
from dropbox.trace import TRACE

def set_read_only_recursive_helper(set_read_only_fn, file_system = None, local_path = None, read_only = None, skip_dir_lower_set = (None, None), file_filter = ('set_read_only_fn', 'Any', 'file_system', 'Any', 'local_path', 'LocalPath', 'read_only', 'bool', 'skip_dir_lower_set', 'Optional[Set[LocalPath]]', 'file_filter', 'Optional[Callable[[LocalPath], bool]]', 'return', 'None')):
    
    try:
        set_read_only_fn(local_path, read_only)
    except FileNotFoundError:
        TRACE('Skipping recursive read-only folder tagging since it disappeared: %r', local_path)
        return None
        except Exception:
            report_exception(component = DesktopComponent.UNKNOWN)
            return None

    traversal = fastwalk_with_exception_handling(file_system, local_path, no_atime = True, follow_symlinks = False)
# WARNING: Decompyle incomplete

