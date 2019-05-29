import os
from mykonos.keywords import ManagementDevice, Element, KeyEvent, Touch, Click, Get
from mykonos.locator import LocatorElement, WatcherElement
from mykonos.version import VERSION

__version__ = VERSION


class mykonos(
    ManagementDevice,
    LocatorElement,
    Element,
    KeyEvent,
    Touch,
    WatcherElement,
    Click,
    Get
):

    def __init__(self):
        for base in mykonos.__bases__:
            base.__init__(self)
