# Source Generated with Decompyle++
# File: rect.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from typing import NamedTuple
Point = NamedTuple('Point', [
    ('x', int),
    ('y', int)])
Size = NamedTuple('Size', [
    ('width', int),
    ('height', int)])
Rect = NamedTuple('Rect', [
    ('origin', Point),
    ('size', Size)])
Margin = NamedTuple('Margin', [
    ('left', int),
    ('top', int),
    ('right', int),
    ('bottom', int)])
