import time
from mykonos.core.core import Core


class KeyEvent(Core):
    def __init__(self):
        self.device_mobile = self.device()

    def press_keycode(self, *argument, **settings):
        """Press key on device.

        This keyword is used to press key on device.

        **Key Support:**

        * home, back, left, right
        * up, down, center, menu
        * search, enter, delete(or del)
        * recent(recent apps), volume_up, volume_down
        * volume_mute, camera, power

        **Example:**

        || Press Keycode                  |back
        """
        if 'locator' in settings:
            locator = settings['locator']

            del settings['locator']
            return locator.press(*argument, **settings)
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device.press(*argument, **settings)
            elif 'watcher' in settings:
                watcher = settings['watcher']
                del settings['watcher']

                return watcher.press(*argument, **settings)
            else:
                return self.device_mobile.press(*argument, **settings)

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
