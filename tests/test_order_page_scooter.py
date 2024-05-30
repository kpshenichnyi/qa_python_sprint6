import pytest
import allure
from pages.base_page import BasePage
from pages.order_page_scooter import OrderPageScooter
from pages.main_page_scooter import MainPageScooter
from locators.locators_main_page import LocatorsMainPageScooter
from locators.locators_order_page import LocatorsOrderPage
from data import TestDataSetOrder
from conftest import driver


class TestOrderPageScooter:

    @allure.title('Проверка позитивного сценария оформления заказа c двумя точками входа')
    @allure.description('Тест для кнопок Заказать в заголовке и середине главной страницы')
    @pytest.mark.parametrize('entry_point, order_dataset', [(LocatorsMainPageScooter.LOCATOR_BUTTON_ORDER_PAGE, TestDataSetOrder.order_dataset_const_1),
                                                        (LocatorsMainPageScooter.LOCATOR_BUTTON_ORDER_TOP, TestDataSetOrder.order_dataset_const_2)
                                                            ])
    def test_order_all_fields_success(self, driver, entry_point, order_dataset):
        test_order_page = OrderPageScooter(driver)
        test_order_page.base_to_accept_cookies()
        test_order_page.base_scroll_to_element(entry_point)
        test_order_page.base_click_to_element(entry_point)
        test_order_page.set_data_about_user(order_dataset)
        test_order_page.set_data_about_rental_period(order_dataset)
        test_order_page.set_confirm_order()
        test_result_text = test_order_page.check_order_has_been_placed()
        test_status_view = test_order_page.check_button_status_view_availability()
        assert "Заказ оформлен" in test_result_text and test_status_view == True
