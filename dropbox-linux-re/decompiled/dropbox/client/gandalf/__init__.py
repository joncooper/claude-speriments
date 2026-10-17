# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from apex.context import ApexContext
from dropbox.client.gandalf.base import Gandalf, GandalfFeatureValue
from dropbox.client.gandalf.impl import Gandalf as GandalfImpl

def make_gandalf(apex_context = None):
    return GandalfImpl(apex_context.stormcrow_client)

