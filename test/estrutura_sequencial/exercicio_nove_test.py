import unittest
from src.estrutura_sequencial.exercicio_nove import converte_temperatura, imprime_temperatura

class TestExercicioOito(unittest.TestCase):
    def test_mensagem_retorno(self):
        temperatura_celsius = 35
        self.assertEqual(imprime_temperatura(temperatura_celsius), f"A temperatura em graus celsius e de {temperatura_celsius}.")

    def test_converte_temperatura(self):
        self.assertEqual(converte_temperatura(temperatura_Fahrenheit=80,), 26.666666666666668)
        self.assertEqual(converte_temperatura(temperatura_Fahrenheit=-100),-73.33333333333334)

    def test_exeptions(self):
        try:
            converte_temperatura(temperatura_Fahrenheit="80")
        except Exception as d:
            self.assertEqual(d.args[0], "Digite uma termperatura válida")
