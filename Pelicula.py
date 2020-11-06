from Scrapping import *
import csv


class Pelicula(Scrapping):

    generos_peliculas = {"1365", "3063", "3276033", "2595", "31574", "6548", "6133", "2298875",
                         "4370", "2243108", "5763", "9744", "26835", "81268388", "7077", "783",
                         "78367", "3979", "52852", "81346420", "7723", "75436", "8883", "8711", "8933"}

    peliculas = {}

    @classmethod
    def scrap_movies(cls):
        peliculas = map(cls.start_scrapping, cls.generos_peliculas)
        return list(peliculas)

    @classmethod
    def listar_peliculas(cls):
        lista_aux = []
        for peliculas in cls.scrap_movies():
            for pelicula in peliculas:
                lista_aux.append(pelicula)
        cls.peliculas.update(lista_aux)

    @classmethod
    def csv_peliculas(cls, url):
        with open("peliculas.csv", mode='a') as f:
            campos = ['Nombre', 'Estreno', 'ID', 'Link']
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writerow({
                'Nombre': cls.get_title(url),
                'Estreno': cls.get_year(url),
                'ID': cls.get_id(url),
                'Link': url,
            })
