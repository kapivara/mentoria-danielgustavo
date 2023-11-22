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
    valor_hora_trabalhada = float(input("Qual valor da hora da sua hora de trabalho? "))
    qtd_horas_trabalhadas = float(input("Quantas horas de trabalho você teve esse mês? "))

    try:
        analise_exeptions(valor_hora_trabalhada, qtd_horas_trabalhadas)
        resultado = calcula_salario_liquido(valor_hora_trabalhada, qtd_horas_trabalhadas)
        print(resultado)
    except Exception as e:
        print(f"Erro: {e}")

    valor_salario_bruto = calcula_salario_bruto(valor_hora_trabalhada,qtd_horas_trabalhadas)
    valor_percentual_ir = calcula_valores_impostos_ir(valor_salario_bruto)
    valor_percentual_inss = calcula_valores_impostos_inss(valor_salario_bruto)
    valor_percentual_fgts = calcula_valores_impostos_fgts(valor_salario_bruto)

    valor_total_descontos = calcula_valor_total_impostos(valor_salario_bruto, valor_percentual_inss, valor_percentual_fgts)

    valor_salario_liquido = calcula_salario_liquido(valor_salario_bruto, valor_percentual_ir, valor_percentual_inss, valor_percentual_fgts)
    
    mensagem_retorno = retorna_mensagem_salario_liquido(valor_salario_bruto, valor_percentual_ir, valor_percentual_inss, valor_percentual_fgts, valor_total_descontos, valor_salario_liquido)
    print(mensagem_retorno
          )
def analise_exeptions(valor_hora, horas_trabalhadas):

    if not isinstance(valor_hora, (float, int)):
        raise Exception ("Digite o 'VALOR' de cada hora trabalhada!!!!")

    elif valor_hora < 0:
        raise ValueError ("O valor da hora de trabalho não pode ser negativo!!!!")

    elif not isinstance(horas_trabalhadas, (float, int)):
        raise Exception ("Digite a quantidade de 'HORAS' trabalhadas!!!!")

    elif horas_trabalhadas < 0:
        raise ValueError ("A quantidade de horas de trabalho não pode ser negativa!!!!")

def calcula_salario_bruto(valor_hora, horas_trabalhadas):

    salario_bruto = valor_hora * horas_trabalhadas

    return salario_bruto            

def calcula_valores_impostos_ir(salario_bruto):
    ranges_salarios = [
        (range(0, 901), 0),
        (range(901, 1501), 5),
        (range(1501, 2501), 10),
        (range(2501, 10000000000), 20),
        ]
    
    for (range_salario, percentual_ir) in ranges_salarios:
        if salario_bruto >= range_salario.start and salario_bruto < range_salario.stop:
            valor_percentual_ir = salario_bruto*(percentual_ir/100)

            return valor_percentual_ir
        
def calcula_valores_impostos_inss(salario_bruto):
    ranges_salarios = [
        (range(0, 901), 10),
        (range(901, 1501), 10),
        (range(1501, 2501), 10),
        (range(2501, 10000000000), 10),
        ]
    
    for (range_salario, percentual_inss) in ranges_salarios:
        if salario_bruto >= range_salario.start and salario_bruto < range_salario.stop:
            valor_percentual_inss = salario_bruto*(percentual_inss/100)

            return valor_percentual_inss

def calcula_valores_impostos_fgts(salario_bruto):
    ranges_salarios = [
        (range(0, 901), 11),
        (range(901, 1501), 11),
        (range(1501, 2501), 11),
        (range(2501, 10000000000), 11),
        ]
    
    for (range_salario, percentual_fgts) in ranges_salarios:
        if salario_bruto >= range_salario.start and salario_bruto < range_salario.stop:
            valor_percentual_fgts = salario_bruto*(percentual_fgts/100)

            return valor_percentual_fgts

def calcula_salario_liquido(salario_bruto, valor_percentual_ir, valor_percentual_inss, valor_percentual_fgts):

    ranges_salarios = [
        (range(0, 901), 0, 10, 11),
        (range(901, 1501), 5, 10, 11),
        (range(1501, 2501), 10, 10, 11),
        (range(2501, 10000000000), 20, 10, 11),
        ]

    for (range_salario, percentual_ir, percentual_inss, percentual_fgts) in ranges_salarios:
        if salario_bruto >= range_salario.start and salario_bruto < range_salario.stop:
            valor_percentual_ir = salario_bruto*(percentual_ir/100)
            valor_percentual_inss = salario_bruto*(percentual_inss/100)
            valor_percentual_fgts = salario_bruto*(percentual_fgts/100)

            salario_liquido = salario_bruto - (valor_percentual_ir + valor_percentual_inss + valor_percentual_fgts)

            return salario_liquido
        
def calcula_valor_total_impostos(salario_bruto, valor_percentual_ir, valor_percentual_inss, valor_percentual_fgts):
    ranges_salarios = [
        (range(0, 901), 0, 10, 11),
        (range(901, 1501), 5, 10, 11),
        (range(1501, 2501), 10, 10, 11),
        (range(2501, 10000000000), 20, 10, 11),
        ]

    for (range_salario, percentual_ir, percentual_inss, percentual_fgts) in ranges_salarios:
        if salario_bruto >= range_salario.start and salario_bruto < range_salario.stop:
            valor_percentual_ir = salario_bruto*(percentual_ir/100)
            valor_percentual_inss = salario_bruto*(percentual_inss/100)
            valor_percentual_fgts = salario_bruto*(percentual_fgts/100)

            valor_total_impostos = valor_percentual_ir + valor_percentual_inss + valor_percentual_fgts

            return valor_total_impostos


def retorna_mensagem_salario_liquido(salario_bruto, valor_percentual_ir, valor_percentual_inss, valor_percentual_fgts, total_descontos, salario_liquido):
    return f"Seu salário bruto e de R${salario_bruto}\nDesconto IR = R${valor_percentual_ir:.2f}\nDesconto INSS R${valor_percentual_inss:.2f}\nDesconto FGTS {valor_percentual_fgts:.2f}\nO total de descontos foi de R${total_descontos:.2f}\nSeu salario liquido e R${salario_liquido:.2f}"



main()
