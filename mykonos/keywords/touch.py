import attr
from alog import debug, error, info
from mykonos.locator.locator_element import LocatorElement

@attr.s
class Touch(LocatorElement):
    data = attr.ib()

    def __attrs_post_init__(self):
        self.device_mobile = self.device(self.data)

    def swipe_screen(self, sx, sy, ex, ey, step=None):
        """ geasture swipe interanction of Android Device
        swipe from (sx, sy) to (ex, ey)
        example :
        tc = Touch(data)
        tc.swipe_screen(189, 210, 954, 336, step=10)
        """
        return self.device_mobile().swipe(sx, sy, ex, ey, step)

    def drag_screen(self, sx, sy, ex, ey, step=None):
        """ geasture drag interanction of Android Device
        example :
        tc = Touch(data)
        tc.drag_sceen(189, 210, 954, 336, step=10)
        """
        return self.device_mobile().drag(sx, sy, ex, ey, step)
