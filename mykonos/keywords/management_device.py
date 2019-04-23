import os
from alog import debug, error, info
from mykonos.core.core import Core

class ManagementDevice(Core):

    def __init__(self):
        pass

    def scan_current_device(self,  *args, **data_result):
        sc = os.system('adb devices')

        if sc==0:
            result = 'device is available'
        else:
            result = 'device is not available'

        return self.device(*args, **data_result)

    def reset_application(self, device, app_package):
        rs = os.system('adb -s '+device+' shell pm clear '+app_package+'')
        return rs

    def open_application(self, device, app_package):
        try:
            op = os.system('adb -s '+device+' shell am start -W '+app_package+'')
            return self.device(device)
        except ValueError as error:
            raise ValueError('open device is failed')

    def close_application(self, device_name, app_package):
        cl = os.system('adb shell am force-stop '+app_package+'')
        return cl

    def info_device(self, device=None, *args, **device_setting):
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
        if device!=None:
            return device(*args, **device_setting).info
        else:
            return self.device(*args, **device_setting).info

    def turn_on_screen(self, **device_setting):
        """ Call keyword_turn_on_screen
        and screen device will be on
        """
        return self.device(*args, **device_setting).screen.on()

    def turn_off_screen(self, **device_setting):
        """ Call keyword_turn_off_screen
        and screen device will be on
        """
        return self.device(*args, **device_setting).screen.off()

    def dump_xml(self):
        """ dump hierarchy of ui and will be saved as hierarchy.xml """
        return self.device().dump()
