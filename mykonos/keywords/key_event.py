import attr
from alog import debug, info, error
from mykonos.core.core import Core, Decorator

@attr.s
class KeyEvent:
    data = attr.ib()

    def __attrs_post_init__(self):
        self.core = Core(Decorator)
        self.device_mobile = self.core.device(self.data)

    def press_home(self):
        """
        Press Home Button on Device"""
        return self.device_mobile.press.home()

    def press_back(self):
        """
        Press back Button on Device"""
        return self.device_mobile.press.back()

    def press_left(self):
        """
        Press left Button on Device"""
        return self.device_mobile.press.left()

    def press_right(self):
        """
        Press right Button on Device"""
        return self.device_mobile.press.right()

    def press_up(self):
        """
        Press up Button on Device"""
        return self.device_mobile.press.up()

    def press_down(self):
        """
        Press down Button on Device"""
        return self.device_mobile.press.down()

    def press_center(self):
        """
        Press center Button on Device"""
        return self.device_mobile.press.center()

    def press_menu(self):
        """
        Press menu Button on Device"""
        return self.device_mobile.press.menu()

    def press_search(self):
        """
        Press search Button on Device"""
        return self.device_mobile.press.search()

    def press_delete(self):
        """
        Press delete Button on Device"""
        return self.device_mobile.press.delete()

    def press_recent(self):
        """
        Press recent Button on Device"""
        return self.device_mobile.press.right()

    def press_volume_up(self):
        """
        Press volume up Button on Device"""
        return self.device_mobile.press.volume_up()

    def press_volume_down(self):
        """
        Press volume down Button on Device"""
        return self.device_mobile.press.volume_down()

    def press_volume_mute(self):
        """
        Press volume mute Button on Device"""
        return self.device_mobile.press.volume_mute()

    def press_camera(self):
        """
        Press camera Button on Device"""
        return self.device_mobile.press.camera()

    def press_power(self):
        """
        Press power Button on Device"""
        return self.device_mobile.press.power()
