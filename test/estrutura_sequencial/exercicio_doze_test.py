import unittest
from src.estrutura_sequencial.exercicio_doze import calcula_peso_ideal, imprime_peso_ideal

class TestExercicioDoze(unittest.TestCase):
    def test_mensagem_retorno(self):
        peso_ideal = 65.65
        self.assertEqual(imprime_peso_ideal(peso_ideal), f"Seu peso ideal seria de {peso_ideal}")
           
    def test_calculo_peso_ideal(self):
        self.assertEqual(calcula_peso_ideal(altura=1.70, sexo="M"), 65.59)
        self.assertEqual(calcula_peso_ideal(altura=1.80, sexo="F"), 67.08)

    def test_exeptions_ex_doze(self):
        try:
            calcula_peso_ideal(altura="10", sexo="M")
        except Exception as d:
            self.assertEqual(d.args[0], "Informe a altura corretamente")

        try:
            calcula_peso_ideal(altura="10", sexo="F")
        except Exception as d:
            self.assertEqual(d.args[0], "Informe a altura corretamente")

        try:
            calcula_peso_ideal(altura=-1.56, sexo="M")
        except Exception as d:
            self.assertEqual(d.args[0], "Numeros negativos não são aceitos!!!!")

        try:
            calcula_peso_ideal(altura=-1.56, sexo="F")
        except Exception as d:
            self.assertEqual(d.args[0], "Numeros negativos não são aceitos!!!!")
            
        try:
            calcula_peso_ideal(altura=1.56, sexo=22)
        except Exception as d:
            self.assertEqual(d.args[0], "Por favor informe o sexo corretamente")
