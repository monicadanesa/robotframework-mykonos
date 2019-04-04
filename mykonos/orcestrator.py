import attr
from alog import debug, error, info
from mykonos.core import Core
from mykonos.global_keywords import Global_Keywords



@attr.s
class Orcestrator:
    data = attr.ib()

    def __attrs_post_init__(self):
        self.core = Core(self.data)
        self.device_mobile = self.core.device_mobile()
        self.global_keywords = Global_Keywords(self.device_mobile)

    def device_info(self):
        return self.global_keywords.get_device_info()
