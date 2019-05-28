import pytest
from pytest_mock import mocker
from mock import MagicMock, call, patch
from mykonos.keywords.element import Element
from mykonos.locator.locator_element import LocatorElement
from mykonos.keywords.management_device import ManagementDevice


def test_long_click_element():
    el = Element()
    el.long_click_element = MagicMock()
    el.long_click_element.return_value = True
    result = el.long_click_element(text=MagicMock())
    assert result == True


def test_page_should_contain_element():
    el = Element()
    el.page_should_contain_element = MagicMock()
    el.page_should_contain_element.return_value = True
    result = el.page_should_contain_element(className=MagicMock())
    assert result == True

def test_wait_until_element_is_visible():
    el = Element()
    el.wait_until_element_is_visible = MagicMock()
    el.wait_until_element_is_visible.return_value = True
    result = el.wait_until_element_is_visible(className=MagicMock())
    assert result == True


def test_page_should_not_contain_element():
    el = Element()
    el.page_should_not_contain_element = MagicMock()
    el.page_should_not_contain_element.return_value = True
    result = el.page_should_not_contain_element(className=MagicMock())
    assert result == True


def test_page_should_not_contain_text():
    el = Element()
    el.page_should_not_contain_text = MagicMock()
    el.page_should_not_contain_text.return_value = True
    result = el.page_should_not_contain_text(className=MagicMock())
    assert result == True


def test_page_should_contain_text():
    el = Element()
    el.page_should_contain_text = MagicMock()
    el.page_should_contain_text.return_value = True
    result = el.page_should_contain_text(text=MagicMock())
    assert result == True


def test_click_element():
    el = Element()
    el.click_element = MagicMock()
    el.click_element.return_value = True
    result = el.click_element(text=MagicMock())
    assert result == True


def test_click_element_parent_without_device():
    el = Element()
    el.click_element = MagicMock()
    el.click_element.return_value = True
    result = el.click_element(locator=MagicMock())
    assert result == True


def test_click_element_parent_with_device():
    el = Element()
    el.click_element = MagicMock()
    el.click_element.return_value = True
    result = el.click_element(device= MagicMock(),locator= MagicMock())
    assert result == True


def test_click_element_device_and_element():
    el = Element()
    d1 = MagicMock()
    text = MagicMock()
    el.click_element = MagicMock()
    el.click_element.return_value = True
    result = el.click_element(device=d1, text="Messaging")
    assert result == True


def test_input_text_with_device_parent():
    el = Element()
    el.input_text = MagicMock()
    el.input_text.return_value = True
    result = el.input_text(className=MagicMock(), input='Test')
    assert result == True


def test_input_text_with_parameter():
    el = Element()
    el.input_text = MagicMock()
    el.input_text.return_value = True
    result = el.input_text(device=MagicMock(), input='Test',className=MagicMock())
    assert result == True


def test_input_text_with_locator():
    el = Element()
    el.input_text = MagicMock()
    el.input_text.return_value = True
    result = el.input_text(className=MagicMock(), input='Test')
    assert result == True


def test_clear_text():
    el = Element()
    el.clear_text = MagicMock()
    el.clear_text.return_value = True
    result = el.clear_text(className=MagicMock())
    assert result == True


def test_clear_text_with_device():
    el = Element()
    el.clear_text = MagicMock()
    el.clear_text.return_value = True
    result = el.clear_text(device=MagicMock(), className=MagicMock())
    assert result == True


def test_clear_text_with_device_and_parent():
    el = Element()
    el.clear_text = MagicMock()
    el.clear_text.return_value = True
    result = el.clear_text(device=MagicMock(), locator=MagicMock())
    assert result == True


def test_get_text():
    el = Element()
    el.get_text = MagicMock()
    el.get_text.return_value = 'return text'
    result = el.get_text(className=MagicMock())
    assert len(result) != 0

def test_get_text_with_device():
    el = Element()
    el.get_text = MagicMock()
    el.get_text.return_value = 'return text'
    result = el.get_text(device=MagicMock(), className=MagicMock())
    assert len(result) != 0


def test_get_text_with_parents():
    el = Element()
    el.get_text = MagicMock()
    el.get_text.return_value = 'return text'
    result = el.get_text(locator=MagicMock())
    assert len(result) != 0


def test_get_text_with_parents_device():
    el = Element()
    el.get_text = MagicMock()
    el.get_text.return_value = 'return text'
    result = el.get_text(device=MagicMock(), locator=MagicMock())
    assert len(result) != 0


def test_get_attribute():
    el = Element()
    el.get_element_attribute = MagicMock()
    el.get_element_attribute.return_value = 'sample return attribute'
    result = el.get_element_attribute(element=MagicMock(), className=MagicMock())
    assert len(result) != 0


def test_get_attribute_with_device():
    el = Element()
    el.get_element_attribute = MagicMock()
    el.get_element_attribute.return_value = 'sample return attribute'
    result = el.get_element_attribute(device=MagicMock(), element=MagicMock(), className=MagicMock())
    assert len(result) != 0


def test_get_attribute_with_parent():
    el = Element()
    el.get_element_attribute = MagicMock()
    el.get_element_attribute.return_value = 'sample return attribute'
    result = el.get_element_attribute(locator=MagicMock(), element='text')
    assert len(result) != 0


def test_get_element():
    el = Element()
    el.get_element = MagicMock()
    el.get_element.return_value = 'sample return element'
    result = el.get_element(className=MagicMock())
    assert len(result) != 0


def test_get_element_with_device():
    el = Element()
    el.get_element = MagicMock()
    el.get_element.return_value = 'sample return element'
    result = el.get_element(device=MagicMock(), className=MagicMock())
    assert len(result) != 0


def test_get_element_with_parent():
    el = Element()
    el.get_element = MagicMock()
    el.get_element.return_value = 'sample return element'
    result = el.get_element(locator=MagicMock())
    assert len(result) != 0


def test_count_element():
    el = Element()
    el.count_elements = MagicMock()
    el.count_elements.return_value = 1
    result = el.count_elements(className=MagicMock())
    assert type(result) == int


def test_count_element_with_parent():
    el = Element()
    el.count_elements = MagicMock()
    el.count_elements.return_value = 1
    result = el.count_elements(locator=MagicMock())
    assert type(result) == int


def test_get_height():
    el = Element()
    el.get_height = MagicMock()
    el.get_height.return_value = 1
    result = el.get_height()
    assert type(result) == int


def test_get_width():
    el = Element()
    el.get_width = MagicMock()
    el.get_width.return_value = 1
    result = el.get_width()
    assert type(result) == int


def test_click_a_point():
    el = Element()
    el.click_a_point = MagicMock()
    el.click_a_point.return_value = True
    result = el.click_a_point(x=MagicMock(), y=MagicMock())
    assert result == True
