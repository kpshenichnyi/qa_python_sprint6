import random
import time

import allure
from random import choice
from conftest import driver
from pages.base_page import BasePage
from data import TestUrls
from locators.locators_main_page import LocatorsMainPageScooter
from locators.locators_order_page import LocatorsOrderPage


class OrderPageScooter(BasePage):

    @allure.step('Открыть страницу заказа Самоката')
    def open_order_page_scooter(self):
        self.base_open_url(TestUrls.SCOOTER_ORDER_PAGE)

    @allure.step('Нажать на логотип Самоката')
    def click_on_logo_scooter_in_header(self):
        self.base_click_to_element(LocatorsMainPageScooter.LOCATOR_LOGO_SAMOKAT)

    @allure.step('Указать имя пользователя')
    def set_name_user_in_order(self, name):
        self.base_wait_visibility_of_element_located(LocatorsOrderPage.LOCATOR_FIELD_NAME)
        self.base_click_to_element(LocatorsOrderPage.LOCATOR_FIELD_NAME)
        return self.base_input_text_to_field(LocatorsOrderPage.LOCATOR_FIELD_NAME, name)

    @allure.step('Указать фамилию пользователя')
    def set_last_name_user_in_order(self, last_name):
        self.base_click_to_element(LocatorsOrderPage.LOCATOR_FIELD_LAST_NAME)
        return self.base_input_text_to_field(LocatorsOrderPage.LOCATOR_FIELD_LAST_NAME, last_name)

    @allure.step('Указать адрес доставки самоката')
    def set_address_in_order(self, address):
        self.base_click_to_element(LocatorsOrderPage.LOCATOR_FIELD_ADDRESS)
        return self.base_input_text_to_field(LocatorsOrderPage.LOCATOR_FIELD_ADDRESS, address)

    @allure.step('Выбрать станцию метро')
    def set_metro_station_in_order(self, metro):
        self.base_click_to_element(LocatorsOrderPage.LOCATOR_FIELD_METRO)
        self.base_input_text_to_field(LocatorsOrderPage.LOCATOR_FIELD_METRO, metro)
        return self.base_click_to_element(LocatorsOrderPage.LOCATOR_FIELD_METRO_ACK_SELECT_STATION)

    @allure.step('Указать контактный номер телефона')
    def set_phone_number_in_order(self, phone):
        self.base_click_to_element(LocatorsOrderPage.LOCATOR_FIELD_PHONE)
        return self.base_input_text_to_field(LocatorsOrderPage.LOCATOR_FIELD_PHONE, phone)

    @allure.step('Перейти к форме с информацией об аренде самоката')
    def set_continue_order(self):
        return self.base_click_to_element(LocatorsOrderPage.LOCATOR_BUTTON_NEXT)

    @allure.step('Установить дату доставки самоката')
    def set_date_start_rent(self):
        date_choise = random.choice([LocatorsOrderPage.LOCATOR_FIELD_DATE_START_DAY_1, LocatorsOrderPage.LOCATOR_FIELD_DATE_START_DAY_2])
        self.base_click_to_element(LocatorsOrderPage.LOCATOR_FIELD_DATE_START)
        self.base_click_to_element(date_choise)

    @allure.step('Установить срок аренды самоката')
    def set_rent_time_in_order(self):
        time_choise = random.choice(
            [LocatorsOrderPage.LOCATOR_TIME_1, LocatorsOrderPage.LOCATOR_TIME_2])
        self.base_click_to_element(LocatorsOrderPage.LOCATOR_FIELD_RENT_TIME)
        self.base_click_to_element(time_choise)

    @allure.step('Установить цвет самоката')
    def set_color_scooter_in_order(self):
        color_choise = random.choice(
            [LocatorsOrderPage.LOCATOR_CHOICE_COLOR_BLACK, LocatorsOrderPage.LOCATOR_CHOICE_COLOR_GREY])
        self.base_click_to_element(color_choise)

    @allure.step('Заполнить комментарий к заказу самоката')
    def set_comment_in_order(self, comment = " "):
        self.base_click_to_element(LocatorsOrderPage.LOCATOR_FIELD_COMMENTS)
        return self.base_input_text_to_field(LocatorsOrderPage.LOCATOR_FIELD_COMMENTS, comment)

    @allure.step('Завершить заказ самоката')
    def set_complete_order(self):
        self.base_click_to_element(LocatorsOrderPage.LOCATOR_BUTTON_ORDER_END)

    # @allure.step('Подтвердить заказ самоката')
    # def set_complete_order(self):
    #     self.base_click_to_element(LocatorsOrderPage.LOCATOR_BUTTON_ORDER_YES)

    @allure.step('Заполнить данные о пользователе самоката')
    def set_data_about_user(self, order_dataset):

        self.set_name_user_in_order(order_dataset[0])
        self.set_last_name_user_in_order(order_dataset[1])
        self.set_address_in_order(order_dataset[2])
        self.set_metro_station_in_order(order_dataset[3])
        self.set_phone_number_in_order(order_dataset[4])
        self.set_continue_order()

    @allure.step('Заполнить данные о сроке аренды самоката')
    def set_data_about_rental_period(self, order_dataset):

        self.set_date_start_rent()
        self.set_rent_time_in_order()
        self.set_color_scooter_in_order()
        self.set_comment_in_order(order_dataset[5])
        self.set_complete_order()

    @allure.step('Подтвердить заказ самоката')
    def set_confirm_order(self):
        self.base_click_to_element(LocatorsOrderPage.LOCATOR_BUTTON_ORDER_YES)


