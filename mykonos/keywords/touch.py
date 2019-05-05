from alog import debug, error, info
from mykonos.core.core import Core

class Touch(Core):
    def __init__(self):
        self.device_mobile = self.device()

    def swipe_screen(self, sx, sy, ex, ey, step=None, device=None):
        """ geasture swipe interanction of Android Device
        swipe from (sx, sy) to (ex, ey)
        example :
        tc = Touch(data)
        tc.swipe_screen(189, 210, 954, 336, step=10)
        """
        try:
            if device!=None:
                return device(*argument, **locator).swipe(sx, sy, ex, ey, step)
            else:
                return self.device_mobile(*argument, **locator).swipe(sx, sy, ex, ey, step)
        except ValueError as error:
             raise ValueError('device cannot be swipe' + error)

    def drag_screen(self, sx, sy, ex, ey, step=None, device=None):
        """ geasture drag interanction of Android Device
        example :
        tc = Touch(data)
        tc.drag_sceen(189, 210, 954, 336, step=10)
        """
        try:
            if device!=None:
                return device(*argument, **locator).drag(sx, sy, ex, ey, step)
            else:
                return self.device_mobile().drag(sx, sy, ex, ey, step)
        except ValueError as error:
             raise ValueError('device cannot be drag' + error)


    def __get_device_scroll(self, *argument, **settings):
        if 'device' in settings:
            device = settings['device']
            del settings['device']
            return device(scrollable=True)
        else:
            return self.device_mobile(scrollable=True)

    def __get_action_device_scroll(self, *argument, **settings):
        device = self.__get_device_scroll(self, *argument, **settings)

        action = settings['action']
        del settings['action']

        if 'horizontal forward' in action:
            return device.scroll.horiz.forward(steps=100)
        elif 'horizontal to begining' in action:
            return device.scroll.horiz.toBeginning(steps=100, max_swipes=1)
        elif 'horizontal to' in action:
            return device.scroll.horiz.to(**settings)
        elif 'horizontal backward' in action:
            return device.scroll.horiz.backward()
        elif 'horizontal to end' in action:
            return device.scroll.horiz.toEnd()
        elif 'vertical backward' in action:
            return device.scroll.vert.backward()
        elif 'vertical to end' in action:
            return device.scroll.vert.toEnd()
        elif 'vertical forward' in action:
            return device.scroll.vert.forward(steps=100)
        elif 'vertical to begining' in action:
            return device.scroll.vert.toBeginning(steps=100, max_swipes=1)
        elif 'vertical to' in action:
            return device.scroll.vert.to(**settings)
        else:
            raise Exception('Action is not available on ui automator')


    def scoll(self, *argument, **settings):
        """ scroll interanction on Android device

        how to use scroll horizontal:
           | scroll                         | steps=100
           | scroll horizontal forward      | steps=100
           | scroll horizontal to begining  | steps=100, max_swipes=1
           | scroll horizontal to           | textName='Calculator', clasName='sampleClass'
           | scroll horizontal backward     |
           | scroll horizontal to end       |

         how to use scroll vertical:
            | scroll                       | steps=100
            | scroll vertical forward      | steps=100
            | scroll vertical to begining  | steps=100, max_swipes=1
            | scroll vertical to           | textName='Calculator', clasName='sampleClass'
            | scroll vertical backward     |
            | scroll vertical to end       |

        Define device on the first time:

         """
        device = self.__get_device_scroll(self, *argument, **settings)
        if 'action' in settings :
            return self.__get_action_device_scroll(self, *argument, **settings)
        else:
            return device.scroll(*argument, **settings)
