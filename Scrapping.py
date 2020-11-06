from bs4 import BeautifulSoup
import requests


class Scrapping:

    id_categorias = {"1365", "3063", "3276033", "2595", "31574", "6548", "6133", "2298875", "4370", "2243108",
                     "5763", "9744", "26835", "81268388", "7077", "783", "78367", "3979", "52852", "81346420",
                     "7723", "75436", "8883", "8711", "8933", "10673", "6721", "69616", "78103", "52117", "1372",
                     "52780", "10375", "11559", "60951", "72404", "10105", "11714", "812683888", "27346", "67708",
                     "4366", "81346420", "75392", "2070390", "26156", "10634", "83059", "89811"}

    @staticmethod
    def netflix(id_categoria): return "https://www.netflix.com/browse/genre/" + id_categoria

    @staticmethod
    def requests_get(url): return requests.get(url)

    @classmethod
    def get_script(cls):
        lista_categorias = list(cls.id_categorias)
        netflix = cls.requests_get(cls.netflix(lista_categorias[0]))
        src = netflix.content
        soup = BeautifulSoup(src, 'lxml')  # crea el objeto y parsea el codigo
        scripts = soup.find_all("script")  # busca todos los scripts
        cls.escribir_archivo(scripts)

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
