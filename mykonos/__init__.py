import os
from mykonos.locator import LocatorElement, WatcherElement
from mykonos.keywords import ManagementDevice, GlobalElement, KeyEvent, Touch, Click, GetConditions, ExpectedConditions, Wait, Decorators
from mykonos.keywords import Parallel
from mykonos.keywords.runonfailure import RunOnFailureKeywords

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
    RunOnFailureKeywords
):

    def __init__(self, run_on_failure="Capture Screen"):
        for base in mykonos.__bases__:
            base.__init__(self)
            self.register_keyword_to_run_on_failure(run_on_failure)
