import unittest
from src.estrutura_sequencial.exercicio_vinte_quatro import analisa_maior_numero, analisa_menor_numero, mensagem_maior_numero, mensagem_menor_numero

class TestExercicioVinte_Quatro(unittest.TestCase):
    def test_analisa_maior_numero(self):
        self.assertEqual(analisa_maior_numero(primeiro_numero=10, segundo_numero=8, terceiro_numero=5),10)
        self.assertEqual(analisa_maior_numero(primeiro_numero=7, segundo_numero=8, terceiro_numero=5),8)
        self.assertEqual(analisa_maior_numero(primeiro_numero=2, segundo_numero=3, terceiro_numero=5),5)
        self.assertEqual(analisa_maior_numero(primeiro_numero=10.1, segundo_numero=8, terceiro_numero=5),10.1)

    def test_analisa_menor_numero(self):
        self.assertEqual(analisa_menor_numero(primeiro_numero=10, segundo_numero=8, terceiro_numero=5),5)
        self.assertEqual(analisa_menor_numero(primeiro_numero=10, segundo_numero=3, terceiro_numero=5),3)
        self.assertEqual(analisa_menor_numero(primeiro_numero=10, segundo_numero=8, terceiro_numero=5),5)
        self.assertEqual(analisa_menor_numero(primeiro_numero=10.1, segundo_numero=8, terceiro_numero=5.3),5.3)

    def test_mensagem_maior_numero(self):
        maior_numero_int = 10
        maior_numero_float = 10.5
        self.assertEqual(mensagem_maior_numero(maior_numero_int), f" O maior numero digitado foi o {maior_numero_int}")
        self.assertEqual(mensagem_maior_numero(maior_numero_float), f" O maior numero digitado foi o {maior_numero_float}")

    def test_mensagem_maior_numero(self):
        menor_numero_int = 5
        menor_numero_float = 3.3
        self.assertEqual(mensagem_menor_numero(menor_numero_int), f" O menor numero digitado foi o {menor_numero_int}")
        self.assertEqual(mensagem_menor_numero(menor_numero_float), f" O menor numero digitado foi o {menor_numero_float}")

    def test_exeptions_exercicio_vinte_quatro(self):
        try:
            analisa_maior_numero(primeiro_numero="10", segundo_numero=5, terceiro_numero=6)
        except Exception as f:
            self.assertEqual(f.args[0], "A informação forncecida, deve ser um numero")

        try:
            analisa_maior_numero(primeiro_numero=10, segundo_numero="4", terceiro_numero=8)
        except Exception as f:
            self.assertEqual(f.args[0], "A informação forncecida, deve ser um numero")

        try:
            analisa_maior_numero(primeiro_numero=10, segundo_numero=5, terceiro_numero="8")
        except Exception as f:
            self.assertEqual(f.args[0], "A informação forncecida, deve ser um numero")

        try:
            analisa_menor_numero(primeiro_numero="10", segundo_numero=5, terceiro_numero=6)
        except Exception as f:
            self.assertEqual(f.args[0], "A informação forncecida, deve ser um numero")

        try:
            analisa_menor_numero(primeiro_numero=10, segundo_numero="4", terceiro_numero=8)
        except Exception as f:
            self.assertEqual(f.args[0], "A informação forncecida, deve ser um numero")

        try:
            analisa_menor_numero(primeiro_numero=10, segundo_numero=5, terceiro_numero="8")
        except Exception as f:
            self.assertEqual(f.args[0], "A informação forncecida, deve ser um numero")
