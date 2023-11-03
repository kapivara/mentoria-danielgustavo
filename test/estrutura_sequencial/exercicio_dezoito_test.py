import unittest
from src.estrutura_sequencial.exercicio_dezoito import analisa_maior_numero, imprime_maior_numero

class TestExercicioDezoito(unittest.TestCase):
    def test_analisa_maior_numero(self):
        self.assertEqual(analisa_maior_numero(numero_um=10, numero_dois=9), 10.0)
        self.assertEqual(analisa_maior_numero(numero_um=-10, numero_dois= -8), -8.0)
        self.assertEqual(analisa_maior_numero(numero_um=-10, numero_dois=5), 5.0)
        self.assertEqual(analisa_maior_numero(numero_um= 10, numero_dois= -5), 10.0)

    def test_exeptions_exercicio_dezoito(self):
        try:
            analisa_maior_numero(numero_um="10", numero_dois=10)
        except Exception as f:
            self.assertEqual(f.args[0], "Por favor, digite um numero correto!!!")

        try:
            analisa_maior_numero(numero_um=10, numero_dois="10")
        except Exception as f:
            self.assertEqual(f.args[0], "Por favor, digite um numero correto!!!")

    def test_imprime_maior_numero(self):
        maior_numero = 10
        self.assertEqual(imprime_maior_numero(maior_numero), f"o maior dos numeros digitados foi o {maior_numero}")
