from bs4 import BeautifulSoup
import requests
import re


class Scrapping:

    generos_series = {"10673", "6721", "69616", "78103", "52117", "1372", "52780", "10375",
                      "11559", "60951", "72404", "10105", "11714", "812683888", "27346", "67708",
                      "4366", "81346420", "75392", "2070390", "26156", "10634", "83059", "89811"}

    links = []

    @staticmethod
    def netflix(id_categoria): return "https://www.netflix.com/browse/genre/" + id_categoria

    @staticmethod
    def requests_get(url): return requests.get(url)

    @classmethod
    def start_scrapping(cls, url):
        netflix = cls.requests_get(url)
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
        return soup.find('h1').text

    @staticmethod
    def get_year(url):
        netflix = requests.get(url)
        soup = BeautifulSoup(netflix.text, 'html.parser')
        return soup.find_all('span')[2].string

    @staticmethod
    def get_category(url):
        netflix = requests.get(url)
        soup = BeautifulSoup(netflix.text, 'html.parser')
        return soup.find('h1').string

    @staticmethod
    def get_sinopsis(url):
        netflix = requests.get(url)
        soup = BeautifulSoup(netflix.text, 'html.parser')
        sinopsis = soup.find('div', class_='title-info-synopsis')
        return sinopsis.text
