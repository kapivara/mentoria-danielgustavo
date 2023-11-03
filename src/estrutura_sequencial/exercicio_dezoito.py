"""
Faça um Programa que peça dois números e imprima o maior deles.#21
"""
print("Caro usuário, esse programa que estas prestes a usar, tem como função imprimir o maior dos dois numeros digitado por vocês, divirta-se!!!!!")

def main():
    numero_um = float(input("Digite o primeiro numero: "))
    numero_dois = float(input("Digite o segundo numero: "))

    maior_numero = analisa_maior_numero(numero_um, numero_dois)

    print (imprime_maior_numero(maior_numero))

def analisa_maior_numero(numero_um, numero_dois):
    if not isinstance(numero_um, (float, int)):
        raise Exception ("Por favor, digite um numero correto!!!")
    
    elif not isinstance(numero_dois, (float, int)):
        raise Exception ("Por favor, digite um numero correto!!!")
    
    if numero_um > numero_dois:
     return numero_um
    
    else:
       return numero_dois
    
def imprime_maior_numero(maior_numero):
   return (f"o maior dos numeros digitados foi o {maior_numero}")

#main()
