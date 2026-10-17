# Source Generated with Decompyle++
# File: debug.pyc (Python 3.11)

from build_number import dropbox_version

def should_trace_event_pipeline():
    return dropbox_version.is_internal_alpha()

