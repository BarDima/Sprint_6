from locators.order_scooter_locators import OrderScooterLocators
from pages.order_scooter_page import OrderPage
from data import (name_top_button, last_name_top_button, address_top_button, phone_top_button, comment_top_button,
                  name_bottom_button, last_name_bottom_button, address_bottom_button, phone_bottom_button, comment_bottom_button)
from pages.home_page import HomePage
class TestOrderPage:
    def test_order_scooter_top_button(self, driver):
        order_page = OrderPage(driver)
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.click_top_button_order()
        order_page.enter_name(name_top_button)
        order_page.enter_last_name(last_name_top_button)
        order_page.enter_address(address_top_button)
        order_page.select_metro_station(OrderScooterLocators.metro_station_rokosovskogo)
        order_page.enter_phone(phone_top_button)
        order_page.click_next_button()
        order_page.select_date(OrderScooterLocators.date_choice_1)
        order_page.select_rental_period(OrderScooterLocators.rental_period_1)
        order_page.choose_scooter_color(OrderScooterLocators.scooter_color_black)
        order_page.enter_comment(comment_top_button)
        order_page.click_submit_order_button()
        order_page.confirm_order()
        assert order_page.is_order_processed()

    def test_order_scooter_bottom_button(self, driver):
        order_page = OrderPage(driver)
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.click_top_button_order()
        order_page.enter_name(name_bottom_button)
        order_page.enter_last_name(last_name_bottom_button)
        order_page.enter_address(address_bottom_button)
        order_page.select_metro_station(OrderScooterLocators.metro_station_cherkizovskya)
        order_page.enter_phone(phone_bottom_button)
        order_page.click_next_button()
        order_page.select_date(OrderScooterLocators.date_choice_2)
        order_page.select_rental_period(OrderScooterLocators.rental_period_2)
        order_page.choose_scooter_color(OrderScooterLocators.scooter_color_grey)
        order_page.enter_comment(comment_bottom_button)
        order_page.click_submit_order_button()
        order_page.confirm_order()
        assert order_page.is_order_processed()
