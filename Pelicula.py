from Scrapping import *
import csv


class Pelicula(Scrapping):

    generos_peliculas = []

    genero = ""

    @classmethod
    def scrap_movies(cls):
        for genero in cls.generos_peliculas:
            cls.start_scrapping(genero)
            cls.set_genero(genero)

    @classmethod
    def set_genero(cls, url):
        cls.genero = cls.get_genre(url)

    @staticmethod
    def escribe_header():
        with open("peliculas.csv", mode='a') as f:
            campos = ['Nombre', 'Edad mínima', 'Estreno', 'ID', 'Categoria', 'Sinopsis', 'Link']
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            f.close()

    @classmethod
    def csv_peliculas(cls):
        cls.escribe_header()
        for generos in cls.links:
            for pelicula in generos:
                with open("peliculas.csv", mode='a') as f:
                    campos = ['Nombre', 'Edad mínima', 'Estreno', 'ID', 'Categoria', 'Sinopsis', 'Link']
                    writer = csv.DictWriter(f, fieldnames=campos)
                    writer.writerow({
                        'Nombre': cls.get_title(pelicula),
                        'Edad mínima': cls.get_maturiy(pelicula),
                        'Estreno': cls.get_year(pelicula),
                        'ID': cls.get_id(pelicula),
                        'Categoria': cls.genero,
                        'Sinopsis': cls.get_sinopsis(pelicula),
                        'Link': "https://netflix.com/title/" + cls.get_id(pelicula)
                    })
