import pytest
from yaml import load
from mykonos.keywords.element import Element
from mykonos.keywords.management_device import ManagementDevice

def test_long_click_element():
    el = Element()
    result = el.long_click_element(text="Maps")
    print(result)
    assert result == True

def test_click_element():
    el = Element()
    result = el.click_element(text="Work")
    print(result)
    assert result == True

def test_click_element_parent_without_device():
    el = Element()
    parent = el.get_locator(className="android.widget.LinearLayout")
    result = el.click_element(None, parent)
    print(result)
    assert result == True

def test_click_element_parent_with_device():
    md =  ManagementDevice()
    d1 = md.scan_current_device()
    el = Element()
    parent = el.get_locator(className="android.widget.LinearLayout")
    result = el.click_element(d1, parent)
    print(result)
    assert result == True
