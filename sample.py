from mykonos.keywords.key_event import KeyEvent
from mykonos.keywords.management_device import ManagementDevice
from mykonos.keywords.element import Element
from mykonos.keywords.touch import Touch
from mykonos.locator.locator_element import LocatorElement
from mykonos.core.core import Core

el = Element()
sample = el.page_should_not_contain_element(className='android.widget.TextView')
sample
text = el.page_should_not_contain_text(className='helllo')
text
le = LocatorElement()
mg = ManagementDevice()
ke = KeyEvent()
el.click_element(device=device_1, locator=parent)
tc = Touch()
device_1 = mg.scan_current_device()
tc.swipe(sx=100, sy=100, ex=200, ey=200, steps=1, device=device_1)
sample = tc.scroll(action='vertical to end',max_swipes=100)
sample

ke.long_press("back",timer=1)

el.clear_text("back",timer=1)
