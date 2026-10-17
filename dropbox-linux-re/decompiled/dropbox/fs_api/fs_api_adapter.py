# Source Generated with Decompyle++
# File: fs_api_adapter.pyc (Python 3.11)

from concurrent.futures import Future
from typing import Callable, cast, Optional, Type
import tprt
from apex.context import ApexContext
from apex.panic import is_panicking
from cffi_transport.cffi_interface import CFFIInterface
from cffi_transport.exceptions import ServiceError, ServiceNotAvailableException
from fs_api_python import FsApiServer
from google.protobuf.descriptor import MethodDescriptor
from google.protobuf.message import Message
from google.protobuf.service import RpcChannel, RpcController
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.exception.exceptions import FsApiPanicException
from dropbox.proto.fs_api.fs_api_service_pb2 import FsApi_Stub, FsApiCreateArgs
from dropbox.proto.fs_api.fs_api_service_tprt_client import FsApiClient
from dropbox.trace import TRACE

class FsApiAdapter(FsApi_Stub):
    pass
# WARNING: Decompyle incomplete


class _FsApiTransportChannel(RpcChannel):
    pass
# WARNING: Decompyle incomplete

