from config import URL_DZEN, URL
from data import (text_list_price, text_several_scooter, text_rental_time, text_order_for_today, text_extension_return,
    text_charger, text_cancel, text_live_outside)
import pytest
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
import allure


class TestHomePage:

    @pytest.mark.parametrize("locator, text_locator, expected_text", [
        (HomePageLocators.drop_down_list_price, HomePageLocators.drop_down_list_price_text, text_list_price),
        (HomePageLocators.drop_down_list_several_scooters, HomePageLocators.drop_down_list_several_scooters_text, text_several_scooter),
        (HomePageLocators.drop_down_list_rental_time, HomePageLocators.drop_down_list_rental_time_text, text_rental_time),
        (HomePageLocators.drop_down_list_order_for_today, HomePageLocators.drop_down_list_order_for_today_text, text_order_for_today),
        (HomePageLocators.drop_down_list_extension_return, HomePageLocators.drop_down_list_extension_return_text, text_extension_return),
        (HomePageLocators.drop_down_list_charger, HomePageLocators.drop_down_list_charger_text, text_charger),
        (HomePageLocators.drop_down_list_cancel, HomePageLocators.drop_down_list_cancel_text, text_cancel),
        (HomePageLocators.drop_down_list_live_outside, HomePageLocators.drop_down_list_live_outside_text, text_live_outside),
    ])

    @allure.step('Проверка соответствия текста выпадающего списка')
    def test_drop_down_list(self, driver, locator, text_locator, expected_text):
        home_page = HomePage(driver)
        home_page.click_drop_down(locator, text_locator, expected_text)

    @allure.step('Проверка перехода на главную страницу при нажатии на логотип Самокат')
    def test_logo_scooter(self, driver):
        home_page = HomePage(driver)
        home_page.click_top_button_order()
        home_page.click_logo_scooter()
        assert home_page.get_current_url() == URL

    @allure.step('Проверка нажатия на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')
    def test_logo_yandex(self, driver):
        home_page = HomePage(driver)
        home_page.click_logo_yandex()
        home_page.switch_to_last_tab()
        home_page.wait_for_url_contains(URL_DZEN)
        assert URL_DZEN in home_page.get_current_url()