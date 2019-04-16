from yaml import load
from mykonos.keywords.key_event import KeyEvent
from mykonos.keywords.management_device import ManagementDevice
from mykonos.keywords.element import Element
from mykonos.keywords.touch import Touch


with open('test/setting.yaml') as f:
    data = load(f)

el = LocatorElement(data)
parent = el.get_locator(text="Messages")
right = el.up_postion(parent, text="Play Store")
right.info


le = LocatorElement(data)
parent = le.get_locator(text="Messages")
result = le.up_postion(parent, text="Maps")
debug(result.info)
assert len(result.info)!=0

el = Element(data)
el.device_mobile(className="android.widget.MultiAutoCompleteTextView").set_text('hey')
el.input_text('hay',className="android.widget.MultiAutoCompleteTextView")
el.clear_text(className="android.widget.MultiAutoCompleteTextView")
locator = el.get_locator(className="android.widget.MultiAutoCompleteTextView")
el.input_text('hello',locator)
el.clear_text(locator)
el.device_mobile(className="android.widget.MultiAutoCompleteTextView").clear_text()

tc = Touch(data)
tc.swipe_screen(0,0,1080,1794, step=5)
