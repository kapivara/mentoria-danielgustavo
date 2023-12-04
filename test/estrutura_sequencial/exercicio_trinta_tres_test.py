import unittest
from src.estrutura_sequencial.exercicio_trinta_tres import validations_excepitons_year, validation_bissext_yaer, bissext_mensage_year


class TestExercicioTrintaTres(unittest.TestCase):
    def test_validations_excepitons_year(self):
        try:
            validations_excepitons_year(year = "2000")
        except Exception as d:
            self.assertEqual(d.args[0], "\nDigite o ano corretamente, os formatos aceitos são 'XXXX' ")

        try:
            validations_excepitons_year(year = -2000)
        except Exception as d:
            self.assertEqual(d.args[0], "Não pode haver anos menores que zero, por favor, digite um ano válido!!!")

        try:
            validations_excepitons_year(year = 2000)
        except Exception as d:
            self.assertEqual(d.args[0], f"O ano {year} e um ano com formato válido!!!")       

    def test_is_triangle_validations(self):
        self.assertEqual(is_triangle_validations(primeiro_lado=10, segundo_lado=10, terceiro_lado=10),True)
        self.assertEqual(is_triangle_validations(primeiro_lado=10, segundo_lado=10, terceiro_lado=9),True)
        self.assertEqual(is_triangle_validations(primeiro_lado=10, segundo_lado=6, terceiro_lado=5),True)
        self.assertEqual(is_triangle_validations(primeiro_lado=10.5, segundo_lado=6.5, terceiro_lado=5.5),True)
        self.assertEqual(is_triangle_validations(primeiro_lado=10, segundo_lado=5, terceiro_lado=5),False)
        self.assertEqual(is_triangle_validations(primeiro_lado=10, segundo_lado=0, terceiro_lado=3),False)
        self.assertEqual(is_triangle_validations(primeiro_lado=10, segundo_lado=-5, terceiro_lado=-5),False)

    def test_is_equilatero_triangle(self):
        self.assertEqual(is_equilatero_triangle(primeiro_lado=10, segundo_lado=10, terceiro_lado=10), True)
        self.assertEqual(is_equilatero_triangle(primeiro_lado=9, segundo_lado=10, terceiro_lado=10), False)

    def test_is_isoceles_triangle(self):
        self.assertEqual(is_isoceles_triangle(primeiro_lado=10, segundo_lado=10, terceiro_lado=8), True)
        self.assertEqual(is_isoceles_triangle(primeiro_lado=10, segundo_lado=10, terceiro_lado=10), False)

    def test_is_escaleno_triangle(self):
        self.assertEqual(is_escaleno_triangle(primeiro_lado=10, segundo_lado=10, terceiro_lado=8), False)
        self.assertEqual(is_escaleno_triangle(primeiro_lado=10, segundo_lado=9, terceiro_lado=8), True)

    def test_return_triangle_type(self):
        self.assertEqual(return_triangle_type(primeiro_lado=10, segundo_lado=10, terceiro_lado=10), "\nAs medidas formam um triangulo equilatero!!!\n")
        self.assertEqual(return_triangle_type(primeiro_lado=10, segundo_lado=10, terceiro_lado=8), "\nAs medidas formam um triangulo Isoceles!!!\n")
        self.assertEqual(return_triangle_type(primeiro_lado=10, segundo_lado=9, terceiro_lado=8), "\nAs medidas formam um triangulo escaleno!!!\n")