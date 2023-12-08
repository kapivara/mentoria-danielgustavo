import unittest
from src.estrutura_sequencial.exercicio_trinta_quatro import exceptions_validations, is_analysis_variable_a, is_calculation_equation

class TestExercicioTrinta_Quatro(unittest.TestCase):
    def test_mensagem_retorno_is_calculation_equation(self):
        self.assertAlmostEqual(is_calculation_equation(variable_a=10, variable_b=10, variable_c=10), "Essa equação NÃO POSSUI raizes reais!!!!",places=2)
        self.assertAlmostEqual(is_calculation_equation(variable_a=2, variable_b=2, variable_c=0),"Essa equação possui DUAS raizes reais: 0.0 e -1.0", places=2)
        self.assertAlmostEqual(is_calculation_equation(variable_a=1, variable_b=0, variable_c=0), "Essa equação possui APENAS UMA raiz real: 0.0", places=2)
    
    def test_exceptions_validations(self):
        try:
            exceptions_validations(variable_a="10", variable_b=10, variable_c=10)
        except Exception as d:
            self.assertEqual(d.args[0], "Digite numeros válidos por favor!!!")

        try:
            exceptions_validations(variable_a=10, variable_b="10", variable_c=10)
        except Exception as d:
            self.assertEqual(d.args[0], "Digite numeros válidos por favor!!!")

        try:
            exceptions_validations(variable_a=10, variable_b=10, variable_c="10")
        except Exception as d:
            self.assertEqual(d.args[0], "Digite numeros válidos por favor!!!")

        try:
            exceptions_validations(variable_a=10, variable_b=10, variable_c=10)
        except Exception as d:
            self.assertEqual(d.args[0], "Tudo ok, podemos prosseguir!!!")

    def test_funcao_is_calculation_equation(self):
        self.assertAlmostEqual(is_calculation_equation(variable_a=10, variable_b=10, variable_c=10), "Essa equação NÃO POSSUI raizes reais!!!!",places=2)
        self.assertAlmostEqual(is_calculation_equation(variable_a=2, variable_b=2, variable_c=0),"Essa equação possui DUAS raizes reais: 0.0 e -1.0", places=2)
        self.assertAlmostEqual(is_calculation_equation(variable_a=1, variable_b=0, variable_c=0), "Essa equação possui APENAS UMA raiz real: 0.0", places=2)
