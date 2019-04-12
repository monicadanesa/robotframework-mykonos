import pytest
import os
from yaml import load
from mykonos.keywords.key_event import KeyEvent

def open_file():
    with open('setting.yaml') as f:
        data = load(f)
    return data


def test_press_menu():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_menu()
    print(result)
    assert result == True


def test_press_left():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_left()
    print(result)
    assert result == True

def test_press_right():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_right()
    print(result)
    assert result == True

def test_press_up():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_up()
    print(result)
    assert result == True

def test_press_down():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_down()
    print(result)
    assert result == True


def test_press_center():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_center()
    print(result)
    assert result == True

def test_press_home():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_home()
    print(result)
    assert result == True

def test_press_search():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_search()
    print(result)
    assert result == True

def test_press_volume_up():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_volume_up()
    print(result)
    assert result == True

def test_press_volume_down():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_volume_down()
    print(result)
    assert result == True

def test_press_camera():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_camera()
    print(result)
    assert result == True

def test_press_back():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_back()
    print(result)
    assert result == True

def test_press():
    data = open_file()
    cls = KeyEvent(data)
    result = cls.press_key(0x07, 0x02)
    print(result)
    assert result == True
