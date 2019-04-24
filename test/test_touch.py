import pytest
from alog import debug, info, error
from mykonos.keywords.touch import Touch
from mykonos.keywords.element import Element

def test_swipe():
    le = Touch()
    el = Element()
    click = el.click_element(className="android.widget.ImageView")
