from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from Pelicula import *


class Webdriver:

    @staticmethod
    def iniciar_sesion(driver):
        driver.find_element_by_class_name('nfEmailPhoneControls').click()
        driver.find_element_by_name('userLoginId').send_keys('catalinamurillo1154@outlook.com')
        driver.find_element_by_name('password').send_keys('darwin1154')
        driver.find_element_by_class_name('btn-small').click()

    @classmethod
    def web_driver(cls):
        firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())  # abre Firefox
        firefox.get('https://www.netflix.com/ar/login')
        cls.iniciar_sesion(firefox)
        cls.elige_usuario(firefox)
        cls.clickea_generos(firefox)
        cls.scrappea_generos(firefox)

    @classmethod
    def elige_usuario(cls, driver):
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a/div/div'  # usuario de Netflix
        ).click()

    @classmethod
    def clickea_generos(cls, driver):
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div/ul/li[4]/a'  # Sección películas
        ).click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div'
        ).click()  # click en géneros

    @classmethod
    def scrappea_generos(cls, driver):
        generos = driver.find_elements_by_class_name('sub-menu-link')  # .
        # esto se podría haber hecho con un map, pero no encontré cómo hacerlo funcionar
        for i in range(len(generos)):
            Pelicula.generos_peliculas.append(generos[i].get_attribute('href'))
        driver.close()
        print(Pelicula.generos_peliculas)
