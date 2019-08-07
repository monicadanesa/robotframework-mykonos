from robot.libraries.BuiltIn import BuiltIn
from mykonos.core.core import Core
from mykonos.keywords.management_device import ManagementDevice
from mykonos.keywords.decorators import Decorators, Parallel

class GlobalElement(Core):
    def __init__(self):
        self.get = GetConditions()
        self.device_mobile = self.device()
        self.management_device = ManagementDevice()

    @Parallel.device_check
    def open_notification(self, device=None, **settings):
        """Open notification a device.

        This keywords is used to open notification of device

        **Example:**
        || Open notification

        With Device/ Pararel :
        ||  @{emulator} =      |  192.168.1.1    | 192.168.1.2
        || Open notification   |device_parallel=@{emulator}


        """

        if device is not None:
            get_device = self.management_device.scan_current_device(device)
            return get_device().open.notification()
        else:
            return self.device_mobile.open.notification()

    @Parallel.device_check
    def open_quick_settings(self, device=None, **settings):
        """Open Quick Setting a device.

        This keywords is used to open setting of device

        **Example:**

        || Open Quick setting  |

        With Device/ Pararel :
        ||  @{emulator} =      |  192.168.1.1    | 192.168.1.2
        || Open Quick setting  |  device_parallel= @{emulator}

        """
        if device is not None:
            get_device = self.management_device.scan_current_device(device)
            return get_device().open.quick_settings()
        else:
            return self.device_mobile.open.quick_settings()

    @Parallel.device_check
    def clear_text(self, device=None, *argument, **settings):
        """Clear text on the text field base on locator.

        This keywords is used to clear text field.

        **Example:**

        ||Clear Text        |  className=sample class

        With Device/ Pararel :
        ||  @{emulator} =      |  192.168.1.1    | 192.168.1.2
        ||  Clear Text         | className=sample class     |device_parallel= @{emulator}
        """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.clear_text()
        else:
            if 'device' is not None:
                get_device = self.management_device.scan_current_device(device)
                return get_device(*argument, **settings).clear_text()
            else:
                return self.device_mobile(*argument, **settings).clear_text()

    @Parallel.device_check
    def input_text(self, device=None, *argument, **settings):
        """Input text on the text field base on locator.

        This keywords is used to input text into text field.

        **Example:**

        || Input Text        |  className=sample class    input=text

        With Device/ Pararel :
        ||  @{emulator} =      |  192.168.1.1    | 192.168.1.2
        ||  Input Text         |  className=sample class | input=text  | device_parallel=@{emulator}

        """
        input = settings['input']
        del settings['input']

        if 'locator' in settings:
            locator = settings['locator']
            return locator.set_text(input)
        else:
            if device is not None:
                get_device = self.management_device.scan_current_device(device)
                return get_device(*argument, **settings).set_text(input)
            else:
                return self.device_mobile(*argument, **settings).set_text(input)

    @Parallel.device_check
    def count_elements(self, device=None, *argument, **settings):
        """Count total element from the page.

        This keywords is used to count total element on the device page.

        **Example:**

        || Count Elements          |  className=sample class

        With Device/ Pararel :
        ||  @{emulator} =   | 192.168.1.1    | 192.168.1.2
        ||  Count Element   | device_parallel=@{emulator}

        **Return:**

        Total of elements (int)

        """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.count
        elif 'watcher' in settings:
            watcher = settings['watcher']
            del settings['watcher']

            return watcher.count
        else:
            if device is not None:
                get_device = self.management_device.scan_current_device(device)
                return get_device(*argument, **settings).count
            else:
                return self.device_mobile(*argument, **settings).count

    @Parallel.device_check
    def turn_on_screen(self, device=None, **settings):
        """Turn on Screen Device.

        **Example:**

        ||  Turn On Screen

        With Device/ Pararel :
        ||  @{emulator} =   | 192.168.1.1    | 192.168.1.2
        ||  Turn On Screen  | device_parallel=@{emulator}

        **Return:**

         True or False
        """
        if device is not None:
            get_device = self.management_device.scan_current_device(device)
            return get_device(**settings).screen.on()
        else:
            return self.device(**settings).screen.on()

    @Parallel.device_check
    def turn_off_screen(self, device=None, **settings):
        """Turn off Screen Device.

        **Example:**

        ||  Turn Off Screen

        With Device/ Pararel :
        ||  @{emulator} =   | 192.168.1.1    | 192.168.1.2
        ||  Turn Off Screen  | device_parallel=@{emulator}

        **Return:**

         True or False
        """
        if device is not None:
            get_device = self.management_device.scan_current_device(device)
            return get_device(**settings).screen.off()
        else:
            return self.device(**settings).screen.off()

    @Parallel.device_check
    def dump_xml(self, device=None, **settings):
        """Dump hierarchy of ui and will be saved as hierarchy.xml.

        **Example:**

        ||  Dump Xml        | file=sample.xml

        With Device /pararel :

        ||  @{emulator} =   |  192.168.1.1              | 192.168.1.2
        ||  Dump Xml        | file=sample.xml           | devices_pararel=@{emulator}

        **Return:**

        xml file of device
        """

        if 'file' in settings:
            file = settings['file']
            del settings['file']

        if device is not None:
            return self.management_device.scan_current_device(device).dump(file)
        else:
            return self.device().dump(file)

    @Parallel.device_check
    def capture_screen(self, file=None, device=None):
        """Capture screen of device testing.

        **Example:**

        ||  Capture Screen

        With file name:

        || Capture Screen        | file=sample

        With Device/ Pararel :
        ||  @{emulator} =   | 192.168.1.1    | 192.168.1.2
        ||   Capture Screen  | device_parallel=@{emulator}
        || Capture Screen    | file=sample  | device_parallel=@{emulator}

        **Return:**

        screen capture of device(*.png)
        """
        if file is not None:
            if device is not None:
                return self.device().screenshot(file+'.png')
            else:
                return self.management_device.scan_current_device(device).screenshot(file+'.png')
        else:
            index = 0
            index += 1
            filename = 'mykonos-screenshot-%d.png' % index
            if device is not None:
                return self.device().screenshot(filename)
            else:
                return self.management_device.scan_current_device(device).screenshot(filename)


class Click(Core):

    def __init__(self):
        self.device_mobile = self.device()
        self.management_device = ManagementDevice()

    @Parallel.device_check
    def click_element(self, device=None, *argument, **settings):
        """Click on UI base on locator.

        This keyword is used to click button or element of device.

        **Example:**

        ||  Click Element                    | className=sample class

        With Device/ Pararel :
        ||  @{emulator} =   | 192.168.1.1    | 192.168.1.2
        ||  Click Element                    | className=sample class  | device_parallel=@{emulator}
        """

        if 'locator' in settings:
            locator = settings['locator']
            return locator.click()

        else:
            if device is not None:
                get_devices = self.management_device.scan_current_device(device)
                return get_devices(*argument, **settings).click()

            elif 'watcher' in settings:
                watcher = settings['watcher']
                del settings['watcher']

                return watcher.click(*argument, **settings)
            else:
                return self.device_mobile(*argument, **settings).click()

    @Decorators.android_version
    def long_click_element(self, device=None, *argument, **settings):
        """Long click on UI base on locator.

        This keyword is used to long click button or element of device.


        **Example:**
        ||  Long Click Element                 | className=sample class

        With Device/ Pararel :
        ||  @{emulator} =   | 192.168.1.1    | 192.168.1.2
        ||  Long Click Element               | className=sample class  | device_parallel=@{emulator}

        """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.long_click()
        else:
            if device is not None:
                get_devices = self.management_device.scan_current_device(device)
                return get_devices.long_click()
            else:
                return self.device_mobile(*argument, **settings).long_click()

    @Decorators.android_version
    def click_a_point(self, device=None, *argument, **settings):
        """Click into pointer target location.

         This keyword is used to click location  based on pointer X and Y.

         **Example:**

         ||  CLick A Point      |x=10   |y=20

         With Device/ Pararel :
         ||  @{emulator} =   | 192.168.1.1    | 192.168.1.2
         ||  CLick A Point   |x=10   |y=20    | device_parallel=@{emulator}

        """
        if 'x' in settings and 'y' in settings:
            x = settings['x']
            y = settings['y']
            del settings['x']
            del settings['y']
        else:
            raise ValueError('pointer x or y is refused')

        if device is not None:
            get_devices = self.management_device.scan_current_device(device)
            return get_devices.click(x, y)
        else:
            return self.device_mobile().click(x, y)


class GetConditions(Core):
    def __init__(self):
        self.device_mobile = self.device()
        self.management_device = ManagementDevice()

    @Parallel.device_check
    def get_info(self, device=None, value=None):
        """Get Info of Device.

        **Example:**

        ||  Get Info         |  value=displayRotation

         With Device/ Pararel :
         ||  @{emulator} =   | 192.168.1.1    | 192.168.1.2
         ||  Get Info        | value=displayRotation | device_parallel=@{emulator}

        **Return:**
        { u'displayRotation': 0,
          u'displaySizeDpY': 640,
          u'displaySizeDpX': 360,
          u'currentPackageName': u'com.android.launcher',
          u'productName': u'takju',
          u'displayWidth': 720,
          u'sdkInt': 18,
          u'displayHeight': 1184,
          u'naturalOrientation': True
        }
        """

        if value is None:
            result = self.device(device).info
        else:
            result = self.device(device).info[value]

        return result

    @Parallel.device_check
    def get_text(self, device=None, *argument, **settings):
        """Get text from element base on locator.

        **Example:**

        ||  Get Text         |  className=sample class

         With Device/ Pararel :
         ||  @{emulator} =   | 192.168.1.1    | 192.168.1.2
         ||  Get Text        | className=sample class | device_parallel=@{emulator}

        **Return:**
        String
        """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.info['text']
        else:
            if device is not None:
                get_devices = self.management_device.scan_current_device(device)
                return get_devices(*argument, **settings).info['text']
            else:
                return self.device_mobile(*argument, **settings).info['text']

    @Parallel.device_check
    def get_element_attribute(self, device=None, *argument, **settings):
        """Get element attribute keyword of device.

        **List of Elements:**

         childCount, bounds, className, contentDescription,
         packageName, resourceName, text, visibleBounds,
         checkable, checked, clickable, enabled, focusable, disable,
         focused, longClickable, scrollable, selected

         **Example:**

         || Get Element Attribute    |  className=sample   | element=text

         **Return:**

         Attribute from element device
        """
        element = settings['element']
        del settings['element']

        if 'locator' in settings:
            locator = settings['locator']
            return locator.info[element]
        else:
            if device is not None:
                get_devices = self.management_device.scan_current_device(device)
                return get_devices(*argument, **settings).info[element]
            else:
                return self.device_mobile(*argument, **settings).info[element]

    @Parallel.device_check
    def get_element(self, device=None, *argument, **settings):
        """Get element info of device .
        This keyword is used to get element info of device.

         **Example:**

        || Get Element    |

        **Return:**

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
            if device is not None:
                get_devices = self.management_device.scan_current_device(device)
                return get_devices(*argument, **settings).info
            else:
                return self.device_mobile(*argument, **settings).info

    @Parallel.device_check
    def get_element_by_coordinate_x(self, device=None, *argument, **settings):
        """Get element by coordinate X.
        This keyword is used to get coordinate X of device.

         **Example:**

        || Get Element By Coordinate X  |  className=sample class

        **Return:**

        Coordinate x(int)
        """
        if device is not None:
            get_devices = self.management_device.scan_current_device(device)
            print(get_devices)
            # bound = self.get_element_attribute(element='bounds', device=get_devices, *argument, **settings)

        else:
            bound = self.get_element_attribute(element='bounds', *argument, **settings)
            bottom = bound['bottom']
            top = bound['top']
            elm_x = (top+bottom)+top
            return elm_x

    def get_element_by_coordinate_y(self, *argument, **settings):
        """Get element by coordinate Y.

        This keyword is used to get coordinate Y of device.

         **Example:**

        || Get Element By Coordinate Y  |  className=sample class

        **Return:**

        Coordinate y(int)
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

        This keyword is used to get widh of device,

        **Example:**

        || Get Width

        **Return:**

        Width of device(int)
        """
        get_device = self.device()
        return get_device.info['displayWidth']

    def get_height(self):
        """Get height from display of device.

        This keyword is used to get widh of device.

        **Example:**

        || Get Height

        **Return:**

        Width of device(int)
        """
        get_device = self.device()
        return get_device.info['displayHeight']

    def get_position(self, position=0, *argument, **settings):
        """Get Position of element.

        This keyword is used to get position of device element.

        **Example:**

        || Get Position       |  className=sample   | position=1

        **Return:**

        Width of device(int)
        """
        if 'locator' in settings:
            locator = settings['locator']
            del settings['locator']
            return locator[position]
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device(*argument, **settings)[position]
            else:
                return self.device_mobile(*argument, **settings)[position]


class ExpectedConditions(Core):
    def __init__(self):
        self.device_mobile = self.device()
        self.get_conditions = GetConditions()

    @Parallel.device_check
    def page_should_contain_element(self, device=None, *argument, **settings):
        """Page should contain element.
        The keyword is used to verify the page is contains locator element.

        **Example:**

        || Page Should Contain Element | className=sample class

        **Return:**

        True or False
        """
        # element = self.get_conditions.get_element(*argument, **settings)

        if 'locator' in settings:
            locator = settings['locator']
            if locator.exists:
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

    @Parallel.device_check
    def page_should_contain_text(self, device=None, *argument, **settings):
        """Page should contain text.
        The keyword is used to verify the page is contains text.

        **Example:**

        || Page Should Contain Text | text=sample text

        **Return:**

        True or False
        """
        text = settings['text']

        if 'device' in settings:
            device = settings['device']
            del settings['device']
            return device(*argument, **settings).exists
        else:
            if device != None:
                get_devices = self.management_device.scan_current_device(device)
                return get_devices(*argument, **settings).exists

            elif 'watcher' in settings:
                watcher = settings['watcher']
                del settings['watcher']

                return watcher.exists(*argument, **settings)
            else:
                return self.device_mobile(*argument, **settings).exists

    @Parallel.device_check
    def __get_device_global(self, device=None, *argument, **settings):
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
    def page_should_not_contain_element(self, device=None, *argument, **settings):
        """Page should not contain element.

        The keyword is used to verify the page is not contains element.

        **Example:**

        || Page Should Not Contain Element | className=sample element

        **Return:**

        True or False
        """
        # element = self.get_conditions.get_element(*argument, **settings)

        if 'locator' in settings:
            locator = settings['locator']
            found = locator.exists
            if found is False:
                return True
            else:
                return False
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                found = device(*argument, **settings).exists
                if found is True:
                    return False
                else:
                    return True
            else:
                found = self.device_mobile(*argument, **settings).exists
                if found is True:
                    return False
                else:
                    return True

    @Parallel.device_check
    def page_should_not_contain_text(self, device=None, *argument, **settings):
        """Page should not contain text.

        The keyword is used to verify the page is not contains text.

        **Example:**

        || Page Should Contain Text | text=sample text

        **Return:**

        True or False

        """
        text = self.get_conditions.get_text(*argument, **settings)

        if 'locator' in settings:
            locator = settings['locator']
            found = locator[text].exists
            if found is False:
                return True
            else:
                return False
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).exists
            else:
                return self.device_mobile(*argument, **settings).exists

    @Parallel.device_check
    def text_should_be_enabled(self, device=None, *argument, **settings):
        """Text should be enabled.

        The keyword is used to identify text enable.

        **Example:**

        || Text Should Be Enabled | text=sample text

        **Return:**

        True or False
        """
        element = self.get_conditions.get_element()
        enabled = element['enabled']
        if 'locator' in settings:
            locator = settings['locator']
            if locator.info['enabled'] is True:
                return True
            else:
                return False
        else:
            if 'device' in settings:
                device_mobile = settings['device']
                del settings['device']

            return self.device_mobile(*argument, **settings).enabled

    @Parallel.device_check
    def text_should_be_disabled(self, device=None, *argument, **settings):
        """Text should be disabled.

        The keyword is used to identify text disabled.

        **Example:**

        || Element Should Be Disabled | text=sample text

        **Return:**

        True or False
        """
        element = self.get_conditions.get_element()
        enabled = element['enabled']
        if 'locator' in settings:
            locator = settings['locator']
            if locator.info['enabled'] is False:
                return True
            else:
                return False
        else:
            if 'device' in settings:
                device_mobile = settings['device']
                del settings['device']

            return self.device_mobile(*argument, **settings).enabled

    @Parallel.device_check
    def element_should_contain_text(self, device=None, *argument, **settings):
        """Element should contain text.

        The keyword is used to identify text on element.

        **Example:**

        || Element Should Contain Text | className=class | text=sample text

        **Return:**

        True or False
        """
        if 'locator' in settings:
            locator = settings['locator']

            try:
                if locator.info['text'] is not None:
                    return True
            except Exception:
                return False
        else:
            if 'device' in settings:
                device_mobile = settings['device']
                del settings['device']

            try:
                if self.device_mobile(*argument, **settings).info['text'] is not None:
                    return True
            except Exception:
                return False

    @Parallel.device_check
    def element_should_not_contain_text(self, device=None, *argument, **settings):
        """Element should contain text.

        The keyword is used to identify text on element.

        **Example:**

        || Element Should Not Contain Text | className=class | text=sample text

        **Return:**

        True or False
        """
        if 'locator' in settings:
            locator = settings['locator']

            try:
                if locator.info['text'] is None:
                    return True
                return False
            except Exception as error:
                return True

        else:
            if 'device' in settings:
                device_mobile = settings['device']
                del settings['device']

            try:
                if self.device_mobile(*argument, **settings).info['text'] is None:
                    return True
                return False
            except Exception as error:
                return True

    @Parallel.device_check
    def check_element_visible(self, device=None, *argument, **settings):
        """Check element visible.

        The keyword is used to check element visible.

        **Example:**

        || Check Element Visible | className=sampleclassName

        **Return:**

        True or False
        """
        if 'locator' in settings:
            locator = settings['locator']

            try:
                if locator.info['visibleBounds'] is None:
                    return False
                return True
            except Exception as error:
                return ("Exception Error: {0}".format(error))

        else:
            if 'device' in settings:
                device_mobile = settings['device']
                del settings['device']

            try:
                if self.device_mobile(*argument, **settings).info['visibleBounds'] is None:
                    return False
                return True
            except Exception as error:
                return ("Exception Error: {0}".format(error))

    @Parallel.device_check
    def check_element_non_visible(self, device=None, *argument, **settings):
        """Check element non visible.

        The keyword is used to check element non visible.

        **Example:**

        || Check Element Non Visible | className=sampleclassName

        **Return:**

        True or False
        """
        if 'locator' in settings:
            locator = settings['locator']

            try:
                if locator.info['visibleBounds'] is None:
                    return True
                return False
            except Exception as error:
                return ("Exception Error: {0}".format(error))

        else:
            if 'device' in settings:
                device_mobile = settings['device']
                del settings['device']

            try:
                if self.device_mobile(*argument, **settings).info['visibleBounds'] is None:
                    return True
                return False
            except Exception as error:
                return ("Exception Error: {0}".format(error))
