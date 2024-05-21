import pytest
from selenium import webdriver
from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from config import URL


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1280, 720)
    driver.get(f'{URL}')
    yield driver
    driver.quit()

