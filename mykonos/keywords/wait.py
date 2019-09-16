from mykonos.core.core import Core
from mykonos.keywords.element import GetConditions
from mykonos.keywords.decorators import Decorators, Parallel
from mykonos.keywords.logging import LoggingKeywords


class Wait(Core):

    def __init__(self):
        self.device_mobile = self.device()
        self.get_conditions = GetConditions()
        self.logging = LoggingKeywords()

    @Decorators.android_version
    @Parallel.device_check
    def wait_until_page_contains(self, device=None, error=None, time=1000, *argument, **settings):
        """This keyword is used to wait until page is contain spesific element.

        **Example:**

        || Wait Until Page Contains | className= sample class | error=sample error
        """

        if 'locator' in settings:
            locator = settings['locator']
            del settings['locator']
            try:
                if locator.wait.exists(timeout=time) is False:
                    return False or error
                return True
                self.logging.log('locator with name %s is exists' % (locator), level="INFO")
            except Exception as error:
                return ("Exception Error: {0}".format(error))
                self.logging.log('locator with name %s is not exists' % (locator), level="ERROR")
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
            try:
                if self.device_mobile(*argument, **settings).wait.exists(timeout=time) is False:
                    return False or error
                return True
                self.logging.log('locator with name %s is exists' % (locator), level="INFO")
            except Exception as error:
                return ("Exception Error: {0}".format(error))
                self.logging.log('locator with name %s is not exists' % (locator), level="ERROR")

    @Decorators.android_version
    def wait_until_element_is_exists(self, time=1000, error=None, *argument, **settings):
        """This keyword is used to wait until spesific element is exists.

        **Example:**

        || Wait Until Element Is Exists | className=sample class or text=Sample Text | erro=sample error
        """
        element = self.get_conditions.get_element(*argument, **settings)

        if 'locator' in settings:
            locator = settings['locator']
            del settings['locator']
            try:
                if locator[element].wait.exists(timeout=time) is False:
                    return False or error
                return True
                self.logging.log('locator with name %s is exists' % (locator), level="INFO")
            except Exception as error:
                return ("Exception Error: {0}".format(error))
                self.logging.log('locator with name %s is exists' % (locator), level="INFO")
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
            try:
                if self.device_mobile(*argument, **settings).wait.exists(timeout=time) is False:
                    return False or error
                return True
                self.logging.log('locator with name %s is exists' % (locator), level="INFO")
            except Exception as error:
                return ("Exception Error: {0}".format(error))
                self.logging.log('locator with name %s is not exists' % (locator), level="ERROR")

    @Decorators.android_version
    def wait_until_page_does_not_contains(self, time=1000, *argument, **settings):
        """This keyword is used to wait until page is not contain spesific element.

        **Example:**

        || Wait Until Page Does Not Contains| className=sample class
        """
        if 'locator' in settings:
            locator = settings['locator']
            del settings['locator']
            try:
                if locator.wait.gone(timeout=time) is True:
                    return True
                return False
                self.logging.log('locator with name %s is exists' % (locator), level="INFO")
            except Exception as error:
                return ("Exception Error: {0}".format(error))
                self.logging.log('locator with name %s is exists' % (locator), level="ERROR")
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
            try:
                if self.device_mobile(*argument, **settings).wait.gone(timeout=time) is True:
                    return True
                return False
                self.logging.log('locator with name %s is exists' % (locator), level="INFO")
            except Exception as error:
                return ("Exception Error: {0}".format(error))
                self.logging.log('locator with name %s is not exists' % (locator), level="ERROR")
