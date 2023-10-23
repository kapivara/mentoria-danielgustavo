"""
Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.#9
"""

def converte_temperatura(temperatura_Fahrenheit):
    
    if not isinstance(temperatura_Fahrenheit, (float, int)):
        raise Exception("Digite uma termperatura válida")

    temperatura_celsius = (5/9) * (temperatura_Fahrenheit-32) 

    return temperatura_celsius

def imprime_temperatura(temperatura_celsius):
     return((f"A temperatura em graus celsius e de {temperatura_celsius}."))

def main():
    temperatura_Fahrenheit = float(input("Qual temperatura desejas converter em celsius? "))
    temperatura_celsius = converte_temperatura(temperatura_Fahrenheit)
    mensagem = imprime_temperatura(temperatura_celsius)
    return(mensagem)

#main()