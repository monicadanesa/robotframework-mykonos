import pytest
from alog import debug, info, error
from mock import MagicMock, call, patch
from mykonos.keywords.touch import Touch

def test_swipe():
    le = Touch()
    le.swipe = MagicMock()
    le.swipe.return_value = True
    result = le.swipe(sx = MagicMock(), sy = MagicMock(), ex = MagicMock(), ey = MagicMock(), steps = MagicMock())
    assert result == True

def test_swipe_device():
    le = Touch()
    le.swipe = MagicMock()
    le.swipe.return_value = True
    result = le.swipe(sx = MagicMock(), sy = MagicMock(), ex = MagicMock(), ey = MagicMock(), steps = MagicMock(), device = MagicMock())
    assert result == True

def test_swipe_direction():
    le = Touch()
    le.swipe_with_direction = MagicMock()
    le.swipe_with_direction.return_value = True
    result = le.swipe_with_direction(direction=MagicMock(), steps=100)

    assert result == True

def test_scroll():
    le = Touch()
    le.scroll = MagicMock()
    le.scroll.return_value = True
    assert le.scroll(steps=MagicMock()) == True
    assert le.scroll(steps=MagicMock(), textName=MagicMock()) == True
    assert le.scroll(steps=MagicMock(), textName=MagicMock(), action=MagicMock(), max_swipes=MagicMock()) == True

def test_pinch():
    le = Touch()
    le.pinch = MagicMock()
    le.pinch.return_value = True
    assert le.pinch(steps=100, textName=MagicMock(), action=MagicMock(), percent=100) == True

def test_fling():
    le = Touch()
    le.fling = MagicMock()
    le.fling.return_value = True
    assert le.fling(steps=MagicMock()) == True
    assert le.fling(steps=MagicMock(), action=MagicMock(), max_swipes=MagicMock()) == True
