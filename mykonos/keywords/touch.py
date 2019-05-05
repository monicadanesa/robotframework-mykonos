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

    def __check_action_device_scroll(self, *argument, **settings):
        device = self.__get_device_scroll(self, *argument, **settings)

        if 'action' in settings :
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
        else:
            return self.__get_device_scroll(self, *argument, **settings).scroll(steps=10)


    def scoll(self, *argument, **settings):
        """ scroll interanction on Android device

        HOW TO CALL IN ROBOT FRAMEWORK:
        how to use scroll horizontal:
           | Scroll                         | steps=100
           | Scroll horizontal forward      | steps=100
           | Scroll horizontal to begining  | steps=100, max_swipes=1
           | Scroll horizontal to           | textName='Calculator', clasName='sampleClass'
           | Scroll horizontal backward     |
           | Scroll horizontal to end       |

         how to use scroll vertical:
            | Scroll                       | steps=100
            | Scroll vertical forward      | steps=100
            | Scroll vertical to begining  | steps=100, max_swipes=1
            | Scroll vertical to           | textName='Calculator', clasName='sampleClass'
            | Scroll vertical backward     |
            | Scroll vertical to end       |

        Define device on the first time:
            | ${device_1}=  Scan Current Device  |    ${emulator}

        how to use scroll horizontal with device:
            | Scroll                         | steps=100                                        | device=${device_1}
            | Scroll horizontal forward      | steps=100                                        | device=${device_1}
            | Scroll horizontal to           | textName='Calculator', clasName='sampleClass'    | device=${device_1}
            | Scroll horizontal backward     | device=${device_1}
            | Scroll horizontal to end       | device=${device_1}

        how to use scroll vertical with device:
            | scroll                       | steps=100                                        | device=${device_1}
            | scroll vertical forward      | steps=100                                        | device=${device_1}
            | scroll vertical to begining  | steps=100, max_swipes=1                          | device=${device_1}
            | scroll vertical to           | textName='Calculator', clasName='sampleClass'    | device=${device_1}
            | scroll vertical backward     | device=${device_1}
            | scroll vertical to end       | device=${device_1}

         """
        return self.__check_action_device_scroll(self, *argument, **settings)
