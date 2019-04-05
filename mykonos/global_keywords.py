import attr
from alog import debug, error, info
from mykonos.core import Core

@attr.s
class Global_Keywords:
    device_mobile = attr.ib()

    def __attrs_post_init__(self):
        pass

    def keyword_device_info(self):
        """
        Retrieve device info and will return with dictionary
        """

        return self.device_mobile.info

    def keyword_turn_on_screen(self):
        """
        Turn on Screen Device"""
        return self.device_mobile.screen.on()

    def keyword_turn_off_screen(self):
        """
        Turn off Screen Device"""
        return self.device_mobile.screen.off()

    def keyword_press_home(self):
        """
        Press Home Button on Device"""
        return self.device_mobile.press.home()

    def keyword_press_back(self):
        """
        Press back Button on Device"""
        return self.device_mobile.press.back()

    def keyword_press_left(self):
        """
        Press left Button on Device"""
        return self.device_mobile.press.left()

    def keyword_press_right(self):
        """
        Press right Button on Device"""
        return self.device_mobile.press.right()

    def keyword_press_up(self):
        """
        Press up Button on Device"""
        return self.device_mobile.press.up()

    def keyword_press_down(self):
        """
        Press down Button on Device"""
        return self.device_mobile.press.down()

    def keyword_press_center(self):
        """
        Press center Button on Device"""
        return self.device_mobile.press.center()

    def keyword_press_menu(self):
        """
        Press menu Button on Device"""
        return self.device_mobile.press.menu()

    def keyword_press_search(self):
        """
        Press search Button on Device"""
        return self.device_mobile.press.search()

    def keyword_press_delete(self):
        """
        Press delete Button on Device"""
        return self.device_mobile.press.delete()

    def keyword_press_recent(self):
        """
        Press recent Button on Device"""
        return self.device_mobile.press.right()

    def keyword_press_volume_up(self):
        """
        Press volume up Button on Device"""
        return self.device_mobile.press.volume_up()

    def keyword_press_volume_down(self):
        """
        Press volume down Button on Device"""
        return self.device_mobile.press.volume_down()

    def keyword_press_volume_mute(self):
        """
        Press volume mute Button on Device"""
        return self.device_mobile.press.volume_mute()

    def keyword_press_camera(self):
        """
        Press camera Button on Device"""
        return self.device_mobile.press.camera()

    def keyword_press_power(self):
        """
        Press power Button on Device"""
        return self.device_mobile.press.power()
