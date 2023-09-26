"""
Faça um Programa que peça um número e então mostre a mensagem
O número informado foi [número tal].
"""

def imprime_numero(numero):
    return f"O número informado foi {numero}."

def main():
    numero = input("Digite aqui um número: ")
    mensagem = imprime_numero(numero)
    print(mensagem)
    return mensagem

#chamada da função principal
#main()