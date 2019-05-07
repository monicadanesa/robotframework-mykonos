import time
from alog import debug, info, error
from mykonos.core.core import Core

class KeyEvent(Core):
    def __init__(self):
        self.device_mobile = self.device()

    def press_keycode(self, *args, **settings):
        """ press key on android device
        keysupport :
        home, back, left, right
        up, down, center, menu
        search, enter, delete(or del)
        recent(recent apps), volume_up, volume_down
        volume_mute, camera, power

        example:
        ke = KeyEvent(data)
        ke.press_keyword("back")
        """
        if 'locator' in settings:
            locator = setting['locator']

            del settings['locator']
            return locator.press(*args, **settings)
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device.press(*args, **settings)
            else:
                return self.device_mobile.press(*args, **settings)

    def long_press(self, *args, **settings):
        try:
            start = time.time()
            time.process_time
            elapse = 0

            seconds = settings['timer']
            del settings['timer']

            while elapsed <= seconds:
                elapsed = time.time()-start

            time.sleep(1)
            self.press_keycode(*args, **settings)

            return True

        except TimeoutError as err:
            error(err)
