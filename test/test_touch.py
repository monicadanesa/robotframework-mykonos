import pytest
from yaml import load
from alog import debug, info, error
from mykonos.keywords.touch import Touch
from mykonos.keywords.element import Element


def open_file():
    with open('setting.yaml') as f:
        data = load(f)
    return data

def test_swipe():
    data = open_file()
    le = Touch(data)
    el = Element(data)
    click = el.click_element(className="android.widget.ImageView")
