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
        """ Call keyword_device_info method from global_keywords class
        and will return dictionary
        Example :
        Example_Code:orcestrator = Orcestrator(data)
        orcestrator.device_info
        Example_robot_framework:
        | ${device_info} | Device Info |
        | Log Dictionary | ${device_info}  |

        Return:
        {'currentPackageName': 'com.google.android.apps.nexuslauncher',
         'displayHeight': 1794,
         'displayRotation': 0,
         'displaySizeDpX': 411,
         'displaySizeDpY': 731,
         'displayWidth': 1080,
         'productName': 'sdk_google_phone_x86',
         'screenOn': True,
         'sdkInt': 25,
         'naturalOrientation': True}
        """
        return self.global_keywords.keyword_device_info()

    def turn_on_screen(self):
        """ Call keyword_turn_on_screen from global keywords class
        and screen device will be on
        """
        return self.global_keywords.keyword_turn_on_screen()

    def turn_off_screen(self):
        """ Call keyword_turn_of_screen from global keywords class
        and screen device will be of
        """
        return self.global_keywords.keyword_turn_off_screen()

    def press_key(self, *keys):
        try:
            if 'home' in keys:
                return self.global_keywords.keyword_press_home()

        except Exception as Argument:
            raise ValueError(Argument)
