import unittest

from src.estrutura_sequencial.exercicio_quarenta import process

class TestExercicioQuarenta(unittest.TestCase):
    def test_process(self):
        scenarios = [
            (326, "3 centenas, 2 dezenas e 6 unidades"),
            (300, "3 centenas, 0 dezenas e 0 unidades"),
            (100, "1 centena, 0 dezenas e 0 unidades"),
            (320, "3 centenas, 2 dezenas e 0 unidades"),
            (310, "3 centenas, 1 dezena e 0 unidades"),
            (305, "3 centenas, 0 dezenas e 5 unidades"),
            (301, "3 centenas, 0 dezenas e 1 unidade"),
            (101, "1 centena, 0 dezenas e 1 unidade"),
            (311, "3 centenas, 1 dezena e 1 unidade"),
            (111, "1 centena, 1 dezena e 1 unidade"),
            (25, "2 dezenas e 5 unidades"),
            (20, "2 dezenas e 0 unidades"),
            (10, "1 dezena e 0 unidades"),
            (21, "2 dezenas e 1 unidade"),
            (11, "1 dezena e 1 unidade"),
            (1, "1 unidade"),
            (7, "7 unidades"),
            (16, "1 dezena e 6 unidades"),
        ]

        for scenario in scenarios:
            self.assertEqual(process(scenario[0]), scenario[1])