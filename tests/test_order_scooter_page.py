import pytest
from locators.order_scooter_locators import OrderScooterLocators
from locators.base_page_locators import BasePageLocators


@pytest.mark.parametrize("entry_point, name, last_name, address, phone, metro_locator, date_locator, rental_period_locator, color_locator, comment", [('top_button', 'Алексей', 'Сидоров', 'улица Набережная, дом 25, квартира 7', '78901234567', OrderScooterLocators.metro_station_rokosovskogo, OrderScooterLocators.date_choice_1, OrderScooterLocators.rental_period_1, OrderScooterLocators.scooter_color_black, 'Привет, жду!'), ('bottom_button', 'Иван', 'Петров', 'улица Строителей, дом 7, квартира 25', '75901234564', OrderScooterLocators.metro_station_cherkizovskya, OrderScooterLocators.date_choice_2, OrderScooterLocators.rental_period_2, OrderScooterLocators.scooter_color_grey, 'Код от подъезда 1111')])
def test_order_scooter(driver, entry_point, name, last_name, address, phone, metro_locator, date_locator, rental_period_locator, color_locator, comment):
    if entry_point == 'top_button':
        driver.find_element(*BasePageLocators.top_button_order).click()
    if entry_point == 'bottom_button':
        element = driver.find_element(*BasePageLocators.bottom_button_order)
        driver.execute_script("arguments[0].click();", element)
    driver.find_element(*BasePageLocators.cookie_button).click()
    driver.find_element(*OrderScooterLocators.name_field).send_keys(name)
    driver.find_element(*OrderScooterLocators.last_name_field).send_keys(last_name)
    driver.find_element(*OrderScooterLocators.address_field).send_keys(address)
    driver.find_element(*OrderScooterLocators.metro_field).click()
    driver.find_element(*metro_locator).click()
    driver.find_element(*OrderScooterLocators.phone_field).send_keys(phone)
    driver.find_element(*OrderScooterLocators.next_button).click()
    driver.find_element(*OrderScooterLocators.date_field).click()
    driver.find_element(*date_locator).click()
    driver.find_element(*OrderScooterLocators.rental_period_field).click()
    driver.find_element(*rental_period_locator).click()
    driver.find_element(*color_locator).click()
    driver.find_element(*OrderScooterLocators.comment_field).send_keys(comment)
    driver.find_element(*BasePageLocators.bottom_button_order).click()
    driver.find_element(*OrderScooterLocators.yes_button)
    assert driver.find_element(*OrderScooterLocators.order_processed).is_displayed()


