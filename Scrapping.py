from bs4 import BeautifulSoup
import requests
import re
import csv


class Scrapping:

    links = []

    @classmethod
    def start_scrapping(cls, url):
        netflix = requests.get(url)
        src = netflix.content
        soup = BeautifulSoup(src, 'lxml')  # crea el objeto y parsea el codigo
        scripts = soup.find_all("script")  # busca todos los scripts
        cls.escribir_archivo(scripts)
        cls.obtener_links()

    @classmethod
    def escribir_archivo(cls, scripts):
        script_file = open("script", "w")
        script_file.write(str(scripts))
        script_file.close()
        cls.eliminar_lineas()

    @staticmethod
    def eliminar_lineas():
        with open("script") as old, open("script.txt", "w") as new:
            lines = old.readlines()
            new.writelines(lines[0])

    @classmethod
    def obtener_links(cls):
        with open("script.txt", "r") as f:
            lines = f.readlines()
            links_contenidos = re.findall(r'https://www.netflix.com/ar-en/title/[0-9]{8}', lines[0])
            cls.links.append(links_contenidos)

    @staticmethod
    def get_id(url):
        return re.findall('\d+', url)[0]

    @staticmethod
    def get_title(url):
        netflix = requests.get(url)
        soup = BeautifulSoup(netflix.text, 'html.parser')
        return soup.find('h1').string

    @staticmethod
    def get_year(url):
        netflix = requests.get(url)
        soup = BeautifulSoup(netflix.text, 'html.parser')
        estreno = soup.find('span', class_="item-year").string
        return estreno

    @staticmethod
    def get_genre(url):
        netflix = requests.get(url)
        soup = BeautifulSoup(netflix.text, 'html.parser')
        genero = soup.find('span', class_='item-genres')
        return genero.text.split(',')[0]

    @staticmethod
    def get_sinopsis(url):
        netflix = requests.get(url)
        soup = BeautifulSoup(netflix.text, 'html.parser')
        sinopsis = soup.find('div', class_='title-info-synopsis')
        return sinopsis.string

    @staticmethod
    def get_maturity(url):
        netflix = requests.get(url)
        soup = BeautifulSoup(netflix.text, 'lxml')
        maturity = soup.find('span', class_="maturity-number")
        return maturity.string

    @staticmethod
    def netflix_header():
        with open("netflix-ar.csv", mode='a') as f:
            header = ["Título", "ID", "URL"]
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            f.close()

    @classmethod
    def netflix_contenido(cls):
        cls.netflix_header()
        for genero in cls.links:
            for contenido in genero:
                with open("netflix-ar.csv", mode="a") as f:
                    campos = ["Título", "ID", "URL"]
                    writer = csv.DictWriter(f, fieldnames=campos)
                    writer.writerow({
                        "Título": cls.get_title(contenido),
                        "ID": cls.get_id(contenido),
                        "URL": "https://netflix.com/title/" + cls.get_id(contenido)
                    })
