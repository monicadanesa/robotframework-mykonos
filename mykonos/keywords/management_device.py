import os
from mykonos.core.core import Core


class ManagementDevice(Core):
    adb_s = 'adb -s '
    adb_start = ' shell am start -W '
    adb_stop = ' shell am force-stop '
    adb_grep_pid = 'adb shell pgrep '
    adb_kill = 'adb shell pkill '
    adb_pm_clear = ' shell pm clear '
    adb_key_event = 'adb shell input keyevent '

    def __init__(self):
        """Devine all global variable."""
        self.index = 0

    def scan_current_device(self,  *args, **data_result):
        """Scan current device on the workstation, and consume.
        to open application
        HOW TO CALL IN ROBOT FRAMEWORK

        |  Scan Current Device                         |  emulator=emulator-554

        """
        os.system('adb devices')
        return self.device(*args, **data_result)

    def open_app(self, device, package):
        """ Open Application on Device.
        HOW TO CALL IN ROBOT FRAMEWORK

        | Open Application      |  emulator=emulator-554   |  sampleapk
        """
        try:
            os.system(self.adb_s + device + self.adb_start + package + '')
            return self.device(device)
        except ValueError as error:
            raise ValueError('open device is failed')

    def _substring_package(self, package):
        return package.split('/')[0]

    def quit_app(self, device, package):
        """Close running application."""
        package = self._substring_package(package)
        cl = os.system(self.adb_kill + package)
        return cl

    def close_all_app(self, device_name):
        """Close all task on the device, and kill all application."""
        try:
            os.system('adb -s '+device_name+' shell am kill-all')
            return self.device(device_name)
        except ValueError:
            raise ValueError('device can not be opened')

    def reset_app(self, device, package):
        """Reset Application on Device.

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Reset Application   |  emulator=emulator-554   |  sample_apk
        """
        try:
            package = self._substring_package(package)
            op = os.system(self.adb_s + device + self.adb_pm_clear + package)
            return op
        except ValueError:
            raise ValueError('device can not be opened')

    def turn_on_screen(self, **device_setting):
        """Call keyword_turn_on_screen.

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Turn On Screen

        return : True or False
        """
        return self.device(**device_setting).screen.on()

    def turn_off_screen(self, **device_setting):
        """Call keyword_turn_off_screen.

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Turn Off Screen

        return : True or False
        """
        return self.device(**device_setting).screen.off()

    def dump_xml(self, *args):
        """Dump hierarchy of ui and will be saved as hierarchy.xml.

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Dump XML

        return : xml file of device
        """
        return self.device().dump(*args)

    def capture_screen(self, file=None):
        """Capture screen of device testing.

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Capture Screen

        with file name:
        | Capture Screen        | file='sample'

        return : screen capture of device(*.png)
        """
        if file is not None:
            return self.device().screenshot(file+'.png')
        else:
            self.index += 1
            filename = 'mykonos-screenshot-%d.png' % self.index
            return self.device().screenshot(filename)

    def hide_keyword(self):
        """ Hide Keyword of Device.

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Hide Keyword

        return : True or False
        """
        rs = os.system(self.adb_key_event+'111')
        return rs
