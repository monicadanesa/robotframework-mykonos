import os
from mykonos.keywords import ManagementDevice, GlobalElement,
KeyEvent, Touch, WatcherElement, Click, GetCondions, ExpectedConditions
from mykonos.locator import LocatorElement, WatcherElement


class mykonos(
    ManagementDevice,
    LocatorElement,
    GlobalElement,
    KeyEvent,
    Touch,
    WatcherElement,
    Click,
    GetCondions,
    ExpectedConditions
):

    def __init__(self):
        for base in mykonos.__bases__:
            base.__init__(self)
