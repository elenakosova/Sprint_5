from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

from const import Const


class TestChangeSection:

    def test_open_sauce_section(self, driver):
        #Проверка работоспособности перехода к разделу «Соусы» в конструкторе:
        driver.get(Const.MAIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_log_in_account))
        driver.find_element(*TestLocators.sauce_constructor).click()
        assert driver.find_element(*TestLocators.select_tab_constructor).text == 'Соусы'

    def test_open_filling_section(self, driver):
        #Проверка работоспособности перехода к разделу «Начинки» в конструкторе:
        driver.get(Const.MAIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_log_in_account))
        driver.find_element(*TestLocators.filling_constructor).click()
        assert driver.find_element(*TestLocators.select_tab_constructor).text == 'Начинки'

    def test_open_bread_section(self, driver):
        #Проверка работоспособности перехода к разделу «Булки» в конструкторе:
        driver.get(Const.MAIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_log_in_account))
        #Раздел «Булки» при входе на сайт является дефолтным, поэтому выбирается другая категория для проверки перехода к разделу «Булки»
        driver.find_element(*TestLocators.filling_constructor).click()
        assert driver.find_element(*TestLocators.select_tab_constructor).text == 'Начинки'
        driver.find_element(*TestLocators.bread_constructor).click()
        assert driver.find_element(*TestLocators.select_tab_constructor).text == 'Булки'