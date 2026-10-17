# Source Generated with Decompyle++
# File: html.pyc (Python 3.11)

from __future__ import absolute_import
from six import unichr
from six.moves.html_entities import name2codepoint
from six.moves.html_parser import HTMLParser

class HTMLTextConverter(HTMLParser):
    convert = (lambda cls, html: parser = cls()parser.feed(html)''.join(parser.text))()
    
    def __init__(self):
        self.text = []
        HTMLParser.__init__(self)

    
    def handle_charref(self, name):
        if name.startswith('x') or name.startswith('X'):
            self.text.append(unichr(int(name[1:], 16)))
            return None
        None.text.append(unichr(int(name)))

    
    def handle_entityref(self, name):
        self.text.append(unichr(name2codepoint[name]))

    
    def handle_data(self, data):
        self.text.append(data)


# WARNING: Decompyle incomplete
