import attr
from alog import debug, error, info
from mykonos.core.core import Core

@attr.s
class ManagementDevice(Core):
    data = attr.ib()

    def __attrs_post_init__(self):
        self.device_mobile = self.device(self.data)

    def device_info(self):
        """ Call keyword_device_info
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

        return self.device_mobile.info

    def turn_on_screen(self):
        """ Call keyword_turn_on_screen
        and screen device will be on
        """
        return self.device_mobile.screen.on()

    def turn_off_screen(self):
        """ Call keyword_turn_off_screen
        and screen device will be on
        """
        return self.device_mobile.screen.off()
