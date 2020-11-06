from unittest import TestCase
from Scrapping import *


class MyTestCase(TestCase):

    def test_anio_estreno_back_to_the_future(self):
        anio = Scrapping.get_year("https://www.netflix.com/title/60010110")
        self.assertEqual("1985", anio)

    def test_titulo_back_to_the_future(self):
        titulo = Scrapping.get_title("https://www.netflix.com/title/60010110")
        self.assertEqual("Back to the Future", titulo)

    def test_id_back_to_the_future(self):
        id_pelicula = Scrapping.get_id("https://www.netflix.com/title/60010110")
        self.assertEqual("60010110", id_pelicula)

    def test_anio_estreno_dunkirk(self):
        anio = Scrapping.get_year("https://www.netflix.com/title/80170278")
        self.assertEqual("2017", anio)

    def test_titulo_dunkirk(self):
        titulo = Scrapping.get_title("https://www.netflix.com/title/80170278")
        self.assertEqual("Dunkirk", titulo)

    def test_id_dunkirk(self):
        id_pelicula = Scrapping.get_id("https://www.netflix.com/title/80170278")
        self.assertEqual("80170278", id_pelicula)