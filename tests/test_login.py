from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

from const import Const


class TestLogInToTheSite:

    def test_check_button_log_in_main_page(self, driver):
        #Логинимся по кнопке «Войти в аккаунт» на главной
        driver.get(Const.MAIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_log_in_account))
        driver.find_element(*TestLocators.button_log_in_account).click()
        assert Const.LOGIN_PAGE == driver.current_url
        #Авторизация
        driver.find_element(*TestLocators.input_email).send_keys(Const.EMAIL)
        driver.find_element(*TestLocators.input_password).send_keys(Const.PASSWORD)
        driver.find_element(*TestLocators.button_log_in).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.button_set_an_order)))
        assert driver.find_element(*TestLocators.button_set_an_order)

    def test_check_personal_account_in_main_page(self, driver):
        #Логинимся через кнопку «Личный кабинет»
        driver.get(Const.MAIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.button_personal_account)))
        driver.find_element(*TestLocators.button_personal_account).click()
        assert driver.find_element(*TestLocators.header_log_in_page)
        assert Const.LOGIN_PAGE == driver.current_url

    def test_check_log_in_in_registration_page(self, driver):
        #Логинимся через кнопку в форме регистрации
        driver.get(Const.REGISTRATION_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.link_log_in)))
        driver.find_element(*TestLocators.link_log_in).click()
        assert driver.find_element(*TestLocators.header_log_in_page)
        assert Const.LOGIN_PAGE == driver.current_url

    def test_check_log_in_in_recovery_page(self, driver):
        #Логинимся через кнопку в форме восстановления пароля
        driver.get(Const.RECOVERY_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.link_log_in)))
        driver.find_element(*TestLocators.link_log_in).click()
        assert driver.find_element(*TestLocators.header_log_in_page)
        assert Const.LOGIN_PAGE == driver.current_url