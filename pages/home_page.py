from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_drop_down(self, locator, text_locator, expected_text):
        self.click_element_script(locator)
        assert self.get_element_text(text_locator) == expected_text

    def click_top_button_order(self):
        self.click_element_script(HomePageLocators.top_button_order)

    def get_element_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    def click_logo_scooter(self):
        self.click_element_script(HomePageLocators.logo_scooter)

    def click_logo_yandex(self):
        self.click_element_script(HomePageLocators.logo_yandex)
