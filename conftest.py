import pytest
from selenium import webdriver

url = 'https://qa-scooter.praktikum-services.ru/'

@pytest.fixture
def driver():
    browser_driver = webdriver.Firefox()
    browser_driver.get(url)
    yield browser_driver
    browser_driver.quit()