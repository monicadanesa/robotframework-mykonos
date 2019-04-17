from yaml import load
from mykonos.keywords.key_event import KeyEvent
from mykonos.keywords.management_device import ManagementDevice
from mykonos.keywords.element import Element
from mykonos.keywords.touch import Touch
from mykonos.locator.locator_element import LocatorElement

# scan device
md = ManagementDevice()
md.scan_current_device()
md.info_device()


result
# get element

# click
el = Element()
el.click_element(element)

md =  ManagementDevice()
d1 = md.scan_current_device("emulator-5554")
d2 = md.scan_current_device("emulator-5556")


le = LocatorElement()
le.get_locator(text="Messaging").click()
le.get_locator(d1, text="Messaging").click()

el = Element()
locator = el.get_locator(text="Messages")
el.click_element(None,locator)
el.click_element(text="Messaging")
