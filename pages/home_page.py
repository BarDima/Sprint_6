from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from config import (text_list_price, text_cancel, text_rental_time, text_live_outside, text_charger,
                    text_extension_return, text_order_for_today, text_several_scooter)

class HomePageScooter:
    def __init__(self, driver):
        self.driver = driver

    def click_and_get_text(self, drop_down_locator, text_locator):
        element = self.driver.find_element(*drop_down_locator)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(text_locator))
        return self.driver.find_element(*text_locator).text

    def check_price_text(self):
        return self.click_and_get_text(HomePageLocators.drop_down_list_price, HomePageLocators.drop_down_list_price_text)

    def check_several_scooters_text(self):
        return self.click_and_get_text(HomePageLocators.drop_down_list_several_scooters, HomePageLocators.drop_down_list_several_scooters_text)

    def check_rental_time_text(self):
        return self.click_and_get_text(HomePageLocators.drop_down_list_rental_time, HomePageLocators.drop_down_list_rental_time_text)

    def check_order_for_today_text(self):
        return self.click_and_get_text(HomePageLocators.drop_down_list_order_for_today, HomePageLocators.drop_down_list_order_for_today_text)

    def check_extension_return_text(self):
        return self.click_and_get_text(HomePageLocators.drop_down_list_extension_return, HomePageLocators.drop_down_list_extension_return_text)

    def check_charger_text(self):
        return self.click_and_get_text(HomePageLocators.drop_down_list_charger, HomePageLocators.drop_down_list_charger_text)

    def check_cancel_text(self):
        return self.click_and_get_text(HomePageLocators.drop_down_list_cancel, HomePageLocators.drop_down_list_cancel_text)

    def check_live_outside_text(self):
        return self.click_and_get_text(HomePageLocators.drop_down_list_live_outside, HomePageLocators.drop_down_list_live_outside_text)

class TestHomePageScooter:
    def test_drop_down_list_price(self, driver):
        home_page = HomePageScooter(driver)
        assert home_page.check_price_text() == text_list_price

    def test_drop_down_several_scooters(self, driver):
        home_page = HomePageScooter(driver)
        assert home_page.check_several_scooters_text() == text_several_scooter

    def test_drop_down_rental_time(self, driver):
        home_page = HomePageScooter(driver)
        assert home_page.check_rental_time_text() == text_rental_time

    def test_drop_down_order_for_today(self, driver):
        home_page = HomePageScooter(driver)
        assert home_page.check_order_for_today_text() == text_order_for_today

    def test_drop_down_extension_return(self, driver):
        home_page = HomePageScooter(driver)
        assert home_page.check_extension_return_text() == text_extension_return

    def test_drop_down_charger(self, driver):
        home_page = HomePageScooter(driver)
        assert home_page.check_charger_text() == text_charger

    def test_drop_down_cancel(self, driver):
        home_page = HomePageScooter(driver)
        assert home_page.check_cancel_text() == text_cancel

    def test_drop_down_live_outside(self, driver):
        home_page = HomePageScooter(driver)
        assert home_page.check_live_outside_text() == text_live_outside





