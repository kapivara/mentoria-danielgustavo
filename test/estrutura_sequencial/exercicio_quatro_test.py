import unittest
from src.estrutura_sequencial.exercicio_quatro import imprime_nota_media, calcula_media

class TestExerciocioQuatro(unittest.TestCase):
    def test_mensagem(self):
        media = 10
        self.assertEqual(imprime_nota_media(media), f"A média da nota desse aluno e de {media} pontos.")

    def test_calcula_media(self):
        self.assertEqual(calcula_media(nota_um=5, nota_dois=4,nota_tres=6,nota_quatro=8),5.75)
        self.assertEqual(calcula_media(nota_um=10, nota_dois=8,nota_tres=5,nota_quatro=10),8.25)
        self.assertEqual(calcula_media(nota_um=8, nota_dois=7,nota_tres=8,nota_quatro=6),7.25)

    def test_media_validacoes(self):
        try:
            calcula_media(nota_um="5", nota_dois=5,nota_tres="8", nota_quatro=8)
        except Exception as e:
            self.assertEqual(e.args[0], "Por favor, digite um numero valido")

        try:
            calcula_media(nota_um=6, nota_dois=5.7,nota_tres="8", nota_quatro=8)
        except Exception as e:
            self.assertEqual(e.args[0], "Por favor, digite um numero valido")


if __name__ == "main":
    unittest.main()
    