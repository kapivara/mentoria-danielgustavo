"""
Faça um Programa que peça 2 números inteiros e um número real.#11
Calcule e mostre:

o produto do dobro do primeiro com metade do segundo.
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""

def calcula_produto_primeiro_numero(primeiro_numero_inteiro, segundo_numero_inteiro):
    if type(primeiro_numero_inteiro) != int:
        raise Exception ("O primeiro número não é um inteiro")
    
    elif type(segundo_numero_inteiro) != int:
        raise Exception("O segundo número não é um inteiro")
    
    resultado = (2 * primeiro_numero_inteiro) * (segundo_numero_inteiro / 2)
    return resultado

def soma_triplo_primeiro_terceiro(primeiro_numero_inteiro, numero_real):
    if type(primeiro_numero_inteiro) != int:
        raise Exception ("O primeiro número não é um inteiro")
    
    if not isinstance(numero_real, (float, int)):
        raise Exception("Digite um número real por favorzinho")

    resultado = (3 * primeiro_numero_inteiro) + numero_real
    return resultado

def terceiro_ao_cubo(numero_real):
    if not isinstance(numero_real, (float, int)):
        raise Exception("Digite um número real por favorzinho")
    
    resultado = numero_real ** 3
    return resultado

def imprime_resultado_dobro(resultado_dobro_primeiro_metade_segundo):
    return(f"O produto do dobro do primeiro com metade do segundo e igual a {resultado_dobro_primeiro_metade_segundo}")

def imprime_resultado_triplo_primeiro(resultado_triplo_primeiro_soma_terceiro):
    return(f"A soma do triplo do primeiro com o terceiro e igual a {resultado_triplo_primeiro_soma_terceiro}")

def imprime_terceiro_ao_cubo(resultado_terceiro_cubo):
    return(f"O terceiro numero elevado ao cubo e igual a {resultado_terceiro_cubo}")

def main():
    primeiro_numero_inteiro = int(input("Digite o primeiro número inteiro: "))
    segundo_numero_inteiro = int(input("Digite o segundo número inteiro: "))
    numero_real = float(input("Digite um número real: "))

    resultado_dobro_primeiro_metade_segundo = calcula_produto_primeiro_numero(primeiro_numero_inteiro, segundo_numero_inteiro)
    resultado_triplo_primeiro_soma_terceiro = soma_triplo_primeiro_terceiro(primeiro_numero_inteiro, numero_real)
    resultado_terceiro_cubo = terceiro_ao_cubo(numero_real)

    mensagem_print_dobro = imprime_resultado_dobro(resultado_dobro_primeiro_metade_segundo)
    mensagem_print_triplo = imprime_resultado_triplo_primeiro(resultado_triplo_primeiro_soma_terceiro)
    mensagem_print_cubo = imprime_terceiro_ao_cubo(resultado_terceiro_cubo)

    return mensagem_print_dobro, mensagem_print_triplo, mensagem_print_cubo

#main()
