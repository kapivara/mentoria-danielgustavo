import unittest
from src.estrutura_sequencial.exercicio_trinta import retorna_dia_semana, analisa_numero_semana

class TestExercicioTrinta(unittest.TestCase):
    def test_analisa_numero_semana(self):
        self.assertEqual(analisa_numero_semana(numero_semana=1), 1)
        self.assertEqual(analisa_numero_semana(numero_semana=2), 2)
        self.assertEqual(analisa_numero_semana(numero_semana=3), 3)
        self.assertEqual(analisa_numero_semana(numero_semana=4), 4)
        self.assertEqual(analisa_numero_semana(numero_semana=5), 5)
        self.assertEqual(analisa_numero_semana(numero_semana=6), 6)
        self.assertEqual(analisa_numero_semana(numero_semana=7), 7)

    def test_retorna_dia_semana(self):
        self.assertEqual(retorna_dia_semana(numero_semana=1), "Domingo")
        self.assertEqual(retorna_dia_semana(numero_semana=2), "Segunda Feira")
        self.assertEqual(retorna_dia_semana(numero_semana=3), "Terça Feira")
        self.assertEqual(retorna_dia_semana(numero_semana=4), "Quarta Feira")
        self.assertEqual(retorna_dia_semana(numero_semana=5), "Quinta Feira")
        self.assertEqual(retorna_dia_semana(numero_semana=6), "Sexta Feira")
        self.assertEqual(retorna_dia_semana(numero_semana=7), "Sabado")

    def test_exeptions_exercicio_trinta(self):
        try:
            analisa_numero_semana(numero_semana="10")
        except Exception as d:
            self.assertEqual(d.args[0], "Por favor, digite um numero valido")

        try:
            analisa_numero_semana(numero_semana=10)
        except Exception as d:
            self.assertEqual(d.args[0], "Numero Invalido!!!")

        try:
            analisa_numero_semana(numero_semana=-10)
        except Exception as d:
            self.assertEqual(d.args[0], "Numero Invalido!!!")
