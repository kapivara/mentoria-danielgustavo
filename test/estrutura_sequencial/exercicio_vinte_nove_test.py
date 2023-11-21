import unittest
from src.estrutura_sequencial.exercicio_vinte_nove import analise_exeptions, calcula_salario_liquido

class TestExercicioNove(unittest.TestCase):
    def test_mensagem_retorno(self):
        valor_hora = 10
        horas_trabalhadas = 220
        salario_bruto = 2200
        valor_percentual_ir = 220
        valor_percentual_inss = 220
        valor_percentual_fgts = 242
        total_descontos = 682
        salario_liquido = 1518
        self.assertAlmostEqual(calcula_salario_liquido(valor_hora, horas_trabalhadas), f"Seu salário bruto e de R${salario_bruto}\nDesconto IR = R${valor_percentual_ir:.2f}\nDesconto INSS R${valor_percentual_inss:.2f}\nDesconto FGTS {valor_percentual_fgts:.2f}\nO total de descontos foi de R${total_descontos:.2f}\nSeu salario liquido e R${salario_liquido:.2f}", places=2)

    def test_funcao_calcula_salario_liquido(self):
        self.assertAlmostEqual(calcula_salario_liquido(valor_hora=100, horas_trabalhadas=220), 22000, places=2)
        self.assertAlmostEqual(calcula_salario_liquido(valor_hora=50.5, horas_trabalhadas=220), 11110, places=2)

    def test_funcao_exeptions_exercicio_vinte_nove(self):
        try:
            analise_exeptions(valor_hora="10.0", horas_trabalhadas=220)
        except Exception as d:
            self.assertEqual(d.args[0], "Digite o 'VALOR' de cada hora trabalhada!!!!")

        try:
            analise_exeptions(valor_hora=-10, horas_trabalhadas=10)
        except Exception as d:
            self.assertEqual(d.args[0], "O valor da hora de trabalho não pode ser negativo!!!!")

        try:
            analise_exeptions(valor_hora=10, horas_trabalhadas="220")   
        except Exception as d:
            self.assertEqual(d.args[0], "Digite a quantidade de 'HORAS' trabalhadas!!!!")

        try:
            analise_exeptions(valor_hora= 10, horas_trabalhadas= -10)
        except Exception as d:
            self.assertEqual(d.args[0], "A quantidade de horas de trabalho não pode ser negativa!!!!")