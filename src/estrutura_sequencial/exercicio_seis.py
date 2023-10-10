"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
import math

print("\n\n Mensagem importante, o resultado da área do circulo, sera sempre aprensentado em centimetros, por isso, caso sua área seja maior que 100 centimentros, por favor realize a conversão \n\n")

def imprime_area(raio):
    return (f"A área deste circulo e de {raio}, centimetros")

def calcula_area(raio_area):
    if not isinstance(raio_area, (float, int)):
        raise Exception("Por favor, digite a medida da área")
    
    elif(raio_area) < 0:
        raise Exception("A medida da área deve ter um valor positivo")
    
    return (raio_area*raio_area)*math.pi

def main():
    raio = float(input("Digite o valor do raio que desejas calcular: "))
    calculo = calcula_area(raio)
    mensagem = imprime_area(calculo)
    print(mensagem)

main()