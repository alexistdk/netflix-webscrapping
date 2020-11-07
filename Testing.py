from unittest import TestCase
from Pelicula import *
from Serie import *


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

    def test_sinopsis_back_to_the_future(self):
        sinopsis_scrappeada = Scrapping.get_sinopsis("https://www.netflix.com/title/60010110")
        sinopsis = "After he accidentally drives a DeLorean time machine from 1985 to 1955, " \
                   "Marty McFly races the clock to ensure his future parents fall in love."
        self.assertEqual(sinopsis, sinopsis_scrappeada)

    def test_maturity_back_to_the_future(self):
        self.assertEqual("13+ ", Scrapping.get_maturity("https://www.netflix.com/title/60010110"))

    def test_madurity_documental_1(self):
        self.assertEqual("13+ ", Scrapping.get_maturity("https://www.netflix.com/title/81254224"))

    def test_madurity_documental_2(self):
        self.assertEqual("16+ ", Scrapping.get_maturity("https://www.netflix.com/title/80182553"))

    def test_temporadas_community(self):
        self.assertEqual(6, Serie.get_cantidad_temporadas("https://www.netflix.com/title/70155589"))

    def test_temporadas_house_of_cards(self):
        self.assertEqual(6, Serie.get_cantidad_temporadas("https://www.netflix.com/title/70178217"))

    def test_temporadas_oitnb(self):  # orange is the new black
        self.assertEqual(7, Serie.get_cantidad_temporadas("https://www.netflix.com/title/70242311"))

    def test_titulo_community(self):
        self.assertEqual("Community", Scrapping.get_title("https://www.netflix.com/title/70155589"))

    def test_id_community(self):
        self.assertEqual("70155589", Scrapping.get_id("https://www.netflix.com/title/70155589"))

    def test_genero_community(self):
        self.assertEqual("Sitcoms", Scrapping.get_genre("https://www.netflix.com/title/70155589"))

    def test_1_cantidad_episodios_rick_n_morty(self):
        self.assertEqual(41, Serie.get_cantidad_episodios("https://www.netflix.com/title/80014749"))

    def test_2_cantidad_episodios_rick_n_morty(self):
        self.assertNotEqual(40, Serie.get_cantidad_episodios("https://www.netflix.com/title/80014749"))

    def test_1_cantidad_episodios_community(self):
        self.assertEqual(109, Serie.get_cantidad_episodios("https://www.netflix.com/title/70155589"))

    def test_2_cantidad_episodios_community(self):
        self.assertNotEqual(110, Serie.get_cantidad_episodios("https://www.netflix.com/title/70155589"))

    def test_1_nombre_episodio_community(self):
        self.assertEqual("Community", Serie.get_nombre_episodio("https://www.netflix.com/title/70155589", 0))

    def test_borrar_numero_episodio(self):
        self.assertEqual("Community", Serie.borrar_numero_del_episodio("1. Community"))

    def test_borrar_numero_episodio_2(self):
        self.assertEqual("Spanish 101", Serie.borrar_numero_del_episodio("2. Spanish 101"))

    def test_edad_minima_community(self):
        self.assertEqual("13+ ", Serie.get_maturity("https://www.netflix.com/title/70155589"))