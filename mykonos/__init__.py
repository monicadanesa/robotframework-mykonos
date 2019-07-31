import os
from mykonos.locator import LocatorElement, WatcherElement
from mykonos.keywords import ManagementDevice, GlobalElement, KeyEvent, Touch, Click, GetConditions, ExpectedConditions, Wait, Decorators
from mykonos.keywords import Parallel

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
    Wait,
    Decorators,
    Parallel
):

    def __init__(self):
        for base in mykonos.__bases__:
            base.__init__(self)
