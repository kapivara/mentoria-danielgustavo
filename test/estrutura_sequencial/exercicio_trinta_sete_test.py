import unittest
from src.estrutura_sequencial.exercicio_trinta_sete import is_number_validation, is_number_quantification

class TestTestExercicioTrintaSete(unittest.TestCase):
    def test_is_number_validation(self):
        self.assertEqual(is_number_validation(int_number=326), "\nEverything ok!!!\n")
        self.assertEqual(is_number_validation(int_number="326"), "Sorry, but your number needs to be an integer\n")
        self.assertEqual(is_number_validation(int_number=1500), "\nSorry, The number cannot be greater than 1000\n")
        self.assertEqual(is_number_validation(int_number=1000), "\nSorry, The number cannot be greater than 1000\n")

    def test_is_number_quantification(self):
        self.assertEqual(is_number_quantification(int_number=326), f"326 = Your number have a 3 hundreds, 2 dozens and 6 units!!!\n")
        self.assertEqual(is_number_quantification(int_number=300), f"300 = Your number have a 3 hundreds, 0 dozens and 0 units!!!\n")
        self.assertEqual(is_number_quantification(int_number=100), f"100 = Your number have a 1 hundreds, 0 dozens and 0 units!!!\n")
        self.assertEqual(is_number_quantification(int_number=320), f"320 = Your number have a 3 hundreds, 2 dozens and 0 units!!!\n")
        self.assertEqual(is_number_quantification(int_number=310), f"310 = Your number have a 3 hundreds, 1 dozens and 0 units!!!\n")
        self.assertEqual(is_number_quantification(int_number=305), f"305 = Your number have a 3 hundreds, 0 dozens and 5 units!!!\n")
        self.assertEqual(is_number_quantification(int_number=301), f"301 = Your number have a 3 hundreds, 0 dozens and 1 units!!!\n")
        self.assertEqual(is_number_quantification(int_number=101), f"101 = Your number have a 1 hundreds, 0 dozens and 1 units!!!\n")
        self.assertEqual(is_number_quantification(int_number=311), f"311 = Your number have a 3 hundreds, 1 dozens and 1 units!!!\n")
        self.assertEqual(is_number_quantification(int_number=111), f"111 = Your number have a 1 hundreds, 1 dozens and 1 units!!!\n")
        self.assertEqual(is_number_quantification(int_number=25), f"25 = Your number have a 0 hundreds, 2 dozens and 5 units!!!\n")
        self.assertEqual(is_number_quantification(int_number=20), f"20 = Your number have a 0 hundreds, 2 dozens and 0 units!!!\n")
        self.assertEqual(is_number_quantification(int_number=11), f"11 = Your number have a 0 hundreds, 1 dozens and 1 units!!!\n")
        self.assertEqual(is_number_quantification(int_number=1), f"1 = Your number have a 0 hundreds, 0 dozens and 1 units!!!\n")
        self.assertEqual(is_number_quantification(int_number=7), f"7 = Your number have a 0 hundreds, 0 dozens and 7 units!!!\n")
        self.assertEqual(is_number_quantification(int_number=16), f"16 = Your number have a 0 hundreds, 1 dozens and 6 units!!!\n")
