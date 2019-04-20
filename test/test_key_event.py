import pytest
from yaml import load
from mykonos.keywords.key_event import KeyEvent



def test_press_home():
    cls = KeyEvent()
    result = cls.press_keycode("home")
    print(result)
    assert result == True

def test_press_menu():
    cls = KeyEvent()
    result = cls.press_keycode("menu")
    print(result)
    assert result == True

def test_press_left():
    cls = KeyEvent()
    result = cls.press_keycode("left")
    print(result)
    assert result == True

def test_press_right():
    cls = KeyEvent()
    result = cls.press_keycode("right")
    print(result)
    assert result == True

def test_press_up():
    cls = KeyEvent()
    result = cls.press_keycode("up")
    print(result)
    assert result == True

def test_press_down():
    cls = KeyEvent()
    result = cls.press_keycode("down")
    print(result)
    assert result == True


def test_press_center():
    cls = KeyEvent()
    result = cls.press_keycode("center")
    print(result)
    assert result == True

def test_press_search():
    cls = KeyEvent()
    result = cls.press_keycode("search")
    print(result)
    assert result == True

def test_press_volume_up():
    cls = KeyEvent()
    result = cls.press_keycode("volume_up")
    print(result)
    assert result == True

def test_press_volume_down():
    cls = KeyEvent()
    result = cls.press_keycode("volume_down")
    print(result)
    assert result == True

def test_press_camera():
    cls = KeyEvent()
    result = cls.press_keycode("camera")
    print(result)
    assert result == True
    
def test_press_back():
    cls = KeyEvent()
    result = cls.press_keycode("back")
    print(result)
    assert result == True

def test_press():
    cls = KeyEvent()
    result = cls.press_keycode(0x07, 0x02)
    print(result)
    assert result == True
