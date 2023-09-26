import unittest
from src.estrutura_sequencial.exercicio_dois import imprime_numero

class TestExercicioDois(unittest.TestCase):
  def test_mensagem(self):
    numero = 5
    self.assertEqual(imprime_numero(numero), f"O número informado foi {numero}.")

if __name__ == '__main__':
    unittest.main()
