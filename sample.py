from yaml import load
from mykonos.keywords.key_event import KeyEvent
from mykonos.keywords.management_device import ManagementDevice
from mykonos.keywords.element import Element
from mykonos.keywords.touch import Touch
from mykonos.locator.locator_element import LocatorElement


md = ManagementDevice()
le = Element()

le.input_text(className="android.widget.Spinner", input="hello")

sample = le.get_locator(text="Browser")

md.capture_screen()
