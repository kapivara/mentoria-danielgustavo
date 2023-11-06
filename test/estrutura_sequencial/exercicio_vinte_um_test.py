import unittest
from src.estrutura_sequencial.exercicio_vinte_um import identifica_tipo_letra

class TestExercicioVinte(unittest.TestCase):
    def test_identifica_tipo_letra(self):
        letra_vogal = "A"
        letra_consoante = "Z"
        self.assertEqual(identifica_tipo_letra(letra_vogal),f"A letra digitada foi {letra_vogal}, e essa letra e uma VOGAL")
        self.assertEqual(identifica_tipo_letra(letra_consoante), f"A letra digitada foi {letra_consoante}, e essa letra e uma CONSOANTE")

    def test_imprime_letra(self):
        letra_vogal = "U"
        letra_consoante = "P"
        self.assertEqual(identifica_tipo_letra(letra_vogal), f"A letra digitada foi {letra_vogal}, e essa letra e uma VOGAL")
        self.assertEqual(identifica_tipo_letra(letra_consoante), f"A letra digitada foi {letra_consoante}, e essa letra e uma CONSOANTE")

    def test_exeptions_exercicio_vinte(self):
        try:
            identifica_tipo_letra(letra=1)
        except Exception as f:
            self.assertEqual(f.args[0], "Um numero não pode ser uma letra")

        try:
            identifica_tipo_letra(letra="SA")
        except Exception as f:
            self.assertEqual(f.args[0], "Você deve digitar apenas uma letra!!!")

        try:
            identifica_tipo_letra("'")
        except Exception as f:
            self.assertEqual(f.args[0], "Não e nenhum das opções")
