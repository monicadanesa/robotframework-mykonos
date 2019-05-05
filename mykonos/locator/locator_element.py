import traceback
from alog import debug, info, error
from mykonos.core.core import Core

class LocatorElement(Core):

    def __init__(self):
        self.device_mobile = self.device()

    def get_locator(self, *argument, **locator):
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

        if 'device' in locator:
             device = locator['device']
             del locator['device']
             return device(*argument, **locator)
        else:
            return self.device_mobile(*argument, **locator)


    def get_child(self, parent, *argument, **locator):
        """ access child locator from device
        example:
        cls = LocatorElement()
        parent = cls.get_locator(text='')
        child = cls.get_child(parent, text='')

        HOW TO CALL IN ROBOT FRAMEWORK
        | ${locator}=  Get Locator          | text=sample text
        | ${child}=   Get Child             | parent=${locator}  text=sample text
        """
        return parent.child(*argument, **locator)

    def get_sibling(self, parent, *argument, **locator):
        """ access sibling locator from device
        example:
        cls = LocatorElement()
        parent = cls.get_locator(text='')
        sibling = cls.get_sibling(parent, text='')

        HOW TO CALL IN ROBOT FRAMEWORK
        | ${locator}=  Get Locator          | text=sample text
        | ${child}=   Get Sibiling          | parent=${locator}  text=sample text
        """
        return parent.sibling(*argument, **locator)

    def left_postion(self, parent, *argument, **locator):
        """ access left position from device
        example:
        cls = LocatorElement()
        parent = cls.get_locator(text='')
        left = cls.left_postion(parent, text='')

        HOW TO CALL IN ROBOT FRAMEWORK
        | ${locator}=  Get Locator          | text=sample text
        | ${left}=     Left Position        | parent=${locator}  text=sample text
        """
        return parent.left(*argument, **locator)

    def right_postion(self, parent, *argument, **locator):
        """ access left position from device
        example:
        cls = LocatorElement()
        parent = cls.get_locator(text='')
        right = cls.right_postion(parent, text='')

        HOW TO CALL IN ROBOT FRAMEWORK
        | ${locator}=  Get Locator          | text=sample text
        | ${right}=    Right Position       | parent=${locator}  text=sample text
        """
        return parent.right(*argument, **locator)

    def up_postion(self, parent, *argument, **locator):
        """ access left position from device
        example:
        cls = LocatorElement()
        parent = cls.get_locator(text='')
        up = cls.up_postion(parent, text='')

        HOW TO CALL IN ROBOT FRAMEWORK
        | ${locator}=  Get Locator          | text=sample text
        | ${up}=    Up Position             | parent=${locator}  text=sample text
        """
        return parent.up(*argument, **locator)

    def down_postion(self, parent, *argument, **locator):
        """ access left position from device
        example:
        cls = LocatorElement()
        parent = cls.get_locator(text='')
        down = cls.up_postion(parent, text='')

        HOW TO CALL IN ROBOT FRAMEWORK
        | ${locator}=  Get Locator        | text=sample text
        | ${down}=    Down Position       | parent=${locator}  text=sample text
        """
        return parent.down(*argument, **locator)
