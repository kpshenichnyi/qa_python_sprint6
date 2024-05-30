
Установка необходимых модулей командой:
pip3 install -r requirements.txt 

Запустить тесты из терминала можно командой:
pytest -v --alluredir=allure_results 

Генерация отчета Allure командой:
allure serve allure_results 

Тестирование проводится на вебдрайвере Firefox

- ***locators/*** - каталог с локаторами для поиска элементов DOM 
- *locators/locators_main_page.py* - локаторы главной страницы
- *locators/locators_order_page.py* - локаторы для для страниц с заказом самоката
- *locators/order_page_locators.py* - локаторы для страниц заказа

- ***tests/*** - каталог с файлами тестов
- *tests/test_main_page_scooter.py* - тесты главной  страницы: переходы от логотипов
- *tests/test_scooter_faq.py - тесты* секции Вопросы и ответов "Вопросы о главном"
- *tests/test_order_page_scooter.py* - тесты с позитивным сценарием заказа самоката по двум точкам входа

- ***pages/*** - каталог с файлами страниц Page Object 
- *pages/base_page.py* - файл POM общих функций: поиск\ожидания\клик элементов
- *pages/main_page_scooter.py* - файл POM главной страницы Самокатов
- *pages/order_page_scooter.py* - файл POM страницы заказа

- ***allure_results/*** - каталог с отчетами по тестам

- *requirements.txt* - файл с внешними зависимостями 

- ***README.md*** - файл с описанием проекта
