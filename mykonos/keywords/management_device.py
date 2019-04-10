import attr
from alog import debug, error, info
from mykonos.core.core import Core

@attr.s
class Management_Device():
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
