import os
from alog import debug, error, info
from mykonos.core.core import Core

class ManagementDevice(Core):
    adb_str = 'adb -s '
    adb_shell_start = ' shell am start -W '
    adb_stop = ' shell am force-stop '
    adb_shell_grep_pid = 'adb shell pgrep '
    adb_shell_kill = 'adb shell pkill '
    adb_shell_pm_clear = ' shell pm clear '
    adb_shell_key_event = 'adb shell input keyevent '

    def __init__(self):
        self.index = 0

    def scan_current_device(self,  *args, **data_result):
        """
        scan current device on the workstation, and consume
        to open application
        HOW TO CALL IN ROBOT FRAMEWORK

        |  Scan Current Device                         |  emulator=emulator-554

        """
        sc = os.system('adb devices')

        if sc==0:
            result = 'device is available'
        else:
            result = 'device is not available'

        return self.device(*args, **data_result)


    def open_app(self, device, app_package):
        """ Open Application on Device
        HOW TO CALL IN ROBOT FRAMEWORK

        |  Open Application                        |  emulator=emulator-554   |  sampleapk
        """
        try:
            op = os.system(self.adb_str + device + self.adb_shell_start + app_package + '')
            return self.device(device)
        except ValueError as error:
            raise ValueError('open device is failed')

    def _substring_package(self, app_package):
        return app_package.split('/')[0]

    def close_app(self, device, app_package):
        """
        Close running application
        """
        package = self._substring_package(app_package)
        cl = os.system(self.adb_shell_kill + package)
        return cl

    def close_all_app(self, device_name):
        """
        Close all task on the device, and kill all application
        """
        try:
            op = os.system('adb -s '+device_name+' shell am kill-all')
            return self.device(device_name)
        except ValueError as error:
            raise ValueError('device can not be opened')

    def reset_app(self, device, app_package):
        """ Reset Application on Device
        HOW TO CALL IN ROBOT FRAMEWORK

        |  Reset Application                        |  emulator=emulator-554   |  sample_apk
        """
        try:
            package = self._substring_package(app_package)
            op = os.system(self.adb_str + device + self.adb_shell_pm_clear + package + '')
            return op
        except ValueError as error:
            raise ValueError('device can not be opened')

    def turn_on_screen(self, **device_setting):
        """ Call keyword_turn_on_screen
        and screen device will be on

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Turn On Screen

        return : True or False
        """
        return self.device(*args, **device_setting).screen.on()

    def turn_off_screen(self, **device_setting):
        """ Call keyword_turn_off_screen
        and screen device will be on

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Turn Off Screen

        return : True or False
        """
        return self.device(*args, **device_setting).screen.off()

    def dump_xml(self,*args):
        """ dump hierarchy of ui and will be saved as hierarchy.xml

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Dump Xml

        return : xml file of device
        """
        return self.device().dump(*args)

    def capture_screen(self, file=None):

        """ capture screen of device testing

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Capture Screen

        with file name:
        | Capture Screen        | file='sample'

        return : screen capture of device(*.png)
        """
        if file !=None:
            return self.device().screenshot(file+'.png')
        else:
            self.index += 1
            filename = 'mykonos-screenshot-%d.png' % self.index
            return self.device().screenshot(filename)

    def hide_keyword(self):
        """ Hide Keyword of Device

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Hide Keyword

        return : True or False
        """
        rs = os.system(self.adb_shell_key_event+'111')
        return rs
