import unittest
from src.estrutura_sequencial.exercicio_treze import calcula_excesso_peixes, calcula_valor_multa, mensagem_retorno_excesso, mensagem_retorno_multa

class TestExercicioTreze(unittest.TestCase):
    def test_mensagem_retorno_excesso(self):
        excesso = 65.65
        self.assertEqual(mensagem_retorno_excesso(excesso), f"A quantidade de peixes em excesso e de {excesso} quilos")

    def test_mensagem_retorno_multa(self):
        multa = 100
        self.assertEqual(mensagem_retorno_multa(multa), f"O valor da multa a ser paga pelo excesso de peixes e de R$ {multa}")    
    
    def test_calculo_excesso_peixes(self):
        self.assertEqual(calcula_excesso_peixes(peso_peixe=69), 19.0)
        self.assertEqual(calcula_excesso_peixes(peso_peixe=70.2), 20.200000000000003)

    def test_exeptions_ex_treze(self):
        try:
            calcula_excesso_peixes(peso_peixe="10")
        except Exception as d:
            self.assertEqual(d.args[0], "Informe o numero correto de quilos de peixes.")

        try:
            calcula_excesso_peixes(peso_peixe=-10)
        except Exception as d:
            self.assertEqual(d.args[0], "O peso dos peixes não pode ser negativo!!!")
