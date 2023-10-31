import unittest
from src.estrutura_sequencial.exercicio_dezesseis import calculo_uso_litros_tinta, qtd_tintas_latas, qtd_tintas_galoes, qtd_latas_e_galoes_tinta, valor_tinta_latas, valor_tinta_galoes, valor_total_galoes_e_latas, retorno_mensagem_litros_tintas, retorno_mensagem_qtds_latas, retorno_mensagem_qtd_latas_e_galoes, retorno_mensagem_qtds_galoes, retorno_mensagem_preco_total_latas_e_galoes, retorno_mensagem_preco_total_galoes_tintas, retorno_mensagem_preco_total_latas_tintas 

class TestExercicioDezesseis(unittest.TestCase):
    def test_uso_litros_tinta(self):
        self.assertEqual(calculo_uso_litros_tinta(area_para_pintura=120), 22.0)
        self.assertEqual(calculo_uso_litros_tinta(area_para_pintura=125.5), 23.008333333333336)

    def qtd_tintas_latas(self):
        self.assertEqual(qtd_tintas_latas(qtd_litros_tinta=22),2)

    def qtd_tintas_galoes(self):
        self.assertEqual(qtd_tintas_galoes(qtd_litros_tinta=22),7)

    def qtd_latas_e_galoes_tinta(self):
        self.assertEqual(qtd_latas_e_galoes_tinta(qtd_litros_tinta=22, area_para_pintura=120),(1,2))

    def valor_tinta_latas(self):
        self.assertEqual(valor_tinta_latas(qtd_latas_tinta=2), 160)

    def valor_tinta_galoes(self):
        self.assertEqual(valor_tinta_galoes(qtd_galoes_tinta=7), 175)

    def valor_total_galoes_e_latas(self):
        self.assertEqual(valor_total_galoes_e_latas(area_para_pintura=120), 130)
     
    def test_exeptions_ex_dezesseis(self):
        try:
            calculo_uso_litros_tinta(area_para_pintura="120")
        except Exception as d:
            self.assertEqual(d.args[0], "Informe corretamente a metragem que precisas pintar")

        try:
            calculo_uso_litros_tinta(area_para_pintura=-120)
        except Exception as d:
            self.assertEqual(d.args[0], "Metragens menores que zero, não podem ser pintadas")
        
    def test_retorno_mensagem_litros_tintas(self):
        qtd_litros_tinta = 22.0
        self.assertEqual(retorno_mensagem_litros_tintas(qtd_litros_tinta), f"A quantidade de LITROS a serem gastos e de {qtd_litros_tinta}")

    def test_retorno_mensagem_qtds_latas(self):
        qtd_latas_tinta = 2
        self.assertEqual(retorno_mensagem_qtds_latas(qtd_latas_tinta), f"A quantidade de LATAS a serem gastas e de {qtd_latas_tinta}") 

    def test_retorno_mensagem_qtds_galoes(self):
        qtd_galoes_tinta = 7
        self.assertEqual(retorno_mensagem_qtds_galoes(qtd_galoes_tinta), f"A quantidade de LATAS a serem gastas e de {qtd_galoes_tinta}")

    def test_retorno_mensagem_qtd_latas_e_galoes(self):
        qtd_latas_e_galoes = (1, 2)
        self.assertEqual(retorno_mensagem_qtd_latas_e_galoes(qtd_latas_e_galoes), f"A quantidade de LATAS e GALOES a serem gastas e de {qtd_latas_e_galoes}, respectivamente")

    def test_retorno_mensagem_preco_total_latas_tintas(self):
        preco_total_latas_tintas = 160
        self.assertEqual(retorno_mensagem_preco_total_latas_tintas(preco_total_latas_tintas), f"O valor total a ser gasto com LATAS de tinta e de R$ {preco_total_latas_tintas}")

    def test_retorno_mensagem_preco_total_galoes_tintas(self):
        preco_total_galoes_tintas = 175
        self.assertEqual(retorno_mensagem_preco_total_galoes_tintas(preco_total_galoes_tintas), f"O valor total a ser gasto com GALOES de tinta e de R$ {preco_total_galoes_tintas}")

    def test_retorno_mensagem_preco_total_latas_e_galoes(self):
        preco_total_tintas_latas_e_galoes = 160
        self.assertEqual(retorno_mensagem_preco_total_latas_e_galoes(preco_total_tintas_latas_e_galoes), f"O valor total a ser gasto comprando LATAS e GALOES e de R$ {preco_total_tintas_latas_e_galoes}")    