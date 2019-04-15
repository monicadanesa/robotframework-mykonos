import pytest
from yaml import load
from mykonos.keywords.element import Element

def open_file():
    with open('setting.yaml') as f:
        data = load(f)
    return data

def test_long_click_element():
    data = open_file()
    el = Element(data)
    result = el.long_click_element(text="Maps")
    print(result)
    assert result == True

def test_click_element():
    data = open_file()
    el = Element(data)
    result = el.click_element(text="Work")
    print(result)
    assert result == True

def test_click_element_parent():
    data = open_file()
    el = Element(data)
    parent = el.get_locator(className="android.widget.LinearLayout")
    result = el.click_element(parent)
    print(result)
    assert result == True

def test_click_element_child():
    data = open_file()
    el = Element(data)
    parent = el.get_locator(className="android.widget.LinearLayout")
    child = el.get_child(parent, text="NO THANKS")
    result = el.click_element(child)
    print(result)
    assert result == True
