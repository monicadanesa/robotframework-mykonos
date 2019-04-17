import attr
import os
from alog import debug, error, info
from mykonos.core.core import Core

@attr.s
class ManagementDevice(Core):

    def __attrs_post_init__(self):
        pass

    def scan_current_device(self, *args, **data_result):
        global sc
        sc = os.system('adb devices')

        if sc==0:
            debug(True)
        else:
            debug(False)

        return self.device(*args, **data_result)

    def reset_application(self, app_package):
        rs = os.system('adb -s '+sc+' shell pm clear '+app_package+'')
        return rs

    def open_application(self, app_activity):
        op = os.system('adb -s '+sc+' shell am start -W '+app_activity+'')
        return op

    def close_application(self, app_package):
        cl = os.system('adb -s '+sc+' am force-stop '+app_package+'')
        return cl

    def info_device(self, **device_setting):
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

        return self.device(*args, **data_result).info

    def turn_on_screen(self, **device_setting):
        """ Call keyword_turn_on_screen
        and screen device will be on
        """
        return self.device(*args, **data_result).screen.on()

    def turn_off_screen(self, **device_setting):
        """ Call keyword_turn_off_screen
        and screen device will be on
        """
        return self.device(*args, **data_result).screen.off()
