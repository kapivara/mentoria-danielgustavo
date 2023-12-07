"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma
ax2 + bx + c.#35

O programa deverá pedir os valores de a, b e c e fazer as consistências,
informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo
grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

*Se o delta calculado for negativo, a equação não possui raizes reais.
Informe ao usuário e encerre o programa;

*Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
informe-a ao usuário;

*Se o delta for positivo, a equação possui duas raiz reais;
informe-as ao usuário;

"""
import math
import sys

def exceptions_validations(variable_a, variable_b, variable_c):
    if not isinstance(variable_a, (float, int)):
        raise Exception ("Digite numeros válidos por favor!!!")
    
    if not isinstance(variable_b, (float, int)):
        raise Exception ("Digite numeros válidos por favor!!!")
    
    elif not isinstance(variable_c, (float, int)):
        raise Exception("Digite numeros válidos por favor!!!")
    
    else:
        return "Tudo ok, podemos prosseguir!!!"
    
def is_analysis_variable_a(variable_a):
        if variable_a == 0:
            print("Essa equação não é do segundo grau, logo, não pode ser calculada nessa função")
            sys.exit()

def is_calculation_equation(variable_a, variable_b, variable_c):
    delta_calculation = variable_b**2 - 4*variable_a*variable_c
    print(delta_calculation)

    if delta_calculation < 0:
        return "Essa equação NÃO POSSUI raizes reais!!!!"

    elif delta_calculation == 0:
        delta_calculation = -variable_b/ (2*variable_a)
        return f"Essa equação possui APENAS uma raiz real: {delta_calculation}"
    
    elif delta_calculation > 0:
        delta_calculation_raiz1 = (-variable_b + math.sqrt(delta_calculation)) / (2*variable_a)
        delta_calculation_raiz2 = (-variable_b - math.sqrt(delta_calculation)) / (2*variable_a)
        return f"Essa equação possui DUAS raizes reais: {delta_calculation_raiz1} e {delta_calculation_raiz2}"

def main():
    variable_a = float(input("Digite o valor de A: "))
    analysis_variables = is_analysis_variable_a(variable_a)

    variable_b = float(input("Digite o valor de B: "))
    variable_c = float(input("Digite o valor de C: "))

    validations_exeptions_variables = exceptions_validations(variable_a, variable_b, variable_c)

    result_equation = is_calculation_equation(variable_a, variable_b, variable_c)

    print(validations_exeptions_variables)
    print(result_equation)

main()
