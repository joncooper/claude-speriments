# Source Generated with Decompyle++
# File: dbxconn.pyc (Python 3.11)

from apex._apex import ffi, lib
from apex.context import ApexContext
from dropbox.proto.apex.dbxconn_pb2 import Config

class Connection:
    
    def __init__(self = None, context = None):
        self.inner = context.inner

    
    def reconfigure(self = None, config = None):
        serialized = config.SerializeToString()
        c_config = ffi.new('char[]', serialized)
        lib.dbxconn_reconfigure(self.inner, c_config, len(serialized))

    
    def reconnect(self = None):
        lib.dbxconn_reconnect(self.inner)

    
    def set_advisory_is_connected(self = None, connected = None):
        lib.dbxconn_set_advisory_is_connected(self.inner, connected)


