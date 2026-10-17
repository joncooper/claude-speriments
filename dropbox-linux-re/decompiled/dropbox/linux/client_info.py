# Source Generated with Decompyle++
# File: client_info.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import uuid
from typing import Optional

class MissingMachineID(Exception):
    pass

_GET_MACHINE_ID_VAL: 'Optional[uuid.UUID]' = None

def get_machine_id():
    global _GET_MACHINE_ID_VAL
    if _GET_MACHINE_ID_VAL:
        return _GET_MACHINE_ID_VAL
    machine_id_val = None
    
    try:
        f = open('/etc/machine-id', 'r')
        machine_id_val = f.read().strip()
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        pass
                    except FileNotFoundError:
                        pass

                    if not machine_id_val:
                        
                        try:
                            f = open('/var/lib/dbus/machine-id', 'r')
                            machine_id_val = f.read().strip()
                            
                            try:
                                None(None, None)
                            with None:
                                if not None:
                                    
                                    try:
                                        
                                        try:
                                            pass
                                        except (FileNotFoundError, IOError):
                                            e = None
                                            raise MissingMachineID('Could not read machine-id'), e
                                            e = None
                                            del e

                                        if not machine_id_val:
                                            raise MissingMachineID('machine-id is empty')
                                        
                                        try:
                                            _GET_MACHINE_ID_VAL = uuid.UUID(machine_id_val)
                                        except ValueError:
                                            e = None
                                            raise MissingMachineID('Could not convert machine-id to UUID'), e
                                            e = None
                                            del e

                                        return _GET_MACHINE_ID_VAL







