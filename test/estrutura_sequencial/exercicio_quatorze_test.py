import unittest
from src.estrutura_sequencial.exercicio_quatorze import calcula_salario_bruto, calcula_imposto_de_renda, calcula_inss, calcula_imposto_sindical, calcula_salario_liquido, mensagem_mostra_salario_bruto, mensagem_mostra_salario_liquido, mensagem_retorno_imposto_de_renda, mensagem_retorno_imposto_sindical, mensagem_retorno_inss

class TestExercicioQuatorze(unittest.TestCase):
    def test_calculo_salario_bruto(self):
        self.assertEqual(calcula_salario_bruto(valor_hora=10, horas_trabalhadas=220), 2200.0)
        self.assertEqual(calcula_salario_bruto(valor_hora=17.50, horas_trabalhadas=220.5), 3858.75)

    def test_calculo_imposto_de_renda(self):
        self.assertEqual(calcula_imposto_de_renda(salario_bruto=15532), 1708.52)

    def test_calculo_inss(self):
        self.assertEqual(calcula_inss(salario_bruto=15532), 1242.56)

    def test_calculo_imposto_sindical(self):
        self.assertEqual(calcula_imposto_sindical(salario_bruto=15532), 776.6)
    
    def test_calculo_salario_liquido(self):
        self.assertEqual(calcula_salario_liquido(salario_bruto=15532, imposto_de_renda=1708.52, inss=1242.56, imposto_sindical=776.6), 11804.32)
        
    def test_exeptions_ex_quatorze(self):
        try:
            calcula_salario_bruto(valor_hora="10", horas_trabalhadas="150")
        except Exception as d:
            self.assertEqual(d.args[0], "Informe o valor correto da sua hora de trabalho!!!!")

        try:
            calcula_salario_bruto(valor_hora=-10, horas_trabalhadas=50)
        except Exception as d:
            self.assertEqual(d.args[0], "O valor da hora não pode ser negativo")

        try:
            calcula_salario_bruto(valor_hora=10, horas_trabalhadas=-50)
        except Exception as d:
            self.assertEqual(d.args[0], "O valor da hora não pode ser negativo")
        
        try:
            calcula_imposto_de_renda(salario_bruto="45856")
        except Exception as d:
            self.assertEqual(d.args[0], "Algo está errado, por favor revise os dados")

        try:
            calcula_imposto_de_renda(salario_bruto=-100)
        except Exception as d:
            self.assertEqual(d.args[0], f"Com salário abaixo de zero, você não precisa pagar IR!!!")
        
        try:
            calcula_inss(salario_bruto="123456")
        except Exception as d:
            self.assertEqual(d.args[0], "Algo está errado, por favor revise os dados")

        try:
            calcula_inss(salario_bruto=-100)
        except Exception as d:
            self.assertEqual(d.args[0], f"Com salário abaixo de zero, você não precisa pagar INSS!!!")

        try:
            calcula_imposto_sindical(salario_bruto="1234567")
        except Exception as d:
            self.assertEqual(d.args[0], "Algo está errado, por favor revise os dados")
        
        try:
            calcula_imposto_sindical(salario_bruto=-100)
        except Exception as d:
            self.assertEqual(d.args[0], f"Com salário abaixo de zero, você não precisa pagar Imposto Sindical!!!")
        
        try:
            calcula_salario_liquido(salario_bruto="1234567", imposto_de_renda="22", inss="1212", imposto_sindical="1231")
        except Exception as d:
            self.assertEqual(d.args[0], "Algo está errado, por favor revise os dados")
        
        try:
            calcula_salario_liquido(salario_bruto=-100, imposto_de_renda=-10, inss=-20, imposto_sindical=-30)
        except Exception as d:
            self.assertEqual(d.args[0], f"Com salário abaixo de zero, você não precisa pagar Imposto Sindical!!!")
        
    def test_mensagem_retorno_salario_bruto(self):
        salario_bruto = 65.65
        self.assertEqual(mensagem_mostra_salario_bruto(salario_bruto), f"Seu salário bruto e de R$ {salario_bruto}")

    def test_mensagem_retorno_salario_imposto_de_renda(self):
        imposto_de_renda = 450
        self.assertEqual(mensagem_retorno_imposto_de_renda(imposto_de_renda), f"Você pagou R$ {imposto_de_renda} de Imposto de Renda")

    def test_mensagem_retorno_inss(self):
        imposto_inss = 1052.00
        self.assertEqual(mensagem_retorno_inss(imposto_inss), f"Você pagou R$ {imposto_inss} de INSS")

    def test_mensagem_retorno_imposto_sindical(self):
        imposto_sindical = 45658
        self.assertEqual(mensagem_retorno_imposto_sindical(imposto_sindical), f"Você pagou R$ {imposto_sindical} de Imposto Sindical")

    def test_mensagem_retorno_mostra_salario_liquido(self):
        salario_bruto = 1000
        self.assertEqual(mensagem_mostra_salario_liquido(salario_bruto), f"Seu salário liquido e de R$ {salario_bruto}")