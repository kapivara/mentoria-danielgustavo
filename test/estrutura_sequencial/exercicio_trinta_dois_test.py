import unittest
from src.estrutura_sequencial.exercicio_trinta_dois import exeptions_validations, is_triangle_validations, is_equilatero_triangle, is_isoceles_triangle, is_escaleno_triangle, return_triangle_type  

class TestExercicioTrintaDois(unittest.TestCase):
    def test_exeptions_validations(self):
        self.assertEqual(exeptions_validations(primeiro_lado="10", segundo_lado=8, terceiro_lado=8), "Por favor, digite um numero correto!!!")
        self.assertEqual(exeptions_validations(primeiro_lado=10, segundo_lado="8", terceiro_lado=8), "Por favor, digite um numero correto!!!")
        self.assertEqual(exeptions_validations(primeiro_lado=10, segundo_lado=8, terceiro_lado="8"), "Por favor, digite um numero correto!!!")

    def test_valida_conceito_nota(self):
        self.assertEqual(valida_conceito_nota(nota_media=3), "E")
        self.assertEqual(valida_conceito_nota(nota_media=5.5), "D")
        self.assertEqual(valida_conceito_nota(nota_media=7), "C")
        self.assertEqual(valida_conceito_nota(nota_media=8), "B")
        self.assertEqual(valida_conceito_nota(nota_media=9.5), "A")

    def test_exeptions_exercicio_trinta_dois(self):
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