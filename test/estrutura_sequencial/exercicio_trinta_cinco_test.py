import unittest
from src.estrutura_sequencial.exercicio_trinta_cinco import is_validations_exeptions, is_validation_date

class TestExercicioTrintaCinco(unittest.TestCase):
    def test_return_mensage_is_validation_date(self):
        self.assertEqual(is_validation_date(date_user="11/12/2023"), "Nice!!!, your date is valid!!!\n")
        self.assertEqual(is_validation_date(date_user="11-12-2023"), "Nice!!!, your date is valid!!!\n")
        self.assertEqual(is_validation_date(date_user="2023/12/11"), "Nice!!!, your date is valid!!!\n")
        self.assertEqual(is_validation_date(date_user="2023-12-11"), "Nice!!!, your date is valid!!!\n")
        self.assertEqual(is_validation_date(date_user="11122023"), "Your date is not valid!!!")
        self.assertEqual(is_validation_date(date_user="daniel"), "Your date is not valid!!!")

    def test_is_validations_exeptions(self):
        try:
            is_validations_exeptions(date_user="11/12/2023")
        except Exception as d:
            self.assertEqual(d.args[0], "Everything ok, let's proceed!!!\n")

        try:
            is_validations_exeptions(date_user="11-12-2023")
        except Exception as d:
            self.assertEqual(d.args[0], "Everything ok, let's proceed!!!\n")

        try:
            is_validations_exeptions(date_user="2023/12/11")
        except Exception as d:
            self.assertEqual(d.args[0], "Everything ok, let's proceed!!!\n")

        try:
            is_validations_exeptions(date_user="2023-12-11")
        except Exception as d:
            self.assertEqual(d.args[0], "Everything ok, let's proceed!!!\n")

        try:
            is_validations_exeptions(date_user="11122023")
        except Exception as d:
            self.assertEqual(d.args[0], "Invalid input: Please enter a valid date in format, or your date is not valid!!!\n")
        
        try:
            is_validations_exeptions(date_user="daniel")
        except Exception as d:
            self.assertEqual(d.args[0], "Invalid input: Please enter a valid date in format, or your date is not valid!!!\n")
