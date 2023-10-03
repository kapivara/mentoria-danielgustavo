import unittest
from src.estrutura_sequencial.exercicio_tres import imprime_resultado, soma_numero

class TestExercicioTres(unittest.TestCase):
  def test_mensagem(self):
    soma = 10
    self.assertEqual(imprime_resultado(soma), f"A soma de N1 + N2 e de {soma}")
    self.assertEqual(soma_numero(numero_um=5,numero_dois=5), soma)

if __name__ == '__main__':
    unittest.main()
