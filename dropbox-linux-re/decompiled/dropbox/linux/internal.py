# Source Generated with Decompyle++
# File: internal.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import os
import subprocess
import sys
import tempfile
from typing import Iterable, List, Text, Union
from build_number import BUILD_KEY, is_frozen
from dropbox.functions import make_bytes
from dropbox.trace import TRACE

def executable(opts = None):
    if is_frozen():
        install_dir = os.path.dirname(sys.executable)
        script_path = os.path.join(install_dir, '%sd' % BUILD_KEY.lower())
        return [
            script_path] + list(opts)
    return [
        None.executable] + list(opts)


def _run_program(cmd = None):
    proc = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
    (stdout, stderr) = proc.communicate()
    if proc.returncode != 0:
        TRACE('command line was %r', cmd)
        TRACE('stdout: %s', stdout)
        TRACE('stderr: %s', stderr)
        raise Exception('Failed to run command (%r)' % proc.returncode)
    return proc.returncode


def run_as_root(cmds = None, desc = None):
    cmd_list = cmds()
    programs = ([
        b'pkexec'], [
        b'gksu',
        b'-m',
        make_bytes(desc),
        b'--'], [
        b'kdesu',
        b'-c'], [
        b'beesu'])
    for p in programs:
        
        return (lambda .0: [ make_bytes(cmd) for cmd in .0 ]), _run_program(p + cmd_list)
        except OSError:
            if e.errno == errno.ENOENT:
                None = None
                del e
                continue
            raise 
            e = None
            del e
        tmp = tempfile.NamedTemporaryFile()
        script = b'#!/bin/bash\nsudo -K\nzenity --entry --title="Dropbox" --text="%s" --entry-text "" --hide-text | sudo -S %s\nif [ "$?" != 0 ]; then\nzenity --error --text="Sorry, wrong password"\nexit 1\nfi\n\n# End' % (make_bytes(desc), b' '.join(cmd_list))
        tmp.write(script)
        tmp.flush()
        None(None, None)
        return 
        with None:
            if not None, _run_program([
                b'bash',
                make_bytes(tmp.name)]):
                pass

