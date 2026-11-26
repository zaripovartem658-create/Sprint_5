import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.urls import Urls
from data.data import ValidData
from web_locators.locators import *


@pytest.fixture
def driver():
    """Фикстура для запуска браузера"""
    driver = webdriver.Chrome()  # Укажите ваш браузер
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    """Фикстура для авторизации пользователя"""
    driver.get(Urls.url_login)
    
    driver.find_element(*AuthLogin.al_email_field).send_keys(ValidData.login)
    driver.find_element(*AuthLogin.al_password_field).send_keys(ValidData.password)
    driver.find_element(*AuthLogin.al_login_button_any_forms).click()
    
    # Ждем, пока прогрузится главная страница (появится кнопка "Оформить заказ")
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(MainPage.mn_order_button)
    )
    return driver