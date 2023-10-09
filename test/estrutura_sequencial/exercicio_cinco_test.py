import unittest
from src.estrutura_sequencial.exercicio_cinco import imprime_conversao, calcula_conversao

class TestExerciocioQuatro(unittest.TestCase):
    def test_mensagem(self):
        conversao = 10
        medida_em_metros = 1
        self.assertEqual(imprime_conversao(medida_em_metros, conversao), f"{medida_em_metros} metro(s), convertido(s) são {conversao} centimetros.")

    def test_calcula_conversao(self):
        self.assertEqual(calcula_conversao(medida_em_metros=4),400)
        self.assertEqual(calcula_conversao(medida_em_metros=10),1000)
        self.assertEqual(calcula_conversao(medida_em_metros=33),3300)

    def test_validacoes_conversao(self):
        try:
            calcula_conversao(medida_em_metros="10")
        except Exception as e:
            self.assertEqual(e.args[0], "Por favor, digite um numero valido")

        try:
            calcula_conversao(medida_em_metros=5.8)
        except Exception as e:
            self.assertEqual(e.args[0], "Por favor, digite um numero valido")

        try:
            calcula_conversao(medida_em_metros=0)
        except Exception as e:
            self.assertEqual(e.args[0], "Impossível converter zero, você deve digitar um numero maior que zero")

        try:
            calcula_conversao(medida_em_metros=-10)
        except Exception as e:
            self.assertEqual(e.args[0], "Por favor, digite um numero positivo")
            

if __name__ == "main":
    unittest.main()
