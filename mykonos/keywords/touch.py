from mykonos.core.core import Core
from mykonos.keywords.management_device import ManagementDevice
from mykonos.keywords.decorators import Parallel

class Touch(Core):
    def __init__(self):
        self.device_mobile = self.device()
        self.management_device = ManagementDevice()

    def __get_device_global(self, device=None, *argument, **settings):
        if 'locator' in settings:
            device = settings['locator']
        else:
            if device is not None:
                devices = self.management_device.scan_current_device(device)
            else:
                devices = self.device_mobile(*argument, **settings)

        return devices

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
            elif 'to' in action:
                return mobile_device.scroll.to(**settings)
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

    @Parallel.device_check
    def swipe(self, sx, sy, ex, ey, steps=10, device=None, **settings):
        """Geasture swipe with interanction on device.
        Swipe from (sx, sy) to (ex, ey).
        **Example:**
        || Swipe        | sx=10  sy=10  ex=20   ey=20   |  steps=100
    """

        if device is not None:
            devices = self.management_device.scan_current_device(device)
            return devices.swipe(sx, sy, ex, ey, steps)
        else:
            return self.device_mobile.swipe(sx, sy, ex, ey, steps)

    @Parallel.device_check
    def swipe_with_direction(self, device=None, *argument, **settings):
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

        if device is not None:
            dvc = self.management_device.scan_current_device(device)
        else:
            dvc = self.device_mobile()

        if 'right' in direction:
            return dvc(*argument, **settings).swipe.right(steps=1)
        elif 'left' in direction:
            return dvc(*argument, **settings).swipe.left(steps=1)
        elif 'up' in direction:
            return dvc(*argument, **settings).swipe.up(steps=1)
        elif 'down' in direction:
            return dvc(*argument, **settings).swipe.down(steps=1)

    @Parallel.device_check
    def drag_screen(self, sx, sy, ex, ey, steps, device=None):
        """Geasture drag interanction on device.
        This keyword is used to drag another point ui object to another point ui object.
        **Example:**
        || Drag Screen    | sx=189 | sy=210 | ex=954 | ey=336   |  steps=100
        """

        if device is not None:
            devices = self.management_device.scan_current_device(device)
            return device().drag(sx, sy, ex, ey, steps)
        else:
            return self.device_mobile().drag(sx, sy, ex, ey, steps)

    @Parallel.device_check
    def pinch(self, device=None, *argument, **settings):
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

            if device is not None:
                dvc = self.management_device.scan_current_device(device)
            else:
                dvc = self.device_mobile()

            if 'In' in action:
                return dvc.pinch.In(percent=10, steps=10)
            elif 'Out' in action:
                return dvc.pinch.Out(percent=10, steps=10)
        else:
            raise Exception('Action is not available on ui automator')

    @Parallel.device_check
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
        if device is not None:
            dvc = self.management_device.scan_current_device(device)
        else:
            dvc = self.device_mobile()

        if 'action' in settings:
            action = settings['action']
            del settings['action']

            if 'horizontal forward' in action:
                return dvc.fling.horiz.forward(max_swipes=10)
            elif 'horizontal to begining' in action:
                return dvc.fling.horiz.toBeginning(max_swipes=10)
            elif 'horizontal backward' in action:
                return dvc.fling.horiz.backward(max_swipes=10)
            elif 'horizontal to end' in action:
                return dvc.fling.horiz.toEnd(max_swipes=10)
            elif 'vertical backward' in action:
                return dvc.fling.vert.backward(max_swipes=10)
            elif 'vertical to end' in action:
                return dvc.fling.vert.toEnd(max_swipes=10)
            elif 'vertical forward' in action:
                return dvc.fling.vert.forward(max_swipes=10)
            elif 'vertical to begining' in action:
                return dvc.fling.vert.toBeginning(max_swipes=10)
            else:
                raise Exception('Action is not available on ui automator')
        else:
            return dvc.fling()
