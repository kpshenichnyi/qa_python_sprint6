import allure

from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
from locators.locators_main_page import LocatorsMainPageScooter, LocatorsFAQ

from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть требуемую страницу')
    def base_open_url(self, URL):
        self.driver.get(URL)

    @allure.step('Получить URL текущей открытой страницы')
    def base_get_current_url(self):
        return self.driver.current_url

    @allure.step('Найти необходимый элемент')
    def base_find_element(self, LOCATOR):
        return self.driver.find_element(*LOCATOR)

    @allure.step('Дождаться загрузки элемента')
    def base_wait_visibility_of_element_located(self, LOCATOR, timeout = 5):
        return WDW(self.driver, timeout).until(EC.visibility_of_element_located(LOCATOR))

    @allure.step("Дождаться доступности элемента для клика")
    def base_wait_until_element_is_clickable(self, LOCATOR, timeout = 5):
        WDW(self.driver, timeout).until(EC.element_to_be_clickable(LOCATOR))

    @allure.step('Кликнуть по выбранному элементу')
    def base_click_to_element(self, LOCATOR):
        self.base_wait_until_element_is_clickable(LOCATOR)
        self.driver.find_element(*LOCATOR).click()

    @allure.step('Прокрутить страницу до выбранного элемента')
    def base_scroll_to_element(self, LOCATOR):
        scroll_to_element = self.driver.find_element(*LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_to_element)

    @allure.step('Получить текст элемента')
    def base_get_text_of_element(self, LOCATOR):
        WDW(self.driver, 10).until(EC.visibility_of_element_located(LOCATOR))
        return self.driver.find_element(*LOCATOR).text

    @allure.step('Ввести значение в поле ввода')
    def base_input_text_to_field(self, LOCATOR, text):
        self.driver.find_element(*LOCATOR).send_keys(text)

    @allure.step("Принять cookies")
    def base_to_accept_cookies(self):
        WDW(self.driver, 5).until(EC.visibility_of_element_located(LocatorsMainPageScooter.LOCATOR_BUTTON_ACCEPT_COOKIES)).click()

    @allure.step("Переключиться на новую вкладку")
    def base_switch_to_new_tab(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Дождаться открытия заданной страницы")
    def base_wait_for_open_page(self, page_url):
        return WDW(self.driver, 10).until(EC.url_to_be(page_url))

