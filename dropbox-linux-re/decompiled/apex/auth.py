# Source Generated with Decompyle++
# File: auth.pyc (Python 3.11)

import dataclasses
import itertools
from concurrent.futures import Future, InvalidStateError
from typing import Dict, Iterator, Optional
from apex._apex import ffi, lib
from apex.lifecycle import raise_if_shutdown
_RETRIEVE_TOKEN_ID: 'Iterator[int]' = itertools.count(1)
_RETRIEVE_TOKEN_CONTEXTS: 'Dict[int, Future[Optional[str]]]' = { }
retrieve_token_callback = (lambda context = None, c_value = None: future = _RETRIEVE_TOKEN_CONTEXTS.pop(int(ffi.cast('unsigned long', context)))value = ffi.string(c_value).decode('utf-8') if c_value != ffi.NULL else Nonetry:
future.set_result(value)Noneexcept InvalidStateError:
None)()
OAuthClient = <NODE:12>()
