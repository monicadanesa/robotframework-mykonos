import pytest
from yaml import load
from alog import debug, info, error
from mykonos.locator.locator_element import LocatorElement


def test_get_locator():
    le = LocatorElement()
    result = le.get_locator(className="android.widget.ImageView")
    debug(result.info)
    assert len(result.info)!=0

def test_get_child():
    le = LocatorElement()
    parent = le.get_locator(className="android.widget.FrameLayout")
    result = le.get_child(parent, className="android.widget.ImageView")
    debug(result.info)
    assert len(result.info)!=0

def test_left_position():
    le = LocatorElement()
    parent = le.get_locator(text="Play Store")
    result = le.left_postion(parent, text="Maps")
    debug(result.info)
    assert len(result.info)!=0

def test_right_position():
    le = LocatorElement()
    parent = le.get_locator(text="Maps")
    result = le.right_postion(parent, text="Play Store")
    debug(result.info)
    assert len(result.info)!=0
