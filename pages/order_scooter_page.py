from pages.base_page import BasePage
from locators.order_scooter_locators import OrderScooterLocators
from locators.home_page_locators import HomePageLocators
from selenium.common.exceptions import TimeoutException

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_top_order_button(self):
        self.click_element(HomePageLocators.top_button_order)

    def click_bottom_order_button(self):
        self.click_element(HomePageLocators.bottom_button_order)

    def accept_cookies(self):
        self.click_element(HomePageLocators.cookie_button)

    def enter_name(self, name):
        self.enter_text_to_field(OrderScooterLocators.name_field, name)

    def enter_last_name(self, last_name):
        self.enter_text_to_field(OrderScooterLocators.last_name_field, last_name)

    def enter_address(self, address):
        self.enter_text_to_field(OrderScooterLocators.address_field, address)

    def select_metro_station(self, metro_locator):
        self.click_element(OrderScooterLocators.metro_field)
        self.click_element(metro_locator)

    def enter_phone(self, phone):
        self.enter_text_to_field(OrderScooterLocators.phone_field, phone)

    def click_next_button(self):
        self.click_element(OrderScooterLocators.next_button)

    def select_date(self, date_locator):
        self.click_element(OrderScooterLocators.date_field)
        self.click_element(date_locator)

    def select_rental_period(self, rental_period_locator):
        self.click_element(OrderScooterLocators.rental_period_field)
        self.click_element(rental_period_locator)

    def choose_scooter_color(self, color_locator):
        self.click_element(color_locator)

    def enter_comment(self, comment):
        self.enter_text_to_field(OrderScooterLocators.comment_field, comment)

    def click_submit_order_button(self):
        self.click_element(HomePageLocators.bottom_button_order)

    def confirm_order(self):
        self.click_element(OrderScooterLocators.yes_button)

    def is_order_processed(self):
        try:
            self.wait_for_element(OrderScooterLocators.order_processed)
            return True
        except TimeoutException:
            return False


