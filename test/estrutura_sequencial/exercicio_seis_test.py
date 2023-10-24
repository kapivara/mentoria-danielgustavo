import unittest
from src.estrutura_sequencial.exercicio_seis import imprime_area, calcula_area

class TestExercicioSeis(unittest.TestCase):
    def test_mensagem_retorno(self):
        raio = 10
        self.assertEqual(imprime_area(raio), f"A área deste circulo e de {raio}, centimetros")

    def test_calcula_area(self):
        self.assertEqual(calcula_area(raio_area=10),314.1592653589793)
        self.assertEqual(calcula_area(raio_area=99),30790.74959783356)
        self.assertEqual(calcula_area(raio_area=23.5),1734.9445429449634)
        self.assertEqual(calcula_area(raio_area=35.8),4026.390808546822)

    def test_exeptions(self):
        try:
            calcula_area(raio_area="10")
        except Exception as d:
            self.assertEqual(d.args[0], "Por favor, digite a medida da área")

        try:
            calcula_area(raio_area=-10)
        except Exception as d:
            self.assertEqual(d.args[0], "A medida da área deve ter um valor positivo")
        