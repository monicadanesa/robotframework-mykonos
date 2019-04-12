import attr
from alog import debug, info, error
from mykonos.core.core import Core

@attr.s
class LocatorElement(Core):
    data = attr.ib()

    def __attrs_post_init__(self):
        self.device_mobile = self.device(self.data)

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
        cls = LocatorElement(data)
        locator = cls.get_locator(text='')
        """
        return self.device_mobile(*argument, **locator)

    def get_child(self, parent, *argument, **locator):
        """ access child locator from device
        example:
        cls = LocatorElement(data)
        locator = cls.get_locator(text='')
        child = cls.get_child(locator, text='')
        """
        return parent.child(*argument, **locator)

    def get_sibling(self, parent, *argument, **locator):
        """ access sibling locator from device
        example:
        cls = LocatorElement(data)
        locator = cls.get_locator(text='')
        sibling = cls.get_sibling(locator, text='')
        """
        return parent.sibling(*argument, **locator)
