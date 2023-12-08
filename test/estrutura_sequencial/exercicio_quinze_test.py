import unittest
from src.estrutura_sequencial.exercicio_quinze import calculo_uso_litros_tinta, qtd_latas_tintas, valor_total_tintas, retorno_mensagem_litros_tintas, retorno_mensagem_qtds_latas, retorno_mensagem_preco_total_tintas

class TestExercicioQuinze(unittest.TestCase):
    def test_uso_litros_tinta(self):
        self.assertEqual(calculo_uso_litros_tinta(area_para_pintura=120), 40.0)
        self.assertEqual(calculo_uso_litros_tinta(area_para_pintura=125.5), 41.833333333333336)

    def test_qtd_latas_tintas(self):
        self.assertEqual(qtd_latas_tintas(qtd_litros_tinta=40),3)

    def test_valor_total_tintas(self):
        self.assertEqual(valor_total_tintas(qtd_latas_tinta=3), 240)
        
    def test_exeptions_ex_quinze(self):
        try:
            calculo_uso_litros_tinta(area_para_pintura="120")
        except Exception as d:
            self.assertEqual(d.args[0], "Informe corretamente a metragem que precisas pintar")

        try:
            calculo_uso_litros_tinta(area_para_pintura=-120)
        except Exception as d:
            self.assertEqual(d.args[0], "Metragens menores que zero, não podem ser pintadas")
        
    def test_retorno_mensagem_litros_tinta(self):
            qtd_litros_tinta = 40
            self.assertEqual(retorno_mensagem_litros_tintas(qtd_litros_tinta), f"A quantidade de litros a serem gastos e de {qtd_litros_tinta}")

    def test_retorno_mensagem_qtds_latas(self):
        qtd_latas_tinta = 3
        self.assertEqual(retorno_mensagem_qtds_latas(qtd_latas_tinta), f"A quantidade de latas a serem gastas e de {qtd_latas_tinta}")

    def test_mensagem_preco_total_tintas(self):
        preco_total_tintas = 120
        self.assertEqual(retorno_mensagem_preco_total_tintas(preco_total_tintas), f"O valor total a ser gasto e de R$ {preco_total_tintas}")

