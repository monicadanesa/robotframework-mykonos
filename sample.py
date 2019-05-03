from mykonos.keywords.key_event import KeyEvent
from mykonos.keywords.management_device import ManagementDevice
from mykonos.keywords.element import Element
from mykonos.keywords.touch import Touch
from mykonos.locator.locator_element import LocatorElement
from mykonos.core.core import Core



# scroll forward(default) vertically(default)
d(scrollable=True).scroll(steps=10)
# scroll forward horizentally
d(scrollable=True).scroll.horiz.forward(steps=100)
# scroll backward vertically
d(scrollable=True).scroll.vert.backward()
# scroll to beginning horizentally
d(scrollable=True).scroll.horiz.toBeginning(steps=100, max_swipes=1000)
# scroll to end vertically
d(scrollable=True).scroll.toEnd()
# scroll forward vertically until specific ui object appears
d(scrollable=True).scroll.to(text="Security")



scroll                              step = 10
scroll                              step = 1000     action = horizontal forward
scroll horizontal backward          step = 1000
scroll vertical backward
scroll vertical forward
scroll horizontal to begining      step = 100 max_swipes=1000
scroll to end
scroll to                          text=Security   className=Apaja


el.get_element_attribute(element='displaySizeDpY', className='packageName')

tc = Touch()

result = tc.scoll(action='horizontal to end')
