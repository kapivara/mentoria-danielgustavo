import unittest
from src.estrutura_sequencial.exercicio_trinta_um import calcula_nota_media, valida_conceito_nota, valida_status_aluno, retorno_mensagem_status_aluno 

class TestExercicioTrinta(unittest.TestCase):
    def test_calcula_nota_media(self):
        self.assertEqual(calcula_nota_media(nota_um=1, nota_dois=3), 2)
        self.assertEqual(calcula_nota_media(nota_um=5, nota_dois=5), 5)
        self.assertEqual(calcula_nota_media(nota_um=7, nota_dois=6), 6.5)
        self.assertEqual(calcula_nota_media(nota_um=14, nota_dois=0), 7)
        self.assertEqual(calcula_nota_media(nota_um=10, nota_dois=9), 9.5)

    def test_valida_conceito_nota(self):
        self.assertEqual(valida_conceito_nota(nota_media=3), "E")
        self.assertEqual(valida_conceito_nota(nota_media=5.5), "D")
        self.assertEqual(valida_conceito_nota(nota_media=7), "C")
        self.assertEqual(valida_conceito_nota(nota_media=8), "B")
        self.assertEqual(valida_conceito_nota(nota_media=9.5), "A")

    def test_exeptions_exercicio_trinta_um(self):
        try:
            calcula_nota_media(nota_um="10", nota_dois=10)
        except Exception as d:
            self.assertEqual(d.args[0], "Por favor, digite um numero correto!!!")

        try:
            calcula_nota_media(nota_um=10, nota_dois="10")
        except Exception as d:
            self.assertEqual(d.args[0], "Por favor, digite um numero correto!!!")

        try:
            calcula_nota_media(nota_um= -10, nota_dois=10)
        except Exception as d:
            self.assertEqual(d.args[0], "Não pode haver notas menores que zero")

        try:
            calcula_nota_media(nota_um=10, nota_dois=-10)
        except Exception as d:
            self.assertEqual(d.args[0], "Não pode haver notas menores que zero")