import unittest
from src.estrutura_sequencial.exercicio_vinte import identifica_letra

class TestExercicioVinte(unittest.TestCase):
    def test_identifica_letra(self):
        letra_masculino = "M"
        letra_feminino = "F"
        self.assertEqual(identifica_letra(letra_masculino),f"A letra digitada foi {letra_masculino}, e o sexo e MASCULINO")
        self.assertEqual(identifica_letra(letra_feminino), f"A letra digitada foi {letra_feminino}, e o sexo e FEMININO")

    def test_imprime_letra(self):
        letra_feminino = "F"
        letra_masculino = "M"
        self.assertEqual(identifica_letra(letra_feminino), f"A letra digitada foi {letra_feminino}, e o sexo e FEMININO")
        self.assertEqual(identifica_letra(letra_masculino), f"A letra digitada foi {letra_masculino}, e o sexo e MASCULINO")

    def test_exeptions_exercicio_vinte(self):
        try:
            identifica_letra(letra="10")
        except Exception as f:
            self.assertEqual(f.args[0], "Sexo invalido, vc deve digitar 'F' ou 'M'!!!!")

        try:
            identifica_letra(letra="G")
        except Exception as f:
            self.assertEqual(f.args[0], "Sexo invalido, vc deve digitar 'F' ou 'M'!!!!")

        try:
            identifica_letra(letra=10)
        except Exception as f:
            self.assertEqual(f.args[0], "Sexo invalido, vc deve digitar 'F' ou 'M'!!!!")