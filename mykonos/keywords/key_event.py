from alog import debug, info, error
from mykonos.core.core import Core

class KeyEvent(Core):
    def __init__(self):
        self.device_mobile = self.device()

    def press_keycode(self, *args, **kwargs):
        """ press key on android device
        keysupport :
        home, back, left, right
        up, down, center, menu
        search, enter, delete(or del)
        recent(recent apps), volume_up, volume_down
        volume_mute, camera, power

        example:
        ke = KeyEvent(data)
        ke.press_keyword("back")
        """
        if 'locator' in kwargs:
            locator = setting['locator']
            del kwargs['locator']
            return locator.press(*args, **kwargs)
        else:
            if 'device' in kwargs:
                device = kwargs['device']
                del kwargs['device']

                return device.press(*args, **kwargs)
            else:
                return self.device_mobile.press(*args, **kwargs)
