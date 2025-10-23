import unittest
from catapulta.catapulta import Catapulta
from catapulta.palos import Palos
from catapulta.gomas import Gomas
from catapulta.tapones import Tapones
from catapulta.corchos import Corchos
from catapulta.pegamento import Pegamento
from catapulta.enemigo import Enemigo

class TestCatapulta(unittest.TestCase):

    def setUp(self):
        self.palos = Palos(longitud=2)
        self.gomas = Gomas(elasticidad=5)
        self.tapones = Tapones(tamaño=1)
        self.corchos = Corchos(flotabilidad=3)
        self.pegamento = Pegamento(resistencia=10)
        self.catapulta = Catapulta(self.palos, self.gomas, self.tapones, self.corchos, self.pegamento)
        self.enemigo = Enemigo(vida=10)

    def test_construir_catapulta(self):
        self.catapulta.construir()
        self.assertTrue(self.catapulta.construida)

    def test_lanzar_proyectil(self):
        self.catapulta.construir()
        daño = self.catapulta.lanzar()
        self.enemigo.recibir_dano(daño)
        self.assertEqual(self.enemigo.vida, 10 - daño)

    def test_enemigo_eliminado(self):
        self.catapulta.construir()
        daño = self.catapulta.lanzar()
        self.enemigo.recibir_dano(daño)
        self.enemigo.recibir_dano(daño)  # Dañar nuevamente para eliminar
        self.assertTrue(self.enemigo.vida <= 0)

if __name__ == '__main__':
    unittest.main()