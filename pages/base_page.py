from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from config import URL, URL_DZEN

class BasePageScooter:
    def __init__(self, driver):
        self.driver = driver

    def click_top_button_order(self):
        self.driver.find_element(*BasePageLocators.top_button_order).click()

    def click_logo_scooter(self):
        self.driver.find_element(*BasePageLocators.logo_scooter).click()

    def check_current_url(self):
        return self.driver.current_url

    def click_logo_yandex(self):
        self.driver.find_element(*BasePageLocators.logo_yandex).click()

    def check_to_new_tab(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])

    def check_waiting_loading(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(f'{URL_DZEN}'))



class TestBasePage:
    def test_logo_scooter(self, driver):
        base_page = BasePageScooter(driver)
        base_page.click_top_button_order()
        base_page.click_logo_scooter()
        assert base_page.check_current_url() == f'{URL}'

    def test_logo_yandex(self, driver):
        base_page = BasePageScooter(driver)
        base_page.click_logo_yandex()
        base_page.check_to_new_tab()
        base_page.check_waiting_loading()
        assert f'{URL_DZEN}' in base_page.check_current_url()