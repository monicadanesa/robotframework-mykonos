from yaml import load
from mykonos.keywords.key_event import KeyEvent
from mykonos.keywords.management_device import ManagementDevice
from mykonos.keywords.element import Element
from mykonos.locator.locator_element import LocatorElement


with open('test/setting.yaml') as f:
    data = load(f)

el = LocatorElement(data)
parent = el.get_locator(text="Maps")
right = el.right_postion(parent, text="Play Store")



le = LocatorElement(data)
parent = le.get_locator(text="Messages")
result = le.up_postion(parent, text="Maps")
debug(result.info)
assert len(result.info)!=0
