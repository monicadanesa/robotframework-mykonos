import pytest
from pytest_mock import mocker
from alog import debug, info, error
from mock import MagicMock, call, patch
from mykonos.locator.locator_element import LocatorElement
from mykonos.locator.locator_element import WatcherElement

def test_get_locator():
    le = LocatorElement()
    le.get_locator = MagicMock()
    className = MagicMock()
    assert le.get_locator(className="android.widget.TextView").info != 0


def test_get_child():
    le = LocatorElement()
    le.get_locator = MagicMock()
    class_name_sample =  MagicMock()
    assert le.get_child(le.get_locator, className="class_name_sample").info!=0

def test_left_position():
    le = LocatorElement()
    le.get_locator = MagicMock()
    text = MagicMock()
    assert le.left_position(le.get_locator(text="Messaging"), text="Browser").info!=0

def test_right_position():
    le = LocatorElement()
    text = MagicMock()
    le.get_locator = MagicMock()
    assert le.right_position(le.get_locator(text='Browser'), text="Messaging").info!=0

def test_up_position():
    le = LocatorElement()
    text = MagicMock()
    le.get_locator = MagicMock()
    assert le.up_position(le.get_locator(text='Browser'), text="Messaging").info!=0

def test_down_position():
    le = LocatorElement()
    text = MagicMock()
    le.get_locator = MagicMock()

    assert le.down_position(le.get_locator(text='Browser'), text="Messaging").info!=0

def test_get_locator_by_index():
    le = LocatorElement()
    le.get_locator_by_index = MagicMock()
    text = MagicMock()
    index = MagicMock()
    le.get_locator_by_index(text='Browser', index=0)

def test_watcher():
    we = WatcherElement()
    we.watcher(name=MagicMock(), className=MagicMock())

def test_watcher_action():
    we = WatcherElement()
    we.watcher_action(action=MagicMock())

def test_handlers():
    le = LocatorElement()
    le.handlers(action=MagicMock(), function=MagicMock())
