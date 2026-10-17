# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import abstractmethod, abstractproperty
from typing import Text
from apex.metrics import MetricsReporter
from dropbox.foundation.raii2.quick import Destroyable

class ContextInterface:
    storage_location = (lambda self = None: pass)()
    metrics_reporter = (lambda self = None: pass)()()


class Context(ContextInterface, Destroyable):
    pass

