"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.#28
"""

def main():
    primeiro_numero = float(input("Digite o primeiro numero: "))
    segundo_numero = float(input("Digite o segundo numero:"))
    terceiro_numero = float(input("Digite o terceiro numero:"))

    lista_numeros = organiza_numeros_decrecente(primeiro_numero, segundo_numero, terceiro_numero)

    mensagem_retorno_numeros_decrecente = mensagem_numeros_decrecentes(lista_numeros)

    print(mensagem_retorno_numeros_decrecente)

def organiza_numeros_decrecente(primeiro_numero, segundo_numero, terceiro_numero):

    if (type (primeiro_numero) not in (float, int) or type (segundo_numero) not in (float, int) or type (terceiro_numero) not in (float, int)):       
        raise Exception ("A informação forncecida, deve ser um numero")
    
    lista_numeros = [primeiro_numero, segundo_numero, terceiro_numero]
    
    lista_numeros.sort(reverse=True)

    return lista_numeros
    
def mensagem_numeros_decrecentes(lista_numeros):
    return(f" O maior numero digitado foi o {lista_numeros}")

#main()
