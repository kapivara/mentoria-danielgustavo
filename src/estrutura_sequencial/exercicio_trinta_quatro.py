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

def exceptions_validations(variable_a, variable_b, variable_c):
    if not isinstance(variable_a, (float, int)):
        raise Exception ("Digite numeros válidos por favor!!!")
    
    if not isinstance(variable_b, (float, int)):
        raise Exception ("Digite numeros válidos por favor!!!")
    
    elif not isinstance(variable_c, (float, int)):
        raise Exception("Digite numeros válidos por favor!!!")
    
def is_calculation_equation(variable_a, variable_b, variable_c):

def main():
    variable_a = float(input("Digite o valor de A: "))
    variable_b = float(input("Digite o valor de B: "))
    variable_c = float(input("Digite o valor de C: "))

    valations_variables = exceptions_validations(variable_a, variable_b, variable_c)

    result_equation = is_calculation_equation(variable_a, variable_b, variable_c)

main()