from mykonos.keywords.key_event import KeyEvent
from mykonos.keywords.management_device import ManagementDevice
from mykonos.keywords.element import Element, Get, Click
from mykonos.keywords.touch import Touch
from mykonos.locator.locator_element import LocatorElement
from mykonos.core.core import Core
from mykonos.locator.locator_element import WatcherElement

el = Element()
text = el.wait_until_page_does_not_contain(className='android.widget.TextView')
text = el.check_element_not_exists(className='android.widget.TextView')
text = el.wait_until_page_does_not_contain(text='android.widget.TextView')

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
