import attr
from alog import debug, info, error
from mykonos.locator.locator_element import LocatorElement

@attr.s
class Element(LocatorElement):

    def __attrs_post_init__(self):
        self.device_mobile = self.scan_current_device()

    def click_element(self, device=None, parent=None, *argument, **locator):
        """ click on UI base on locator """
        try:
            if parent!=None:
                return parent.click()
            else:
                if device!=None:
                    return device(*argument, **locator).click()
                else:
                    return self.device_mobile(*argument, **locator).click()

        except ValueError as error:
             raise ValueError('element cannot be click' + error)

    def long_click_element(self, device=None, parent=None, *argument, **locator):
        """ long click on UI base on locator """
        try:
            if parent!=None:
                return parent.click()
            else:
                if device!=None:
                    return device(*argument, **locator).long_click()
                else:
                    return self.device_mobile(*argument, **locator).long_click()

        except ValueError as error:
             raise ValueError('element cannot be click' + error)

    def clear_text(self, device=None, parent=None, *argument, **locator):
        """ clear text on text field base on locator """
        try:
            if parent!=None:
                return parent.clear_text()
            else:
                if device!=None:
                    return device(*argument, **locator).clear_text()
                else:
                    return self.device_mobile(*argument, **locator).clear_text()

        except ValueError as error:
             raise ValueError('element cannot be clear' + error)

    def input_text(self, device=None, parent=None, text=None, *argument, **locator):
        """ input text on text field base on locator """
        try:
            if parent!=None:
                return parent.set_text(text)
            else:
                if device!=None:
                    return device(*argument, **locator).set_text(text)
                else:
                    return self.device_mobile(*argument, **locator).set_text(text)
        except ValueError as error:
             raise ValueError('element cannot be input' + error)
