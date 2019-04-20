from alog import debug, info, error
from mykonos.core.core import Core

class LocatorElement(Core):

    def __init__(self):
        self.device_mobile = self.device()

    def get_locator(self, device=None, *argument, **locator):
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
        cls = LocatorElement(data)
        locator = cls.get_locator(text='')
        """
        print(locator)

        if device!=None:
            return device(*argument, **locator)
        else:
            return self.device_mobile(*argument, **locator)


    def get_child(self, parent, *argument, **locator):
        """ access child locator from device
        example:
        cls = LocatorElement(data)
        parent = cls.get_locator(text='')
        child = cls.get_child(parent, text='')
        """
        return parent.child(*argument, **locator)

    def get_sibling(self, parent, *argument, **locator):
        """ access sibling locator from device
        example:
        cls = LocatorElement(data)
        parent = cls.get_locator(text='')
        sibling = cls.get_sibling(parent, text='')
        """
        return parent.sibling(*argument, **locator)

    def left_postion(self, parent, *argument, **locator):
        """ access left position from device
        example:
        cls = LocatorElement(data)
        parent = cls.get_locator(text='')
        left = cls.left_postion(parent, text='')
        """
        return parent.left(*argument, **locator)

    def right_postion(self, parent, *argument, **locator):
        """ access left position from device
        example:
        cls = LocatorElement(data)
        parent = cls.get_locator(text='')
        right = cls.right_postion(parent, text='')
        """
        return parent.right(*argument, **locator)

    def up_postion(self, parent, *argument, **locator):
        """ access left position from device
        example:
        cls = LocatorElement(data)
        parent = cls.get_locator(text='')
        up = cls.up_postion(parent, text='')
        """
        return parent.up(*argument, **locator)

    def down_postion(self, parent, *argument, **locator):
        """ access left position from device
        example:
        cls = LocatorElement(data)
        parent = cls.get_locator(text='')
        down = cls.up_postion(parent, text='')
        """
        return parent.down(*argument, **locator)
