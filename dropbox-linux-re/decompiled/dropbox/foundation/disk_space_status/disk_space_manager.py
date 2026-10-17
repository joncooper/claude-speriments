# Source Generated with Decompyle++
# File: disk_space_manager.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import ABCMeta, abstractmethod
from typing import Optional
from six import add_metaclass
from sync_engine_boundary.nucleus_interface import NucleusInterface
from disk_space_state import DiskSpaceState
from disk_space_variant import DiskSpaceVariant
DiskSpaceManager = <NODE:12>()

class DebugDiskSpaceManager(DiskSpaceManager):
    set_nucleus_interface = (lambda self = None, nucleus = None: pass)()
    force_trigger_update = (lambda self = None, state = None, variant = abstractmethod, selsync_able_size = (0,): pass)()
    reset_state_machine = (lambda self = None: pass)()
    force_update_disk_state = (lambda self = None: pass)()

