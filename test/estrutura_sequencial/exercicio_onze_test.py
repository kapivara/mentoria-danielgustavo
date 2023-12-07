import unittest
from src.estrutura_sequencial.exercicio_onze import calcula_produto_primeiro_numero, soma_triplo_primeiro_terceiro, terceiro_ao_cubo, imprime_terceiro_ao_cubo, imprime_resultado_dobro, imprime_resultado_triplo_primeiro

class TestExercicioOnze(unittest.TestCase):
    def test_mensagem_retorno(self):
        resultado_dobro_primeiro_metade_segundo = 45
        resultado_triplo_primeiro_soma_terceiro = 50
        resultado_terceiro_cubo = 100
        self.assertEqual(imprime_resultado_dobro(resultado_dobro_primeiro_metade_segundo), f"O produto do dobro do primeiro com metade do segundo e igual a {resultado_dobro_primeiro_metade_segundo}")
        self.assertEqual(imprime_resultado_triplo_primeiro(resultado_triplo_primeiro_soma_terceiro), f"A soma do triplo do primeiro com o terceiro e igual a {resultado_triplo_primeiro_soma_terceiro}")
        self.assertEqual(imprime_terceiro_ao_cubo(resultado_terceiro_cubo), f"O terceiro numero elevado ao cubo e igual a {resultado_terceiro_cubo}")
    
    def test_calculo_produto_primeiro_numero(self):
        self.assertEqual(calcula_produto_primeiro_numero(primeiro_numero_inteiro=35, segundo_numero_inteiro=10), 350.0)
        self.assertEqual(calcula_produto_primeiro_numero(primeiro_numero_inteiro=-15, segundo_numero_inteiro=15), -225.0)

    def test_soma_triplo_primeiro_terceiro(self):
        self.assertEqual(soma_triplo_primeiro_terceiro(primeiro_numero_inteiro=25, numero_real=3.14), 78.14)
        self.assertEqual(soma_triplo_primeiro_terceiro(primeiro_numero_inteiro=-10, numero_real= 47.8), 17.799999999999997)

    def test_terceiro_ao_cubo(self):
        self.assertEqual(terceiro_ao_cubo(numero_real=-3.14), -30.959144000000002)
        self.assertEqual(terceiro_ao_cubo(numero_real=536.45678), 154384684.80187938)

    def test_exeptions_ex_onze(self):
        try:
            calcula_produto_primeiro_numero(primeiro_numero_inteiro="10", segundo_numero_inteiro=20)
        except Exception as d:
            self.assertEqual(d.args[0], "O primeiro número não é um inteiro")
        
        try:
            calcula_produto_primeiro_numero(primeiro_numero_inteiro=10, segundo_numero_inteiro="20")
        except Exception as d:
            self.assertEqual(d.args[0], "O segundo número não é um inteiro")

        try:
            soma_triplo_primeiro_terceiro(primeiro_numero_inteiro="10", numero_real=80)
        except Exception as d:
            self.assertEqual(d.args[0], "O primeiro número não é um inteiro")

        try:
            soma_triplo_primeiro_terceiro(primeiro_numero_inteiro=10, numero_real="80")
        except Exception as d:
            self.assertEqual(d.args[0], "Digite um número real por favorzinho")

        try:
            terceiro_ao_cubo(numero_real="10.898989889898989")
        except Exception as d:
            self.assertEqual(d.args[0], "Digite um número real por favorzinho")
            