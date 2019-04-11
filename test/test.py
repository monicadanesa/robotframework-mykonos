import pytest
import os
from yaml import load
from mykonos.keywords.key_event import KeyEvent
from mykonos.keywords.management_device import ManagementDevice

def scan_current_device():
    global sc
    sc = os.system('adb devices')
    if "10" in sc:
        return True
    else:
        return False
    global d
    d = Device(sc)

def reset_application(app_package):
    rs = os.system('adb -s '+sc+' shell pm clear '+app_package+'')
    return rs

def open_application(app_activity):
    op = os.system('adb -s '+sc+' shell am start -W '+app_activity+'')
    return op

def close_application(app_package):
    cl = os.system('adb -s '+sc+' am force-stop '+app_package+'')
    return cl

def open_file():
    with open('setting.yaml') as f:
        data = load(f)
    return data

def test_device_info():
    data = open_file()
    cls = ManagementDevice(data)
    result = cls.device_info()

    if len(result)==10:
        return True
    else:
        return False
