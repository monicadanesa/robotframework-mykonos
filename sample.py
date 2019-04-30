from yaml import load
from mykonos.keywords.key_event import KeyEvent
from mykonos.keywords.management_device import ManagementDevice
from mykonos.keywords.element import Element
from mykonos.keywords.touch import Touch
from mykonos.locator.locator_element import LocatorElement

md = ManagementDevice()


from uiautomator import Device

d = Device()

sample = d(resourceId="com.android.launcher3:id/apps_view")
