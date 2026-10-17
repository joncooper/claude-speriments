# Source Generated with Decompyle++
# File: dbxlog.pyc (Python 3.11)

import enum
from typing import Any, Callable, Dict, List, Text
from apex._apex import ffi, lib

class InvalidLoggerIdException(Exception):
    pass


class Level(enum.Enum):
    INFO = lib.INFO
    WARN = lib.WARN
    CRITICAL = lib.CRITICAL


class Logger:
    
    def __init__(self = None, inner = None):
        self.inner = inner

    
    def stats(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def drain(self = None):
        return lib.dbxlog_drain(self.inner)

    
    def log(self, level, threadname, filename = None, line = None, msg = None, kvs = ('level', 'Level', 'threadname', 'Text', 'filename', 'Text', 'line', 'int', 'msg', 'Text', 'kvs', 'Dict[Text, Text]', 'return', 'None')):
        c_threadname = ffi.new('char[]', threadname.encode('utf-8'))
        c_filename = ffi.new('char[]', filename.encode('utf-8'))
        c_msg = ffi.new('char[]', msg.encode('utf-8'))
        kv_items = list(kvs.items())
        _c_keys_keepalive = kv_items()
        c_keys = ffi.new('char *[]', _c_keys_keepalive)
        _c_values_keepalive = kv_items()
        c_values = ffi.new('char *[]', _c_values_keepalive)
        c_record = ffi.new('Record *', {
            'threadname': c_threadname,
            'file': c_filename,
            'line': line,
            'level': level.value,
            'msg': c_msg,
            'num_kvs': len(kv_items),
            'keys': c_keys,
            'values': c_values })
        return lib.dbxlog_log(self.inner, c_record[0])

    
    def add_redacted_value(self = None, redacted_value = None, placeholder = None):
        lib.dbxlog_add_redacted_value(ffi.new('char[]', redacted_value.encode('utf-8')), ffi.new('char[]', placeholder.encode('utf-8')))



def _get_stats(stats_fn = None):
    out = ffi.new('Stat **')
    out_len = ffi.new('uintptr_t *')
    stats_fn(out, out_len)
    
    try:
        ret = []
        for i in range(out_len[0]):
            stat = out[0][i]
            cur_stat_dict = { }
            for field_name, _ in ffi.typeof(stat).fields:
                val = getattr(stat, field_name)
                if val >= 0:
                    cur_stat_dict[field_name] = val
                ret.append(cur_stat_dict)
                lib.dbxlog_free_stats(out[0], out_len[0])
            lib.dbxlog_free_stats(out[0], out_len[0])
            return ret


