from web_locators.locators import *


class TestStellarBurgersConstructorForm:

    def test_constructor_go_to_sauces_scroll_to_sauces(self, login):
        """Переход на вкладку "Соусы" """
        driver = login

        driver.find_element(*MainPage.mn_constructor_button).click()
        
        sauces_tab = driver.find_element(*MainPage.mn_sauces_button)
        sauces_tab.click()

        assert 'tab_tab_type_current' in sauces_tab.get_attribute('class')

    def test_constructor_go_to_filling_scroll_to_filling(self, login):
        """Переход на вкладку "Начинки" """
        driver = login

        driver.find_element(*MainPage.mn_constructor_button).click()
        
        filling_tab = driver.find_element(*MainPage.mn_filling_button)
        filling_tab.click()

        assert 'tab_tab_type_current' in filling_tab.get_attribute('class')

    def test_constructor_go_to_bun_scroll_to_bun(self, login):
        """Переход на вкладку "Булки" """
        driver = login

        driver.find_element(*MainPage.mn_constructor_button).click()
        
        driver.find_element(*MainPage.mn_filling_button).click()
        
        bun_tab = driver.find_element(*MainPage.mn_ban_button)
        bun_tab.click()

        assert 'tab_tab_type_current' in bun_tab.get_attribute('class')
