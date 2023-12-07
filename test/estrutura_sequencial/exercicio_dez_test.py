import unittest
from src.estrutura_sequencial.exercicio_dez import converte_temperatura, imprime_temperatura

class TestExercicioDez(unittest.TestCase):
    def test_mensagem_retorno(self):
        temperatura_fahrenheit = 45
        self.assertEqual(imprime_temperatura(temperatura_fahrenheit), f"A temperatura em graus fahrenheit e de {temperatura_fahrenheit}.")

    def test_converte_temperatura(self):
        self.assertEqual(converte_temperatura(temperatura_celsius=35,), 95)
        self.assertEqual(converte_temperatura(temperatura_celsius=-100),-148)

    def test_exeptions(self):
        try:
            converte_temperatura(temperatura_Fahrenheit="80")
        except Exception as d:
            self.assertEqual(d.args[0], "Digite uma termperatura válida")
