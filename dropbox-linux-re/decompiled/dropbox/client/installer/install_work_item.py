# Source Generated with Decompyle++
# File: install_work_item.pyc (Python 3.11)

import os
from enum import auto, Enum
from shutil import copy2 as _copy2
from typing import Callable, List, Optional
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import retry, RetryException
from dropbox.trace import TRACE
replace = (lambda src = None, dst = None: try:
os.replace(src, dst)Noneexcept OSError:
e = Noneraise RetryException(inner = e)e = Nonedel e)()

class InstallWorkItemType(Enum):
    COPY = auto()
    COPY_IF_SOURCE_EXISTS = auto()
    MOVE = auto()
    MOVE_IF_SOURCE_EXISTS = auto()
    MOVE_FALLBACK_TO_COPY = auto()


class InstallWorkItem:
    
    def __init__(self = None, item_type = None, *, source_dir, source_name, dest_dir, dest_name, temp_dir, callback):
        pass
    # WARNING: Decompyle incomplete

    
    def run(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def rollback(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return 'InstallWorkItem({item_type}, source_dir={source_dir}, source_name={source_name}, dest_dir={dest_dir},dest_name={dest_name}, temp_dir={temp_dir}, callback={callback})'.format(item_type = self.item_type, source_dir = self.source_dir, source_name = self.source_name, dest_dir = self.dest_dir, dest_name = self.dest_name, temp_dir = self.temp_dir, callback = self.callback)



def run_all_work_items(work_items = None):
    for i, item in enumerate(work_items):
        TRACE('Running work item: %s', item)
        item.run()
        except Exception:
            TRACE('Could not run work item, rolling back')
            for j in range(i, -1, -1):
                rollback_item = work_items[j]
                TRACE('Rolling back work item: %s', rollback_item)
                rollback_item.rollback()
                except Exception:
                    TRACE('Rollback unexpectedly threw exception: %s', rollback_item)
                    report_exception(severity = Severity.CRITICAL, component = DesktopComponent.INSTALLER)
                    continue
                raise 
                return None

