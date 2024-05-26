import time
import pytest
import allure

from pages.base_page import BasePage
from pages.main_page_scooter import MainPageScooter, MainPageFAQSection
from locators.locators_main_page import LocatorsFAQ


from conftest import driver

class TestFaqScooterRental:

    @pytest.mark.parametrize("test_faq_id, actual_question, actual_answer, expected_question, expected_answer", [
                            (MainPageFAQSection.faq_click_question_id_0, MainPageFAQSection.get_text_question_for_faq_0, MainPageFAQSection.get_text_answer_for_faq_0,
                                "Сколько это стоит? И как оплатить?", "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
                            (MainPageFAQSection.faq_click_question_id_1, MainPageFAQSection.get_text_question_for_faq_1, MainPageFAQSection.get_text_answer_for_faq_1,
                                "Хочу сразу несколько самокатов! Так можно?", "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
                            (MainPageFAQSection.faq_click_question_id_2, MainPageFAQSection.get_text_question_for_faq_2, MainPageFAQSection.get_text_answer_for_faq_2,
                                "Как рассчитывается время аренды?", "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
                            (MainPageFAQSection.faq_click_question_id_3, MainPageFAQSection.get_text_question_for_faq_3, MainPageFAQSection.get_text_answer_for_faq_3,
                                "Можно ли заказать самокат прямо на сегодня?", "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
                            (MainPageFAQSection.faq_click_question_id_4, MainPageFAQSection.get_text_question_for_faq_4, MainPageFAQSection.get_text_answer_for_faq_4,
                              "Можно ли продлить заказ или вернуть самокат раньше?", "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
                            (MainPageFAQSection.faq_click_question_id_5, MainPageFAQSection.get_text_question_for_faq_5, MainPageFAQSection.get_text_answer_for_faq_5,
                              "Вы привозите зарядку вместе с самокатом?", "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
                            (MainPageFAQSection.faq_click_question_id_6, MainPageFAQSection.get_text_question_for_faq_6, MainPageFAQSection.get_text_answer_for_faq_6,
                              "Можно ли отменить заказ?", "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
                            (MainPageFAQSection.faq_click_question_id_7, MainPageFAQSection.get_text_question_for_faq_7, MainPageFAQSection.get_text_answer_for_faq_7,
                              "Я жизу за МКАДом, привезёте?", "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
                            ])
    def test_click_on_all_section_questions_answers(self, driver, test_faq_id, actual_question, actual_answer, expected_question, expected_answer):
        test_page = MainPageFAQSection(driver)
        test_page.base_to_accept_cookies()
        test_page.faq_scroll_to_questions_answers()
        # f'MainPageFAQSection.{test_faq_id}(test_page)'
        test_faq_id(test_page)
        text_actual_question = actual_question(test_page)
        text_actual_answer = actual_answer(test_page)

        assert text_actual_question == expected_question
        assert text_actual_answer == expected_answer



