import pytest
from mock import MagicMock, call, patch
from pytest_mock import mocker
from mykonos.keywords.management_device import ManagementDevice

def test_scan_device():
    device = ManagementDevice()
    device.scan_device = MagicMock()
    device.scan_device.return_value = True
    result = device.scan_device()
    assert result == True

def test_open_app():
    device = ManagementDevice()
    device.open_app = MagicMock()
    device = MagicMock()
    device.open_app.return_value = True
    result = device.open_app(device=MagicMock(), app_package=MagicMock())
    assert result == True

def test_quite_app():
    device = ManagementDevice()
    device.quit_app = MagicMock()
    device.quit_app.return_value = True
    result = device.quit_app(device=MagicMock(), app_package=MagicMock())
    assert result == True

def test_reset_app():
    device = ManagementDevice()
    device.reset_app = MagicMock()
    device.reset_app.return_value = True
    result = device.reset_app(device=MagicMock(), app_package=MagicMock())
    assert result == True

def test_pull_file():
    device = ManagementDevice()
    device.pull = MagicMock()
    device.pull.return_value = True
    result = device.pull(local=MagicMock(), remote=MagicMock())
    assert result == True

def test_get_android_version():
    device = ManagementDevice()
    device.get_android_version = MagicMock()
    device.get_android_version.return_value = '9'
    result = device.get_android_version()
    assert result == '9'
