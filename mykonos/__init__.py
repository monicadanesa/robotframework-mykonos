import os
from mykonos.keywords import *
from mykonos.locator import LocatorElement
from mykonos.version import VERSION

__version__ = VERSION

class mykonos(
    ManagementDevice,
    LocatorElement,
    Element,
    KeyEvent,
    Touch,
):

    def __init__(self):
        for base in mykonos.__bases__:
            base.__init__(self)
