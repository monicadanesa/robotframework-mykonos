from alog import debug, info, error
from mykonos.core.core import Core

class Element(Core):

    def __init__(self):
        self.device_mobile = self.device()

    def open_notification(self, **setting):
        """ open notification of Android"""
        if 'locator' in setting:
            locator = setting['locator']
            return locator.open.notification()
        else:
            if 'device' in setting:
                device = setting['device']
                return device.open.notification()
            else:
                return self.device_mobile.open.notification()

    def open_quick_settings(self, **setting):
        """ open quick settings of Android"""
        if 'locator' in setting:
            locator = setting['locator']
            return locator.open.quick_settings()
        else:
            if 'device' in setting:
                device = setting['device']
                return device.open.quick_settings()
            else:
                return self.device_mobile.open.quick_settings()

    def click_element(self, *argument, **setting):
        """ click on UI base on locator """
        try:
            if 'locator' in setting:
                locator = setting['locator']
                return locator.click()
            else:
                if 'device' in setting:
                    device = setting['device']
                    del setting['device']

                    return device(*argument, **setting).click()
                else:
                    return self.device_mobile(*argument, **setting).click()

        except ValueError as error:
             raise ValueError('element cannot be click')

    def long_click_element(self, *argument, **setting):
        """ long click on UI base on locator """
        try:
            if 'locator' in setting:
                locator = setting['locator']
                return locator.long_click()
            else:
                if 'device' in setting:
                    device = setting['device']
                    del setting['device']
                    return device(*argument, **locator).long_click()
                else:
                    return self.device_mobile(*argument, **setting).long_click()

        except ValueError as error:
             raise ValueError('element cannot be click')

    def clear_text(self, *argument, **setting):
        """ clear text on text field base on locator """
        try:
            if 'locator' in setting:
                locator = setting['locator']
                return locator.clear_text()
            else:
                if 'device' in setting:
                    device = setting['device']
                    del setting['device']
                    return device(*argument, **setting).clear_text()
                else:
                    return self.device_mobile(*argument, **setting).clear_text()

        except ValueError as error:
             raise ValueError('element cannot be clear')

    def input_text(self, *argument, **setting):
        """ input text on text field base on locator """
        try:
            input = setting['input']
            del setting['input']

            if 'locator' in setting:
                locator = setting['locator']
                return locator.set_text(input)
            else:
                if 'device' in setting:
                    device = setting['device']
                    del setting['device']

                    return device(*argument, **setting).set_text(input)
                else:
                    return self.device_mobile(*argument, **setting).set_text(input)

        except ValueError as error:
             raise ValueError('element cannot be input')

    def get_text(self, *argument, **setting):
        """ get text from element base on locator """
        try:

            if 'locator' in setting:
                locator = setting['locator']
                return locator.info['text']
            else:
                if 'device' in setting:
                    device = setting['device']
                    del setting['device']
                    return device(*argument, **setting).info['text']
                else:
                    return self.device_mobile(*argument, **setting).info['text']

        except ValueError as error:
             raise ValueError('get text from element error')

    def get_element_attribute(self, *argument, **setting):
        """ get element attribute using list of the elements :
        List of Elements:
         childCount, bounds, className, contentDescription,
         packageName, resourceName, text, visibleBounds,
         checkable, checked, clickable, enabled, focusable,
         focused, longClickable, scrollable, selected

         example :
         get_element_attribute(element="text", className="")
         """
        try:
            element = setting['element']
            del setting['element']

            if 'locator' in setting:
                locator = setting['locator']
                return locator.info[element]
            else:
                if 'device' in setting:
                    device = setting['device']
                    del setting['device']

                    return device(*argument, **setting).info[element]
                else:
                    return self.device_mobile(*argument, **setting).info[element]
        except ValueError as error:
            return ValueError('get error when get element attribute')

        def click_a_point(self, *argument, **setting):
            """Click into target target pointer location
            example :
            tc.click(x, y)
            """
            try:
                if device!=None:
                    return device(*argument, **locator).click(x, y)
                else:
                    return self.device_mobile().click(x, y)
            except ValueError as error:
                raise ValueError('pointer location is refused')
