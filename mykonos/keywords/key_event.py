import attr
from alog import debug, info, error
from mykonos.core.core import Core

@attr.s
class KeyEvent(Core):
    data = attr.ib()

    def __attrs_post_init__(self):
        self.device_mobile = self.device(self.data)

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
        return self.device_mobile.press(*args, **kwargs)
