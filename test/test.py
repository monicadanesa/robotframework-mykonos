import pytest

from yaml import load
from mykonos.orcestrator import Orcestrator


def open_file():
    with open('setting.yaml') as f:
        data = load(f)
    return data

def test_device_info():
    data = open_file()
    orc = Orcestrator(data)
    result = orc.device_info()

    if len(result)==10:
        return True
    else:
        return False

def test_turn_on_screen():
    data = open_file()
    orc = Orcestrator(data)
    result = orc.turn_on_screen()
    return result

def test_press_key_home():
    data = open_file()
    orc = Orcestrator(data)
    result = orc.press_key('home')
