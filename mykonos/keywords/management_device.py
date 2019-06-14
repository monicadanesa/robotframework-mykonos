import os
import subprocess
from mykonos.core.core import Core


class ManagementDevice(Core):
    adb_s = 'adb -s '
    adb_start = ' shell am start -W '
    adb_stop = ' adb shell am force-stop '
    adb_grep_pid = 'adb shell pgrep '
    adb_kill = 'adb shell pkill '
    adb_pm_clear = 'shell pm clear'
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

    def __get_current_package(self):
        cmd = "adb shell dumpsys activity | grep top-activity | awk '{ print $8 }'"
        top_activity = self.__shell_pipe(cmd)
        start_pid = str(top_activity).find("'")
        end_pid = str(top_activity).find(":")
        end_package_name = str(top_activity).find("/")
        pid = str(top_activity)[start_pid:end_pid]
        package = str(top_activity)[end_pid+1:end_package_name]

        return package

    def reset_app(self, device, package):
        """Reset Application on Device.

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Reset Application   |  emulator=emulator-554
        """
        try:
            reset = os.system('adb -s'+device+' shell pm clear '+package)
            return reset
        except ValueError:
            raise ValueError('reset apps is failed')

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

    def force_close(self):
        """Force Closed Application.
        HOW TO CALL IN ROBOT FRAMEWORK
        with location
        | Force Close
        """
        package = self.__get_current_package()

        result = os.system(self.adb_stop + package)
        reconect = os.system('adb reconnect')

        return result
