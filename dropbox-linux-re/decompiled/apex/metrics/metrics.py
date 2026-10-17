# Source Generated with Decompyle++
# File: metrics.pyc (Python 3.11)

import datetime as dt
from dataclasses import dataclass
from typing import List, Mapping, NamedTuple, Sequence
from apex._apex import ffi, lib
from  import Counter, Metric, MetricsReporter, Set, Stats, Timer

class StatsImpl(Stats):
    
    def __init__(self = None, inner = None):
        self._inner = inner

    
    def __del__(self = None):
        lib.metrics_stats_destroy(self._inner)

    
    def record(self = None, value = None):
        lib.metrics_stats_record(self._inner, value)

    
    def record_duration(self = None, value = None):
        lib.metrics_stats_record(self._inner, value.total_seconds() * 1000)



class TimerImpl(Timer):
    
    def __init__(self = None, inner = None):
        self._inner = inner

    
    def __del__(self = None):
        lib.metrics_timer_destroy(self._inner)

    
    def reset(self = None):
        lib.metrics_timer_reset(self._inner)

    
    def record(self = None):
        lib.metrics_timer_record(self._inner)



class CounterImpl(Counter):
    
    def __init__(self = None, inner = None):
        self._inner = inner

    
    def __del__(self = None):
        lib.metrics_counter_destroy(self._inner)

    
    def reset(self = None):
        lib.metrics_counter_reset(self._inner)

    
    def increment(self = None, value = None):
        lib.metrics_counter_increment_by(self._inner, value)

    
    def decrement(self = None, value = None):
        lib.metrics_counter_decrement_by(self._inner, value)

    
    def record(self = None):
        lib.metrics_counter_record(self._inner)



class SetImpl(Set):
    
    def __init__(self = None, inner = None):
        self._inner = inner

    
    def __del__(self = None):
        lib.metrics_set_destroy(self._inner)

    
    def observe(self = None, value = None):
        buf = value.encode('utf-8')
        c_bytes = ffi.new('char[]', buf)
        lib.metrics_set_observe(self._inner, c_bytes)


Span = <NODE:12>()
MetricsReporterInner = NamedTuple('MetricsReporterInner', [
    ('data', ffi.CData)])

class MetricsReporterImpl(MetricsReporter):
    
    def __init__(self = None, inner = None):
        self.inner = inner

    
    def raw_ptr(self = None):
        return int(ffi.cast('uintptr_t', self.inner.data))

    root = (lambda ctx = None: MetricsReporterImpl(MetricsReporterInner(lib.metrics_reporter_create_root(ctx))))()
    
    def child(self = None, tags = None):
        c_tag_keys_list = tags.keys()()
        c_tag_keys = ffi.new('char *[]', c_tag_keys_list)
        c_tag_vals_list = tags.values()()
        c_tag_vals = ffi.new('char *[]', c_tag_vals_list)
        return MetricsReporterImpl(MetricsReporterInner(lib.metrics_reporter_create_child(self.inner.data, len(tags), c_tag_keys, c_tag_vals)))

    
    def __del__(self = None):
        lib.metrics_reporter_destroy(self.inner.data)

    
    def create_stats(self = None, metric = None, tags = None):
        c_ns = ffi.new('char[]', metric.ns.encode('utf-8'))
        c_name = ffi.new('char[]', metric.name.encode('utf-8'))
        c_tag_keys_list = tags.keys()()
        c_tag_keys = ffi.new('char *[]', c_tag_keys_list)
        c_tag_vals_list = tags.values()()
        c_tag_vals = ffi.new('char *[]', c_tag_vals_list)
        return StatsImpl(lib.metrics_reporter_create_stats(self.inner.data, c_ns, c_name, len(tags), c_tag_keys, c_tag_vals))

    
    def create_counter(self = None, metric = None, tags = None):
        c_ns = ffi.new('char[]', metric.ns.encode('utf-8'))
        c_name = ffi.new('char[]', metric.name.encode('utf-8'))
        c_tag_keys_list = tags.keys()()
        c_tag_keys = ffi.new('char *[]', c_tag_keys_list)
        c_tag_vals_list = tags.values()()
        c_tag_vals = ffi.new('char *[]', c_tag_vals_list)
        return CounterImpl(lib.metrics_reporter_create_counter(self.inner.data, c_ns, c_name, len(tags), c_tag_keys, c_tag_vals))

    
    def create_timer(self = None, metric = None, tags = None):
        c_ns = ffi.new('char[]', metric.ns.encode('utf-8'))
        c_name = ffi.new('char[]', metric.name.encode('utf-8'))
        c_tag_keys_list = tags.keys()()
        c_tag_keys = ffi.new('char *[]', c_tag_keys_list)
        c_tag_vals_list = tags.values()()
        c_tag_vals = ffi.new('char *[]', c_tag_vals_list)
        return TimerImpl(lib.metrics_reporter_create_timer(self.inner.data, c_ns, c_name, len(tags), c_tag_keys, c_tag_vals))

    
    def create_set(self = None, metric = None, tags = None):
        c_ns = ffi.new('char[]', metric.ns.encode('utf-8'))
        c_name = ffi.new('char[]', metric.name.encode('utf-8'))
        c_tag_keys_list = tags.keys()()
        c_tag_keys = ffi.new('char *[]', c_tag_keys_list)
        c_tag_vals_list = tags.values()()
        c_tag_vals = ffi.new('char *[]', c_tag_vals_list)
        return SetImpl(lib.metrics_reporter_create_set(self.inner.data, c_ns, c_name, len(tags), c_tag_keys, c_tag_vals))

    
    def submit_spans(self = None, spans = None):
        cffi_keepalive = []
        c_spans_arr = []
        for span in spans:
            c_namespace = ffi.new('char[]', span.namespace.encode('utf-8'))
            c_name = ffi.new('char[]', span.name.encode('utf-8'))
            tag_items = list(span.tags.items())
            c_tag_names_arr = tag_items()
            c_tag_names = ffi.new('char *[]', c_tag_names_arr)
            c_tag_values_arr = tag_items()
            c_tag_values = ffi.new('char *[]', c_tag_values_arr)
            samples = list(span.samples)
            c_sample_values = ffi.new('double[]', samples)
            c_spans_arr.append(ffi.new('Span *', {
                'ns': c_namespace,
                'name': c_name,
                'num_tags': len(tag_items),
                'tag_names': c_tag_names,
                'tag_values': c_tag_values,
                'num_samples': len(samples),
                'sample_values': c_sample_values }))
            cffi_keepalive += [
                c_namespace,
                c_name,
                c_tag_names,
                c_tag_names_arr,
                c_tag_values,
                c_tag_values_arr,
                c_sample_values]
            
            def <listcomp>(.0):
                return [ val[0] for val in .0 ]

            c_spans = 'Span[]'(<listcomp>, c_spans_arr())
            lib.metrics_reporter_submit_spans(self.inner.data, c_spans, len(spans))
            return None


