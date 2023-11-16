import unittest
from src.estrutura_sequencial.exercicio_vinte_oito import calculo_aumento_salario

class TestExercicioVinteOito(unittest.TestCase):
    def test_calculo_aumento_salario(self):
        salario_base = 250
        atualizacao_salario = 300
        diferenca = 50
        self.assertAlmostEqual(calculo_aumento_salario(salario_base), f"Seu salário base era de R${salario_base}\nSeu novo salário agora será R${atualizacao_salario:.2f}\nUma diferença de R${diferenca:.2f}", places=2)


    def test_exeptions_ex_vinte_oito(self):
        try:
            calculo_aumento_salario(salario_base="250")
        except Exception as d:
            self.assertEqual(d.args[0], "Informe o valor correto da sua hora de trabalho!!!!")

        try:
            calculo_aumento_salario(salario_base=-250)
        except Exception as d:
            self.assertEqual(d.args[0], "O valor da hora não pode ser negativo")

    def test_mensagem_retorno_aumento_salario(self):
        salario_base = 250
        atualizacao_salario = 300
        diferenca = 50
        self.assertEqual(calculo_aumento_salario(salario_base), f"Seu salário base era de R${salario_base}\nSeu novo salário agora será R${atualizacao_salario:.2f}\nUma diferença de R${diferenca:.2f}")