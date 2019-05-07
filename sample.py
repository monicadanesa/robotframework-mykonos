from mykonos.keywords.key_event import KeyEvent
from mykonos.keywords.management_device import ManagementDevice
from mykonos.keywords.element import Element
from mykonos.keywords.touch import Touch
from mykonos.locator.locator_element import LocatorElement
from mykonos.core.core import Core

el = Element()
le = LocatorElement()

parent_1 = le.get_locator(className="android.widget.LinearLayout")

el.get_height()
test

from uiautomator import Device

d = Device()
tc  = d(text='All contacts').info['bounds']

width = d.info['displayWidth']
height = d.info['displayHeight']
bottom = d(text='All contacts').info['bounds']['bottom']
right = d(text='All contacts').info['bounds']['right']
left = d(text='All contacts').info['bounds']['left']
top = d(text='All contacts').info['bounds']['top']
