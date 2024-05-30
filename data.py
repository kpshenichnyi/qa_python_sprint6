from locators.locators_main_page import LocatorsFAQ

class TestUrls:

    SCOOTER_MAIN_PAGE = 'https://qa-scooter.praktikum-services.ru/'
    SCOOTER_ORDER_PAGE = f'{SCOOTER_MAIN_PAGE}order'
    DZEN_MAIN_PAGE = 'https://dzen.ru/?yredirect=true'


class TestDataSetOrder:
        # Тестовые данные для совершения заказа
    order_dataset_const_1 = ['Клим', 'Чугункин', 'Артельная, 16', 'Лихоборы', '+79001234568', ' без комментариев ']

    order_dataset_const_2 = ['Семен Семеныч', 'Горбунков', 'Профсоюзная 21', 'Речной вокзал', '+79001234568', ' ']