from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_locators.locators import *
from data.urls import Urls


class TestStellarBurgersProfileForm:

    def test_click_profile_button_open_profile_form(self, login):
        """ Открыть личный кабинет """
        driver = login

        driver.find_element(*MainPage.mn_profile_button).click()

        assert Urls.url_profile == driver.current_url and WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LKProfile.lk_history_shop_button)
        )

    def test_click_constructor_button_show_constructor_form(self, login):
        """ Переход из личного кабинета в конструктор при нажатии кнопки 'Конструктор' """
        driver = login

        driver.find_element(*MainPage.mn_profile_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LKProfile.lk_info_message))
        
        driver.find_element(*MainPage.mn_constructor_button).click()

        # Ищем конкретный элемент по локатору прямо в assert
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPage.mn_constructor_title)
        )

    def test_click_logo_button_show_constructor_form(self, login):
        """ Переход из личного кабинета в конструктор при нажатии на лого """
        driver = login

        driver.find_element(*MainPage.mn_profile_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LKProfile.lk_info_message))
        
        driver.find_element(*MainPage.mn_logo).click()

        # Ищем конкретный элемент по локатору прямо в assert
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPage.mn_constructor_title)
        )

    def test_click_logout_button_in_lk_open_login_form(self, login):
        """ Выйти из аккаунта """
        driver = login

        driver.find_element(*MainPage.mn_profile_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LKProfile.lk_info_message))

        driver.find_element(*LKProfile.lk_logout_button).click()

        assert driver.current_url == Urls.url_login and WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthLogin.al_login_button_any_forms)
        )
