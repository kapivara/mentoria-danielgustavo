import unittest
from src.estrutura_sequencial.exercicio_oito import calcula_salario_final, imprime_salario

class TestExercicioOito(unittest.TestCase):
    def test_mensagem_retorno(self):
        salario_final = 10
        self.assertEqual(imprime_salario(salario_final), f" O seu salario no fim do mês, será de R$ {salario_final:.2f}.")

    def calcula_salario_final(self):
        self.assertEqual(calcula_salario_final(valor_hora=100, horas_trabalhadas=220), 22000.00)
        self.assertEqual(calcula_salario_final(valor_hora=50, horas_trabalhadas=220),11000.00)

    def test_exeptions(self):
        try:
            calcula_salario_final(valor_hora="10", horas_trabalhadas=5)
        except Exception as d:
            self.assertEqual(d.args[0], "Digite o VALOR' de horas trabalhadas!!!!")

        try:
            calcula_salario_final(valor_hora= 10, horas_trabalhadas="10")   
        except Exception as d:
            self.assertEqual(d.args[0], "Digite a quantidade de 'HORAS' trabalhadas!!!!")

        try:
            calcula_salario_final(valor_hora= -10, horas_trabalhadas=10)
        except Exception as d:
            self.assertEqual(d.args[0], "As medidas dos lados devem ter valores positivos!!!")
