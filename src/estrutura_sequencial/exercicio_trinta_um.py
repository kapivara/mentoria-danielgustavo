"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média.#33

A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento	| Conceito
Entre 9.0 e 10.0	    |   A
Entre 7.5 e 9.0	        |   B
Entre 6.0 e 7.5	        |   C
Entre 4.0 e 6.0	        |   D
Entre 4.0 e zero	    |   E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito
for D ou E.
"""

def main():
    nota_um = float(input("Digite o valor da primeira nota: "))
    nota_dois = float(input("Digite o valor da segunda nota: "))

    nota_media = calcula_nota_media(nota_um, nota_dois)

    conceito = valida_conceito_nota(nota_media)

    retorno_mensagem_situacao_aluno = retorno_mensagem_situacao_aluno(nota_media, conceito)

def calcula_nota_media(nota_um, nota_dois):

    if not isinstance(nota_um, nota_dois, (float, int)):
        raise Exception ("Por favor, digite um numero correto!!!")
    
    elif nota_um or nota_dois > 0:
        raise Exception ("Não pode haver notas menores que zero")

def valida_conceito_nota():

    