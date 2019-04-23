import pytest
from mock import MagicMock, call, patch
from pytest_mock import mocker
from mykonos.keywords.management_device import ManagementDevice

def test_scan_device(mocker):
    device = ManagementDevice()
    device.scan_device = MagicMock()
    device.scan_device.return_value = True
    assert device.scan_device() == True

def test_open_application(mocker):
    class_name = ManagementDevice()
    class_name.open_application = MagicMock()
    device_name = MagicMock()
    app_package = MagicMock()
    device = MagicMock()
    class_name.open_application.return_value = device
    assert class_name.open_application(device_name, app_package) == device

def test_info_device(mocker):
    class_name = ManagementDevice()
    class_name.info_device = MagicMock()
    device_name = MagicMock()
    class_name.info_device.return_value = {}
    assert class_name.info_device() == {}
    assert class_name.info_device(device_name) == {}
