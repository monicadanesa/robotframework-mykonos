import attr
from alog import debug, info, error
from mykonos.locator.locator_element import LocatorElement

@attr.s
class Element(LocatorElement):
    data = attr.ib()

    def __attrs_post_init__(self):
        self.device_mobile = self.device(self.data)

    def click_element(self, object, *argument, **locator):
        """ click on UI base on locator """
        return self.device_mobile.click()
