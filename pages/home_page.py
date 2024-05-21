from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
import allure

class HomePage(BasePage):
    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверка соответствия текста')
    def click_drop_down(self, locator, text_locator, expected_text):
        self.click_element_script(locator)
        assert self.get_element_text(text_locator) == expected_text

    @allure.step('Клик на верхнюю кнопку Заказать')
    def click_top_button_order(self):
        self.click_element_script(HomePageLocators.top_button_order)

    @allure.step('Ожидание элемента страницы')
    def get_element_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step('Клик на логотип Самокат')
    def click_logo_scooter(self):
        self.click_element_script(HomePageLocators.logo_scooter)

    @allure.step('Клик на логотип Яндекс')
    def click_logo_yandex(self):
        self.click_element_script(HomePageLocators.logo_yandex)
