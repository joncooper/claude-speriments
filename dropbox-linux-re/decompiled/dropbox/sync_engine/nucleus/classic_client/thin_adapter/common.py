# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

_TPRT_ENABLED_FOR_TESTS = True

def set_tprt_enabled_for_tests(enabled = None):
    global _TPRT_ENABLED_FOR_TESTS
    _TPRT_ENABLED_FOR_TESTS = enabled


def is_tprt_enabled():
    if not _TPRT_ENABLED_FOR_TESTS:
        return False

