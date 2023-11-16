"""
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

import sys

def calculo_aumento_salario(salario_base):
    ranges_salario = [
    (range(0, 281), 20),
    (range(281, 701), 15),
    (range(701, 1501), 10),
    (range(1501, 125000), 5),
]
    for (range_salario, percentual) in ranges_salario:
        if (salario_base in range_salario):
            atualizacao_salario = salario_base + (salario_base *(percentual / 100))
            diferenca = atualizacao_salario - salario_base
            return (f"Seu salário base era de R${salario_base}\nSeu novo salário agora será R${atualizacao_salario:.2f}\nUma diferença de R${diferenca:.2f}")

def main():
    print("\n Abaixo você vai ter acesso ao programa de calculos de aumentos, basta digitar seu salário corretamente para saber quanto de aumento você terá!!!\n")

    try:
        salario_base = int(input("Digite aqui seu salario para saber seu percentual de aumento: "))
    except ValueError:
       print("\nDigite seu salario corretamente!!!!\n")
       sys.exit(1)

    if salario_base < 0:
        raise Exception ("Não podes ter um salario menor que zero!!!")

    salario_atualizado = calculo_aumento_salario(salario_base)

    print(salario_atualizado)

#main()
