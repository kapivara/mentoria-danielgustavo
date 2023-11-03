"""
Faça um Programa que peça um valor e mostre na tela
se o valor é positivo ou negativo.#22
"""

print("\nCaro usuário, esse programa que estas prestes a usar, tem como função analisar seu numero, e lhe informar se ele e positivo ou neganito!!!!!\n")

def main():
    numero = float(input("Digite aqui o numero: "))

    resultado_analise = analisa_numero(numero)

    print (imprime_numero(resultado_analise))

def analisa_numero(numero):
    if not isinstance(numero, (float, int)):
        raise Exception ("Por favor, digite um numero correto!!!")
    
    elif numero == 0:
        raise Exception ("Zero e um numero neutro")
    
    elif numero > 0:
        return (f"O numero {numero} e positivo!!!")
    
    elif numero < 0:
        return (f"O numero {numero} e negativo!!!")
      
def imprime_numero(resultado_analise):
    return (resultado_analise)

#main()
