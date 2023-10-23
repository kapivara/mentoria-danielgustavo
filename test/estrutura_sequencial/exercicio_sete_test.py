import unittest
from src.estrutura_sequencial.exercicio_sete import imprime_area_quadrado, calcula_area_quadrado

class TestExercicioSete(unittest.TestCase):
    def test_mensagem_retorno(self):
        dobro_area = 10
        self.assertEqual(imprime_area_quadrado(dobro_area), f"O dobro da area deste quadrado e de {dobro_area} centimentros.")

    def test_calcula_area(self):
        self.assertEqual(calcula_area_quadrado(lado_um=10, lado_dois=5), 100)
        self.assertEqual(calcula_area_quadrado(lado_um= 23.5, lado_dois=18.7),878.9)

    def test_exeptions(self):
        try:
            calcula_area_quadrado(lado_um="10", lado_dois=5)
        except Exception as d:
            self.assertEqual(d.args[0], "Digite um numero válido")

        try:
            calcula_area_quadrado(lado_um=10, lado_dois="5")   
        except Exception as d:
            self.assertEqual(d.args[0], "Digite um numero válido")

        try:
            calcula_area_quadrado(lado_um=-10, lado_dois=5)
        except Exception as d:
            self.assertEqual(d.args[0], "As medidas dos lados devem ter valores positivos!!!")
        