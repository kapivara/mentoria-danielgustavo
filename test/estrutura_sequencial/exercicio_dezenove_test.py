import unittest
from src.estrutura_sequencial.exercicio_dezenove import analisa_numero, imprime_numero

class TestExercicioDezenove(unittest.TestCase):
    def test_analisa_numero_positivo(self):
        numero = 10
        self.assertEqual(analisa_numero(numero), f"O numero {numero} e positivo!!!")

    def test_analisa_numero_negativo(self):
        numero = -10
        self.assertEqual(analisa_numero(numero), f"O numero {numero} e negativo!!!")   

    def test_exeptions_exercicio_dezenove(self):
        try:
            analisa_numero(numero="10")
        except Exception as f:
            self.assertEqual(f.args[0], "Por favor, digite um numero correto!!!")

        try:
            analisa_numero(numero=0)
        except Exception as f:
            self.assertEqual(f.args[0], "Zero e um numero neutro")

    def test_imprime_numero(self):
        resultado = 10
        self.assertEqual(imprime_numero(resultado), 10)
