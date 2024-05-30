from selenium.webdriver.common.by import By


class LocatorsOrderPage:
    # Заголовок формы для заказчика
    LOCATOR_HEADER_ABOUT_USER = By.CSS_SELECTOR, ".Order_Header__BZXOb"
    # Поле для ввода имени
    LOCATOR_FIELD_NAME = By.XPATH, "//input[@placeholder='* Имя']"
    # Поле для ввода фамилии
    LOCATOR_FIELD_LAST_NAME = By.XPATH, "//input[@placeholder='* Фамилия']"
    # Поле для ввода адреса
    LOCATOR_FIELD_ADDRESS = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    # Поле для ввода станции метро
    LOCATOR_FIELD_METRO = By.CSS_SELECTOR, "input[placeholder='* Станция метро']"
    # Поле для выбора станции метро
    LOCATOR_FIELD_METRO_ACK_SELECT_STATION = (By.XPATH, ".//li[@class='select-search__row']")
    # Поле для ввода телефона
    LOCATOR_FIELD_PHONE = By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"
    # Кнопка перехода к форме с данными об аренде
    LOCATOR_BUTTON_NEXT = By.XPATH, "//button[text()='Далее']"
    # Поле с датой поставки самоката
    LOCATOR_FIELD_DATE_START = By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']"
    # Выбор даты поставки самоката = текущая дата
    LOCATOR_FIELD_DATE_START_DAY_1 = By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]"
    # Выбор даты поставки самоката = текущая дата
    LOCATOR_FIELD_DATE_START_DAY_2 = By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--031']"
    # Поле со сроком поставки самоката
    LOCATOR_FIELD_RENT_TIME = By.XPATH, "//div[text()='* Срок аренды']"
    # Выбор срока аренды самоката = сутки
    LOCATOR_TIME_1 = By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']"
    # Выбор срока аренды самоката = трое суток
    LOCATOR_TIME_2 = By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']"
    # Выбор цвета самоката = черный
    LOCATOR_CHOICE_COLOR_BLACK = By.ID, "black"
    # Выбор цвета самоката = серый
    LOCATOR_CHOICE_COLOR_GREY = By.ID, "grey"
    # Поле с комментарием для доставки
    LOCATOR_FIELD_COMMENTS = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    # Кнопка завершения заказа
    LOCATOR_BUTTON_ORDER_END = By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]'
    # Кнопка подтверждения заказа
    LOCATOR_BUTTON_ORDER_YES = By.XPATH, "//button[text()='Да']"

    LOCATOR_WINDOW_ORDER_SUCCESS = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']" #and text()='Хотите оформить заказ?']"
    LOCATOR_WINDOW_ORDER_CONFIRM = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"
    LOCATOR_TEXT_WINDOW_ORDER_PLACED = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']"
    LOCATOR_BUTTON_ORDER_VIEW_STATUS = By.XPATH, "//button[contains(@class,'Button_Button_') and text()='Посмотреть статус']"
