# Source Generated with Decompyle++
# File: upload_network_interface.pyc (Python 3.11)

import time
from abc import abstractmethod
from typing import Any, Dict, List, NamedTuple, Optional, Text
from dropbox.client.features.transfer.constants import FileTransfersApiErrorBase, FileTransfersApiServerError
from dropbox.client.features.transfer.logger import AnalyticsEventType, AnalyticsLoggingFields
from dropbox.client.features.transfer.network_utils import make_api_request
from dropbox.exception import ExcInfo
from dropbox.foundation.futures import FailedFuture, ResolvedFuture
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from typing import Callable
    from dropbox.client.features.transfer.network_utils import FileTransfersApiResponse
    from dropbox.foundation.futures import Future
FileById = NamedTuple('FileById', [
    ('file_id', Text),
    ('destination_path', Text)])
FileByBlocks = NamedTuple('FileByBlocks', [
    ('tokens', List[Text]),
    ('destination_path', Text),
    ('local_identifier', Text)])
FileResult = NamedTuple('FileResult', [
    ('file_id', Text),
    ('original_file_id', Text),
    ('failed', bool),
    ('error_type', Optional[Text])])

class UploadNetworkInterface:
    commit_files_by_id = (lambda self = None, files_to_add = None: pass)()
    commit_files_by_blocks = (lambda self = None, files_to_add = None: pass)()
    upload_block = (lambda self = None, block_bytes = None, on_progress = abstractmethod: pass)()
    files_remove = (lambda self = None, relative_path = None: pass)()


class FileTransfersContentUploadNetworkInterface(UploadNetworkInterface):
    
    def __init__(self = None, context = None, logger = None):
        self._context = context
        self._logger = logger
        self._transfer_id = None

    
    def register_transfer(self = None, transfer_id = None):
        self._transfer_id = transfer_id

    
    def commit_files_by_id(self = None, files_to_add = None):
        pass
    # WARNING: Decompyle incomplete

    
    def commit_files_by_blocks(self = None, files_to_add = None):
        pass
    # WARNING: Decompyle incomplete

    
    def upload_block(self = None, block_bytes = None, on_progress = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_error_type(self = None, error = None):
        error_type = 'unknown'
    # WARNING: Decompyle incomplete

    
    def files_remove(self = None, relative_path = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _handle_upload_block_response(self = None, res = None):
        
        try:
            return ResolvedFuture(res['token'])
        except Exception:
            TRACE('[FileTransfers] upload block unexpected response: no token returned')
            return 


    
    def _handle_commit_files_response(self = None, res = None):
        
        try:
            file_results = res['added_file_results']
            parsed_results = []
            for file_result in file_results:
                success = file_result['add_file_result']['.tag'] == 'file'
                if success:
                    parsed_results.append(FileResult(failed = False, original_file_id = file_result['original_file_identifier'], file_id = file_result['add_file_result']['transfer_file_id'], error_type = None))
                    continue
                error_type_res = file_result['add_file_result'].get('error_type')
                error_type = error_type_res.get('.tag') if error_type_res else None
                parsed_results.append(FileResult(failed = True, original_file_id = file_result['original_file_identifier'], file_id = file_result['original_file_identifier'], error_type = error_type))
        except Exception:
            TRACE('[FileTransfers] commit files response could not be parsed')
            return 
            return ResolvedFuture(parsed_results)


    
    def _handle_files_remove_response(self = None, res = None):
        
        try:
            removed_results = res['removed_file_results']
            if (lambda .0: pass# WARNING: Decompyle incomplete
)(removed_results()):
                raise FileTransfersApiServerError('Removal of file failed', res, None)
        except Exception:
            TRACE('[FileTransfers] removal of file failed')
            return 

        return ResolvedFuture(None)


