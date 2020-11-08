from Scrapping import *


class Serie(Scrapping):

    generos_series = []

    @classmethod
    def scrapp_series(cls):
        for genero in cls.generos_series:
            cls.start_scrapping(genero)

    @staticmethod
    def get_temporadas(url, indice):
        netflix = requests.get(url)
        src = netflix.content
        soup = BeautifulSoup(src, 'lxml')
        temporadas = soup.find_all('div', class_="season")
        return temporadas[indice]

    @staticmethod
    def get_cant_temporadas(url):
        netflix = requests.get(url)
        src = netflix.content
        soup = BeautifulSoup(src, 'lxml')
        temporadas = soup.find_all('div', class_="season")
        return temporadas

    @staticmethod
    def escribe_header():
        with open("series.csv", mode='a') as f:
            campos = ['Nombre', 'Edad mínima', 'Estreno', 'ID', 'Categoria', 'Sinopsis',
                      'Temporadas', 'Cantidad de Capitulos', 'URL']
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            f.close()

    @classmethod
    def csv_series(cls, url):
        with open("series.csv", mode='a') as f:
            campos = ['Nombre', 'Edad mínima', 'Estreno', 'ID', 'Categoria',
                      'Sinopsis', 'Temporadas', 'Cantidad de Capitulos', 'URL']
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writerow({
                'Nombre': cls.get_title(url),
                'Edad mínima': cls.get_maturity(url),
                'Estreno': cls.get_year(url),
                'ID': cls.get_id(url),
                'Categoria': cls.get_genre(url),
                'Sinopsis serie': cls.get_sinopsis(url),
                'Temporadas': cls.get_cant_temporadas(url),
                'Cantidad de Capitulos': cls.get_cantidad_episodios(url),
                'URL': url
            })

    @classmethod
    def get_cantidad_episodios(cls, url):
        netflix = requests.get(url)
        src = netflix.content
        soup = BeautifulSoup(src, 'lxml')
        cantidad = soup.find_all('div', class_="episode")
        return len(cantidad)

    @classmethod
    def get_nombre_episodio(cls, url, indice):
        netflix = requests.get(url)
        src = netflix.content
        soup = BeautifulSoup(src, 'lxml')
        nombre = soup.find_all('h3', class_="episode-title")
        return cls.borrar_numero_del_episodio(nombre[indice].string)

    @classmethod
    def borrar_numero_del_episodio(cls, string):
        nombre = string.split(' ')
        nombre.pop(0)
        return ' '.join(nombre)

    @classmethod
    def get_sinopsis_episodio(cls, url, indice):
        netflix = requests.get(url)
        soup = BeautifulSoup(netflix.content, 'lxml')
        sinopsis = soup.find_all('p', class_="epsiode-synopsis")
        print(sinopsis[indice].string)

    @classmethod
    def get_sinopsis_temporada(cls, url, indice):
        netflix = requests.get(url)
        soup = BeautifulSoup(netflix.content, 'lxml')
        sinopsis = soup.find_all('p', class_="season-synopsis")
        return sinopsis[indice].string

    @classmethod
    def get_info_temporada(cls, url):
        serie = requests.get(url)
        soup = BeautifulSoup(serie.content, 'lxml')
        for temporada in soup.find_all('div', class_="season"):
            sinopsis_temporada = temporada.div.p.text
            print("\n", sinopsis_temporada)
            for capitulo in temporada.find_all('div', class_="episode"):
                print(capitulo.p.text)
