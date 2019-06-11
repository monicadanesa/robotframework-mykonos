from mykonos.core.core import Core


class GlobalElement(Core):
    """ Element class for all method that related with keywords Mykonos."""

    def __init__(self):
        self.device_mobile = self.device()
        self.get = GetCondions()

    def open_notification(self, **settings):
        """Open notification of Android.

        HOW TO CALL IN ROBOT FRAMEWORK
        | Open notification                  |

        With device:
        | ${device}=  Scan Current Device  |  ${emulator}
        | Open notification                  |  device=${device}

        Return:
        True or False
        """

        if 'device' in settings:
            device = settings['device']
            return device.open.notification()
        else:
            return self.device_mobile.open.notification()

    def open_quick_settings(self, **settings):
        """Open Quick setting of Android.

        HOW TO CALL IN ROBOT FRAMEWORK
        | Open Quick setting                 |

        With device:
        | ${device}=  Scan Current Device  |  ${emulator}
        | Open Quick setting                |  device=${device}

        Return:
        True or False
        """
        if 'device' in settings:
            device = settings['device']
            return device.open.quick_settings()
        else:
            return self.device_mobile.open.quick_settings()

    def clear_text(self, *argument, **settings):
        """Clear text on text field base on locator.
        HOW TO CALL IN ROBOT FRAMEWORK
        |  Clear Text                         |  className=sample class

        With locator:
        | ${get_locator}= Get Locator         | text=sample text
        | Clear Text                          | locator=${get_locator}

        With device:
        | ${device}=  Scan Current Device   | ${emulator}
        | Clear Text                          | device=${device}  text=sample

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
        """Input text on text field base on locator.
        HOW TO CALL IN ROBOT FRAMEWORK
        |  Input Text                   |  className=sample class    input=text

        With locator:
        | ${get_locator}= Get Locator   | text=sample text
        | Input Text                    | locator=${get_locator}     input=text

        With device:
        | ${device}=  Scan Current Device   | ${emulator}
        | Input Text        | device=${device}  text=attribute input=text

        Return:
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

    def count_elements(self, *argument, **settings):
        """Count total element from the page.

         HOW TO CALL IN ROBOT FRAMEWORK

         |  Count Elements                   |  className=sample class
         with locator:
         | ${get_locator}= Get Locator       | text=sample text
         | Count Elements                    | locator=${get_locator}

         Return:
         total of elements (int)
        """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.count
        else:
            return self.device_mobile(*argument, **settings).count

    def turn_on_screen(self, **settings):
        """Call keyword_turn_on_screen.

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Turn On Screen

        return : True or False
        """
        return self.device(**settings).screen.on()

    def turn_off_screen(self, **settings):
        """Call keyword_turn_off_screen.

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Turn Off Screen

        return : True or False
        """
        return self.device(**settings).screen.off()

    def dump_xml(self, *args):
        """Dump hierarchy of ui and will be saved as hierarchy.xml.

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Dump XML

        return : xml file of device
        """
        return self.device().dump(*args)

    def capture_screen(self, file=None):
        """Capture screen of device testing.

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Capture Screen

        with file name:
        | Capture Screen        | file=sample

        return : screen capture of device(*.png)
        """
        if file is not None:
            return self.device().screenshot(file+'.png')
        else:
            self.index += 1
            filename = 'mykonos-screenshot-%d.png' % self.index
            return self.device().screenshot(filename)


class Click(Core):

    def __init__(self):
        self.device_mobile = self.device()

    def click_element(self, *argument, **settings):
        """Click on UI base on locator.

        HOW TO CALL IN ROBOT FRAMEWORK
        |  Click Element                    | className=sample class

        With locator:
        | ${get_locator}= Get Locator       | text=sample text
        |  Click Element                    | locator=${get_locator}=

        With device:
        | ${device}=  Scan Current Device  | ${emulator}
        | Click Element                     | device=${device}    text=sample

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
            elif 'watcher' in settings:
                watcher = settings['watcher']
                del settings['watcher']

                return watcher.click(*argument, **settings)
            else:
                return self.device_mobile(*argument, **settings).click()

    def long_click_element(self, *argument, **settings):
        """Long click on UI base on locator.

        HOW TO CALL IN ROBOT FRAMEWORK
        |  Long Click Element                 | className=sample class

        With locator:
        | ${get_locator}= Get Locator         | text=sample text
        |  Long Click Element                 | locator=${get_locator}

        With device:
        | ${device}=  Scan Current Device   | ${emulator}
        |  Long Click Element                 | device=${device}  text=sample

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

    def click_a_point(self, *argument, **settings):
            """Click into pointer target location.

             HOW TO CALL IN ROBOT FRAMEWORK
             |  CLick A Point         |className=sample class    |x=10   |y=20

             With device:
             | ${device}=  Scan Current Device   |${emulator}
             | Click A Point  |device=${device}  |className=sample |x=10  |y=20

             Return:
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


class GetCondions(Core):
    def __init__(self):
        self.device_mobile = self.device()

    def get_text(self, *argument, **settings):
        """Get text from element base on locator.
        HOW TO CALL IN ROBOT FRAMEWORK
        |  Get Text                          |  className=sample class

        With locator:
        | ${get_locator}= Get Locator        | text=sample text
        | Get Text                           | locator=${get_locator}

        With device:
        | ${device}=  Scan Current Device  | ${emulator}
        |  Get Text                | device=${device}  className=sample

        Return:
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
        """Get element attribute keyword on Android Device.
        List of Elements:
         childCount, bounds, className, contentDescription,
         packageName, resourceName, text, visibleBounds,
         checkable, checked, clickable, enabled, focusable,
         focused, longClickable, scrollable, selected
         HOW TO CALL IN ROBOT FRAMEWORK
         |Get Element Attribute         |  className=sample  element=text

         With locator:
         | ${get_locator}= Get Locator  | text=sample text
         | Get Element Attribute        | locator=${get_locator}   element=text

         With device:
         | ${device}=  Scan Current Device    | ${emulator}
         | Get Element Attribute  | device=${device} text=sample  element=index

         Return:
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

    def get_element(self, *argument, **settings):
        """Call keyword_device_info.

        HOW TO CALL IN ROBOT FRAMEWORK:
        without device :
        | Get Element    |

        with device :
        | ${device}=  Scan Current Device         | ${emulator}
        | Get Element                               | device=${device}

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
        """Get element by coordinate x.

        HOW TO CALL IN ROBOT FRAMEWORK:
        | Get Element By Coordinate X  |  className=sample class

        return :
        coordinate x(int)
        """
        bound = self.get_element_attribute(element='bounds', *argument, **settings)

        bottom = bound['bottom']
        top = bound['top']
        elm_x = (top+bottom)+top

        return elm_x

    def get_element_by_coordinate_y(self, *argument, **settings):
        """Get element by coordinate y.

        HOW TO CALL IN ROBOT FRAMEWORK:
        | Get Element By Coordinate Y  |  className=sample class

        Return :
        coordinate y(int)
        """
        bound = self.get_element_attribute(element='bounds', *argument, **settings)
        display_height = self.get_height()
        height = display_height
        left = bound['left']
        right = bound['right']
        elm_y = height-(right+left)
        return elm_y

    def get_width(self):
        """Get width from display of device.

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Get Width

        Return : width of device(int)
        """
        get_device = self.device()
        return get_device.info['displayWidth']

    def get_height(self):
        """Get height from display of device.

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Get Height

        Return : width of device(int)
        """
        get_device = self.device()
        return get_device.info['displayHeight']


class ExpectedConditions(Core):
    def __init__(self):
        self.device_mobile = self.device()
        self.get_conditions = GetCondions()

    def page_should_contain_element(self, *argument, **settings):
        """Page should contain element.

        HOW TO CALL IN ROBOT FRAMEWORK:
        | Page Should Contain Element | className=sample class
        """
        element = self.get_conditions.get_element(*argument, **settings)

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
        """Page should contain text.

        HOW TO CALL IN ROBOT FRAMEWORK
        | Page Should Contain Text | text=sample text
        """
        # text = self.get_conditions.get_text(*argument, **settings)
        text = settings['text']

        if 'device' in settings:
            device = settings['device']
            del settings['device']
            return device(*argument, **settings).exists
        else:
            return self.device_mobile(*argument, **settings).exists

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

    def page_should_not_contain_element(self, *argument, **settings):
        """Page should not contain element.
        HOW TO CALL IN ROBOT FRAMEWORK
        | Page Should Not Contain Element | text=sample element
        """
        element = self.get_conditions.get_element(*argument, **settings)

        if 'locator' in settings:
            locator = settings['locator']
            found = locator[element].exists
            if found is False:
                return False
            elif found is True:
                return ValueError('found element')
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                found = self.__get_device_global(*argument, **settings).exists
                if found is True:
                    return False
                else:
                    raise True

    def page_should_not_contain_text(self, *argument, **settings):
        """Page should contain text
        HOW TO CALL IN ROBOT FRAMEWORK
        | Page Should Contain Text | text=sample text
        """
        text = self.get_conditions.get_text(*argument, **settings)

        if 'locator' in settings:
            locator = settings['locator']
            found = locator[text].exists
            if found is False:
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

    def text_should_be_visible(self, *argument, **settings):
        """text should be visible
        HOW TO CALL IN ROBOT FRAMEWORK
        | Text Should Be Visible | text=sample text
        """
        text = self.get_conditions.get_text(*argument, **settings)

        if 'locator' in settings:
            locator = settings['locator']
            if locator[text].exists:
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
