from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from const import Const

class TestTransfetAccountPage:

    # Проверка перехода по клику на «Личный кабинет»
    def test_check_transfer_to_account_page(self, driver):
        driver.get(Const.MAIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.button_log_in_account)))
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.button_log_in)))
        assert driver.find_element(*TestLocators.header_log_in_page)

    # Проверка перехода из личного кабинета в конструктор по клику на «Конструктор»
    def test_check_transfer_to_constructor_from_account_page(self, driver):
        driver.get(Const.LOGIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.header_log_in_page)))
        driver.find_element(*TestLocators.input_email).send_keys(Const.EMAIL)
        driver.find_element(*TestLocators.input_password).send_keys(Const.PASSWORD)
        driver.find_element(*TestLocators.button_log_in).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.button_personal_account)))
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.menu_item_profile)))
        driver.find_element(*TestLocators.main_header_constructor).click()
        assert driver.find_element(*TestLocators.header_constructor)
        assert Const.MAIN_PAGE == driver.current_url

    # Проверка перехода из личного кабинета в конструктор по клику на лого сайта
    def test_check_tap_logo_transfer_to_constructor_from_account_page(self, driver):
        driver.get(Const.LOGIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.header_log_in_page)))
        driver.find_element(*TestLocators.input_email).send_keys(Const.EMAIL)
        driver.find_element(*TestLocators.input_password).send_keys(Const.PASSWORD)
        driver.find_element(*TestLocators.button_log_in).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.button_personal_account)))
        driver.find_element(*TestLocators.logo_main_page).click()
        assert driver.find_element(*TestLocators.header_constructor)
        assert Const.MAIN_PAGE == driver.current_url