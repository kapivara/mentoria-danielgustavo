import unittest
from src.estrutura_sequencial.exercicio_vinte_cinco import analisa_menor_preco, mensagem_menor_preco

class TestExercicioVinte_Cinco(unittest.TestCase):
    def test_analisa_menor_preco(self):
        self.assertEqual(analisa_menor_preco(primeiro_produto=10, segundo_produto=8, terceiro_produto=5),5)
        self.assertEqual(analisa_menor_preco(primeiro_produto=10, segundo_produto=3, terceiro_produto=5),3)
        self.assertEqual(analisa_menor_preco(primeiro_produto=10, segundo_produto=8, terceiro_produto=5),5)
        self.assertEqual(analisa_menor_preco(primeiro_produto=10.1, segundo_produto=8, terceiro_produto=5.3),5.3)

    def test_mensagem_menor_preco(self):
        menor_preco_int = 5
        menor_preco_float = 3.3
        self.assertEqual(mensagem_menor_preco(menor_preco_int), f"O produto com menor valor custa R$ {menor_preco_int}")
        self.assertEqual(mensagem_menor_preco(menor_preco_float), f"O produto com menor valor custa R$ {menor_preco_float}")

    def test_exeptions_exercicio_vinte_cinco(self):
        try:
            analisa_menor_preco(primeiro_produto="10", segundo_produto=5, terceiro_produto=6)
        except Exception as f:
            self.assertEqual(f.args[0], "Por favor forneça corretamente o valor do produto")

        try:
            analisa_menor_preco(primeiro_produto=10, segundo_produto="4", terceiro_produto=8)
        except Exception as f:
            self.assertEqual(f.args[0], "Por favor forneça corretamente o valor do produto")

        try:
            analisa_menor_preco(primeiro_produto=10, segundo_produto=5, terceiro_produto="8")
        except Exception as f:
            self.assertEqual(f.args[0], "Por favor forneça corretamente o valor do produto")
