from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Usuario:

    @staticmethod
    def inicia_sesion():
        firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())  # abre chrome
        firefox.get('https://www.netflix.com/ar/login')
        firefox.find_element_by_class_name('nfEmailPhoneControls').click()
        firefox.find_element_by_name('userLoginId').send_keys('catalinamurillo1154@outlook.com')
        firefox.find_element_by_name('password').send_keys('darwin1154')
        firefox.find_element_by_class_name('btn-small').click()
        firefox.implicitly_wait(10)
        firefox.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a/div/div'
        ).click()
