from mykonos.keywords.key_event import KeyEvent
from mykonos.keywords.management_device import ManagementDevice
from mykonos.keywords.element import Element, Get, Click
from mykonos.keywords.touch import Touch
from mykonos.locator.locator_element import LocatorElement
from mykonos.core.core import Core
from mykonos.locator.locator_element import WatcherElement

el = Element()
sample = el.page_should_not_contain_element(className='android.widget.TextView')
sample
text = el.page_should_not_contain_text(className='helllo')
text
le = LocatorElement()

mg = ManagementDevice()
mg.scan_current_device()
ke = KeyEvent()
we = WatcherElement()
tc = Touch()

gt = Get()
el.page_should_contain_text(text='helllo')
page_should_contain_text
