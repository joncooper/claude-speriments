# Source Generated with Decompyle++
# File: ts_sink.pyc (Python 3.11)

from typing import List
from apex.metrics.metrics import MetricsReporterImpl, Span
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.metrics.amp.bridge_gen.amp_span import AmpSpan
from dropbox.foundation.metrics.amp.bridge_gen.bridge_interface_amp_sink import AmpSinkBridgeInterface

class SamplesSink(AmpSinkBridgeInterface):
    
    def __init__(self = None, inner = None):
        self.inner = inner

    
    def report(self = None, data = None):
        (lambda .0: [ _amp_span_to_span(s) for s in .0 ])(data())
        return ResolvedFuture(None)



def _amp_span_to_span(amp_span = None):
    return Span(amp_span.ns, amp_span.metric_name, amp_span.tags, amp_span.samples)

