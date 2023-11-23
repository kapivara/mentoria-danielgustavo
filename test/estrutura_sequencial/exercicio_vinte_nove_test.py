import unittest
from src.estrutura_sequencial.exercicio_vinte_nove import analise_exeptions, calcula_salario_liquido, calcula_salario_bruto, calcula_valor_total_impostos, calcula_valor_imposto_fgts, calcula_valor_imposto_inss, calcula_valor_imposto_ir, retorna_mensagem_salario_liquido

class TestExercicioNove(unittest.TestCase):
    def test_mensagem_retorno(self):
        salario_bruto = 2200
        valor_percentual_ir = 220
        valor_percentual_inss = 220
        valor_percentual_fgts = 242
        total_descontos = 682
        salario_liquido = 1518
        self.assertAlmostEqual(retorna_mensagem_salario_liquido(salario_bruto, valor_percentual_ir, valor_percentual_inss, valor_percentual_fgts, total_descontos, salario_liquido), f"Seu salário bruto e de R${salario_bruto:.2f}\nO desconto IR(-) = R${valor_percentual_ir:.2f}\nO desconto do INSS(-) = R${valor_percentual_inss:.2f}\nO valor do se FGTS e de = R${valor_percentual_fgts:.2f}\nO total de descontos foi de = R${total_descontos:.2f}\nSeu salario liquido e de = R${salario_liquido:.2f}", places=2)

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

    def test_funcao_calcula_salario_bruto(self):
        self.assertEqual(calcula_salario_bruto(valor_hora=3, horas_trabalhadas=220), 660.00)
        self.assertAlmostEqual(calcula_salario_bruto(valor_hora=5, horas_trabalhadas=220), 1100.00)
        self.assertEqual(calcula_salario_bruto(valor_hora=100, horas_trabalhadas=220), 22000)
        self.assertAlmostEqual(calcula_salario_bruto(valor_hora=50.5, horas_trabalhadas=220), 11110.00, places=2)
        self.assertAlmostEqual(calcula_salario_bruto(valor_hora=150.65, horas_trabalhadas=220),33143.00, places=2)

    def test_calcula_salario_liquido(self):
        self.assertAlmostEqual(calcula_salario_liquido(salario_bruto=660, valor_percentual_ir=0.00, valor_percentual_inss=220), 594.00, places=2)
        self.assertAlmostEqual(calcula_salario_liquido(salario_bruto=1100.00, valor_percentual_ir=55.00, valor_percentual_inss=66.00), 935.00, places=2)
        self.assertAlmostEqual(calcula_salario_liquido(salario_bruto=2200.00, valor_percentual_ir=220.00, valor_percentual_inss=220), 1760.00, places=2)
        self.assertAlmostEqual(calcula_salario_liquido(salario_bruto=33000.00, valor_percentual_ir=6600.00, valor_percentual_inss=3300.00), 23100.00, places=2)
        self.assertAlmostEqual(calcula_salario_liquido(salario_bruto=18000.40, valor_percentual_ir=3600.08, valor_percentual_inss=1800.04), 12600.28, places=2)

    def test_calcula_valor_imposto_ir(self):
        self.assertAlmostEqual(calcula_valor_imposto_ir(salario_bruto=660.00), 0.00, places=2)
        self.assertAlmostEqual(calcula_valor_imposto_ir(salario_bruto=1100.00), 55.00, places=2)
        self.assertAlmostEqual(calcula_valor_imposto_ir(salario_bruto = 2200.00), 220.00, places=2)
        self.assertAlmostEqual(calcula_valor_imposto_ir(salario_bruto = 3300.00), 660.00, places=2)
        self.assertAlmostEqual(calcula_valor_imposto_ir(salario_bruto = 33482.00), 6696.40, places=2)

    def test_calculo_valor_imposto_inss(self):
        self.assertAlmostEqual(calcula_valor_imposto_inss(salario_bruto=660.00), 66.00, places=2)
        self.assertAlmostEqual(calcula_valor_imposto_inss(salario_bruto=1100.00), 110.00, places=2)
        self.assertAlmostEqual(calcula_valor_imposto_inss(salario_bruto = 2200), 220.00, places=2)
        self.assertAlmostEqual(calcula_valor_imposto_inss(salario_bruto = 3300), 330.00, places=2)
        self.assertAlmostEqual(calcula_valor_imposto_inss(salario_bruto = 33482), 3348.20, places=2)

    def test_calcula_valor_imposto_fgts(self):
        self.assertAlmostEqual(calcula_valor_imposto_fgts(salario_bruto = 660), 72.60, places=2)
        self.assertAlmostEqual(calcula_valor_imposto_fgts(salario_bruto = 1100), 121.00, places=2)
        self.assertAlmostEqual(calcula_valor_imposto_fgts(salario_bruto = 2200), 242.00, places=2)
        self.assertAlmostEqual(calcula_valor_imposto_fgts(salario_bruto = 3300), 363.00, places=2)
        self.assertAlmostEqual(calcula_valor_imposto_fgts(salario_bruto = 33482), 869.36, places=2)

    def test_calcula_valor_total_impostos(self):
        self.assertAlmostEqual(calcula_valor_total_impostos(salario_bruto=660.00, valor_percentual_ir=0.00, valor_percentual_inss=66.00), 66.00, places=2)
        self.assertAlmostEqual(calcula_valor_total_impostos(salario_bruto=1100.00, valor_percentual_ir=55.00, valor_percentual_inss=110), 165.00, places=2)
        self.assertAlmostEqual(calcula_valor_total_impostos(salario_bruto=2200.00, valor_percentual_ir=220.00, valor_percentual_inss=220), 440.00, places=2)
        self.assertAlmostEqual(calcula_valor_total_impostos(salario_bruto=33000.00, valor_percentual_ir=6600.00, valor_percentual_inss=3300.00), 9900.00, places=2)
        self.assertAlmostEqual(calcula_valor_total_impostos(salario_bruto=18000.40, valor_percentual_ir=3600.08, valor_percentual_inss=1800.04), 5400.12, places=2)
