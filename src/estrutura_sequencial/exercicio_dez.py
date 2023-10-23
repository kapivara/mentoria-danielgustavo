"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e
mostre em graus Fahrenheit.#10
"""

def converte_temperatura(temperatura_celsius):
    
    if not isinstance(temperatura_celsius, (float, int)):
        raise Exception("Digite uma termperatura válida")

    temperatura_Fahrenheit = (temperatura_celsius * 9/5) + 32 

    return temperatura_Fahrenheit


def imprime_temperatura(temperatura_fahrenheit):
     return((f"A temperatura em graus fahrenheit e de {temperatura_fahrenheit}."))

def main():
    temperatura_celsius = float(input("Qual temperatura desejas converter em fahrenheit? "))
    temperatura_fahrenheit = converte_temperatura(temperatura_celsius)
    mensagem = imprime_temperatura(temperatura_fahrenheit)
    return(mensagem)

#main()