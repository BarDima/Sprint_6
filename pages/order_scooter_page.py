from pages.base_page import BasePage
from locators.order_scooter_locators import OrderScooterLocators
from locators.home_page_locators import HomePageLocators
from selenium.common.exceptions import TimeoutException
import allure

class OrderPage(BasePage):
    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)



    @allure.step('Вводим данные в поле Имя')
    def enter_name(self, name):
        self.enter_text_to_field(OrderScooterLocators.name_field, name)

    @allure.step('Вводим данные в поле Фамилия')
    def enter_last_name(self, last_name):
        self.enter_text_to_field(OrderScooterLocators.last_name_field, last_name)

    @allure.step('Вводим данные в поле Адрес')
    def enter_address(self, address):
        self.enter_text_to_field(OrderScooterLocators.address_field, address)

    @allure.step('Выбираем станцию метро')
    def select_metro_station(self, metro_locator):
        self.click_element(OrderScooterLocators.metro_field)
        self.click_element(metro_locator)

    @allure.step('Вводим данные в поле Телефон')
    def enter_phone(self, phone):
        self.enter_text_to_field(OrderScooterLocators.phone_field, phone)

    @allure.step('Нажимаем кнопку далее')
    def click_next_button(self):
        self.click_element(OrderScooterLocators.next_button)

    @allure.step('Выбираем дату доставки')
    def select_date(self, date_locator):
        self.click_element(OrderScooterLocators.date_field)
        self.click_element(date_locator)

    @allure.step('Выбираем срок аренды')
    def select_rental_period(self, rental_period_locator):
        self.click_element(OrderScooterLocators.rental_period_field)
        self.click_element(rental_period_locator)

    @allure.step('Выбираем цвет самоката')
    def choose_scooter_color(self, color_locator):
        self.click_element(color_locator)

    @allure.step('Добавляем комментарий')
    def enter_comment(self, comment):
        self.enter_text_to_field(OrderScooterLocators.comment_field, comment)

    @allure.step('Нажимаем кнопку заказать')
    def click_submit_order_button(self):
        self.click_element(HomePageLocators.bottom_button_order)

    @allure.step('Подтверждаем заказ')
    def confirm_order(self):
        self.click_element(OrderScooterLocators.yes_button)

    @allure.step('Проверяем подтверждение заказа')
    def is_order_processed(self):
        try:
            self.wait_for_element(OrderScooterLocators.order_processed)
            return True
        except TimeoutException:
            return False


