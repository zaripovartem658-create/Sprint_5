import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_locators.locators import *
from data.urls import Urls
from data.data import ValidData, InvalidData


class TestStellarBurgersRegistration:

    def test_registration_correct_email_and_pwd_successful_registration(self, driver):
        """При успешной регистрации перенос на страницу входа"""
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_name_field).send_keys(ValidData.user_name)
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(ValidData.login)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(ValidData.password)

        driver.find_element(*AuthRegistre.ar_register_button).click()

        assert driver.current_url == Urls.url_login and WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(AuthLogin.al_element_with_login_text)
        )

    def test_registration_empty_name_nothing_happens(self, driver):
        """ При пустом поле Имя ничего не происходит: ошибки и перехода на страницу входа нет """
        driver.get(Urls.url_register)

        # Используем данные из модуля данных
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(ValidData.login)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(ValidData.password)

        driver.find_element(*AuthRegistre.ar_register_button).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(AuthRegistre.ar_register_button))
        time.sleep(2)
        
        assert driver.current_url == Urls.url_register and len(
            driver.find_elements(*AuthRegistre.ar_error_message)
        ) == 0

    @pytest.mark.parametrize('email_list', InvalidData.invalid_emails)
    def test_registration_incorrect_email_show_error(self, driver, email_list):
        """ При некорректном email появляется ошибка, что пользователь уже существует """
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_name_field).send_keys(ValidData.user_name)
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(email_list)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(ValidData.password)

        driver.find_element(*AuthRegistre.ar_register_button).click()
        
        # Проверяем текст ошибки прямо в assert
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthRegistre.ar_error_message_2)
        ).text == 'Такой пользователь уже существует'

    @pytest.mark.parametrize('password_list', InvalidData.short_passwords)
    def test_login_incorrect_password_less_six_symbols_show_error(self, driver, password_list):
        """При вводе некорректного пароля, отображает ошибку 'Некорректный пароль'"""
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_name_field).send_keys(ValidData.user_name)
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(ValidData.login)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(password_list)

        driver.find_element(*AuthRegistre.ar_register_button).click()
        
        # Проверяем текст ошибки прямо в assert
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthRegistre.ar_error_message)
        ).text == 'Некорректный пароль'
