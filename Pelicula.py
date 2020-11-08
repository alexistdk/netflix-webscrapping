from Scrapping import *


class Pelicula(Scrapping):

    generos_peliculas = []

    @classmethod
    def scrapp_movies(cls):
        for genero in cls.generos_peliculas:
            cls.start_scrapping(genero)

    @staticmethod
    def escribe_header():
        with open("peliculas.csv", mode='a') as f:
            campos = ['Nombre', 'Edad mínima', 'Estreno', 'ID', 'Categoria', 'Sinopsis', 'URL']
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            f.close()

    @classmethod
    def csv_peliculas(cls, url):
        with open("peliculas.csv", mode='a') as f:
            campos = ['Nombre', 'Edad mínima', 'Estreno', 'ID', 'Categoria', 'Sinopsis', 'URL']
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writerow({
                'Nombre': cls.get_title(url),
                'Edad mínima': cls.get_maturity(url),
                'Estreno': cls.get_year(url),
                'ID': cls.get_id(url),
                'Categoria': cls.get_genre(url),
                'Sinopsis': cls.get_sinopsis(url),
                'URL': url
            })
