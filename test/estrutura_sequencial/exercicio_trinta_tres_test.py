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
            year = 2000
            validations_excepitons_year(year)
        except Exception as d:
            self.assertEqual(d.args[0], f"O ano {year} e um ano com formato válido!!!")      

    def test_validation_bissext_yaer(self):
        self.assertEqual(validation_bissext_yaer(year=2000), True)
        self.assertEqual(validation_bissext_yaer(year=2001), False)

    def test_bissext_mensage_year_bissext(self):
        year = 2000
        self.assertEqual(bissext_mensage_year(year = 2000), f"{year}, e um ano bissexto!!!")
    
    def test_bissext_mensage_year_no_bissext(self):
        year = 2001
        self.assertEqual(bissext_mensage_year(year = 2001), f"{year}, não e um ano bissexto!!!")
