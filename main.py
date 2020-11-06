from Pelicula import *


def scrappear_peliculas():
    Pelicula.scrap_movies()
    Pelicula.csv_peliculas()


if __name__ == "__main__":
    scrappear_peliculas()
