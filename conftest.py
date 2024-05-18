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
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(HomePageLocators.text_questions_about_important))
    yield driver
    driver.quit()

