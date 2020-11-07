from Scrapping import *
import csv


class Serie(Scrapping):

    generos_series = []

    @classmethod
    def scrapp_series(cls):
        cls.links = []
        for genero in cls.generos_series:
            cls.start_scrapping(genero)
            cls.set_genero(genero)

    @staticmethod
    def get_cantidad_temporadas(url):
        netflix = requests.get(url)
        src = netflix.content
        soup = BeautifulSoup(src, 'lxml')
        temporadas = soup.find_all('div', class_="season")
        return len(temporadas)

    @staticmethod
    def escribe_header():
        with open("peliculas.csv", mode='a') as f:
            campos = ['Nombre',
                      'Edad mínima',
                      'Estreno',
                      'ID',
                      'Categoria',
                      'Sinopsis',
                      'Temporadas',
                      # 'Cantidad de Capitulos'
                      # 'Capitulos',
                      'Link'
                      ]
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            f.close()

    @classmethod
    def csv_series(cls):
        cls.escribe_header()
        for generos in cls.links:
            for serie in generos:
                with open("series.csv", mode='a') as f:
                    campos = ['Nombre', 'Edad mínima', 'Estreno', 'ID', 'Categoria', 'Sinopsis', 'Temporadas', 'Link']
                    writer = csv.DictWriter(f, fieldnames=campos)
                    writer.writerow({
                        'Nombre': cls.get_title(serie),
                        'Edad mínima': cls.get_maturiy(serie),
                        'Estreno': cls.get_year(serie),
                        'ID': cls.get_id(serie),
                        'Categoria': cls.get_genre(serie),
                        'Sinopsis': cls.get_sinopsis(serie),
                        'Temporadas': cls.get_cantidad_temporadas(serie)
                    })

    @classmethod
    def get_cantidad_episodios(cls, url):
        netflix = requests.get(url)
        src = netflix.content
        soup = BeautifulSoup(src, 'lxml')
        cantidad = soup.find_all('div', class_="episode")
        return len(cantidad)

    @classmethod
    def get_nombre_episodio(cls, url):
        netflix = requests.get(url)
        src = netflix.content
        soup = BeautifulSoup(src, 'lxml')
        nombre = soup.find_all('h3', class_="episode-title")
        return cls.borrar_numero_del_episodio(nombre[0].string)

    @classmethod
    def borrar_numero_del_episodio(cls, string):
        nombre = string.split(' ')
        nombre.pop(0)
        return ' '.join(nombre)

