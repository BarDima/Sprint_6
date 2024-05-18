from selenium.webdriver.common.by import By
class OrderScooterLocators:
    name_field = (By.CSS_SELECTOR, "input[placeholder='* Имя']")# поле имя
    last_name_field = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")# поле фамилия
    address_field = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")# поле адрес
    metro_field = (By.XPATH, "*//input[@class='select-search__input']")#поле станция метро
    metro_station_rokosovskogo = (By.XPATH, "*//li[@data-value='1']")#выбор станции метро Рокоссовского
    metro_station_cherkizovskya = (By.XPATH, "*//li[@data-value='2']")#выбор станции Черкизовская
    phone_field = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")# поле "телефон"
    next_button = (By.XPATH, "*//button[text()='Далее']")#кнопка "далее"
    date_field = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")#поле ввода "Когда привезти самокат"
    date_choice_1 = (By.XPATH, "*//div[@aria-label='Choose четверг, 30-е мая 2024 г.']")#выбор даты "Когда привезти самокат"
    date_choice_2 = (By.XPATH, "*//div[@aria-label='Choose суббота, 1-е июня 2024 г.']")#выбор даты "Когда привезти самокат"
    rental_period_field = (By.XPATH, "*//div[@class='Dropdown-placeholder']")#поле ввода срок аренды
    rental_period_1 = (By.XPATH, "*//div[text()='сутки']")#выбор срока аренды
    rental_period_2 =(By.XPATH, "*//div[text()='двое суток']")#выбор срока аренды
    scooter_color_black = (By.ID, 'black')#чекбокс черный
    scooter_color_grey = (By.ID, 'grey')#чекбокс серый
    yes_button = (By.XPATH, "*//button[contains(@class, 'Button_Middle') and text()='Да']")#кнопка "Да", всплывающее окно подтверждение заказа
    order_processed = (By.XPATH, "*//div[@class='Order_Modal__YZ-d3']")#всплывающее окно "Заказ оформлен"
    comment_field = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")#поле ввода комментарий