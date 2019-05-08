import traceback
from alog import debug, info, error
from mykonos.core.core import Core

class LocatorElement(Core):

    def __init__(self):
        self.device_mobile = self.device()

    def get_locator(self, *argument, **settings):
        """ access locator from device
        selector support :
        text, textContains, textMatches, textStartsWith
        className, classNameMatches
        description, descriptionContains, descriptionMatches, descriptionStartsWith
        checkable, checked, clickable, longClickable
        scrollable, enabled,focusable, focused, selected
        packageName, packageNameMatches
        resourceId, resourceIdMatches
        index, instance
        example :
        cls = LocatorElement()
        locator = cls.get_locator(text='')

        HOW TO CALL IN ROBOT FRAMEWORK

        without device:
        | ${locator}= Get Locator           | text=sample text

        with device:
        Define device on the first time:
        | ${device_1}=  Scan Current Device  |    ${emulator}
        | ${locator}= Get Locator            | text=sample text     |  device=${device_1}

        """

        if 'device' in settings:
             device = settings['device']
             del settings['device']
             return device(*argument, **settings)
        else:
            return self.device_mobile(*argument, **settings)


    def get_child(self, parent, *argument, **settings):
        """ access child locator from device
        example:
        cls = LocatorElement()
        parent = cls.get_locator(text='')
        child = cls.get_child(parent, text='')

        HOW TO CALL IN ROBOT FRAMEWORK
        | ${locator}=  Get Locator          | text=sample text
        | ${child}=   Get Child             | parent=${locator}  text=sample text
        """
        return parent.child(*argument, **settings)

    def get_sibling(self, parent, *argument, **settings):
        """ access sibling locator from device
        example:
        cls = LocatorElement()
        parent = cls.get_locator(text='')
        sibling = cls.get_sibling(parent, text='')

        HOW TO CALL IN ROBOT FRAMEWORK
        | ${locator}=  Get Locator          | text=sample text
        | ${child}=   Get Sibiling          | parent=${locator}  text=sample text
        """
        return parent.sibling(*argument, **settings)

    def left_position(self, parent, *argument, **settings):
        """ access left position from device
        example:
        cls = LocatorElement()
        parent = cls.get_locator(text='')
        left = cls.left_postion(parent, text='')

        HOW TO CALL IN ROBOT FRAMEWORK
        | ${locator}=  Get Locator          | text=sample text
        | ${left}=     Left Position        | parent=${locator}  text=sample text
        """
        return parent.left(*argument, **settings)

    def right_position(self, parent, *argument, **settings):
        """ access left position from device
        example:
        cls = LocatorElement()
        parent = cls.get_locator(text='')
        right = cls.right_postion(parent, text='')

        HOW TO CALL IN ROBOT FRAMEWORK
        | ${locator}=  Get Locator          | text=sample text
        | ${right}=    Right Position       | parent=${locator}  text=sample text
        """
        return parent.right(*argument, **settings)

    def up_position(self, parent, *argument, **settings):
        """ access left position from device
        example:
        cls = LocatorElement()
        parent = cls.get_locator(text='')
        up = cls.up_postion(parent, text='')

        HOW TO CALL IN ROBOT FRAMEWORK
        | ${locator}=  Get Locator          | text=sample text
        | ${up}=    Up Position             | parent=${locator}  text=sample text
        """
        return parent.up(*argument, **settings)

    def down_position(self, parent, *argument, **settings):
        """ access left position from device
        example:
        cls = LocatorElement()
        parent = cls.get_locator(text='')
        down = cls.up_postion(parent, text='')

        HOW TO CALL IN ROBOT FRAMEWORK
        | ${locator}=  Get Locator        | text=sample text
        | ${down}=    Down Position       | parent=${locator}  text=sample text
        """
        return parent.down(*argument, **settings)

    def get_locator_by_index(self, *argument, **settings):
        index = int(settings['index'])
        del settings['index']

        if 'locator' in settings:
            locator = settings['locator']
            del settings['locator']

            return locator[index]
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device(*argument, **settings)[index]
            else:
                return self.device_mobile(*argument, **settings)[index]
