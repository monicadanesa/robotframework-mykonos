from mykonos.keywords.key_event import KeyEvent
from mykonos.keywords.management_device import ManagementDevice
from mykonos.keywords.element import Element
from mykonos.keywords.touch import Touch
from mykonos.locator.locator_element import LocatorElement
from mykonos.core.core import Core

el = Element()
le = LocatorElement()

sample = le.get_locator_by_index(className='android.widget.FrameLayout', index=2)
sample
tc = Touch()
tc.scroll()
sample = tc.scroll(action='vertical to end',max_swipes=100)
sample
from uiautomator import Device

d = Device()
tc  = d(text='All contacts').info['bounds']

d(scrollable=True).scroll.horiz.toEnd(max_swipes=10, steps=100)
