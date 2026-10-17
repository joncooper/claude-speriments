# Source Generated with Decompyle++
# File: ultimatesymlinkresolver.pyc (Python 3.11)

import collections
import os
import pprint
import socket
import time
from six import itervalues
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.fastwalk_bridge import fastwalk
from dropbox.fileevents.common import RECURSE_ALL, RECURSE_NONE, RECURSE_ONE
from dropbox.fileutils import absreadlink
from dropbox.functions import desanitize
from dropbox.sync_engine_boundary.file_system_constants import FILE_TYPE_DIRECTORY, FILE_TYPE_POSIX_SYMLINK
from dropbox.trace import TRACE

class UltimateSymlinkResolver(object):
    
    class FileNode(object):
        
        def __init__(self, abspath, inlinks = (None,)):
            self.abspath = abspath
        # WARNING: Decompyle incomplete

        
        def __repr__(self):
            return f'''FileNode({self.abspath!r}, inlinks={self.inlinks!r})'''


    
    class DirNode(object):
        
        def __init__(self, abspath, inlinks, child_symlinks = (None, None)):
            self.abspath = abspath
        # WARNING: Decompyle incomplete

        
        def __repr__(self):
            return f'''DirNode({self.abspath!r}, inlinks={self.inlinks!r}, child_symlinks={self.child_symlinks!r})'''


    
    class SymlinkNode(object):
        
        def __init__(self, abspath, abslink, outlinks, inlinks, parent_directories = (None, None, None)):
            self.abspath = abspath
            self.abslink = abslink
        # WARNING: Decompyle incomplete

        
        def __repr__(self):
            return f'''SymlinkNode({self.abspath!r}, {self.abslink!r}, outlinks={self.outlinks!r}, inlinks={self.inlinks!r}, parent_directories={self.parent_directories!r})'''


    test = (lambda : serv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)oldtimeout = serv.gettimeout()serv.settimeout(0.2)start = time.time()try:
serv.connect('/tmp/.dbfseventsd')serv.settimeout(oldtimeout)except Exception:
if time.time() - start > 1:
raise continue
def realp(x):
print(x)symlink_resolver = UltimateSymlinkResolver(log = realp)symlink_resolver.add_watch('/Applications')print(pprint.pformat(symlink_resolver.nodes.values()))linereader = serv.makefile()(CREATE, RENAME, DELETE, UPDATE, STAT, EXCHANGE) = range(6)line = linereader.readline()if line == '':
Noneline = None[:-1].decode('utf-8')print(line)if line == 'dropped':
continue(event, data) = line.split('\t', 1)if event == 'update':
ev = (UPDATE, desanitize(data))elif event == 'create':
ev = (CREATE, desanitize(data))elif event == 'delete':
ev = (DELETE, desanitize(data))elif event == 'stat':
ev = (STAT, desanitize(data))elif event == 'rename':
(pathfrom, pathto) = data.split('\t', 1)()ev = (RENAME, pathfrom, pathto)elif event == 'exchange':
(pathfrom, pathto) = data.split('\t', 1)()ev = (EXCHANGE, pathfrom, pathto)if ev[0] == CREATE:
symlink_resolver.file_created(ev[1])elif ev[0] == DELETE:
symlink_resolver.file_deleted(ev[1])elif ev[0] == RENAME:
if ev[1] != '':
symlink_resolver.file_deleted(ev[1])if ev[2] != '':
symlink_resolver.file_created(ev[2])print(pprint.pformat(list(symlink_resolver.reverse_resolve_symlinks(ev[1]))))try:
print(pprint.pformat(list(symlink_resolver.reverse_resolve_symlinks(ev[2]))))except Exception:
(lambda .0: [ desanitize(a) for a in .0 ])

        continue
)()
    
    def __init__(self, case_insensitive, debug, log = (True, None, None)):
        self.watchpoints = set()
        self.nodes = dict()
        self.symlink_roots = set()
        self.debug = debug
        self.log = log
        self.case_insensitive = case_insensitive

    
    def add_watch(self, path, recurse = (RECURSE_ALL,)):
        pass
    # WARNING: Decompyle incomplete

    
    def get_watches(self):
        return frozenset(self.watchpoints)

    
    def remove_watch(self, dir):
        pass

    
    def add_node(self, abspath, parent_symlink = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def forward_resolve_symlink(self, symlinkpath):
        node = self.nodes[symlinkpath]
        seen = set()
    # WARNING: Decompyle incomplete

    
    def is_symlink_root(self, dirpath):
        pass
    # WARNING: Decompyle incomplete

    
    def add_children(self, abspath):
        if self.log:
            self.log('IN add_children(%r)' % abspath)
    # WARNING: Decompyle incomplete

    
    def add_symlink(self, abspath, linkpath, parent_symlink, parent_directory = (None, None)):
        if self.log:
            self.log(f'''IN add_symlink({abspath!r}, {linkpath!r}, parent_symlink={parent_symlink!r}, parent_directory={parent_directory!r})''')
    # WARNING: Decompyle incomplete

    
    def add_components(self, node, startat = (0,)):
        if self.log:
            self.log(f'''IN add_components({node.abspath!s}, startat={startat!r})''')
        for i in range(startat, len(node.outlinks)):
            accessat = self.access_at(node, i)
            if not accessat:
                pass
            elif accessat not in self.nodes:
                self.add_node(accessat, parent_symlink = (node.abspath, i))
                continue
            self.nodes[accessat].inlinks.add((i, node.abspath))
            node.outlinks[i] = (node.outlinks[i][0], accessat)
            if type(self.nodes[accessat]) is UltimateSymlinkResolver.DirNode and accessat not in self.symlink_roots and self.is_symlink_root(accessat):
                self.symlink_roots.add(accessat)
                self.add_children(accessat)
            if self.log:
                self.log(f'''OUT add_components({node.abspath!s}, startat={startat!r})''')
                return None
            return None

    
    def access_at(self, node, i):
        pass
    # WARNING: Decompyle incomplete

    
    def is_under_watchpoint(self, path):
        pass
    # WARNING: Decompyle incomplete

    is_watched = is_under_watchpoint
    
    def discard_path(self, path):
        brokenset = set()
        
        try:
            node = self.nodes[path]
        except KeyError:
            tocheck = path + '/'
            for node in itervalues(self.nodes):
                if node.abspath.startswith(tocheck):
                    pass
                

        tocheck = collections.deque()
    # WARNING: Decompyle incomplete

    
    def is_working_symlink(self, symlinkpath):
        pass
    # WARNING: Decompyle incomplete

    
    def restore_link(self, path):
        pass
    # WARNING: Decompyle incomplete

    
    def file_deleted(self, path):
        if self.case_insensitive:
            path = path.lower()
        ret = self.discard_path(path)
        if self.debug:
            self.debug(pprint.pformat(self.nodes.values()))
        return ret

    
    def file_created(self, path):
        pass
    # WARNING: Decompyle incomplete

    
    def reverse_resolve_symlinks(self, path):
        pass
    # WARNING: Decompyle incomplete


