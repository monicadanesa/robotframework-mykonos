from mykonos.keywords.key_event import KeyEvent
from mykonos.keywords.management_device import ManagementDevice
from mykonos.keywords.element import Element
from mykonos.keywords.touch import Touch
from mykonos.locator.locator_element import LocatorElement
from mykonos.core.core import Core

el = Element()
sample = el.get_element_by_coordinate_y(text='All contacts')

sample
test = el.get_element_by_coordinate_x(text='All contacts')

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

d

top
width
height
left

right
bottom

elm_y = height-(right+left)
elm_x = (top+bottom)+top

elm_x
elm_y

mg = ManagementDevice()
device_1 = mg.scan_current_device()
device_1
tc = Touch()
check = tc.scoll(action='vertical to end', device=device_1)

check
