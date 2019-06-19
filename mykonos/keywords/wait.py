from mykonos.core.core import Core
from mykonos.keywords.element import GetConditions


class Wait(Core):

    def __init__(self):
        self.device_mobile = self.device()
        self.get_conditions = GetConditions()

    def wait_until_element_is_exists(self, *argument, **settings):
        """Wait Until Element Is Exists.
           How to call in ROBOT FRAMEWORK
           | Wait Until Element Is Exists | className= sample class
        """
        element = self.get_conditions.get_element(*argument, **settings)

        if 'locator' in settings:
            locator = settings['locator']
            if locator[element].wait.exists(timeout=1000):
                return True
            else:
                raise ValueError('Locator Not Found')
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).wait.exists(timeout=1000)
            else:
                return self.device_mobile(*argument, **settings).wait.exists(timeout=1000)

    def wait_until_page_contains(self, time=1000, *argument, **settings):
        """Wait Until Page Contains
        HOW TO CALL IN ROBOT FRAMEWORK
        |Wait Untile Page Contains | className=sample class or text = sample text
        """
        element = self.get_conditions.get_element(*argument, **settings) or self.get_element(*argument, **settings)
        if 'locator' in settings:
            locator = settings['locator']
            if locator[element].wait.exists(timeout=time):
                return True
            else:
                raise ValueError('Element Not Found')
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).wait.exists(timeout=time)
            else:
                return self.device_mobile(*argument, **settings).wait.exists(timeout=time)

    def wait_until_page_contains_element(self, time=1000, *argument, **settings):
        """Wait Until Page Contains Element
        HOW TO CALL IN ROBOT FRAMEWORK
        |Wait Untile Page Contains Element| className=sample class or text = sample text
        """
        element = self.get_conditions.get_element(*argument, **settings)
        if 'locator' in settings:
            locator = settings['locator']
            if locator[element].wait.exists(timeout=time):
                return True
            else:
                raise ValueError('Element Not Found')
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).wait.exists(timeout=time)
            else:
                return self.device_mobile(*argument, **settings).wait.exists(timeout=time)

    def wait_until_page_does_not_contain(self, time=1000, *argument, **settings):
        """Wait Until Page Does Not Contains
        HOW TO CALL IN ROBOT FRAMEWORK
        |Wait Until Page Does Not Contains| className=sample class or text = sample text
        """
        element = self.get_conditions.get_element(*argument, **settings)
        if 'locator' in settings:
            locator = settings['locator']
            del settings['locator']
            if locator[element].wait.gone(timeout=time):
                return False
            else:
                raise ValueError('Element Not Found')
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).wait.gone(timeout=time)
            else:
                return self.device_mobile(*argument, **settings).wait.gone(timeout=time)

    def wait_until_page_does_not_contain_element(self, time=1000, *argument, **settings):
        """Wait Until Page Does Not Contains Element
        HOW TO CALL IN ROBOT FRAMEWORK
        |Wait Until Page Does Not Contains Element| className=sample className
        """
        element = self.get_conditions.get_element(*argument, **settings)
        if 'locator' in settings:
            locator = settings['locator']
            del settings['locator']
            if locator[element].wait.gone(timeout=time):
                return False
            else:
                raise ValueError('Element Not Found')
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).wait.gone(timeout=time)
            else:
                return self.device_mobile(*argument, **settings).wait.gone(timeout=time)
