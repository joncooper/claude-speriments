# Source Generated with Decompyle++
# File: deals_service_types.pyc (Python 3.11)


class NotificationButtonInfo:
    
    def text: 'str'(self, typed_dict):
        for key in typed_dict:
            setattr(self, key, typed_dict[key])
            return None



class NotificationInfo:
    
    def intervalInMinutes: 'int'(self, typed_dict):
        self.buttonInfo = None
        for key in typed_dict:
            if key == 'buttonInfo':
                setattr(self, key, NotificationButtonInfo(typed_dict[key]))
                continue
            setattr(self, key, typed_dict[key])
            return None


