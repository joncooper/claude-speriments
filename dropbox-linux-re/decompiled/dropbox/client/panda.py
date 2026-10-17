# Source Generated with Decompyle++
# File: panda.pyc (Python 3.11)

from __future__ import absolute_import, print_function
import base64
import zlib
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception, Severity
from dropbox.trace import TRACE

def panda():
    
    try:
        data = b'\neJyllr1qAzEMx3c/hbnlKJiOxXmEW4qnQpY733EZCmkLhUIfv/62JMuXtNWQIbF+kv6xJAshD21R\n677rbVWH59Sus22HJ+u5cPYoqg+6HLAwSuuHf2U2EZqWSzYAw9k3uOKy2DOmmaHatq6usoXQtMbp\nOQWg0wmi5ib9eRhIRK0nAWAaOQVVzOA/WhakAqgZM8/RkFfUeDwAAeSZ4lbsGmHmPpoMf5wZZpFd\nod+uf4eScoh3hAfdWWEyG1Ad0vQbUmbt2C9fH5QVuq4HMKXZvDTA76lpsPdCIgTajjxLZjXb0oQI\nF0Ogr+wmFM6jdGahgcYHepRugkPF9dREcPQYHCNjewzxXEv5408MLoeoDYPuHeijUq5yE4RGmEjU\nMkdwm4LxAmVR4kyAtpaR4lo/TZqmt7UtgS6TsFQDoBa9GgywTpcos8hCZCCZqG4uVgQZvxaknae6\nKILFZOhIhcx6B0mqftckLQURrNkKMFicjiZn5XN9rKzEw4JZ3bGk5TBE1kqXW7QR89xNPLHnAjHs\n0FC+4mlePtn5hcvQhovTYzXV3gS6NdiHxWKbnfZnM6L7b/Y8ZrCtiPnc6Ir3Ln1abKuZ+yns6ZYm\nu5clzxrml7RVG5rs0xTTiJDVwLY+LA4jRufydiDPlD6rhxrrqwaxjOyhNtz+DCg0c7KZrTmaYlQ3\nI/OqfP74fFvf95Akl5EHoQhmZigvl9fr9fL13Utog9/nR9CRtW9EE6sNhd909wfPSHOudtaKvKMQ\nP3D9VuY='
        TRACE('!! This is an internal alpha build!')
        companda = base64.b64decode(data)
        TRACE('%s', zlib.decompress(companda).decode('utf-8'))
        return None
    except Exception:
        report_exception(component = DesktopComponent.UNKNOWN)
        return None



def sloth():
    
    try:
        data = '\n=====(((=))=====(=)))===========\n      " `,      |\' /\n      /"/        |""\n     """|        \\"|\n     |"||        " "\n     "" "        |"|\\\n    /""~\\\\.      /" ""~,\n   ""~""""`"",~`~"!!"!" \\\n   /"""""/""! "~""" "" "~",\n  //\\""!!""~"!"!"\\"""/~!~, C~"~P\n // !!"""""! "~ " !!"!! "," O o"~\n ||   !!"!!~!!~||"  !     "" Y ""\n \\\\     !  !  !            `"U"\'\n  \\\\\n   \\\\  0))\n    \\`-~/~\n     `~\'\n        '.strip('\n')
        TRACE('!! This is an external alpha build!')
        TRACE('%s', data)
        return None
    except Exception:
        report_exception(severity = Severity.DEBUG, component = DesktopComponent.UNKNOWN)
        return None


