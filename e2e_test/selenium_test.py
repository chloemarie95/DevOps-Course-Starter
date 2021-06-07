from e2e_test import driver, test_app
import pytest

def test_check_title(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'

