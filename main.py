from Pelicula import *
from Usuario import *


def scrappear_peliculas():
    Pelicula.scrap_movies()
    Pelicula.csv_peliculas()


if __name__ == "__main__":
    Usuario.inicia_sesion()
