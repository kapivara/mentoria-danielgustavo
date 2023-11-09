import unittest
from src.estrutura_sequencial.exercicio_vinte_seis import organiza_numeros_decrecente, mensagem_numeros_decrecentes

class TestExercicioVinte_Cinco(unittest.TestCase):
    def test_organiza_numeros_decrecente(self):
        self.assertEquals(organiza_numeros_decrecente(primeiro_numero=10, segundo_numero=8, terceiro_numero=5), [10, 8, 5])
        self.assertEquals(organiza_numeros_decrecente(primeiro_numero=10, segundo_numero=3, terceiro_numero=5), [10, 5, 3])
        self.assertEquals(organiza_numeros_decrecente(primeiro_numero=15, segundo_numero=12, terceiro_numero=3), [15, 12, 3])
        self.assertEquals(organiza_numeros_decrecente(primeiro_numero=10.1, segundo_numero=8.4, terceiro_numero=5.3), [10.1, 8.4, 5.3])

    def test_mensagem_numeros_decrecentes(self):
        lista_numeros = [5, 10, 8]
        self.assertEqual(mensagem_numeros_decrecentes(lista_numeros), f" O maior numero digitado foi o {lista_numeros}")

    def test_exeptions_exercicio_vinte_cinco(self):
        try:
            organiza_numeros_decrecente(primeiro_numero="10", segundo_numero=5, terceiro_numero=6)
        except Exception as f:
            self.assertEqual(f.args[0], "A informação forncecida, deve ser um numero")

        try:
            organiza_numeros_decrecente(primeiro_numero=10, segundo_numero="4", terceiro_numero=8)
        except Exception as f:
            self.assertEqual(f.args[0], "A informação forncecida, deve ser um numero")

        try:
            organiza_numeros_decrecente(primeiro_numero=10, segundo_numero=5, terceiro_numero="8")
        except Exception as f:
            self.assertEqual(f.args[0], "A informação forncecida, deve ser um numero")
