from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from Pelicula import *
from Serie import *


class Webdriver:

    @classmethod
    def web_driver(cls):
        firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())  # abre Firefox
        firefox.get('https://www.netflix.com/ar/login')
        cls.iniciar_sesion(firefox)
        cls.elige_usuario(firefox)
        cls.clickea_genero(firefox, 'Películas')
        cls.scrappea_generos_peliculas(firefox)
        cls.clickea_genero(firefox, 'Series')
        cls.scrappea_generos_series(firefox)
        firefox.close()

    @staticmethod
    def iniciar_sesion(driver):
        driver.find_element_by_class_name('nfEmailPhoneControls').click()
        driver.find_element_by_name('userLoginId').send_keys()
        driver.find_element_by_name('password').send_keys()
        driver.find_element_by_class_name('btn-small').click()

    @classmethod
    def elige_usuario(cls, driver):
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a/div/div'  # usuario de Netflix
        ).click()

    @classmethod
    def clickea_genero(cls, driver, genero):
        driver.find_element_by_link_text(genero).click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div'
        ).click()  # click en géneros

    @classmethod
    def scrappea_generos_peliculas(cls, driver):
        generos = driver.find_elements_by_class_name('sub-menu-link')  # .
        # esto se podría haber hecho con un map, pero no pude hacerlo funcionar
        for i in range(len(generos)):
            Pelicula.generos_peliculas.append(generos[i].get_attribute('href'))
        driver.back()

    @classmethod
    def scrappea_generos_series(cls, driver):
        generos = driver.find_elements_by_class_name('sub-menu-link')
        for i in range(len(generos)):
            Serie.generos_series.append(generos[i].get_attribute('href'))
