import os
from mykonos.locator import LocatorElement, WatcherElement
from mykonos.keywords import ManagementDevice, GlobalElement, KeyEvent, Touch, Click, GetConditions, ExpectedConditions, Wait


class mykonos(
    ManagementDevice,
    LocatorElement,
    GlobalElement,
    KeyEvent,
    Touch,
    WatcherElement,
    Click,
    GetConditions,
    ExpectedConditions,
    Wait
):

    def __init__(self):
        for base in mykonos.__bases__:
            base.__init__(self)
