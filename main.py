from Pelicula import *
from Webdriver import *
from Serie import *
import pandas as pd
from requests import get


def netflix():
    Scrapping.netflix_header()
    Scrapping.netflix_contenido()


def scrappear_contenido():
    Pelicula.scrapp_movies()
    Serie.scrapp_series()


def escribir_csvs():
    df = pd.read_csv("netflix-ar.csv")
    Serie.escribe_header()
    Pelicula.escribe_header()
    for i in range(len(df.index)):
        url = df.URL[i]
        netflix = get(url)
        soup = BeautifulSoup(netflix.content, 'lxml')
        if soup.find_all('div', class_="season"):
            Serie.csv_series(url)
        else:
            Pelicula.csv_peliculas(url)


if __name__ == "__main__":
    Webdriver.web_driver()
    netflix()
    scrappear_contenido()
    escribir_csvs()
