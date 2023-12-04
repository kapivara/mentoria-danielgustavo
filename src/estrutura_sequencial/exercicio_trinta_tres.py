"""
Faça um Programa que peça um número correspondente a um determinado ano e em
seguida informe se este ano é ou não bissexto.#36
"""

def validations_excepitons_year(year):
    if type(year) != int:
        raise Exception("\nDigite o ano corretamente, os formatos aceitos são 'XXXX' ")
     
    elif year < 0:
        raise Exception("Não pode haver anos menores que zero, por favor, digite um ano válido!!!")

    else:
        return f"O ano {year} e um ano com formato válido!!!"

def validation_bissext_yaer(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    
    else:
        return False
    
def bissext_mensage_year(year):
    return_mensage = validation_bissext_yaer(year)
    if return_mensage:
        return f"{year}, e um ano bissexto!!!"
    
    else:
        return f"{year}, não e um ano bissexto!!!"

def main():
    year = int(input("Digite um ano para saber se ele e bissexto: "))

    year_validations = validations_excepitons_year(year)

    bissext_definition = validation_bissext_yaer(year)

    return_mensage_year_bissext = bissext_mensage_year(year)

    print(year_validations)
    print(bissext_definition)
    print(return_mensage_year_bissext)

main()