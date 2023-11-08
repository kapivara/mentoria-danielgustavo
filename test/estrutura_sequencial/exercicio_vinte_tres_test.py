import unittest
from src.estrutura_sequencial.exercicio_vinte_tres import analisa_numeros, mensagem_maior_numero

class TestExercicioVinte_Tres(unittest.TestCase):
    def test_analisa_numeros(self):
        self.assertEqual(analisa_numeros(primeiro_numero=10, segundo_numero=8, terceiro_numero=5),10)
        self.assertEqual(analisa_numeros(primeiro_numero=10, segundo_numero=8.1, terceiro_numero=5),10)
        self.assertEqual(analisa_numeros(primeiro_numero=10, segundo_numero=8, terceiro_numero=5.2),10)
        self.assertEqual(analisa_numeros(primeiro_numero=10.1, segundo_numero=8, terceiro_numero=5),10.1)

    def test_mensagem_aprovado_reprovado(self):
        maior_numero_int = 10
        maior_numero_float = 10.5
        self.assertEqual(mensagem_maior_numero(maior_numero_int), f" O maior numero digitado foi o {maior_numero_int}")
        self.assertEqual(mensagem_maior_numero(maior_numero_float), f" O maior numero digitado foi o {maior_numero_float}")

    def test_exeptions_exercicio_vinte_tres(self):
        try:
            analisa_numeros(primeiro_numero="10", segundo_numero=5, terceiro_numero=6)
        except Exception as f:
            self.assertEqual(f.args[0], "A informação forncecida, deve ser um numero, primeiro numero")

        try:
            analisa_numeros(primeiro_numero=10, segundo_numero="4", terceiro_numero=8)
        except Exception as f:
            self.assertEqual(f.args[0], "A informação forncecida, deve ser um numero, segundo numero")

        try:
            analisa_numeros(primeiro_numero=10, segundo_numero=5, terceiro_numero="8")
        except Exception as f:
            self.assertEqual(f.args[0], "A informação forncecida, deve ser um numero, terceiro numero")