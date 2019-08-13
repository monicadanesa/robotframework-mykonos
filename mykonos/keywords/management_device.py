import os
import subprocess
from mykonos.core.core import Core
from mykonos.keywords.management_device_utils import DeviceUtils

class ManagementDevice(Core):
    adb_s = 'adb -s '
    adb_start = ' shell am start -W '
    adb_stop = ' shell am force-stop '
    adb_grep_pid = 'adb shell pgrep '
    adb_kill = 'adb shell pkill '
    adb_pm_clear = 'shell pm clear'
    adb_key_event = 'adb shell input keyevent '
    adb_pull = 'adb pull '
    adb_push = 'adb push '
    adb_activity = 'adb shell dumpsys activity | grep '
    adb_disable = 'adb shell pm disable'
    adb_check_version = 'adb shell getprop ro.build.version.release'
    adb_devices = 'adb devices | grep -v devices | grep device | cut -f 1'

    def __init__(self):
        """Devine all global variable."""
        self.index = 0

    def get_devices(self):
        list = []
        cmd = 'adb devices'
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        byte_decode = out.decode()
        # Get Index
        start = [i+1 for i in range(len(byte_decode)) if byte_decode.find('\n', i) == i]
        end = [i for i in range(len(byte_decode)) if byte_decode.find('\t', i) == i]

        if len(start) < len(end):
            total = len(start)
        else:
            total = len(end)
        for i in range(0, total):
            list.append(byte_decode[start[i]:end[i]])
        return list

    def scan_current_device(self,  *args, **settings):
        """Scan current device on the workstation, and consume to open application.
        **Example:**
        ||  Scan Current Device                        |  emulator-554
        """
        return self.device(*args)

    def open_app(self, device, package):
        """Open Application on device.
        This keyword is used to open new applications.
        **Example:**
        ||  Open Application      |  device=emulator-554   | package=sample_apk
        """
        try:
            os.system(self.adb_s + device + self.adb_start + package + '')
            return self.device(device)
        except ValueError:
            raise ValueError('open device is failed')

    def _substring_package(self, package):
        return package.split('/')[0]

    def quit_app(self, device, package):
        """Quit application on device.
        This keyword is used to close application without kill a session.
        **Example:**
        ||  Quit App      |  device=emulator-554   | package=sample_apk
        """
        package = self._substring_package(package)
        cl = os.system(self.adb_kill + package)
        return cl

    def close_all_app(self, device):
        """Close all tasks on device, and kill all application sessions.
        **Example:**
        || Close All App      |  device=emulator-554   |
        """
        try:
            os.system('adb -s '+device+' shell am kill-all')
            return self.device(device)
        except ValueError:
            raise ValueError('device can not be opened')

    def __append_current_package(self, cmd):
        top_activity = self.__shell_pipe(cmd)
        start_pid = str(top_activity).find("'")
        end_pid = str(top_activity).find(":")
        end_package_name = str(top_activity).find("/")
        pid = str(top_activity)[start_pid:end_pid]
        package = str(top_activity)[end_pid+1:end_package_name]
        return package


    def __get_current_package(self, **settings):
        get_device = self.get_devices()
        if 'device' in settings:
            device = settings['device']
            out = self.__shell_pipe(cmd="adb -s %s shell dumpsys activity | grep top-activity | awk '{ print $8 }'")
            self.__append_current_package(out)
        else:
            if len(get_device) == 1:
                out = self.__shell_pipe(cmd="adb shell dumpsys activity | grep top-activity | awk '{ print $8 }'")
                self.__append_current_package(out)
            else:
                for i in get_device:
                    out = self.__shell_pipe(cmd="adb -s %s shell dumpsys activity | grep top-activity | awk '{ print $8 }'")
                    self.__append_current_package(out)

    def reset_app(self, device, package):
        """Reset Application on Device.
        This keyword is used to reset the current application while sesion is keep alive.
        **Example:**
        || Reset Application   |  emulator=emulator-554 | package=sample_apk
        """
        try:
            reset = self.__shell_pipe(cmd='adb -s %s shell pm clear %s' % (device, package))
            # reset = os.system('adb -s'+device+' shell pm clear '+package)
            return reset
        except ValueError:
            raise ValueError('reset apps is failed')

    def hide_keyboard(self):
        """Hide Keyword on Device.
        This keyword is used to hide keyboard device.
        **Example:**
        || Hide keyboard      |
        """
        rs = os.system(self.adb_key_event+'111')
        return rs

    def pull(self, **settings):
        """Pull file from Device.
        This Keyword is used to retrieves file from device.
        **Example:**
        || Pull         | local=sample_path  | remote=sample_location
        || Pull         | local=sample_path  |
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
        This keyword is used to put file in spesific path of device.
        **Example:**
        || Push         | local=sample_path  | remote=sample_location
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
        **Example:**
        || Switch Application      | device=sample_device  | new_app=sample_app
        """
        old = self.__get_old_package()
        new = new_app.info['currentPackageName']
        current = self.device().info['currentPackageName']
        result = self.open_app(device, old)
        return result

    def close_app(self, device, package):
        """Close Application the device.
        This keywords is used to close the current application and kill session on device.
        **Example:**
        || Close App        | devices=${emulator} | package=Package Activity
        """
        try:
            closed = self.__shell_pipe(cmd='adb -s %s shell am force-stop %s' % (device, package))
            # closed = os.system('adb -s '+device+' shell am force-stop '+package)
            return closed
        except ValueError:
            raise ValueError('device not found')

    def get_android_version(self, **settings):
        get_device = self.get_devices()
        if 'device' in settings:
            device = settings['device']
            out = self.__shell_pipe(cmd='adb -s %s shell getprop ro.build.version.release'%device)
            yield(out.decode().replace('\n', ''))
        else:
            if len(get_device) == 1:
                out = self.__shell_pipe(cmd=self.adb_check_version)
                yield(out.decode().replace('\n', ''))
            else:
                for i in get_device:
                    out = self.__shell_pipe(cmd='adb -s %s shell getprop ro.build.version.release'%i)
                    yield(out.decode().replace('\n', ''))
