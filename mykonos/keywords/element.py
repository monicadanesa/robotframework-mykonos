from alog import debug, info, error
from mykonos.core.core import Core

class Element(Core):

    def __init__(self):
        self.device_mobile = self.device()

    def open_notification(self, **settings):
        """ open notification of Android

        HOW TO CALL IN ROBOT FRAMEWORK

        | Open notification                  |

        with device:
        | ${device_1}=  Scan Current Device  |  ${emulator}
        | Open notification                  |  device=${device_1}

        Return:
        True or False
        """

        if 'device' in settings:
            device = settings['device']
            return device.open.notification()
        else:
            return self.device_mobile.open.notification()

    def open_quick_settings(self, **settings):
        """ open quick settingss of Android
        HOW TO CALL IN ROBOT FRAMEWORK

        | Open Quick Notification                  |

        with device:
        | ${device_1}=  Scan Current Device        |  ${emulator}
        | Open Quick Notification                  |  device=${device_1}

        Return:
        True or False
        """

        if 'device' in settings:
            device = settings['device']
            return device.open.quick_settings()
        else:
            return self.device_mobile.open.quick_settings()

    def click_element(self, *argument, **settings):
        """ click on UI base on locator
        selector support :
        text, textContains, textMatches, textStartsWith
        className, classNameMatches
        description, descriptionContains, descriptionMatches, descriptionStartsWith
        checkable, checked, clickable, longClickable
        scrollable, enabled,focusable, focused, selected
        packageName, packageNameMatches
        resourceId, resourceIdMatches
        index, instance

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Click Element                    | className=sample class

        with locator:
        | ${get_locator}= Get Locator       | text=sample text
        |  Click Element                    | locator=${get_locator}

        with device:
        | ${device_1}=  Scan Current Device  | ${emulator}
        |  Click Element                     | device=${device_1}    text=sample text

        with locator and device
        | ${get_locator}= Get Locator        | text=sample text
        | ${device_1}=  Scan Current Device  | ${emulator}
        |  Click Element                     | device=${device_1}    locator=${get_locator}

        Return:
        True or False
         """
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
        """ long click on UI base on locator
        selector support :
        text, textContains, textMatches, textStartsWith
        className, classNameMatches
        description, descriptionContains, descriptionMatches, descriptionStartsWith
        checkable, checked, clickable, longClickable
        scrollable, enabled,focusable, focused, selected
        packageName, packageNameMatches
        resourceId, resourceIdMatches
        index, instance

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Long Click Element                    | className=sample class

        with locator:
        | ${get_locator}= Get Locator            | text=sample text
        |  Long Click Element                    | locator=${get_locator}

        with device:
        | ${device_1}=  Scan Current Device      | ${emulator}
        |  Long Click Element                    | device=${device_1}    text=sample text

        with locator and device
        | ${get_locator}= Get Locator           | text=sample text
        | ${device_1}=  Scan Current Device     | ${emulator}
        |  Long Click Element                   | device=${device_1}    locator=${get_locator}

        Return:
        True or False
         """
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
        """ clear text on text field base on locator
        selector support :
        text, textContains, textMatches, textStartsWith
        className, classNameMatches
        description, descriptionContains, descriptionMatches, descriptionStartsWith
        checkable, checked, clickable, longClickable
        scrollable, enabled,focusable, focused, selected
        packageName, packageNameMatches
        resourceId, resourceIdMatches
        index, instance

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Clear Text                            |  className=sample class

        with locator:
        | ${get_locator}= Get Locator            | text=sample text
        | Clear Text                             | locator=${get_locator}

        with device:
        | ${device_1}=  Scan Current Device      | ${emulator}
        |  Clear Text                            | device=${device_1}    text=sample text

        with locator and device
        | ${get_locator}= Get Locator           | text=sample text
        | ${device_1}=  Scan Current Device     | ${emulator}
        |  Clear Text                           | device=${device_1}    locator=${get_locator}

        """
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
        """ input text on text field base on locator
        selector support :
        text, textContains, textMatches, textStartsWith
        className, classNameMatches
        description, descriptionContains, descriptionMatches, descriptionStartsWith
        checkable, checked, clickable, longClickable
        scrollable, enabled,focusable, focused, selected
        packageName, packageNameMatches
        resourceId, resourceIdMatches
        index, instance

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Input Text                            |  className=sample class    input=Sampling text for input

        with locator:
        | ${get_locator}= Get Locator            | text=sample text
        | Input Text                             | locator=${get_locator}     input=Sampling text for input

        with device:
        | ${device_1}=  Scan Current Device      | ${emulator}
        |  Input Text                            | device=${device_1}    text=sample text   input=Sampling text for input

        with locator and device
        | ${get_locator}= Get Locator           | text=sample text
        | ${device_1}=  Scan Current Device     | ${emulator}
        |  Input Text                           | device=${device_1}    locator=${get_locator}      input=Sampling text for input

        return:
        True or False
        """
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
        """ get text from element base on locator
        selector support :
        text, textContains, textMatches, textStartsWith
        className, classNameMatches
        description, descriptionContains, descriptionMatches, descriptionStartsWith
        checkable, checked, clickable, longClickable
        scrollable, enabled,focusable, focused, selected
        packageName, packageNameMatches
        resourceId, resourceIdMatches
        index, instance

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Get Text                              |  className=sample class

        with locator:
        | ${get_locator}= Get Locator            | text=sample text
        | Get Text                               | locator=${get_locator}

        with device:
        | ${device_1}=  Scan Current Device      | ${emulator}
        |  Get Text                              | device=${device_1}    className=sample class

        with locator and device
        | ${get_locator}= Get Locator           | text=sample text
        | ${device_1}=  Scan Current Device     | ${emulator}
        |  Get Text                             | device=${device_1}    locator=${get_locator}

        return:
        String

        """
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


         HOW TO CALL IN ROBOT FRAMEWORK

         |  Get Element Attribute                             |  className=sample class

         with locator:
         | ${get_locator}= Get Locator                        | text=sample text
         | Get Element Attribute                              | locator=${get_locator}

         with device:
         | ${device_1}=  Scan Current Device                  | ${emulator}
         |  Get Element Attribute                             | device=${device_1}    className=sample class

         with locator and device
         | ${get_locator}= Get Locator                        | text=sample text
         | ${device_1}=  Scan Current Device                  | ${emulator}
         | Get Element Attribute                              | device=${device_1}    locator=${get_locator}

         return:
         attribute from element device
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

         HOW TO CALL IN ROBOT FRAMEWORK

         |  CLick A Point                            |  className=sample class                        | x=100     |  y=200

         with device:
         | ${device_1}=  Scan Current Device         | ${emulator}
         |  Click A Point                            | device=${device_1}   | className=sample class  | x=100     |  y=200

         return:
         True or False

        """
        if 'x' in settings and 'y' in settings:
            x = settings['x']
            y = settings['y']
            del settings['x']
            del settings['y']
        else:
            raise ValueError('pointer x or y is refused')


        if 'device' in settings:
            device = settings['device']
            del settings['device']
            return device(*argument, **settings).click(x, y)
        else:
            return self.device_mobile().click(x, y)

    def get_element(self, *argument, **settings):
        """ Call keyword_device_info
        and will return dictionary
        Example :
        Example_Code:orcestrator = Orcestrator(data)
        orcestrator.device_info

        HOW TO CALL IN ROBOT FRAMEWORK:
        without device :
        | Get Element    |

        with device :
        | ${device_1}=  Scan Current Device         | ${emulator}
        | Get Element                               | device=${device_1}

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
        if 'device' in settings:
            device = settings['device']
            del settings['device']

            return device(*argument, **settings).info
        else:
            return self.device_mobile(*argument, **settings).info

    def get_element_by_coordinate_x(self, *argument, **settings):
        """
        get element by coordinate x

        HOW TO CALL IN ROBOT FRAMEWORK:
        | Get Element By Coordinate X  |  className=sample class

        return :
        coordinate x(int)
        """
        bound = self.get_element_attribute(element='bounds', *argument, **settings)

        right = bound['right']
        left = bound['left']
        bottom = bound['bottom']
        top = bound['top']
        elm_x = (top+bottom)+top

        return elm_x

    def get_element_by_coordinate_y(self, *argument, **settings):
        """
        get element by coordinate y

        HOW TO CALL IN ROBOT FRAMEWORK:
        | Get Element By Coordinate Y  |  className=sample class

        return :
        coordinate y(int)

        """
        bound = self.get_element_attribute(element='bounds', *argument, **settings)
        display_height = self.get_height()
        height = display_height
        left = bound['left']
        right = bound['right']
        elm_y = height-(right+left)
        return elm_y

    def page_should_contain_element(self, *argument, **settings):
        """
        page should contain element
        HOW TO CALL IN ROBOT FRAMEWORK:
        | Page Should Contain Element | className=sample class
        """
        element = self.get_element(*argument, **settings)

        if 'locator' in settings:
            locator = settings['locator']
            if locator[element].exists:
                return True
            else:
                raise ValueError('locator not found')
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).exists
            else:
                return self.device_mobile(*argument, **settings).exists

    def page_should_contain_text(self, *argument, **settings):
        """
        page should contain text
        HOW TO CALL IN ROBOT FRAMEWORK
        | Page Should Contain Text | text=sample text
        """
        text = self.get_text(*argument, **settings)

        if 'locator' in settings:
            locator = settings['locator']
            if locator[text].exists:
                return True
            else:
                raise ValueError('text not found')
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).exists
            else:
                return self.device_mobile(*argument, **settings).exists

    def page_should_not_contain_element(self, *argument, **settings):
        """
        page should not contain element
        HOW TO CALL IN ROBOT FRAMEWORK
        | Page Should Not Contain Element | text=sample element
        """
        element = self.get_element(*argument, **settings)

        if 'locator' in settings:
            locator = settings['locator']
            found = locator[element].exists
            if found == False:
                return True
            else:
                return ValueError('found element')
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).exists
            else:
                return self.device_mobile(*argument, **settings).exists

    def page_should_not_contain_text(self, *argument, **settings):
        """
        page should contain text
        HOW TO CALL IN ROBOT FRAMEWORK
        | Page Should Contain Text | text=sample text
        """
        text = self.get_text(*argument, **settings)

        if 'locator' in settings:
            locator = settings['locator']
            found = locator[text].exists
            if found == False:
                return True
            else:
                return ValueError('device')
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).exists
            else:
                return self.device_mobile(*argument, **settings).exists

    def count_elements(self, *argument, **settings):
        """ Count total element from the page
        - locator is used for user who want to get locator first before count element
        example :
        element = get_locator("className=name of class ")
        total_element = count_elements(locator=element)

        - device mobile is used for user who input element directly on device
        total_element = count_elements("className=name of class ")

         HOW TO CALL IN ROBOT FRAMEWORK

         |  Count Elements                              |  className=sample class
         with locator:
         | ${get_locator}= Get Locator                  | text=sample text
         | Count Elements                               | locator=${get_locator}

         return:
         total of elements (int)
        """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.count
        else:
            return self.device_mobile(*argument, **settings).count

    def get_width(self):
        """ Get width from display of device
        example : get_width()

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Get Width

        return : width of device(int)
        """
        get_device = self.device()
        return get_device.info['displayWidth']

    def get_height(self):
        """ Get height from display of device
        example : get_height()

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Get Height

        return : width of device(int)
        """
        get_device = self.device()
        return get_device.info['displayHeight']
