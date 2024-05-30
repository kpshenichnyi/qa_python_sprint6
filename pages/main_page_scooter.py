import allure
from conftest import driver
from pages.base_page import BasePage
from locators.locators_main_page import LocatorsMainPageScooter, LocatorsFAQ


class MainPageScooter(BasePage):

    @allure.step('Инициализируем работу со страницей в браузере Firefox')
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Дождаться загрузки заголовка "Самокат на пару дней" на главной странице')
    def main_wait_for_load_page_title(self):
        self.base_wait_visibility_of_element_located(LocatorsMainPageScooter.LOCATOR_MAIN_PAGE_TITLE)


    @allure.step('Нажать на логотип Яндекса')
    def click_on_logo_yandex_in_header(self):
        self.base_click_to_element(LocatorsMainPageScooter.LOCATOR_LOGO_YANDEX)


    @allure.step('Нажать кнопку Заказать в заголовке страницы')
    def main_click_button_order_top(self):
        self.base_click_to_element(LocatorsMainPageScooter.LOCATOR_BUTTON_ORDER_TOP)


    @allure.step('Нажать кнопку Заказать в середине странице')
    def main_click_button_order_page(self):
        self.base_click_to_element(LocatorsMainPageScooter.LOCATOR_BUTTON_ORDER_PAGE)


class MainPageFAQSection(BasePage):

    @allure.step('Инициализируем работу со страницей в браузере Firefox')
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Прокрутить страницу до секции "Вопросы о важном"')
    def faq_scroll_to_questions_answers(self):
        self.base_scroll_to_element(LocatorsFAQ.LOCATOR_HEADER_SECTION_QA)


    @allure.step('Клик на вопрос - 0')
    def faq_click_question_id_0(self):
        self.base_click_to_element(LocatorsFAQ.LOCATOR_QUESTION_0)


    @allure.step('Получить текст вопроса - 0')
    def get_text_question_for_faq_0(self):
        return self.base_get_text_of_element(LocatorsFAQ.LOCATOR_QUESTION_0)


    @allure.step('Получить текст ответа, на вопрос - 0')
    def get_text_answer_for_faq_0(self):
        return self.base_get_text_of_element(LocatorsFAQ.LOCATOR_ANSWER_0)


    @allure.step('Клик на вопрос - 1')
    def faq_click_question_id_1(self):
        self.base_click_to_element(LocatorsFAQ.LOCATOR_QUESTION_1)


    @allure.step('Получить текст вопроса - 1')
    def get_text_question_for_faq_1(self):
        return self.base_get_text_of_element(LocatorsFAQ.LOCATOR_QUESTION_1)


    @allure.step('Получить текст ответа, на вопрос - 1')
    def get_text_answer_for_faq_1(self):
        return self.base_get_text_of_element(LocatorsFAQ.LOCATOR_ANSWER_1)


    @allure.step('Клик на вопрос - 2')
    def faq_click_question_id_2(self):
        self.base_click_to_element(LocatorsFAQ.LOCATOR_QUESTION_2)


    @allure.step('Получить текст вопроса - 2')
    def get_text_question_for_faq_2(self):
        return self.base_get_text_of_element(LocatorsFAQ.LOCATOR_QUESTION_2)


    @allure.step('Получить текст ответа, на вопрос - 2')
    def get_text_answer_for_faq_2(self):
        return self.base_get_text_of_element(LocatorsFAQ.LOCATOR_ANSWER_2)


    @allure.step('Клик на вопрос - 3')
    def faq_click_question_id_3(self):
        self.base_click_to_element(LocatorsFAQ.LOCATOR_QUESTION_3)


    @allure.step('Получить текст вопроса - 3')
    def get_text_question_for_faq_3(self):
        return self.base_get_text_of_element(LocatorsFAQ.LOCATOR_QUESTION_3)


    @allure.step('Получить текст ответа, на вопрос - 3')
    def get_text_answer_for_faq_3(self):
        return self.base_get_text_of_element(LocatorsFAQ.LOCATOR_ANSWER_3)


    @allure.step('Клик на вопрос - 4')
    def faq_click_question_id_4(self):
        self.base_click_to_element(LocatorsFAQ.LOCATOR_QUESTION_4)


    @allure.step('Получить текст вопроса - 4')
    def get_text_question_for_faq_4(self):
        return self.base_get_text_of_element(LocatorsFAQ.LOCATOR_QUESTION_4)


    @allure.step('Получить текст ответа, на вопрос - 4')
    def get_text_answer_for_faq_4(self):
        return self.base_get_text_of_element(LocatorsFAQ.LOCATOR_ANSWER_4)


    @allure.step('Клик на вопрос - 5')
    def faq_click_question_id_5(self):
        self.base_click_to_element(LocatorsFAQ.LOCATOR_QUESTION_5)


    @allure.step('Получить текст вопроса - 5')
    def get_text_question_for_faq_5(self):
        return self.base_get_text_of_element(LocatorsFAQ.LOCATOR_QUESTION_5)


    @allure.step('Получить текст ответа, на вопрос - 5')
    def get_text_answer_for_faq_5(self):
        return self.base_get_text_of_element(LocatorsFAQ.LOCATOR_ANSWER_5)


    @allure.step('Клик на вопрос - 6')
    def faq_click_question_id_6(self):
        self.base_click_to_element(LocatorsFAQ.LOCATOR_QUESTION_6)


    @allure.step('Получить текст вопроса - 6')
    def get_text_question_for_faq_6(self):
        return self.base_get_text_of_element(LocatorsFAQ.LOCATOR_QUESTION_6)


    @allure.step('Получить текст ответа, на вопрос - 6')
    def get_text_answer_for_faq_6(self):
        return self.base_get_text_of_element(LocatorsFAQ.LOCATOR_ANSWER_6)


    @allure.step('Клик на вопрос - 7')
    def faq_click_question_id_7(self):
        self.base_click_to_element(LocatorsFAQ.LOCATOR_QUESTION_7)


    @allure.step('Получить текст вопроса - 7')
    def get_text_question_for_faq_7(self):
        return self.base_get_text_of_element(LocatorsFAQ.LOCATOR_QUESTION_7)


    @allure.step('Получить текст ответа, на вопрос - 7')
    def get_text_answer_for_faq_7(self):
        return self.base_get_text_of_element(LocatorsFAQ.LOCATOR_ANSWER_7)

