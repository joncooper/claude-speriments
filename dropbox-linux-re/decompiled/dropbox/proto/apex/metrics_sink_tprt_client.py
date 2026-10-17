# Source Generated with Decompyle++
# File: metrics_sink_tprt_client.pyc (Python 3.11)

from concurrent.futures import futures
import typing
import tprt
from google.protobuf.service import RpcController
from dropbox.proto.apex import metrics_sink_pb2 as dropbox__dot__proto__dot__apex__dot__metrics_sink_pb2

class MetricsSinkClient:
    
    def __init__(self = None, raw_client = None):
        self._raw_client = raw_client

    
    def SubmitSpans(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__apex__dot__metrics_sink_pb2.MetricsSinkRequest', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__apex__dot__metrics_sink_pb2.MetricsSinkResponse], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__apex__dot__metrics_sink_pb2.MetricsSinkResponse]')):
        pass
    # WARNING: Decompyle incomplete



def _parse_and_complete(bytes_future, typed_future, output_type):
    pass
# WARNING: Decompyle incomplete


def _parse_response(future, output_type):
    pass
# WARNING: Decompyle incomplete


def _parse_stream_response(output, output_type):
    response = output_type()
    response.ParseFromString(output)
    return response


class StreamingQueue:
    
    def __init__(self, tprt_queue, message_type):
        self.tprt_queue = tprt_queue
        self.message_type = message_type

    
    def get(self):
        item = self.tprt_queue.get()
    # WARNING: Decompyle incomplete

    
    def stop(self):
        self.tprt_queue.stop()

    
    def size(self):
        return self.tprt_queue.qsize()

    
    def connection_reset(self):
        self.tprt_queue.connection_reset()


