import pytest
from selenium import webdriver
from locators import TestLocators


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()

    yield driver
    driver.quit()