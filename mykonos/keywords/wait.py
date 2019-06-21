from mykonos.core.core import Core
from mykonos.keywords.element import GetConditions


class Wait(Core):

    def __init__(self):
        self.device_mobile = self.device()
        self.get_conditions = GetConditions()

    def wait_until_element_is_exists(self, time=1000, *argument, **settings):
        """This keyword is used to wait until spesific element is exists.

    **Example:**

    || Wait Until Element Is Exists | className= sample class
        """

        if 'locator' in settings:
            locator = settings['locator']

            if locator.wait.exists(timeout=time):
                return True
            else:
                return False
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).wait.exists(timeout=time)
            else:
                return self.device_mobile(*argument, **settings).wait.exists(timeout=time)

    def wait_until_page_contains(self, time=1000, *argument, **settings):
        """This keyword is used to wait until page is contain spesific element.

        **Example:**

        || Wait Until Page Contains | className=sample class
        """
        element = self.get_conditions.get_element(*argument, **settings)
            locator = settings['locator']
            if locator[element].wait.exists(timeout=time):
                return True
            else:
                return False
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).wait.exists(timeout=time)
            else:
                return self.device_mobile(*argument, **settings).wait.exists(timeout=time)

    def wait_until_page_does_not_contains(self, time=1000, *argument, **settings):
        """This keyword is used to wait until page is not contain spesific element.

        **Example:**

        || Wait Until Page Does Not Contains| className=sample class
        """
        element = self.get_conditions.get_element(*argument, **settings)
        if 'locator' in settings:
            locator = settings['locator']
            del settings['locator']
            if locator[element].wait.gone(timeout=time):
                return True
            else:
                return False
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).wait.gone(timeout=time)
            else:
                return self.device_mobile(*argument, **settings).wait.gone(timeout=time)
