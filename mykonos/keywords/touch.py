from mykonos.core.core import Core
from mykonos.keywords.management_device import ManagementDevice
from mykonos.keywords.decorators import Decorators, Parallel

class Touch(Core):
    def __init__(self):
        self.device_mobile = self.device()
        self.management_device = ManagementDevice()

    def __get_device_global(self, *argument, **settings):
        if 'locator' in settings:
            device = settings['locator']
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                device = device(*argument, **settings)
            else:
                device = self.device_mobile(*argument, **settings)

        return device


    @Parallel.device_check
    def scroll(self, device=None, *argument, **settings):
        """Scroll interanction on device.
        This keyword is used to perfom scroll on device.
        **Example:**
        How to use scroll horizontal:
        || Scroll     | steps=100
        || Scroll     | steps=100     action=horizontal forward
        || Scroll     | steps=100  max_swipes=1   action=horizontal to begining
        || Scroll     | textName='Calculator' clasName='sampleClass'    action=horizontal to
        || Scroll     | action=horizontal backward
        || Scroll     | action=horizontal to end
        How to use scroll vertical:
        || Scroll    | steps=100
        || Scroll    | steps=100      action=vertical forward
        || Scroll    | steps=100 max_swipes=1     action=vertical to begining
        || Scroll    | textName='Calculator' clasName='sampleClass'       action=vertical to
        || Scroll    | action=vertical backward
        || Scroll    | action=vertical to end
                 """
        if device is not None:

            if isinstance(device, str):
                mobile_device = self.management_device.scan_current_device(device)(scrollable=True)
            else:
                mobile_device = []
                mobile_device.append(self.management_device.scan_current_device(device)(scrollable=True))
        else:
                mobile_device = self.device_mobile(scrollable=True)

        if 'action' in settings:
            action = settings['action']
            del settings['action']

            if 'horizontal forward' in action:
                return mobile_device.scroll.horiz.forward(**settings)
            elif 'horizontal to begining' in action:
                return mobile_device.scroll.horiz.toBeginning(**settings)
            elif 'horizontal backward' in action:
                return mobile_device.scroll.horiz.backward(**settings)
            elif 'horizontal to end' in action:
                return mobile_device.scroll.horiz.toEnd(**settings)
            elif 'horizontal to' in action:
                return mobile_device.scroll.horiz.to(**settings)
            elif 'vertical backward' in action:
                return mobile_device.scroll.vert.backward(**settings)
            elif 'vertical to end' in action:
                return mobile_device.scroll.vert.toEnd(**settings)
            elif 'vertical forward' in action:
                return mobile_device.scroll.vert.forward(**settings)
            elif 'vertical to begining' in action:
                return mobile_device.scroll.vert.toBeginning(**settings)
            elif 'vertical to' in action:
                return mobile_device.scroll.vert.to(**settings)
            else:
                raise Exception('Action is not available on ui automator')
        else:
            return mobile_device.scroll(steps=10)


    def __check_action_device_fling(self, *argument, **settings):
        device = self.__get_device_scroll(self, *argument, **settings)

        if 'action' in settings:
            action = settings['action']
            del settings['action']

            if 'horizontal forward' in action:
                return device.fling.horiz.forward(max_swipes=10)
            elif 'horizontal to begining' in action:
                return device.fling.horiz.toBeginning(max_swipes=10)
            elif 'horizontal backward' in action:
                return device.fling.horiz.backward(max_swipes=10)
            elif 'horizontal to end' in action:
                return device.fling.horiz.toEnd(max_swipes=10)
            elif 'vertical backward' in action:
                return device.fling.vert.backward(max_swipes=10)
            elif 'vertical to end' in action:
                return device.fling.vert.toEnd(max_swipes=10)
            elif 'vertical forward' in action:
                return device.fling.vert.forward(max_swipes=10)
            elif 'vertical to begining' in action:
                return device.fling.vert.toBeginning(max_swipes=10)
            else:
                raise Exception('Action is not available on ui automator')
        else:
            return self.__get_device_scroll(self, *argument, **settings).fling()

    def swipe(self, sx, sy, ex, ey, steps, **settings):
        """Geasture swipe with interanction on device.
        Swipe from (sx, sy) to (ex, ey).
        **Example:**
        || Swipe        | sx=10  sy=10  ex=20   ey=20   |  steps=100
        """

        if 'device' in settings:
            device = settings['device']

            del settings['device']
            return device.swipe(sx, sy, ex, ey, steps)
        else:
            return self.device_mobile.swipe(sx, sy, ex, ey, steps)

    def swipe_with_direction(self, *argument, **settings):
        """Gesture swipe with direction on device.
        Swipe with direction : right, left, up and down
        **Example:**
        ||Swipe                             | direction=right   |  steps=100
        ||Swipe                             | direction=left    |  steps=100
        ||Swipe                             | direction=up      |  steps=100
        ||Swipe                             | direction=down    |  steps=100
        """
        direction = settings['direction']
        del settings['direction']

        if 'steps' in settings:
            steps = settings['steps']
            del settings['steps']

        dvc = self.__get_device_global(*argument, **settings)

        if 'right' in direction:
            return dvc.swipe.right(steps=1)
        elif 'left' in direction:
            return dvc.swipe.left(steps=1)
        elif 'up' in direction:
            return dvc.swipe.up(steps=1)
        elif 'down' in direction:
            return dvc.swipe.down(steps=1)

    def drag_screen(self, sx, sy, ex, ey, steps, *argument, **settings):
        """Geasture drag interanction on device.
        This keyword is used to drag another point ui object to another point ui object.
        **Example:**
        || Drag Screen    | sx=189 | sy=210 | ex=954 | ey=336   |  steps=100
        """
        device = settings['device']

        if device is not None:
            return device(*argument, **settings).drag(sx, sy, ex, ey, steps)
        else:
            return self.device_mobile().drag(sx, sy, ex, ey, steps)


    @Decorators.android_version
    def pinch(self, *argument, **settings):
        """Pinch interaction on Device
        **Example:**
        || Pinch      | steps=100     action=In    percent=100
        || Pinch      | steps=100     action=Out   percent=100
        """

        if 'percent' in settings:
            percent = settings['percent']

            del settings['percent']

        if 'steps' in settings:
            steps = settings['steps']

            del settings['steps']

        if 'action' in settings:
            action = settings['action']
            del settings['action']

            device = self.__get_device_global(*argument, **settings)

            if 'In' in action:
                return device.pinch.In(percent=10, steps=10)
            elif 'Out' in action:
                return device.pinch.Out(percent=10, steps=10)
        else:
            raise Exception('Action is not available on ui automator')

    @Decorators.android_version
    def fling(self, *argument, **settings):
        """Fling interanction on Android device.
        This keyword is used to perform fling to spesific ui object.
        **Example:**
        How to user without action:
        || Fling
        How to use fling horizontal:
        || Fling            | action=horizontal forward
        || Fling            | max_swipes=1   action=horizontal to begining
        || Fling            | action=horizontal backward
        || Fling            | action=horizontal to end
        How to use scroll vertical:
        || Fling            | action=vertical forward
        || Fling            | max_swipes=1   action=vertical to begining
        || Fling            | action=vertical backward
        || Fling            | action=vertical to end
         """
        return self.__check_action_device_fling(self, *argument, **settings)
