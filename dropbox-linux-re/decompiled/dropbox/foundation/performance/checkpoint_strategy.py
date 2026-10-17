# Source Generated with Decompyle++
# File: checkpoint_strategy.pyc (Python 3.11)

from abc import ABCMeta, abstractmethod
from typing import Set, Text

def PerfSessionCheckpointStrategy():
    '''PerfSessionCheckpointStrategy'''
    should_end_after_checkpoint = (lambda self = None, name = None: pass)()

PerfSessionCheckpointStrategy = <NODE:27>(PerfSessionCheckpointStrategy, 'PerfSessionCheckpointStrategy', metaclass = ABCMeta)

class NullCheckpointStrategy(PerfSessionCheckpointStrategy):
    
    def should_end_after_checkpoint(self = None, name = None):
        return False



class MultiEndCheckpointStrategy(PerfSessionCheckpointStrategy):
    
    def __init__(self = None, checkpoints = None):
        pass
    # WARNING: Decompyle incomplete

    
    def should_end_after_checkpoint(self = None, name = None):
        self._checkpoints.discard(name)
        return len(self._checkpoints) == 0


