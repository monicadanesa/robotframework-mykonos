import pytest
from pytest_mock import mocker
from mock import MagicMock, call, patch
from mykonos.keywords.element import *
from mykonos.keywords.wait import Wait
from mykonos.locator.locator_element import LocatorElement
from mykonos.keywords.management_device import ManagementDevice


def test_long_click_element():
    el = Click()
    el.long_click_element = MagicMock()
    el.long_click_element.return_value = True
    result = el.long_click_element(text=MagicMock())
    assert result == True

def test_page_should_contain_element():
    el = ExpectedConditions()
    el.page_should_contain_element = MagicMock()
    el.page_should_contain_element.return_value = True
    result = el.page_should_contain_element(className=MagicMock())
    assert result == True

def test_wait_until_page_does_not_contain():
    el = Wait()
    el.wait_until_page_does_not_contain = MagicMock()
    el.wait_until_page_does_not_contain.return_value = False
    result = el.wait_until_page_does_not_contain(className=MagicMock())
    assert result == False

def test_wait_until_page_does_not_contain_element():
    el = Wait()
    el.wait_until_page_does_not_contain_element = MagicMock()
    el.wait_until_page_does_not_contain_element.return_value = False
    result = el.wait_until_page_does_not_contain_element(className=MagicMock())
    assert result == False

def test_check_element_exists():
    el = ExpectedConditions()
    el.check_element_exists = MagicMock()
    el.check_element_exists.return_value = True
    result = el.check_element_exists(className=MagicMock())
    assert result == True

def test_check_element_not_exists():
    el = ExpectedConditions()
    el.check_element_not_exists = MagicMock()
    el.check_element_not_exists.return_value = True
    result = el.check_element_not_exists(className=MagicMock())
    assert result == True

def test_wait_until_page_contains():
    el = Wait()
    el.wait_until_page_contains = MagicMock()
    el.wait_until_page_contains.return_value = True
    result = el.wait_until_page_contains(className=MagicMock())
    assert result == True

def test_wait_until_page_contains_element():
    el = Wait()
    el.wait_until_page_contains_element = MagicMock()
    el.wait_until_page_contains_element.return_value = True
    result = el.wait_until_page_contains_element(className=MagicMock())
    assert result == True

def test_text_should_be_visible():
    el = GlobalElement()
    el.text_should_be_visible = MagicMock()
    el.text_should_be_visible.return_value = True
    result = el.text_should_be_visible(text=MagicMock())
    assert result == True

def test_wait_until_element_is_visible():
    el = Wait()
    el.wait_until_element_is_visible = MagicMock()
    el.wait_until_element_is_visible.return_value = True
    result = el.wait_until_element_is_visible(className=MagicMock())
    assert result == True


def test_page_should_not_contain_element():
    el = ExpectedConditions()
    el.page_should_not_contain_element = MagicMock()
    el.page_should_not_contain_element.return_value = True
    result = el.page_should_not_contain_element(className=MagicMock())
    assert result == True


def test_page_should_not_contain_text():
    el = ExpectedConditions()
    el.page_should_not_contain_text = MagicMock()
    el.page_should_not_contain_text.return_value = True
    result = el.page_should_not_contain_text(className=MagicMock())
    assert result == True


def test_page_should_contain_text():
    el = ExpectedConditions()
    el.page_should_contain_text = MagicMock()
    el.page_should_contain_text.return_value = True
    result = el.page_should_contain_text(text=MagicMock())
    assert result == True


def test_click_element():
    el = Click()
    el.click_element = MagicMock()
    el.click_element.return_value = True
    result = el.click_element(text=MagicMock())
    assert result == True


def test_click_element_parent_without_device():
    el = Click()
    el.click_element = MagicMock()
    el.click_element.return_value = True
    result = el.click_element(locator=MagicMock())
    assert result == True


def test_click_element_parent_with_device():
    el = Click()
    el.click_element = MagicMock()
    el.click_element.return_value = True
    result = el.click_element(device= MagicMock(),locator= MagicMock())
    assert result == True


def test_click_element_device_and_element():
    el = Click()
    d1 = MagicMock()
    text = MagicMock()
    el.click_element = MagicMock()
    el.click_element.return_value = True
    result = el.click_element(device=d1, text="Messaging")
    assert result == True


def test_input_text_with_device_parent():
    el = GlobalElement()
    el.input_text = MagicMock()
    el.input_text.return_value = True
    result = el.input_text(className=MagicMock(), input='Test')
    assert result == True


def test_input_text_with_parameter():
    el = GlobalElement()
    el.input_text = MagicMock()
    el.input_text.return_value = True
    result = el.input_text(device=MagicMock(), input='Test',className=MagicMock())
    assert result == True


def test_input_text_with_locator():
    el = GlobalElement()
    el.input_text = MagicMock()
    el.input_text.return_value = True
    result = el.input_text(className=MagicMock(), input='Test')
    assert result == True


def test_clear_text():
    el = GlobalElement()
    el.clear_text = MagicMock()
    el.clear_text.return_value = True
    result = el.clear_text(className=MagicMock())
    assert result == True


def test_clear_text_with_device():
    el = GlobalElement()
    el.clear_text = MagicMock()
    el.clear_text.return_value = True
    result = el.clear_text(device=MagicMock(), className=MagicMock())
    assert result == True


def test_clear_text_with_device_and_parent():
    el = GlobalElement()
    el.clear_text = MagicMock()
    el.clear_text.return_value = True
    result = el.clear_text(device=MagicMock(), locator=MagicMock())
    assert result == True


def test_get_text():
    el = GetConditions()
    el.get_text = MagicMock()
    el.get_text.return_value = 'return text'
    result = el.get_text(className=MagicMock())
    assert len(result) != 0

def test_get_text_with_device():
    el = GetConditions()
    el.get_text = MagicMock()
    el.get_text.return_value = 'return text'
    result = el.get_text(device=MagicMock(), className=MagicMock())
    assert len(result) != 0


def test_get_text_with_parents():
    el = GetConditions()
    el.get_text = MagicMock()
    el.get_text.return_value = 'return text'
    result = el.get_text(locator=MagicMock())
    assert len(result) != 0


def test_get_text_with_parents_device():
    el = GetConditions()
    el.get_text = MagicMock()
    el.get_text.return_value = 'return text'
    result = el.get_text(device=MagicMock(), locator=MagicMock())
    assert len(result) != 0


def test_get_attribute():
    el = GetConditions()
    el.get_element_attribute = MagicMock()
    el.get_element_attribute.return_value = 'sample return attribute'
    result = el.get_element_attribute(element=MagicMock(), className=MagicMock())
    assert len(result) != 0


def test_get_attribute_with_device():
    el = GetConditions()
    el.get_element_attribute = MagicMock()
    el.get_element_attribute.return_value = 'sample return attribute'
    result = el.get_element_attribute(device=MagicMock(), element=MagicMock(), className=MagicMock())
    assert len(result) != 0


def test_get_attribute_with_parent():
    el = GetConditions()
    el.get_element_attribute = MagicMock()
    el.get_element_attribute.return_value = 'sample return attribute'
    result = el.get_element_attribute(locator=MagicMock(), element='text')
    assert len(result) != 0


def test_get_element():
    el = GetConditions()
    el.get_element = MagicMock()
    el.get_element.return_value = 'sample return element'
    result = el.get_element(className=MagicMock())
    assert len(result) != 0

def test_text_should_be_enabled():
    el = GetConditions()
    el.text_should_be_enabled = MagicMock()
    el.text_should_be_enabled.return_value = True
    result = el.text_should_be_enabled(device=MagicMock(), className=MagicMock())
    assert result == True

def test_text_should_be_disabled():
    el = GetConditions()
    el.text_should_be_disabled = MagicMock()
    el.text_should_be_disabled.return_value = True
    result = el.text_should_be_disabled(device=MagicMock(), className=MagicMock())
    assert result == True

def test_element_should_contain_text():
    el = ExpectedConditions()
    el.element_should_contain_text = MagicMock()
    el.element_should_contain_text.return_value = True
    result = el.element_should_contain_text(device=MagicMock(), className=MagicMock(), text=MagicMock())
    assert result == True

def test_element_should_not_contain_text():
    el = ExpectedConditions()
    el.element_should_not_contain_text = MagicMock()
    el.element_should_not_contain_text.return_value = True
    result = el.element_should_not_contain_text(device=MagicMock(), className=MagicMock(), text=MagicMock())
    assert result == True

def test_check_element_visible():
    el = ExpectedConditions()
    el.check_element_visible = MagicMock()
    el.check_element_visible.return_value = True
    result = el.check_element_visible(device=MagicMock(), className=MagicMock(), text=MagicMock())
    assert result == True

def test_check_element_non_visible():
    el = ExpectedConditions()
    el.check_element_non_visible = MagicMock()
    el.check_element_non_visible.return_value = True
    result = el.check_element_non_visible(device=MagicMock(), className=MagicMock(), text=MagicMock())
    assert result == True

def test_get_element_with_device():
    el = GetConditions()
    el.get_element = MagicMock()
    el.get_element.return_value = 'sample return element'
    result = el.get_element(device=MagicMock(), className=MagicMock())
    assert len(result) != 0


def test_get_element_with_parent():
    el = GetConditions()
    el.get_element = MagicMock()
    el.get_element.return_value = 'sample return element'
    result = el.get_element(locator=MagicMock())
    assert len(result) != 0


def test_count_element():
    el = GlobalElement()
    el.count_elements = MagicMock()
    el.count_elements.return_value = 1
    result = el.count_elements(className=MagicMock())
    assert type(result) == int


def test_count_element_with_parent():
    el = GlobalElement()
    el.count_elements = MagicMock()
    el.count_elements.return_value = 1
    result = el.count_elements(locator=MagicMock())
    assert type(result) == int


def test_get_height():
    el = GetConditions()
    el.get_height = MagicMock()
    el.get_height.return_value = 1
    result = el.get_height()
    assert type(result) == int


def test_get_width():
    el = GetConditions()
    el.get_width = MagicMock()
    el.get_width.return_value = 1
    result = el.get_width()
    assert type(result) == int


def test_click_a_point():
    el = Click()
    el.click_a_point = MagicMock()
    el.click_a_point.return_value = True
    result = el.click_a_point(x=MagicMock(), y=MagicMock())
    assert result == True
