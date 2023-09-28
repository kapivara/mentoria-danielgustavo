import unittest
from src.estrutura_sequencial.exercicio_tres import imprime_resultado

class TestExercicioTres(unittest.TestCase):
  def test_mensagem(self):
    soma = 10
    self.assertEqual(imprime_resultado(soma), f"A soma de N1 + N2 e de {soma}.")

if __name__ == '__main__':
    unittest.main()