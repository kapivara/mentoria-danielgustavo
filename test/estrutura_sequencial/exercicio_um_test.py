import unittest
from src.estrutura_sequencial.exercicio_um import main

class TestExercicioUm(unittest.TestCase):
  def test_mensagem(self):
    self.assertEqual(main(), "Alo mundo")

if __name__ == '__main__':
    unittest.main()
