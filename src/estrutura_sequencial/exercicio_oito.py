"""
Faça um Programa que pergunte quanto você ganha por hora e o número de
horas trabalhadas no mês. Calcule e mostre o total do seu salário no
referido mês.#8
"""        

def calcula_salario_final(valor_hora, horas_trabalhadas):

    if not isinstance(valor_hora, (float, int)):
        raise Exception ("Digite o 'VALOR' de cada hora trabalhada!!!!")
    
    elif valor_hora < 0:
        raise Exception ("O valor da hora de trabalho não pode ser negativo!!!!")
    
    elif not isinstance(horas_trabalhadas, (float, int)):
        raise Exception ("Digite a quantidade de 'HORAS' trabalhadas!!!!")
    
    elif horas_trabalhadas < 0:
        raise Exception ("A quantidad de horas de trabalho não pode ser negativo!!!!")
       

    salario_final = valor_hora * horas_trabalhadas

    return salario_final

def imprime_salario(salario_final):
     return ((f" O seu salario no fim do mês, será de R$ {salario_final}."))

def main():
    valor_hora = float(input("Qual valor da sua hora de trabalho ? "))
    horas_trabalhadas = float(input("Quantas horas você trabalhou esse mês ? "))
    valor_salario = calcula_salario_final(valor_hora, horas_trabalhadas)
    mensagem = imprime_salario(valor_salario)
    return(mensagem)

#main()
