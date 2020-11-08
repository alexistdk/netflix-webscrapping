from Pelicula import *
from Webdriver import *
from Serie import *


def scrappear_peliculas():
    Pelicula.scrapp_movies()
    Pelicula.csv_peliculas()


def scrappear_series():
    Serie.scrapp_series()
    Serie.csv_series()


if __name__ == "__main__":
    Webdriver.web_driver()
    # scrappear_peliculas()
    # scrappear_series()
