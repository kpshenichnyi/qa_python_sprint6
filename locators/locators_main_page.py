from selenium.webdriver.common.by import By


class LocatorsMainPageScooter:
    # Заголовок страницы "Самокат на пару дней"
    LOCATOR_MAIN_PAGE_TITLE = [By.XPATH, "//div[contains(@class, 'Home_Header')]"]
    # логотип «Яндекса»
    LOCATOR_LOGO_YANDEX = By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]"
    # логотип «Самоката»
    LOCATOR_LOGO_SAMOKAT = By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]"
    # кнопка Заказать вверху страницы
    LOCATOR_BUTTON_ORDER_TOP = By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"
    # кнопка Заказать на странице
    LOCATOR_BUTTON_ORDER_PAGE = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"
    # кнопка Принять куки "да все привыкли"
    LOCATOR_BUTTON_ACCEPT_COOKIES = By.ID, "rcc-confirm-button"


class LocatorsFAQ:
    # Заголовок секции 'Вопросы о важном'
    LOCATOR_HEADER_SECTION_QA = By.XPATH, "//div[text()='Вопросы о важном']"

    # Вопрос с идентификатором 0
    LOCATOR_QUESTION_0 = (By.XPATH, "//div[@id = 'accordion__heading-0']")
    # Ответ на вопрос с идентификатором 0
    LOCATOR_ANSWER_0 = By.XPATH, '//div[@id="accordion__panel-0"]/p'
    # Вопрос с идентификатором 1
    LOCATOR_QUESTION_1 = By.XPATH, "//div[@id = 'accordion__heading-1']"
    # Ответ на вопрос с идентификатором 1
    LOCATOR_ANSWER_1 = By.XPATH, '//div[@id="accordion__panel-1"]/p'
    # Вопрос с идентификатором 2
    LOCATOR_QUESTION_2 = By.XPATH, "//div[@id = 'accordion__heading-2']"
    # Ответ на вопрос с идентификатором 2
    LOCATOR_ANSWER_2 = By.XPATH, '//div[@id="accordion__panel-2"]/p'
    # Вопрос с идентификатором 3
    LOCATOR_QUESTION_3 = By.XPATH, "//div[@id = 'accordion__heading-3']"
    # Ответ на вопрос с идентификатором 3
    LOCATOR_ANSWER_3 = By.XPATH, '//div[@id="accordion__panel-3"]/p'
    # Вопрос с идентификатором 4
    LOCATOR_QUESTION_4 = By.XPATH, "//div[@id = 'accordion__heading-4']"
    # Ответ на вопрос с идентификатором 4
    LOCATOR_ANSWER_4 = By.XPATH, '//div[@id="accordion__panel-4"]/p'
    # Вопрос с идентификатором 5
    LOCATOR_QUESTION_5 = By.XPATH, "//div[@id = 'accordion__heading-5']"
    # Ответ на вопрос с идентификатором 5
    LOCATOR_ANSWER_5 = By.XPATH, '//div[@id="accordion__panel-5"]/p'
    # Вопрос с идентификатором 6
    LOCATOR_QUESTION_6 = By.XPATH, "//div[@id = 'accordion__heading-6']"
    # Ответ на вопрос с идентификатором 6
    LOCATOR_ANSWER_6 = By.XPATH, '//div[@id="accordion__panel-6"]/p'
    # Вопрос с идентификатором 7
    LOCATOR_QUESTION_7 = By.XPATH, "//div[@id = 'accordion__heading-7']"
    # Ответ на вопрос с идентификатором 7
    LOCATOR_ANSWER_7 = By.XPATH, '//div[@id="accordion__panel-7"]/p'

