import pytest
from yaml import load
from mykonos.keywords.element import Element
from mykonos.keywords.key_event import KeyEvent
from mykonos.keywords.management_device import ManagementDevice

def test_long_click_element():
    el = Element()
    cls = KeyEvent()
    result = el.long_click_element(text="Messaging")
    cls.press_keycode("back")
    print(result)
    assert result == True

def test_click_element():
    el = Element()
    cls = KeyEvent()
    result = el.click_element(text="Messaging")
    cls.press_keycode("back")
    print(result)
    assert result == True

def test_click_element_parent_without_device():
    el = Element()
    cls = KeyEvent()
    parent = el.get_locator(text="Messaging")
    result = el.click_element(None, parent)
    cls.press_keycode("back")
    print(result)
    assert result == True

def test_click_element_parent_with_device():
    md =  ManagementDevice()
    d1 = md.scan_current_device()
    el = Element()
    cls = KeyEvent()
    parent = el.get_locator(text="Messaging")
    result = el.click_element(d1, parent)
    cls.press_keycode("back")
    print(result)
    assert result == True

def test_input_text_with_device_parent():
    el = Element()
    cls = KeyEvent()
    device_1 = el.scan_current_device("emulator-5554")
    el.click_element(text="Messaging")
    el.click_element(resourceId="com.android.messaging:id/start_new_conversation_button")
    locator = el.get_locator(className="android.widget.MultiAutoCompleteTextView")
    result = el.input_text(device_1, locator, "hallo")
    cls.press_keycode("back")
    print(result)
    assert result == True

def test_input_text_with_parameter():
    el = Element()
    device_1 = el.scan_current_device("emulator-5554")
    locator = el.get_locator(className="android.widget.MultiAutoCompleteTextView")
    result = el.input_text(device=device_1, text="hayy",className="android.widget.MultiAutoCompleteTextView")
    print(result)
    assert result == True

def test_input_text_with_locator():
    el = Element()
    result = el.input_text(text="hey", className="android.widget.MultiAutoCompleteTextView")
    print(result)
    assert result == True

def test_clear_text():
    el = Element()
    result = el.clear_text(className="android.widget.MultiAutoCompleteTextView")
    print(result)
