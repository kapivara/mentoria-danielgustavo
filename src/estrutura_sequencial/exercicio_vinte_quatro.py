"""
Faça um Programa que leia três números e mostre o maior e o menor deles.#26
"""

print("\n Digite três numeros para saber qual deles e maior e qual e o menor!!!\n")

def main():
    primeiro_numero = float(input("Digite o primeiro numero: "))
    segundo_numero = float(input("Digite o segundo numero:"))
    terceiro_numero = float(input("Digite o terceiro numero:"))

    maior_numero = analisa_maior_numero(primeiro_numero, segundo_numero, terceiro_numero)
    menor_numero = analisa_menor_numero(primeiro_numero, segundo_numero, terceiro_numero)

    mensagem_retorno_maior_numero = mensagem_maior_numero(maior_numero)
    mensagem_retorno_menor_numero = mensagem_menor_numero(menor_numero)

    print(mensagem_retorno_maior_numero)
    print(mensagem_retorno_menor_numero)

def analisa_maior_numero(primeiro_numero, segundo_numero, terceiro_numero):

    if (type (primeiro_numero) not in (float, int) or type (segundo_numero) not in (float, int) or type (terceiro_numero) not in (float, int)):       
        raise Exception ("A informação forncecida, deve ser um numero")
    
    
    elif primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
        return(primeiro_numero)
    
    elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
        return(segundo_numero)
    
    else:
        return(terceiro_numero)
    
def analisa_menor_numero(primeiro_numero, segundo_numero, terceiro_numero):

    if (type (primeiro_numero) not in (float, int) or type (segundo_numero) not in (float, int) or type (terceiro_numero) not in (float, int)):       
        raise Exception ("A informação forncecida, deve ser um numero")
    
    elif primeiro_numero < segundo_numero and primeiro_numero < terceiro_numero:
        return(primeiro_numero)
    
    elif segundo_numero < primeiro_numero and segundo_numero < terceiro_numero:
        return(segundo_numero)
    
    else:
        return(terceiro_numero)
    
def mensagem_maior_numero(maior_numero):
    return(f" O maior numero digitado foi o {maior_numero}")

def mensagem_menor_numero(menor_numero):
    return(f" O menor numero digitado foi o {menor_numero}")

#main()
