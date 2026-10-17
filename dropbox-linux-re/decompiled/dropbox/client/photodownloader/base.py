# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import abc
from typing import Any, Dict, List, Optional, Set, Text, Tuple, Union
from dropbox.camera import Device
from dropbox.client.configuration.interface import LocalConfigurationInterface
MYPY = False
if MYPY:
    from dropbox.client.camera_upload.camera_uploads import CameraHandler

class PhotoDownloaderBase(object):
    
    def __init__(self = None, *n, **kw):
        self.controller = None

    update_action_defaults = (lambda self = None: pass)()
    get_action = (lambda self = None, local_config = None, saved_action = abc.abstractmethod, first_run = ('local_config', 'Optional[LocalConfigurationInterface]', 'saved_action', 'Optional[Any]', 'first_run', 'Optional[bool]', 'return', 'Optional[Union[Text, Dict]]'): pass)()
    set_action = (lambda self = None, path = None, device = abc.abstractmethod: pass)()
    app_quit = (lambda self = None, saved_old_action = None: pass)()
    handle_never = (lambda self = None, old_action = None, device = abc.abstractmethod: pass)()
    register = (lambda self = None, handler = None: pass)()
    listen = (lambda self = None: pass)()
    unregister = (lambda self = None: pass)()
    shutdown = (lambda self = None: pass)()
    get_connected_devices = (lambda self = None: pass)()

