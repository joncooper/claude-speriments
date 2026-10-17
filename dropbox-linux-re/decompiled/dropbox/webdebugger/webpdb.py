# Source Generated with Decompyle++
# File: webpdb.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import threading
from pdb import Pdb
import tornado.websocket as tornado
from six.moves.queue import Queue
from dropbox.db_thread import db_thread

class WebPdbHandler(tornado.websocket.WebSocketHandler):
    
    def open(self, *args):
        self.wpdb = db_thread(WebPdb)(self)
        self.wpdb.start()

    
    def on_message(self, message):
        self.wpdb.command(message)

    
    def on_close(self):
        self.wpdb.stop()



class WebPdbStream(object):
    
    def __init__(self, websocket):
        self._queue = Queue()
        self.websocket = websocket

    
    def write(self, data):
        self.websocket.write_message(data)

    
    def writelines(self, lines):
        self.write(''.join(lines))

    
    def put(self, msg):
        self._queue.put(msg)

    
    def read(self):
        return self._queue.get()

    
    def readline(self):
        return self._queue.get()

    
    def readlines(self):
        pass
    # WARNING: Decompyle incomplete

    
    def flush(self):
        pass

    
    def close(self):
        self.websocket.close()



class WebPdb(threading.Thread):
    pass
# WARNING: Decompyle incomplete

