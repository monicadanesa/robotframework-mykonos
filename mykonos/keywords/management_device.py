import os
import subprocess
from mykonos.core.core import Core


class ManagementDevice(Core):
    adb_s = 'adb -s '
    adb_start = ' shell am start -W '
    adb_stop = ' shell am force-stop '
    adb_grep_pid = 'adb shell pgrep '
    adb_kill = 'adb shell pkill '
    adb_pm_clear = ' shell pm clear '
    adb_key_event = 'adb shell input keyevent '
    adb_pull = 'adb pull '
    adb_push = 'adb push '
    adb_activity = 'adb shell dumpsys activity | grep '

    def __init__(self):
        """Devine all global variable."""
        self.index = 0

    def scan_current_device(self,  *args, **settings):
        """Scan current device on the workstation, and consume.
        to open application
        HOW TO CALL IN ROBOT FRAMEWORK

        |  Scan Current Device                         |  emulator=emulator-554

        """
        os.system('adb devices')
        return self.device(*args, **settings)

    def open_app(self, device, package):
        """Open Application on Device.
        HOW TO CALL IN ROBOT FRAMEWORK

        | Open Application      |  device=emulator-554   | package=sample_apk
        """
        try:
            os.system(self.adb_s + device + self.adb_start + package + '')
            return self.device(device)
        except ValueError:
            raise ValueError('open device is failed')

    def _substring_package(self, package):
        return package.split('/')[0]

    def quit_app(self, device, package):
        """Quit running application."""
        package = self._substring_package(package)
        cl = os.system(self.adb_kill + package)
        return cl

    def close_all_app(self, device):
        """Close all task on the device, and kill all application."""
        try:
            os.system('adb -s '+device+' shell am kill-all')
            return self.device(device)
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

    def turn_on_screen(self, **settings):
        """Call keyword_turn_on_screen.

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Turn On Screen

        return : True or False
        """
        return self.device(**settings).screen.on()

    def turn_off_screen(self, **settings):
        """Call keyword_turn_off_screen.

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Turn Off Screen

        return : True or False
        """
        return self.device(**settings).screen.off()

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
        | Capture Screen        | file=sample

        return : screen capture of device(*.png)
        """
        if file is not None:
            return self.device().screenshot(file+'.png')
        else:
            self.index += 1
            filename = 'mykonos-screenshot-%d.png' % self.index
            return self.device().screenshot(filename)

    def hide_keyword(self):
        """Hide Keyword of Device.

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Hide Keyword

        return : True or False
        """
        rs = os.system(self.adb_key_event+'111')
        return rs

    def pull(self, **settings):
        """Pull file into Device.

        HOW TO CALL IN ROBOT FRAMEWORK
        with location
        |  Pull         | local=sample_path  | remote=sample_location
        without location
        |  Pull         | local=sample_path  |

        return : True or False
        """
        local = settings['local']

        if 'remote' in settings:
            remote = settings['remote']
            rs = os.system(self.adb_pull + local + remote)
        else:
            rs = os.system(self.adb_pull + local)

        if rs != 0:
            return False
        else:
            return True

    def push(self, **settings):
        """Push file into Device.

        HOW TO CALL IN ROBOT FRAMEWORK
        with location
        |  Push       | local=sample_path  | remote=sample_location

        return : True or False
        """
        local = settings['local']
        remote = settings['remote']
        rs = os.system(self.adb_push + local + ' ' + remote)

        if rs != 0:
            return False
        else:
            return True

    def __shell_pipe(self, cmd):
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        return out

    def __return_dumpsy_package(self, cmd):
        out = self.__shell_pipe(cmd)
        start = str(out).find('{')
        end = str(out).find('/')
        slice_1 = str(out)[start:end]
        result = str(slice_1)[str(slice_1).find(':')+1:]

        return result

    def __get_old_package(self):
        return self.__return_dumpsy_package(self.adb_activity + 'mPreviousProcess')

    def __adb_clear_cache(self):
        clear_cache = self.__shell_pipe('adb shell pm trim-caches')
        return clear_cache

    def switch_application(self, device, new_app):
        """Switch application the devices.

        This keywords return previous active application
        and it can be used in the next application.

        HOW TO CALL IN ROBOT FRAMEWORK
        with location
        |  Switch Application      | device=sample_device  | new_app=sample_app

        """
        old = self.__get_old_package()
        new = new_app.info['currentPackageName']
        current = self.device().info['currentPackageName']
        result = self.open_app(device, old)

        return result
