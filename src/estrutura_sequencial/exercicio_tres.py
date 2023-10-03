"""
Faça um Programa que peça dois números e imprima a soma.
"""

def imprime_resultado(resultado):
    return f"A soma de N1 + N2 e de {resultado}"

def soma_numero(numero_um, numero_dois):
    if type(numero_um) != int:
        raise Exception("O primeiro número não é um inteiro")
    
    if type(numero_dois) != int:
        raise Exception("O segundo número não é um inteiro")
    
    return numero_um + numero_dois
    
def main():
    numero_um = input("Digite aqui o primeiro número: ")
    numero_dois = input("Digite aqui o segundo número: ")
    resultado = soma_numero(numero_um, numero_dois)
    mensagem = imprime_resultado(resultado)
    print(mensagem)
