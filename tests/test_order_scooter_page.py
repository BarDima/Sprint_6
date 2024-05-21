from locators.order_scooter_locators import OrderScooterLocators
from pages.order_scooter_page import OrderPage

class TestOrderPage:
    def test_order_scooter_top_button(self, driver):
        order_page = OrderPage(driver)
        order_page.click_top_order_button()
        order_page.accept_cookies()
        order_page.enter_name('Алексей')
        order_page.enter_last_name('Сидоров')
        order_page.enter_address('улица Набережная, дом 25, квартира 7')
        order_page.select_metro_station(OrderScooterLocators.metro_station_rokosovskogo)
        order_page.enter_phone('78901234567')
        order_page.click_next_button()
        order_page.select_date(OrderScooterLocators.date_choice_1)
        order_page.select_rental_period(OrderScooterLocators.rental_period_1)
        order_page.choose_scooter_color(OrderScooterLocators.scooter_color_black)
        order_page.enter_comment('Привет, жду!')
        order_page.click_submit_order_button()
        order_page.confirm_order()
        assert order_page.is_order_processed()

    def test_order_scooter_bottom_button(self, driver):
        order_page = OrderPage(driver)
        order_page.click_top_order_button()
        order_page.accept_cookies()
        order_page.enter_name('Иван')
        order_page.enter_last_name('Петров')
        order_page.enter_address('улица Строителей, дом 7, квартира 25')
        order_page.select_metro_station(OrderScooterLocators.metro_station_cherkizovskya)
        order_page.enter_phone('75901234564')
        order_page.click_next_button()
        order_page.select_date(OrderScooterLocators.date_choice_2)
        order_page.select_rental_period(OrderScooterLocators.rental_period_2)
        order_page.choose_scooter_color(OrderScooterLocators.scooter_color_grey)
        order_page.enter_comment('Код от подъезда 1111')
        order_page.click_submit_order_button()
        order_page.confirm_order()
        assert order_page.is_order_processed()
