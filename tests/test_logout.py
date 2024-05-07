from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

from const import Const


class TestLogOutInAccountPage:

    # Проверка выхода из аккаунта по кнопке «Выйти» в личном кабинете
    def test_check_button_log_out_main_page(self, driver):
        driver.get(Const.LOGIN_PAGE)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.header_log_in_page)))

        driver.find_element(*TestLocators.input_email).send_keys(Const.EMAIL)
        driver.find_element(*TestLocators.input_password).send_keys(Const.PASSWORD)
        driver.find_element(*TestLocators.button_log_in).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.button_set_an_order)))
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.menu_item_profile)))
        driver.find_element(*TestLocators.menu_item_log_in).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.input_email)))
        assert driver.find_element(*TestLocators.header_log_in_page)