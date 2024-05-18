from selenium.webdriver.common.by import By

class BasePageLocators:
    top_button_order = (By.XPATH, "*//button[@class='Button_Button__ra12g']")#верхняя кнопка "Заказать"
    bottom_button_order = (By.XPATH, "*//button[contains(@class, 'Button_Middle') and text()='Заказать']")#нижняя кнопка "Заказать"
    logo_yandex = (By.XPATH, "*//a[contains(@class, 'Header_LogoYandex')]")#логотип Яндекс
    logo_scooter = (By.XPATH, "*//a[contains(@class, 'Header_LogoScooter')]")#логотип самокат
    cookie_button = (By.ID, 'rcc-confirm-button')  # кнопка куки