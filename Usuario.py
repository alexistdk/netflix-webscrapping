from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Usuario:

    @staticmethod
    def firefox():
        firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())  # abre chrome
        return firefox

    @classmethod
    def inicia_sesion(cls):
        firefox = cls.firefox()
        firefox.get('https://www.netflix.com/ar/login')
        firefox.find_element_by_class_name('nfEmailPhoneControls').click()
        firefox.find_element_by_name('userLoginId').send_keys('catalinamurillo1154@outlook.com')
        firefox.find_element_by_name('password').send_keys('darwin1154')
        firefox.find_element_by_class_name('btn-small').click()
        firefox.implicitly_wait(10)
        firefox.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a/div/div'  # usuario de Netflix
        ).click()
        firefox.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div/ul/li[4]/a'  # Sección películas
        ).click()
        firefox.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div'
        ).click()  # click en géneros
        firefox.find_element_by_link_text('Acción').click()  # click en acción

    # TODO
    # arreglar la función de arriba para separarla en varias funciones
    # averiguar como separar Selenium en varias funciones
    # hacer click en todas categorias y almacenar el id de cada página en las listas
