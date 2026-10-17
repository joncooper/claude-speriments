# Source Generated with Decompyle++
# File: sysctl.pyc (Python 3.11)

from __future__ import absolute_import
import subprocess
from typing import Optional, Dict, IO, List, Text, Union
from dropbox.functions import make_str

class ImmutableLine(object):
    
    def __init__(self = None, line = None):
        self.line = line

    
    def __repr__(self = None):
        return 'ImmutableLine(%s)' % self.line

    
    def __str__(self = None):
        return self.line



class KeyValueLine(object):
    
    def __init__(self = None, line = None):
        self.orig_line = line
        (key, value) = line.strip().split('=', 1)()
        self.line = line
        self.key = key
        self.value = value
        self.value_index = line.rfind(value)

    
    def set_value(self = None, value = None):
        self.value = str(value)
        self.line = self.orig_line[:self.value_index] + str(value)

    
    def __repr__(self = None):
        return f'''KeyValueLine({self.line!s}, {self.key!s} = {self.value!s})'''

    
    def __str__(self = None):
        return self.line



class SysctlParser(object):
    
    def __init__(self = None, name = None):
        self.lines = []
        self.variables = { }
        if name:
            self.load(name)
            return None

    
    def _add_kv_line(self = None, line = None):
        kv_line = KeyValueLine(line)
        self.lines.append(kv_line)
        self.variables[kv_line.key] = kv_line

    
    def load(self = None, name = None):
        file_obj = open(name, 'rb')
        for b_line in file_obj:
            line = make_str(b_line).rstrip('\n')
            stripped_line = line.strip()
            if stripped_line or stripped_line[0] in set([
                '#',
                ';']):
                self.lines.append(ImmutableLine(line))
                continue
            if '=' in line:
                self._add_kv_line(line)
                continue
            self.lines.append(ImmutableLine(line))
            None(None, None)
        with None:
            if not None:
                pass
        return self

    
    def add_immutable_line(self = None, line = None):
        self.lines.append(ImmutableLine(line))

    
    def set(self = None, key = None, value = None):
        if key in self.variables:
            self.variables[key].set_value(value)
            return None
        None._add_kv_line(f'''{key!s} = {value!s}''')

    
    def get(self = None, key = None):
        return self.variables[key].value

    
    def __str__(self = None):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.lines()) + '\n'



def get_sysctl_values(*args):
    cmd = [
        '/sbin/sysctl',
        '-n'] + list(args)
    output = subprocess.check_output(cmd)
    ret = output.strip().split(b'\n')
    return ret

