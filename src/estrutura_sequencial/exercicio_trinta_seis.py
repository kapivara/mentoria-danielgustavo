"""
Faça um Programa para um caixa eletrônico.

O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas.#38

As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de
10 reais e o máximo de 600 reais. O programa não deve se preocupar com a
quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de
100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de
100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

def is_amount_validation(withdrawal_amount):
    if type(withdrawal_amount) != int:
        raise ValueError ("Sorry, this bank's teller doesn't work with cents!!!\n")
        
    elif withdrawal_amount < 0:
        return ValueError ("\nWe cannot provide negative values\n")
        
    else:
        return "\nEverything ok, we are separating your money\n"

def is_money_separate(withdrawal_amount):
    if withdrawal_amount < 10 or withdrawal_amount > 600:
        return "\nThe requested amount cannot be withdrawn, please choose an amount between 10 and 600 dollars\n"

    notes_avaible = [100, 50, 10, 5, 1]
    result = []

    for notes in notes_avaible:
        notes_amount = withdrawal_amount // notes
        if notes_amount > 0:
            result.append(f"{notes_amount} note's ${notes}")
            withdrawal_amount %= notes
    
    return result 

def main():
    withdrawal_amount = int(input("\nWhat amount do you want to withdraw? "))

    amount_validations = is_amount_validation(withdrawal_amount)

    result_amount = is_money_separate(withdrawal_amount)

    print(amount_validations)

    if isinstance(result_amount, str):
        print(result_amount)

    else:
        print ("\nSuccessful Withdrawal\n")
        for notes in result_amount:
            print (notes)

if __name__ == "__main__":
    main()
