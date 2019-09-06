import os
from mykonos.keywords import Parallel
from mykonos.locator import LocatorElement, WatcherElement
from mykonos.keywords import ManagementDevice, GlobalElement, KeyEvent, Touch, Click, GetConditions, ExpectedConditions, Wait, Decorators
from mykonos.keywords.logging import LoggingKeywords

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
    Parallel,
    LoggingKeywords
):

    def __init__(self):
        for base in mykonos.__bases__:
            base.__init__(self)
