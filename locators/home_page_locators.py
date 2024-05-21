from selenium.webdriver.common.by import By

class HomePageLocators:
    drop_down_list_price = (By.XPATH, "//*[@id='accordion__heading-0']")#выпадающий список 'Сколько это стоит? И как оплатить?'
    drop_down_list_price_text = (By.XPATH, "//*[@id='accordion__panel-0']" )#текст выпадающего списка 'Сколько это стоит? И как оплатить?'
    drop_down_list_several_scooters = (By.ID, 'accordion__heading-1')#выпадающий список "Хочу сразу несколько самокатов! Так можно?"
    drop_down_list_several_scooters_text = (By.ID, 'accordion__panel-1')#текст выпадающего списка "Хочу сразу несколько самокатов! Так можно?"
    drop_down_list_rental_time = (By.ID, 'accordion__heading-2')#выпадающий список "Как рассчитывается время аренды?"
    drop_down_list_rental_time_text = (By.ID, 'accordion__panel-2')#текст выпадающего списка "Как рассчитывается время аренды?"
    drop_down_list_order_for_today = (By.ID, 'accordion__heading-3')#выпадающий список "Можно ли заказать самокат прямо на сегодня?"
    drop_down_list_order_for_today_text = (By.ID, 'accordion__panel-3')#текст выпадающего списка "Можно ли заказать самокат прямо на сегодня?"
    drop_down_list_extension_return = (By.ID, 'accordion__heading-4')#выпадающий список "Можно ли продлить заказ или вернуть самокат раньше?"
    drop_down_list_extension_return_text =(By.ID, 'accordion__panel-4')#текст выпадающего списка "Можно ли продлить заказ или вернуть самокат раньше?"
    text_questions_about_important = (By.XPATH, "*//div[text()='Вопросы о важном']")#текст раздела "Вопросы о важном"
    drop_down_list_charger = (By.ID, 'accordion__heading-5')#выпадающий список "Вы привозите зарядку вместе с самокатом?"
    drop_down_list_charger_text = (By.ID, 'accordion__panel-5')#текст выпадающего списка "Вы привозите зарядку вместе с самокатом?"
    drop_down_list_cancel = (By.ID, 'accordion__heading-6')#выпадающий список "Можно ли отменить заказ?"
    drop_down_list_cancel_text = (By.ID, 'accordion__panel-6')#текст выпадающего списка "Можно ли отменить заказ?"
    drop_down_list_live_outside = (By.ID, 'accordion__heading-7')#выпадающий список "Я жизу за МКАДом, привезёте?"
    drop_down_list_live_outside_text = (By.ID, 'accordion__panel-7')#текст выпадающего списка "Я жизу за МКАДом, привезёте?"
    top_button_order = (By.XPATH, "*//button[@class='Button_Button__ra12g']")  # верхняя кнопка "Заказать"
    bottom_button_order = (
    By.XPATH, "*//button[contains(@class, 'Button_Middle') and text()='Заказать']")  # нижняя кнопка "Заказать"
    logo_yandex = (By.XPATH, "*//a[contains(@class, 'Header_LogoYandex')]")  # логотип Яндекс
    logo_scooter = (By.XPATH, "*//a[contains(@class, 'Header_LogoScooter')]")  # логотип самокат
    cookie_button = (By.ID, 'rcc-confirm-button')  # кнопка куки

