"""
Faça um Programa que peça dois números e imprima a soma.
"""

def imprime_resultado(soma):
    return f"A soma de N1 + N2 e de {soma}"

def main():
    N1 = input("Digite aqui o primeiro número: ")
    N2 = input("Digite aqui o segundo número: ")
    soma = N1 + N2
    mensagem = imprime_resultado(soma)
    print(mensagem)
