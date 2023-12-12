import unittest
from src.estrutura_sequencial.exercicio_trinta_seis import is_amount_validation, is_money_separate

class TestExercicioTrintaCinco(unittest.TestCase):
    def test_is_money_separate(self):
        self.assertEqual(is_money_separate(withdrawal_amount=256), ["2 note's $100", "1 note's $50", "1 note's $5", "1 note's $1"])
        self.assertEqual(is_money_separate(withdrawal_amount=399), ["3 note's $100", "1 note's $50", "4 note's $10", "1 note's $5", "4 note's $1"])
        self.assertEqual(is_money_separate(withdrawal_amount=555), ["5 note's $100", "1 note's $50", "1 note's $5"])
        self.assertEqual(is_money_separate(withdrawal_amount=650), "\nThe requested amount cannot be withdrawn, please choose an amount between 10 and 600 dollars\n")
        self.assertEqual(is_money_separate(withdrawal_amount=5), "\nThe requested amount cannot be withdrawn, please choose an amount between 10 and 600 dollars\n")
    def test_is_validations_exeptions(self):
        try:
            is_amount_validation(withdrawal_amount=399.50)
        except Exception as d:
            self.assertEqual(d.args[0], "Sorry, this bank's teller doesn't work with cents!!!\n")

        try:
            is_amount_validation(withdrawal_amount=-399)
        except Exception as d:
            self.assertEqual(d.args[0], "\nWe cannot provide negative values\n")

        try:
            is_amount_validation(withdrawal_amount=399)
        except Exception as d:
            self.assertEqual(d.args[0], "\nEverything ok, we are separating your money\n")
