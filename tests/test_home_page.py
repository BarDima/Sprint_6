from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import BasePageLocators
from config import URL_DZEN, URL
from config import (text_list_price, text_several_scooter, text_rental_time, text_order_for_today, text_extension_return,
                    text_charger, text_cancel, text_live_outside)




class TestHomePage:
    def test_drop_down_list_price(self, driver):
        element = driver.find_element(*HomePageLocators.drop_down_list_price)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.drop_down_list_price_text))
        assert driver.find_element(*HomePageLocators.drop_down_list_price_text).text == text_list_price

    def test_drop_down_several_scooters(self, driver):
        element = driver.find_element(*HomePageLocators.drop_down_list_several_scooters)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.drop_down_list_several_scooters_text))
        assert driver.find_element(*HomePageLocators.drop_down_list_several_scooters_text).text == text_several_scooter

    def test_drop_down_rental_time(self, driver):
        element = driver.find_element(*HomePageLocators.drop_down_list_rental_time)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.drop_down_list_rental_time_text))
        assert driver.find_element(*HomePageLocators.drop_down_list_rental_time_text).text == text_rental_time

    def test_drop_down_order_for_today(self, driver):
        element = driver.find_element(*HomePageLocators.drop_down_list_order_for_today)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.drop_down_list_order_for_today_text))
        assert driver.find_element(*HomePageLocators.drop_down_list_order_for_today_text).text == text_order_for_today

    def test_drop_down_extension_return(self, driver):
        element = driver.find_element(*HomePageLocators.drop_down_list_extension_return)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.drop_down_list_extension_return_text))
        assert driver.find_element(*HomePageLocators.drop_down_list_extension_return_text).text == text_extension_return

    def test_drop_down_charger(self, driver):
        element = driver.find_element(*HomePageLocators.drop_down_list_charger)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.drop_down_list_charger_text))
        assert driver.find_element(*HomePageLocators.drop_down_list_charger_text).text == text_charger

    def test_drop_down_cancel(self, driver):
        element = driver.find_element(*HomePageLocators.drop_down_list_cancel)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.drop_down_list_cancel_text))
        assert driver.find_element(*HomePageLocators.drop_down_list_cancel_text).text == text_cancel

    def test_drop_down_live_outside(self, driver):
        element = driver.find_element(*HomePageLocators.drop_down_list_live_outside)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.drop_down_list_live_outside_text))
        assert driver.find_element(*HomePageLocators.drop_down_list_live_outside_text).text == text_live_outside

    def test_logo_scooter(self, driver):
        driver.find_element(*BasePageLocators.top_button_order).click()
        driver.find_element(*BasePageLocators.logo_scooter).click()
        assert driver.current_url == f'{URL}'

    def test_logo_yandex(self, driver):
        driver.find_element(*BasePageLocators.logo_yandex).click()
        all_tabs = driver.window_handles
        driver.switch_to.window(all_tabs[-1])
        WebDriverWait(driver, 10).until(expected_conditions.url_contains(f'{URL_DZEN}'))
        assert f'{URL_DZEN}' in driver.current_url
