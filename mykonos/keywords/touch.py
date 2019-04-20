import attr
from alog import debug, error, info
from mykonos.core.core import Core

@attr.s
class Touch(Core):
    def __attrs_post_init__(self):
        self.device_mobile = self.device()

    def swipe_screen(self, sx, sy, ex, ey, step=None, device=None):
        """ geasture swipe interanction of Android Device
        swipe from (sx, sy) to (ex, ey)
        example :
        tc = Touch(data)
        tc.swipe_screen(189, 210, 954, 336, step=10)
        """
        try:
            if device!=None:
                return device(*argument, **locator).swipe(sx, sy, ex, ey, step)
            else:
                return self.device_mobile().swipe(sx, sy, ex, ey, step)
        except ValueError as error:
             raise ValueError('device cannot be swipe' + error)

    def drag_screen(self, sx, sy, ex, ey, step=None, device=None):
        """ geasture drag interanction of Android Device
        example :
        tc = Touch(data)
        tc.drag_sceen(189, 210, 954, 336, step=10)
        """
        try:
            if device!=None:
                return device(*argument, **locator).drag(sx, sy, ex, ey, step)
            else:
                return self.device_mobile().drag(sx, sy, ex, ey, step)
        except ValueError as error:
             raise ValueError('device cannot be drag' + error)
