"""
Faça um Programa que leia três números e mostre o maior deles.#25
"""
print("\n Digite três numeros para saber qual deles e maior!!!\n")

def main():
    primeiro_numero = float(input("Digite o primeiro numero: "))
    segundo_numero = float(input("Digite o segundo numero:"))
    terceiro_numero = float(input("Digite o terceiro numero:"))

    maior_numero = analisa_numeros(primeiro_numero, segundo_numero, terceiro_numero)

    mensagem_retorno_maior_numero = mensagem_maior_numero(maior_numero)

    print(mensagem_retorno_maior_numero)

def analisa_numeros(primeiro_numero, segundo_numero, terceiro_numero):

    if not isinstance(primeiro_numero, (float, int)):
        raise Exception ("A informação forncecida, deve ser um numero, primeiro numero")
    
    elif not isinstance(segundo_numero, (float, int)):
        raise Exception ("A informação forncecida, deve ser um numero, segundo numero")
    
    elif not isinstance(terceiro_numero, (float, int)):
        raise Exception ("A informação forncecida, deve ser um numero, terceiro numero")
    
    elif primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
        return(primeiro_numero)
    
    elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
        return(segundo_numero)
    
    else:
        return(terceiro_numero)
    
def mensagem_maior_numero(maior_numero):
    return(f" O maior numero digitado foi o {maior_numero}")

#main()
