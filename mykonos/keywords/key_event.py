import time
from mykonos.core.core import Core
from mykonos.keywords.management_device import ManagementDevice
from mykonos.keywords.decorators import Parallel


class KeyEvent(Core):
    def __init__(self):
        self.device_mobile = self.device()
        self.management_device = ManagementDevice()

    @Parallel.device_check
    def press_keycode(self, device=None, *argument, **settings):
        """Press key on device.

        This keyword is used to press key on device.

        **Key Support:**

        * home, back, left, right
        * up, down, center, menu
        * search, enter, delete(or del)
        * recent(recent apps), volume_up, volume_down
        * volume_mute, camera, power

        **Example:**

        || Press Keycode                  |keys=back
        """
        if 'keys' in settings:
            keys = settings['keys']
            del settings['keys']

        if 'locator' in settings:
            locator = settings['locator']

            del settings['locator']
            return locator.press(*argument, **settings)
        else:
            if device is not None:
                get_device = self.management_device.scan_current_device(device)
                return get_device.press(keys)

            elif 'watcher' in settings:
                watcher = settings['watcher']
                del settings['watcher']

                return watcher.press(keyss)
            else:
                return self.device_mobile.press(keys)

    def long_press(self, *args, **setting):
        """Long press on device.

        This keyword is used to press key on device with optional duration.

        **Example:**

        || Long Press                  |back  |timer=100

        **Return:**
        True or False
        """
        try:
            start = time.time()
            time.process_time
            elapsed = 0

            timer = setting['timer']
            del setting['timer']

            while elapsed <= timer:
                elapsed = time.time()-start

            self.press_keycode(*args, **setting)

            return True

        except Exception:
            return False
