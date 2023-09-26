import unittest
from exercicio_dois import main, imprime_numero

class TestExercicioDois(unittest.TestCase):
  def test_mensagem(self):
    self.assertEqual(main())
    self.assertEqual(imprime_numero())

if __name__ == '__main__':
    unittest.main()