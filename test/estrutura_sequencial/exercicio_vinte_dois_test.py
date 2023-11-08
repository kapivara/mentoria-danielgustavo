import unittest
from src.estrutura_sequencial.exercicio_vinte_dois import calcula_nota_media, mensagem_aprovado_reprovado

class TestExercicioVinte(unittest.TestCase):
    def test_calcula_nota_media(self):
        self.assertEqual(calcula_nota_media(nota_um=10, nota_dois=10),10)
        self.assertEqual(calcula_nota_media(nota_um=5.2, nota_dois=3.4), 4.3)

    def test_mensagem_aprovado_reprovado(self):
        self.assertEqual(mensagem_aprovado_reprovado(nota_media=10), "Aluno APROVADO COM DISTINÇÃO!!!")
        self.assertEqual(mensagem_aprovado_reprovado(nota_media=8.5), "Aluno APROVADO!!!")
        self.assertEqual(mensagem_aprovado_reprovado(nota_media=8), "Aluno APROVADO!!!")
        self.assertEqual(mensagem_aprovado_reprovado(nota_media=5), "Aluno Reprovado!!!")
        self.assertEqual(mensagem_aprovado_reprovado(nota_media=5.2), "Aluno Reprovado!!!")

    def test_exeptions_exercicio_vinte_dois(self):
        try:
            calcula_nota_media(nota_um=-5, nota_dois=7)
        except Exception as f:
            self.assertEqual(f.args[0], "A nota não pode ser negativa!!!")

        try:
            calcula_nota_media(nota_um=5, nota_dois=-7)
        except Exception as f:
            self.assertEqual(f.args[0], "A nota não pode ser negativa!!!")

        try:
            calcula_nota_media(nota_um="10", nota_dois=5)
        except Exception as f:
            self.assertEqual(f.args[0], "As notas devem ser numeros!!!")

        try:
            calcula_nota_media(nota_um=3, nota_dois="10")
        except Exception as f:
            self.assertEqual(f.args[0], "As notas devem ser numeros!!!")

