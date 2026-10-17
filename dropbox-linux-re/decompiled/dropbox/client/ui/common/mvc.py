# Source Generated with Decompyle++
# File: mvc.pyc (Python 3.11)

from __future__ import absolute_import
from weakref import ref, WeakKeyDictionary
from six import iteritems
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception

class ObservableProperty(object):
    
    def __init__(self, default = (None,)):
        self._default = default
        self._values = WeakKeyDictionary()
        self._callbacks = WeakKeyDictionary()

    
    def bind(self, obj, handler):
        if obj not in self._callbacks:
            self._callbacks[obj] = set()
        self._callbacks[obj].add(handler)

    
    def unbind(self, obj, handler):
        self._callbacks.get(obj, set()).remove(handler)

    
    def unbind_all(self, obj):
        callbacks = self._callbacks.get(obj)
        if not callbacks:
            return None
        None.clear()

    
    def _convert(self, obj, value):
        return value

    
    def _dispatch(self, obj):
        for handler in self._callbacks.get(obj, ()):
            handler()
            except Exception:
                report_exception(component = DesktopComponent.UNKNOWN)
                continue
            return None

    
    def __get__(self, obj, obj_type):
        pass
    # WARNING: Decompyle incomplete

    
    def __set__(self, obj, value):
        current_value = self._values.get(obj, self._default)
        converted_value = self._convert(obj, value)
        if converted_value == current_value:
            return None
        self._values[obj] = None
        self._dispatch(obj)



class ObservableModel(object):
    __observable_properties__ = None
    
    def bind(self, **kwargs):
        for name, handler in iteritems(kwargs):
            prop = getattr(self.__class__, name, None)
            if not isinstance(prop, ObservableProperty):
                raise KeyError('Property %r is not observable' % name)
            prop.bind(self, handler)
            return None

    
    def unbind(self, **kwargs):
        for name, handler in iteritems(kwargs):
            prop = getattr(self.__class__, name, None)
            if not isinstance(prop, ObservableProperty):
                raise KeyError('Property %r is not observable' % name)
            prop.unbind(self, handler)
            return None

    
    def clear_bindings(self):
        observable_properties = self.__observable_properties__
    # WARNING: Decompyle incomplete



class ObservableListProperty(ObservableProperty):
    pass
# WARNING: Decompyle incomplete


class _ObservableList(list):
    pass
# WARNING: Decompyle incomplete


class ObservableSetProperty(ObservableProperty):
    pass
# WARNING: Decompyle incomplete


class _ObservableSet(set):
    pass
# WARNING: Decompyle incomplete


class ObservableDictProperty(ObservableProperty):
    pass
# WARNING: Decompyle incomplete


class _ObservableDict(dict):
    pass
# WARNING: Decompyle incomplete

