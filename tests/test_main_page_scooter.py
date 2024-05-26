import pytest
import allure

from pages.main_page_scooter import MainPageScooter
from pages.order_page_scooter import OrderPageScooter
from data import TestUrls
from conftest import driver


class TestMainPage:

    @allure.title('Клик по логотипу Самокат возвращает на главную страницу')
    @allure.description('Проверить что после клика по логотипу "Самокат" в заголовке страницы, осуществлен переход на главную страницу "Самокат"')
    def test_click_logo_scooter_redirect_main(self, driver):
        test_order_page = OrderPageScooter(driver)
        test_main_page = MainPageScooter(driver)
        test_order_page.open_order_page_scooter()
        test_order_page.click_on_logo_scooter_in_header()
        test_main_page.main_wait_for_load_page_title()
        test_expected_url = TestUrls.SCOOTER_MAIN_PAGE
        test_actual_url = test_main_page.base_get_current_url()

        assert test_actual_url == test_expected_url

    @allure.title('Клик по логотипу Яндекса открывает Дзен')
    @allure.description('Проверить что после клика по логотипу "Яндекс" в заголовке страницы, открывается новое окно со страницей Дзен')
    def test_click_logo_yandex_open_dzen(self, driver):
        test_main_page = MainPageScooter(driver)
        test_main_page.base_open_url(TestUrls.SCOOTER_MAIN_PAGE)
        test_main_page.click_on_logo_yandex_in_header()
        test_main_page.base_switch_to_new_tab()
        test_main_page.base_wait_for_open_page(TestUrls.DZEN_MAIN_PAGE)
        test_expected_url = TestUrls.DZEN_MAIN_PAGE
        test_actual_url = test_main_page.base_get_current_url()

        assert test_actual_url == test_expected_url
