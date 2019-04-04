import attr
from alog import debug, error, info
from mykonos.core import Core

@attr.s
class Global_Keywords:
    device_mobile = attr.ib()

    def __attrs_post_init__(self):
        pass

    def get_device_info(self):
        return self.device_mobile.info
