from alog import debug, info, error
from mykonos.core.core import Core

class Element(Core):

    def __init__(self):
        self.device_mobile = self.device()

    def open_notification(self, **settings):
        """ open notification of Android"""
        if 'locator' in settings:
            locator = settings['locator']
            return locator.open.notification()
        else:
            if 'device' in settings:
                device = settings['device']
                return device.open.notification()
            else:
                return self.device_mobile.open.notification()

    def open_quick_settingss(self, **settings):
        """ open quick settingss of Android"""
        if 'locator' in settings:
            locator = settings['locator']
            return locator.open.quick_settingss()
        else:
            if 'device' in settings:
                device = settings['device']
                return device.open.quick_settingss()
            else:
                return self.device_mobile.open.quick_settingss()

    def click_element(self, *argument, **settings):
        """ click on UI base on locator """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.click()
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device(*argument, **settings).click()
            else:
                return self.device_mobile(*argument, **settings).click()

    def long_click_element(self, *argument, **settings):
        """ long click on UI base on locator """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.long_click()
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **locator).long_click()
            else:
                return self.device_mobile(*argument, **settings).long_click()


    def clear_text(self, *argument, **settings):
        """ clear text on text field base on locator """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.clear_text()
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).clear_text()
            else:
                return self.device_mobile(*argument, **settings).clear_text()

    def input_text(self, *argument, **settings):
        """ input text on text field base on locator """
        input = settings['input']
        del settings['input']

        if 'locator' in settings:
            locator = settings['locator']
            return locator.set_text(input)
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device(*argument, **settings).set_text(input)
            else:
                return self.device_mobile(*argument, **settings).set_text(input)


    def get_text(self, *argument, **settings):
        """ get text from element base on locator """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.info['text']
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).info['text']
            else:
                return self.device_mobile(*argument, **settings).info['text']


    def get_element_attribute(self, *argument, **settings):
        """ get element attribute using list of the elements :
        List of Elements:
         childCount, bounds, className, contentDescription,
         packageName, resourceName, text, visibleBounds,
         checkable, checked, clickable, enabled, focusable,
         focused, longClickable, scrollable, selected

         example :
         get_element_attribute(element="text", className="")
         """
        element = settings['element']
        del settings['element']

        if 'locator' in settings:
            locator = settings['locator']
            return locator.info[element]
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device(*argument, **settings).info[element]
            else:
                return self.device_mobile(*argument, **settings).info[element]

    def click_a_point(self, *argument, **settings):
        """Click into pointer target location
        example :
        click_a_point(x=value, y=value)
        """
        if 'x' in settings and 'y' in settings:
            x = settings['x']
            y = settings['y']
            del settings['x']
            del settings['y']
        else:
            raise ValueError('pointer x or y refused')
        if 'device' in settings:
            device = settings['device']
            del settings['device']
            return device(*argument, **locator).click(x, y)
        else:
            return self.device_mobile().click(x, y)

    def get_element(self, *argument, **settings):
        """ Call keyword_device_info
        and will return dictionary
        Example :
        Example_Code:orcestrator = Orcestrator(data)
        orcestrator.device_info
        Example_robot_framework:
        | ${device_info} | Device Info |
        | Log Dictionary | ${device_info}  |
        Return:
        {'currentPackageName': 'com.google.android.apps.nexuslauncher',
         'displayHeight': 1794,
         'displayRotation': 0,
         'displaySizeDpX': 411,
         'displaySizeDpY': 731,
         'displayWidth': 1080,
         'productName': 'sdk_google_phone_x86',
         'screenOn': True,
         'sdkInt': 25,
         'naturalOrientation': True}
        """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.info
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device(*argument, **settings).info
            else:
                return self.device_mobile(*argument, **settings).info

    def count_elements(self, *argument, **settings):
        """ Count total element from the page
        - locator is used for user who want to get locator first before count element
        example :
        element = get_locator("className=name of class ")
        total_element = count_elements(locator=element)

        - device mobile is used for user who input element directly on device
        total_element = count_elements("className=name of class ")

        """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.count
        else:
            return self.device_mobile(*argument, **settings).count

    def get_width(self):
        """ Get width from display of device
        example : get_width()
        return : int
        """
        get_device = self.device()
        return get_device.info['displayWidth']

    def get_height(self):
        """ Get height from display of device
        example : get_height()
        return : int
        """
        get_device = self.device()
        return get_device.info['displayHeight']
