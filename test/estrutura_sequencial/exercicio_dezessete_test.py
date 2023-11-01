import unittest
from src.estrutura_sequencial.exercicio_dezessete import calcula_tempo_dowload, transformar_tempo_em_minutos, retorno_tempo_para_dowload 

class TestExercicioDezessete(unittest.TestCase):
    def test_calcula_tempo_dowload(self):
        self.assertEqual(calcula_tempo_dowload(velocidade_net=10, tamanho_arquivo=2048), 204.8)
        self.assertEqual(calcula_tempo_dowload(velocidade_net=10.5, tamanho_arquivo=2048.5), 195.0952380952381)

    def test_transformar_tempo_em_minutos(self):
        self.assertEqual(transformar_tempo_em_minutos(tempo_dowload=204.8),3.4133333333333336)
   
    def test_exeptions_ex_dezessete(self):
        try:
            calcula_tempo_dowload(velocidade_net=10, tamanho_arquivo="2048")
        except Exception as d:
            self.assertEqual(d.args[0], "Informe o tamanho correto do arquivo!!!")

        try:
            calcula_tempo_dowload(velocidade_net="10", tamanho_arquivo=2048)
        except Exception as d:
            self.assertEqual(d.args[0], "Informe a velocidade correta da sua net!!!")

        try:
            calcula_tempo_dowload(velocidade_net=-10, tamanho_arquivo=2048)
        except Exception as d:
                self.assertEqual(d.args[0], "A velocidade da sua net não pode ser negativa")
        
        try:
            calcula_tempo_dowload(velocidade_net=10, tamanho_arquivo=-2048)
        except Exception as d:
                self.assertEqual(d.args[0], "O tamanho do arquivo não pode ser negativo")

    def test_retorno_tempo_para_dowload(self):
        tempo_dowload = 33
        self.assertEqual(retorno_tempo_para_dowload(tempo_dowload), f"O tempo aproximado para se findar seu dowload, será de {tempo_dowload} minutos")
