from Pelicula import *
from Webdriver import *


def scrappear_peliculas():
    Pelicula.scrap_movies()
    Pelicula.csv_peliculas()


if __name__ == "__main__":
    Webdriver.web_driver()
    scrappear_peliculas()
