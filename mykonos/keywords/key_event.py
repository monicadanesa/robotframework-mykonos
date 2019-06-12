import time
from mykonos.core.core import Core


class KeyEvent(Core):
    """Devine all global variable."""

    def __init__(self):
        """Call device from Core."""
        self.device_mobile = self.device()

    def press_keycode(self, *argument, **settings):
        """Press key on android device.

        keysupport :
        home, back, left, right
        up, down, center, menu
        search, enter, delete(or del)
        recent(recent apps), volume_up, volume_down
        volume_mute, camera, power

        HOW TO CALL IN ROBOT FRAMEWORK
        | Press Keycode                  |back

        With device:
        | ${device}=  Scan Current Device     |  ${emulator}
        | Press Keycode                       |device=${device}  |back
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
        """Long press of Android.

        HOW TO CALL IN ROBOT FRAMEWORK
        | Long Press                  |back  |timer=100
        With device:
        | ${device}=  Scan Current Device  |  ${emulator}
        | Long Press                       |device=${device}  |back  |timer=100

        Return:
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
