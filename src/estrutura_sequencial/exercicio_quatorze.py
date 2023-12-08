"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês
#16

Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a descrição abaixo:
( + ) Salário Bruto : R$
( - ) IR (11%) : R$
( - ) INSS (8%) : R$
( - ) Sindicato ( 5%) : R$
( = ) Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido."""

def calcula_salario_bruto(valor_hora, horas_trabalhadas):
    if not isinstance(valor_hora, (float, int)):
        raise Exception ("Informe o valor correto da sua hora de trabalho!!!!")
    
    elif not isinstance(horas_trabalhadas, (float, int)):
        raise Exception ("Informe o valor correto da quantidade de horas trabalhadas!!!!")
    
    elif valor_hora < 0:
        raise Exception ("O valor da hora não pode ser negativo")
    
    elif horas_trabalhadas < 0:
        raise Exception ("O valor da hora não pode ser negativo")

    salario_bruto = valor_hora * horas_trabalhadas
    
    return salario_bruto

def calcula_imposto_de_renda(salario_bruto):
    if not isinstance(salario_bruto, (float, int)):
        raise Exception ("Algo está errado, por favor revise os dados")
    
    elif salario_bruto < 0:
        return(f"Com salário abaixo de zero, você não precisa pagar IR!!!")
    
    imposto_de_renda = salario_bruto * 0.11
    
    return imposto_de_renda

def calcula_inss(salario_bruto):
    if not isinstance(salario_bruto, (float, int)):
        raise Exception ("Algo está errado, por favor revise os dados")
    
    elif salario_bruto < 0:
        return(f"Com salário abaixo de zero, você não precisa pagar INSS!!!")

    inss = salario_bruto * 0.08

    return inss 

def calcula_imposto_sindical(salario_bruto):
    if not isinstance(salario_bruto, (float, int)):
        raise Exception ("Algo está errado, por favor revise os dados")
    
    elif salario_bruto < 0:
        return(f"Com salário abaixo de zero, você não precisa pagar Imposto Sindical!!!")

    imposto_sindical = salario_bruto * 0.05

    return imposto_sindical

def calcula_salario_liquido(salario_bruto, imposto_de_renda, inss, imposto_sindical):
    if not isinstance(salario_bruto, (float, int)):
        raise Exception ("Algo está errado, por favor revise os dados")
    
    elif salario_bruto < 0:
        return(f"Com salário abaixo de zero, você não precisa pagar Imposto Sindical!!!")
    
    salario_liquido = salario_bruto - imposto_de_renda - inss - imposto_sindical

    return salario_liquido

def mensagem_mostra_salario_bruto(salario_bruto):
    return (f"Seu salário bruto e de R$ {salario_bruto}")

def mensagem_retorno_imposto_de_renda(imposto_de_renda):
    return (f"Você pagou R$ {imposto_de_renda} de Imposto de Renda")

def mensagem_retorno_inss(imposto_inss):
    return (f"Você pagou R$ {imposto_inss} de INSS")

def mensagem_retorno_imposto_sindical(imposto_sindical):
    return (f"Você pagou R$ {imposto_sindical} de Imposto Sindical")

def mensagem_mostra_salario_liquido(salario_liquido):
    return (f"Seu salário liquido e de R$ {salario_liquido}")

def main():
    valor_hora = float(input("Qual valor da sua hora de trabalho? "))
    horas_trabalhadas = float(input("Quantas horas trabalhou esse mês? "))
    salario_bruto = calcula_salario_bruto(valor_hora, horas_trabalhadas)
    imposto_de_renda = calcula_imposto_de_renda(salario_bruto)
    inss = calcula_inss(salario_bruto)
    imposto_sindical = calcula_imposto_sindical(salario_bruto)
    salario_liquido = calcula_salario_liquido(salario_bruto, imposto_de_renda, inss, imposto_sindical)

    retorno_mensagem_salario_bruto = mensagem_mostra_salario_bruto(salario_bruto)
    retorno_imposto_de_renda = mensagem_retorno_imposto_de_renda(imposto_de_renda)
    retorno_inss = mensagem_retorno_inss(inss)
    retorno_imposto_sindical = mensagem_retorno_imposto_sindical(imposto_sindical)
    retorno_salario_liquido = mensagem_mostra_salario_liquido(salario_liquido)

    print(retorno_mensagem_salario_bruto)
    print(retorno_imposto_de_renda)
    print(retorno_inss)
    print(retorno_imposto_sindical)
    print(retorno_salario_liquido)

#main()
