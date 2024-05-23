from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def click_element_script(self, locator):
        element = self.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)


    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_url_contains(self, url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_part))

    def switch_to_last_tab(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])

    def enter_text_to_field(self, locator, text):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)




