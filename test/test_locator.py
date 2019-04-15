import pytest
from yaml import load
from alog import debug, info, error
from mykonos.locator.locator_element import LocatorElement


def open_file():
    with open('setting.yaml') as f:
        data = load(f)
    return data


def test_get_locator():
    data = open_file()
    le = LocatorElement(data)
    result = le.get_locator(className="android.widget.ImageView")
    debug(result.info)
    assert len(result.info)!=0

def test_get_child():
    data = open_file()
    le = LocatorElement(data)
    parent = le.get_locator(className="android.widget.FrameLayout")
    result = le.get_child(parent, className="android.widget.ImageView")
    debug(result.info)
    assert len(result.info)!=0
