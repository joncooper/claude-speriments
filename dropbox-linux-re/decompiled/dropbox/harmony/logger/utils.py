# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from typing import Optional, Text

def get_viewer_count_amis_bucket(viewer_count = None):
    if viewer_count >= 0 and viewer_count < 10:
        return str(viewer_count)
    if None >= 10 and viewer_count < 20:
        return '10-19'
    if None >= 20 and viewer_count < 50:
        return '20-49'
    if None >= 50 and viewer_count < 100:
        return '50-99'
    if None >= 100:
        return '100+'


def get_application_type_from_aid(aid = None):
    if not aid:
        return 'unknown'
    aid_lower = None.lower()
    if 'excel' in aid_lower:
        return 'Microsoft Excel'
    if None in aid_lower:
        return 'Microsoft PowerPoint'
    if None in aid_lower:
        return 'Microsoft Word'

