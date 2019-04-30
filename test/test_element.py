import pytest
# from yaml import load
from mykonos.keywords.element import Element
from mykonos.keywords.key_event import KeyEvent
from mykonos.locator.locator_element import LocatorElement
from mykonos.keywords.management_device import ManagementDevice


# def test_long_click_element():
#     el = Element()
#     cls = KeyEvent()
#     result = el.long_click_element(text="Messaging")
#     cls.press_keycode("home")
#     print(result)
#     assert result == True

def test_click_a_point():
    el = Element()
    cls = KeyEvent()
    result = el.click_a_point(x=537, y=955)
    print(result)
    assert result == True

# def test_click_element():
#     el = Element()
#     cls = KeyEvent()
#     result = el.click_element(text="Messaging")
#     cls.press_keycode("home")
#     print(result)
#     assert result == True
#
# def test_click_element_parent_without_device():
#     el = Element()
#     le = LocatorElement()
#     cls = KeyEvent()
#     cls.press_keycode("back")
#     parent = le.get_locator(text="Messaging")
#     result = el.click_element(locator=parent)
#     cls.press_keycode("home")
#     print(result)
#     assert result == True
#
# def test_click_element_parent_with_device():
#     md =  ManagementDevice()
#     d1 = md.scan_current_device()
#     el = Element()
#     le = LocatorElement()
#     cls = KeyEvent()
#     parent = le.get_locator(text="Messaging")
#     result = el.click_element(device=d1,locator=parent)
#     cls.press_keycode("home")
#     print(result)
#     assert result == True
#
# def test_click_element_device_and_element():
#     md =  ManagementDevice()
#     d1 = md.scan_current_device()
#     el = Element()
#     cls = KeyEvent()
#     result = el.click_element(device=d1, text="Messaging")
#     assert result == True
#
# def test_input_text_with_device_parent():
#     md =  ManagementDevice()
#     el = Element()
#     le = LocatorElement()
#     cls = KeyEvent()
#     device_1 = md.scan_current_device("emulator-5554")
#     el.click_element(resourceId="com.android.messaging:id/start_new_conversation_button")
#     parent = le.get_locator(className="android.widget.MultiAutoCompleteTextView")
#     result = el.input_text(className="android.widget.MultiAutoCompleteTextView", input="hay")
#     assert result == True
#
# def test_input_text_with_parameter():
#     md =  ManagementDevice()
#     el = Element()
#     le = LocatorElement()
#     device_1 = md.scan_current_device("emulator-5554")
#     result = el.input_text(device=device_1, input="hallo",className="android.widget.MultiAutoCompleteTextView")
#     assert result == True
#
# def test_input_text_with_locator():
#     el = Element()
#     result = el.input_text(className="android.widget.MultiAutoCompleteTextView", input="test_input_text_with_locator")
#     print(result)
#     assert result == True
#
# def test_clear_text():
#     el = Element()
#     cls = KeyEvent()
#     result = el.clear_text(className="android.widget.MultiAutoCompleteTextView")
#     print(result)
#
# def test_clear_text_with_device():
#     md =  ManagementDevice()
#     el = Element()
#     cls = KeyEvent()
#     device_1 = md.scan_current_device("emulator-5554")
#     el.input_text(className="android.widget.MultiAutoCompleteTextView", input="clear try")
#     result = el.clear_text(device=device_1, className="android.widget.MultiAutoCompleteTextView")
#     print(result)
#
# def test_clear_text_with_device_and_parent():
#     md = ManagementDevice()
#     el = Element()
#     le = LocatorElement()
#     cls = KeyEvent()
#     device_1 = md.scan_current_device("emulator-5554")
#     parent = le.get_locator(className="android.widget.MultiAutoCompleteTextView")
#     el.input_text(className="android.widget.MultiAutoCompleteTextView", input="clear try")
#     result = el.clear_text(device=device_1, locator=parent)
#     cls.press_keycode("home")
#
# def test_get_text():
#     el = Element()
#     result = el.get_text(className="android.widget.TextView")
#     assert result == 'Camera'
#
# def test_get_text_with_device():
#     el = Element()
#     md = ManagementDevice()
#     device_1 = md.scan_current_device("emulator-5554")
#     result = el.get_text(device=device_1, className="android.widget.TextView")
#     assert result == 'Camera'
#
# def test_get_text_with_parents():
#     el = Element()
#     le = LocatorElement()
#     parent = le.get_locator(className="android.widget.TextView")
#     result = el.get_text(locator=parent)
#     assert result == 'Camera'
#
# def test_get_text_with_parents_device():
#     el = Element()
#     le = LocatorElement()
#     md = ManagementDevice()
#     device_1 = md.scan_current_device("emulator-5554")
#     parent = le.get_locator(className="android.widget.TextView")
#     result = el.get_text(device=device_1, locator=parent)
#     assert result == 'Camera'
#
# def test_get_attribute():
#     el = Element()
#     result = el.get_element_attribute(element='text', className="android.widget.TextView")
#     assert result == 'Camera'
#
# def test_get_attribute_with_device():
#     el = Element()
#     md = ManagementDevice()
#     device_1 = md.scan_current_device("emulator-5554")
#     result = el.get_element_attribute(device=device_1, element='text', className="android.widget.TextView")
#     assert result == 'Camera'
#
# def test_get_attribute_with_parent():
#     el = Element()
#     le = LocatorElement()
#     parent = le.get_locator(className="android.widget.TextView")
#     result = el.get_element_attribute(locator=parent, element='text')
#     assert result == 'Camera'
