import unittest
from src.estrutura_sequencial.exercicio_vinte_sete import analisa_turno

class TestExercicioVinteSete(unittest.TestCase):
    def test_identifica_letra(self):
        letra_matutino = "M"
        letra_vespertino = "V"
        letra_noturno = "N"
        self.assertEqual(analisa_turno(letra_matutino),f"A letra digitada foi {letra_matutino}, seu turno e o MATUTINO!!!, Bom dia")
        self.assertEqual(analisa_turno(letra_vespertino),f"A letra digitada foi {letra_vespertino}, seu turno e o VESPERTINO!!!, Boa Tarde")
        self.assertEqual(analisa_turno(letra_noturno), f"A letra digitada foi {letra_noturno}, seu turno e o NOTURNO!!!, Boa noite")

    def test_exeptions_exercicio_vinte_sete(self):
        try:
            analisa_turno(turno_aluno_maiusculo="10")
        except Exception as f:
            self.assertEqual(f.args[0], "Digite uma opção válida!!!")

        try:
            analisa_turno(turno_aluno_maiusculo="G")
        except Exception as f:
            self.assertEqual(f.args[0], "Digite uma opção válida!!!")

        try:
            analisa_turno(turno_aluno_maiusculo=10)
        except Exception as f:
            self.assertEqual(f.args[0], "Digite uma opção válida!!!")