import time
from mykonos.core.core import Core


class KeyEvent(Core):
    """Devine all global variable."""

    def __init__(self):
        """Call device from Core."""
        self.device_mobile = self.device()

    def press_keycode(self, *args, **setting):
        """Press key on android device.

        keysupport :
        home, back, left, right
        up, down, center, menu
        search, enter, delete(or del)
        recent(recent apps), volume_up, volume_down
        volume_mute, camera, power

        HOW TO CALL IN ROBOT FRAMEWORK
        | Long Press                  |back

        With device:
        | ${device}=  Scan Current Device  |  ${emulator}
        | Long Press                       |device=${device}  |back
        """
        if 'locator' in setting:
            locator = setting['locator']

            del setting['locator']
            return locator.press(*args, **setting)
        else:
            if 'device' in setting:
                device = setting['device']
                del setting['device']

                return device.press(*args, **setting)
            else:
                return self.device_mobile.press(*args, **setting)

    def long_press(self, *args, **setting):
        """Long press of Android.

        HOW TO CALL IN ROBOT FRAMEWORK
        | Long Press                  |back  |timer=1

        With device:
        | ${device}=  Scan Current Device  |  ${emulator}
        | Long Press                       |device=${device}  |back  |timer=1

        Return:
        True or False
        """
        try:
            start = time.time()
            time.process_time
            elapsed = 0

            seconds = setting['timer']
            del setting['timer']

            while elapsed <= seconds:
                elapsed = time.time()-start

            time.sleep(1)
            self.press_keycode(*args, **setting)

            return True

        except Exception:
            return False
