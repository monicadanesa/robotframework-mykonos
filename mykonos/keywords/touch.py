from alog import debug, error, info
from mykonos.core.core import Core

class Touch(Core):
    def __init__(self):
        self.device_mobile = self.device()

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

    def swipe(self, sx, sy, ex, ey, steps, **settings):
        """ geasture swipe with interanction on Android Device
        swipe from (sx, sy) to (ex, ey)
        example :
        tc = Touch(data)
        tc.swipe(189, 210, 954, 336, step=10)

        HOW TO CALL IN ROBOT FRAMEWORK:

        without device :
        | Swipe                             | sx=10  sy=10  ex=20   ey=20   |  steps=100

        with device :

        Define device on the first time:
        | ${device_1}=  Scan Current Device  |    ${emulator}
        | Swipe                              | sx=10  sy=10  ex=20   ey=20   |  steps=100  | device=${device_1}

        """

        if 'device' in settings:
            device = settings['device']

            del settings['device']
            return device.swipe(sx, sy, ex, ey, steps)
        else:
            return self.device_mobile.swipe(sx, sy, ex, ey, steps)


    def swipe_with_direction(self, *argument, **settings):
        """ gesture swipe with direction on Android Device
        swipe with direction : right, left, up and down

        without device :
        | Swipe                             | direction=right   |  steps=100
        | Swipe                             | direction=left    |  steps=100
        | Swipe                             | direction=up      |  steps=100
        | Swipe                             | direction=down    |  steps=100

        with device :

        Define device on the first time:
        | ${device_1}=  Scan Current Device | ${emulator}
        | Swipe                             | direction=right   |  steps=100    | device=${device_1}
        | Swipe                             | direction=left    |  steps=100    | device=${device_1}
        | Swipe                             | direction=up      |  steps=100    | device=${device_1}
        | Swipe                             | direction=down    |  steps=100    | device=${device_1}
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


    def drag_screen(self, sx, sy, ex, ey, steps=None, device=None):
        """ geasture drag interanction of Android Device
        example :
        tc = Touch(data)
        tc.drag_sceen(189, 210, 954, 336, step=10)
        """
        try:
            if device!=None:
                return device(*argument, **locator).drag(sx, sy, ex, ey, steps)
            else:
                return self.device_mobile().drag(sx, sy, ex, ey, steps)
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
                return device.scroll.horiz.forward(**settings)
            elif 'horizontal to begining' in action:
                return device.scroll.horiz.toBeginning(**settings)
            elif 'horizontal backward' in action:
                return device.scroll.horiz.backward(**settings)
            elif 'horizontal to end' in action:
                return device.scroll.horiz.toEnd(**settings)
            elif 'horizontal to' in action:
                return device.scroll.horiz.to(**settings)
            elif 'vertical backward' in action:
                return device.scroll.vert.backward(**settings)
            elif 'vertical to end' in action:
                return device.scroll.vert.toEnd(**settings)
            elif 'vertical forward' in action:
                return device.scroll.vert.forward(**settings)
            elif 'vertical to begining' in action:
                return device.scroll.vert.toBeginning(**settings)
            elif 'vertical to' in action:
                return device.scroll.vert.to(**settings)
            else:
                raise Exception('Action is not available on ui automator')
        else:
            return self.__get_device_scroll(self, *argument, **settings).scroll(steps=10)


    def scroll(self, *argument, **settings):
        """ scroll interanction on Android device

        HOW TO CALL IN ROBOT FRAMEWORK:
        how to use scroll horizontal:
           | Scroll                         | steps=100
           | Scroll                         | steps=100     action=horizontal forward
           | Scroll                         | steps=100  max_swipes=1   action=horizontal to begining
           | Scroll                         | textName='Calculator' clasName='sampleClass'    action=horizontal to
           | Scroll                         | action=horizontal backward
           | Scroll                         | action=horizontal to end

         how to use scroll vertical:
            | Scroll                       | steps=100
            | Scroll                       | steps=100      action=vertical forward
            | Scroll                       | steps=100 max_swipes=1     action=vertical to begining
            | Scroll                       | textName='Calculator' clasName='sampleClass'       action=vertical to
            | Scroll                       | action=vertical backward
            | Scroll                       | action=vertical to end

        Define device on the first time:
            | ${device_1}=  Scan Current Device  |    ${emulator}

        how to use scroll horizontal with device:
            | Scroll                         | steps=100                                        | device=${device_1}
            | Scroll                         | steps=100                                        | device=${device_1}      |  action=horizontal forward
            | Scroll                         | textName='Calculator' clasName='sampleClass'     | device=${device_1}      | action=horizontal to
            | Scroll                         | device=${device_1}                               |  action=horizontal backward
            | Scroll                         | device=${device_1}                               |  action=horizontal to end

        how to use scroll vertical with device:
            | Scroll                         | steps=100                                        | device=${device_1}
            | Scroll                         | steps=100                                        | device=${device_1}      |  action=vertical forward
            | Scroll                         | textName='Calculator' clasName='sampleClass'     | device=${device_1}      | action=vertical to
            | Scroll                         | device=${device_1}                               |  action=vertical backward
            | Scroll                         | device=${device_1}                               |  action=vertical to end
         """
        return self.__check_action_device_scroll(self, *argument, **settings)

    def pinch(self, *argument, **settings):
        """ pinch interaction on Android Device

        HOW TO CALL IN ROBOT FRAMEWORK:
        without element locator:
           | Pinch                          | steps=100     action=In    percent=100
           | Pinch                          | steps=100     action=Out   percent=100

       with element locator
          | Pinch                          | steps=100     action=In    percent=100     className=sample class
          | Pinch                          | steps=100     action=Out   percent=100     className=sample class


       with device
          |  ${device_1}=  Scan Current Device  |    ${emulator}

         | Pinch                          | steps=100     action=In    percent=100    device=${device_1}
         | Pinch                          | steps=100     action=Out   percent=100    device=${device_1}

         | Pinch                          | steps=100     action=In    percent=100     className=sample class   device=${device_1}
         | Pinch                          | steps=100     action=Out   percent=100     className=sample class   device=${device_1}


        return :
        True and False
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
