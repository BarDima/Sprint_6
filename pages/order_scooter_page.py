from locators.order_scooter_locators import OrderScooterLocators
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest

class OrderScooterPage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator)).click()

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def open_order_form(self, entry_point):
        if entry_point == 'top_button':
            self.click(BasePageLocators.top_button_order)
        elif entry_point == 'bottom_button':
            element = self.find_element(BasePageLocators.bottom_button_order)
            self.driver.execute_script("arguments[0].click();", element)
        self.click(BasePageLocators.cookie_button)

    def fill_personal_info(self, name, last_name, address, phone, metro_locator):
        self.send_keys(OrderScooterLocators.name_field, name)
        self.send_keys(OrderScooterLocators.last_name_field, last_name)
        self.send_keys(OrderScooterLocators.address_field, address)
        self.click(OrderScooterLocators.metro_field)
        self.click(metro_locator)
        self.send_keys(OrderScooterLocators.phone_field, phone)
        self.click(OrderScooterLocators.next_button)

    def fill_rental_info(self, date_locator, rental_period_locator, color_locator, comment):
        self.click(OrderScooterLocators.date_field)
        self.click(date_locator)
        self.click(OrderScooterLocators.rental_period_field)
        self.click(rental_period_locator)
        self.click(color_locator)
        self.send_keys(OrderScooterLocators.comment_field, comment)
        self.click(BasePageLocators.bottom_button_order)

    def confirm_order(self):
        self.click(OrderScooterLocators.yes_button)
        return self.find_element(OrderScooterLocators.order_processed).is_displayed()



@pytest.mark.parametrize("entry_point, name, last_name, address, phone, metro_locator, date_locator, rental_period_locator, color_locator, comment", [
    ('top_button', 'Алексей', 'Сидоров', 'улица Набережная, дом 25, квартира 7', '78901234567', OrderScooterLocators.metro_station_rokosovskogo, OrderScooterLocators.date_choice_1, OrderScooterLocators.rental_period_1, OrderScooterLocators.scooter_color_black, 'Привет, жду!'),
    ('bottom_button', 'Иван', 'Петров', 'улица Строителей, дом 7, квартира 25', '75901234564', OrderScooterLocators.metro_station_cherkizovskya, OrderScooterLocators.date_choice_2, OrderScooterLocators.rental_period_2, OrderScooterLocators.scooter_color_grey, 'Код от подъезда 1111')
])
def test_order_scooter(driver, entry_point, name, last_name, address, phone, metro_locator, date_locator, rental_period_locator, color_locator, comment):
    order_page = OrderScooterPage(driver)
    order_page.open_order_form(entry_point)
    order_page.fill_personal_info(name, last_name, address, phone, metro_locator)
    order_page.fill_rental_info(date_locator, rental_period_locator, color_locator, comment)
    assert order_page.confirm_order()