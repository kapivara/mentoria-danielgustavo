import unittest
from src.estrutura_sequencial.exercicio_tres import imprime_resultado, soma_numero

class TestExercicioTres(unittest.TestCase):
  def test_mensagem(self):
    soma = 10
    self.assertEqual(imprime_resultado(soma), f"A soma de N1 + N2 e de {soma}")

  def test_soma(self):
      self.assertEqual(soma_numero(numero_um=5,numero_dois=5), 10)
      self.assertEqual(soma_numero(numero_um=-15,numero_dois=-25), -40)
      self.assertEqual(soma_numero(numero_um=-5,numero_dois=5), 0)

  def test_soma_validacoes(self):
      try: 
         soma_numero(numero_um="5",numero_dois=5)
      except Exception as e:
        self.assertEqual(e.args[0], "O primeiro número não é um inteiro") 

      try: 
         soma_numero(numero_um=5,numero_dois="5")
      except Exception as e:
        self.assertEqual(e.args[0], "O segundo número não é um inteiro") 



if __name__ == '__main__':
    unittest.main()
