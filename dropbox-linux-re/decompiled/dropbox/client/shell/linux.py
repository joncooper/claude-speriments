# Source Generated with Decompyle++
# File: linux.pyc (Python 3.11)

from typing import Any, Dict, List, Optional, Text, Tuple

queue
from dropbox.client.message_queue import MessageQueueThread
import six.moves.queue, moves
from dropbox.client.shell.base import ShellControllerBase
from dropbox.client.ui.icon_overlay import do_context_action, encode_menu, get_option_group, parse_verb
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.dbexceptions import InterruptError, TimeoutError
from dropbox.event import report_aggregate_event
from dropbox.exception.reporting import report_exception
from dropbox.fastwalk_bridge import fastwalk
from dropbox.proto.nucleus.common_api_types_pb2 import LookupSyncIconReply
from dropbox.sync_engine_boundary.types.local_props import FileSyncStatus
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE

class _LinuxShellInteractionThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

LinuxShellInteractionThread = db_thread(_LinuxShellInteractionThreadImpl)
on_linux_shell_thread = LinuxShellInteractionThread.on_queue
MYPY = False
if MYPY:
    InQueueType = Queue.Queue[Tuple[(Optional[Text], int)]]
named_pipe_inqueue: 'InQueueType' = Queue.Queue()
named_pipe_outqueue: 'Queue.Queue[Text]' = Queue.Queue()

class CommandServerProxy(object):
    
    def get_message(self = None, block = None, timeout = None):
        pass
    # WARNING: Decompyle incomplete

    
    def break_block(self):
        named_pipe_inqueue.put(None)

    
    def respond(self, ret):
        named_pipe_outqueue.put(ret)


NautilusThreadState = Tuple[(List[Text], bool)]
NAUTILUS_MESSAGE_THREAD_NAME = 'NautilusMessageThread'

class NautilusMessageThread(StoppableThread):
    pass
# WARNING: Decompyle incomplete


class ShellController(ShellControllerBase):
    
    def __init__(self, control_thread):
        self._linux_shell_thread = LinuxShellInteractionThread()
        self._linux_shell_thread.daemon = True
        self._linux_shell_thread.start()
        self.control_thread = control_thread
        self._nautilus_status_message_thread = None

    
    def touch_files(self, local_paths):
        for local_path in local_paths:
            self.control_thread.shell_touch(path = Text(local_path))
            return None

    reset_root_path = (lambda self = None, local_path = None: to_touch = set()tree_to_touch = local_pathif tree_to_touch:
try:
for _, ents in fastwalk(tree_to_touch):
for dirent in ents:
to_touch.add(dirent.fullpath)try:
continueexcept Exception:
report_exception(component = DesktopComponent.SHELL_INTEGRATION_NAUTILUS)try:
continuetry:
continueexcept Exception:
report_exception(component = DesktopComponent.SHELL_INTEGRATION_NAUTILUS)self.touch_files(to_touch)None)()
    
    def extension_debug_state(self = None):
        return { }

    
    def start_status_thread(self, app, sync_engine_adapter):
        self._nautilus_status_message_thread = db_thread(NautilusMessageThread)(app, sync_engine_adapter, self.control_thread)
        self._nautilus_status_message_thread.daemon = True
        self._nautilus_status_message_thread.start()


