import pytest
from yaml import load
from mykonos.keywords.key_event import KeyEvent

def open_file():
    with open('setting.yaml') as f:
        data = load(f)
    return data

def test_press_back():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_keycode("back")
    print(result)
    assert result == True

def test_press_home():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_keycode("home")
    print(result)
    assert result == True

def test_press_menu():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_keycode("menu")
    print(result)
    assert result == True

def test_press_left():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_keycode("left")
    print(result)
    assert result == True

def test_press_right():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_keycode("right")
    print(result)
    assert result == True

def test_press_up():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_keycode("up")
    print(result)
    assert result == True

def test_press_down():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_keycode("down")
    print(result)
    assert result == True


def test_press_center():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_keycode("center")
    print(result)
    assert result == True

def test_press_search():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_keycode("search")
    print(result)
    assert result == True

def test_press_volume_up():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_keycode("volume_up")
    print(result)
    assert result == True

def test_press_volume_down():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_keycode("volume_down")
    print(result)
    assert result == True

def test_press_camera():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_keycode("camera")
    print(result)
    assert result == True


def test_press_back():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_keycode("back")
    print(result)
    assert result == True

def test_press():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_keycode(0x07, 0x02)
    print(result)
    assert result == True
