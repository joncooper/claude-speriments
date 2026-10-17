# Source Generated with Decompyle++
# File: process_metrics.pyc (Python 3.11)

from dataclasses import dataclass
from enum import IntEnum
from apex._apex import ffi, lib
HeapStatistics = <NODE:12>()

class _HeapStatisticsResultEnum(IntEnum):
    Success = 0
    NotImplemented = 1
    RetrievalFailed = 2


def heap_usage():
    usage = ffi.new('HeapStatisticsResult *')
    lib.process_heap_usage(usage)
    if usage.tag == _HeapStatisticsResultEnum.Success:
        return HeapStatistics(usage.success.size_in_use, usage.success.time_to_retrieve_micros)
    if None.tag == _HeapStatisticsResultEnum.NotImplemented:
        raise NotImplementedError()
    if usage.tag == _HeapStatisticsResultEnum.RetrievalFailed:
        raise OSError(usage.retrieval_failed)
    raise IndexError('Unexpected union tag: {}'.format(usage.tag))

