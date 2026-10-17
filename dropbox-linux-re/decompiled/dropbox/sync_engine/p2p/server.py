# Source Generated with Decompyle++
# File: server.pyc (Python 3.11)

from __future__ import absolute_import, print_function
import socket
import ssl
import time
from types import TracebackType
from typing import Callable, Dict, Optional, Tuple, Type, Union
import tornado.httpserver as tornado
import tornado.web as tornado
from six.moves import range
from tornado.gen import Return
from build_number import get_build_channel, is_test
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client_api.hashing import DROPBOX_HASH_LENGTH
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.exception_decorators import handle_exceptions_ex_2
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import make_bytes
from dropbox.threadutils import StoppableThreadWithAccount, ThreadPool
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info

class P2PStartupError(Exception):
    pass


class P2PServerHandler(tornado.web.RequestHandler):
    pass
# WARNING: Decompyle incomplete


class P2PServer(object):
    NS_KEY = 'ns'
    BLOCKHASH_KEY = 'blockhash'
    BLOCKS_ROUTE = f'''/blocks/(?P<{NS_KEY!s}>[^\\/]+)/(?P<{BLOCKHASH_KEY!s}>[^\\/]+)'''
    FIRST_PORT = dropbox_url_info.p2p_port
    NUM_PORTS_TO_TRY = 1000 if is_test() or get_build_channel() == 'developer' else 10
    
    def __init__(self = None, get_block_fn = None, check_block_fn = None, ssl_context_fn = (None,), account = ('get_block_fn', 'Callable[[bytes, int], Optional[bytes]]', 'check_block_fn', 'Callable[[bytes, int], bool]', 'ssl_context_fn', 'Callable[[int], ssl.SSLContext]', 'account', 'Optional[AccountInterface]', 'return', 'None')):
        self._handler_pool_head = ThreadPool('p2p_server_handler_pool_head', pool_size = 1, max_num_threads = 4, account = account)
        self._handler_pool_get = ThreadPool('p2p_server_handler_pool_get', pool_size = 1, max_num_threads = 4, account = account)
        routing_context = self._make_routing_context(ssl_context_fn)
        app = tornado.web.Application([
            (self.BLOCKS_ROUTE, P2PServerHandler, {
                'thread_pool_head': self._handler_pool_head,
                'thread_pool_get': self._handler_pool_get,
                'get_block_fn': get_block_fn,
                'check_block_fn': check_block_fn,
                'ssl_context_fn': ssl_context_fn })], log_function = (lambda handler: pass))
        self._io_loop = tornado.ioloop.IOLoop()
        self._server = tornado.httpserver.HTTPServer(app, ssl_options = routing_context)
        self.port = self._bind_server_to_available_port(self._server, self.FIRST_PORT, self.NUM_PORTS_TO_TRY)
        self.running = False

    
    def run_server(self):
        
        try:
            self._io_loop.make_current()
            self._server.start()
            TRACE('Started P2P server on port %s', self.port)
            self.running = True
            self._io_loop.start()
            TRACE('P2P Server exiting...')
            
            try:
                pass
            except Exception:
                TRACE('P2P server did not start!')
                report_exception(component = DesktopComponent.SEC_NETWORKING)
                
                try:
                    pass
                try:
                    self._server.stop()
                    self._handler_pool_head.shutdown(wait = True)
                    self._handler_pool_get.shutdown(wait = True)
                    self.running = False
                    self._io_loop.close()
                    return None
                except:
                    self._server.stop()
                    self._handler_pool_head.shutdown(wait = True)
                    self._handler_pool_get.shutdown(wait = True)
                    self.running = False
                    self._io_loop.close()




    
    def stop(self):
        
        try:
            self._io_loop.add_callback(self._io_loop.stop)
            return None
        except RuntimeError:
            report_bad_assumption('Called stop twice on P2PServer IOLoop!')
            return None


    _bind_server_to_available_port = (lambda server, start_port, num_tries: for i in range(num_tries):
server.bind(start_port + i)None, start_port + iexcept socket.error:
continueraise P2PStartupError('Could not find an available port'))()
    _make_routing_context = (lambda ssl_context_fn: pass# WARNING: Decompyle incomplete
)()


class P2PServerThread(StoppableThreadWithAccount):
    pass
# WARNING: Decompyle incomplete

