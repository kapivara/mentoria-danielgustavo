"""
Sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.

O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.

No exemplo o valor da hora é 5 e a quantidade de hora é 220.

Descrição	Valor
Salário Bruto: (5 * 220)	R$ 1100,00
(-) IR (5%)	                R$ 55,00
(-) INSS ( 10%)	            R$ 110,00
FGTS (11%)	                R$ 121,00
Total de descontos	        R$ 165,00
Salário Liquido	            R$ 935,00
"""

import sys

def main():
    valor_hora_trabalhada = int(input("Qual valor da hora da sua hora de trabalho?"))
    qtd_horas_trabalhadas = int(input("Quantas horas de trabalho você teve esse mês?"))

    salario_liquido = calcula_salario_liquido(valor_hora_trabalhada, qtd_horas_trabalhadas)
    print(salario_liquido)

def analise_exeptions(valor_hora, horas_trabalhadas):

    if not isinstance(valor_hora, (float, int)):
        raise Exception ("Digite o 'VALOR' de cada hora trabalhada!!!!")

    elif valor_hora < 0:
        raise ValueError ("O valor da hora de trabalho não pode ser negativo!!!!")

    elif not isinstance(horas_trabalhadas, (float, int)):
        raise ValueError ("Digite a quantidade de 'HORAS' trabalhadas!!!!")

    elif horas_trabalhadas < 0:
        raise ValueError ("A quantidad de horas de trabalho não pode ser negativo!!!!")

def calcula_salario_liquido(valor_hora, horas_trabalhadas):

    ranges_salario = [
        (range(0, 901), 0, 10, 11),
        (range(901, 1501), 5, 10, 11),
        (range(1501, 2501), 10, 10, 11),
        (range(2501, 125000), 20, 10, 11),]
    
    salario_bruto = valor_hora * horas_trabalhadas
    
    for (range_salario, percentual_ir, percentual_inss, percentual_fgts) in ranges_salario:
        if (salario_bruto in range_salario):
            salario_liquido = salario_bruto - (percentual_ir, percentual_inss, percentual_fgts / 100)
            total_descontos = (percentual_ir + percentual_inss + percentual_fgts) / 100
            return (f"Seu salário bruto e de R${salario_bruto}\nDesconto IR = R${percentual_ir:.2f}\nDesconto INSS R${percentual_inss:.2f}\nDesconto FGTS {percentual_fgts}\nO total de descontos foi de R${total_descontos}\nSeu salario liquido e R${salario_liquido}")

main()
