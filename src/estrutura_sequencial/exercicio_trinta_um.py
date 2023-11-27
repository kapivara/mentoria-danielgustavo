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
    nome_aluno = str(input("Digite seu nome caro aluno: "))
    nota_um = float(input("Digite o valor da primeira nota: "))
    nota_dois = float(input("Digite o valor da segunda nota: "))

    nota_media = calcula_nota_media(nota_um, nota_dois)

    valida_conceito = valida_conceito_nota(nota_media)

    status = valida_status_aluno(nota_media)

    retorno_mensagem_situacao_aluno = retorno_mensagem_status_aluno(nome_aluno, nota_media, valida_conceito, status)
    print(retorno_mensagem_situacao_aluno)

def calcula_nota_media(nota_um, nota_dois):

    if not isinstance(nota_um, (float, int)):
        raise Exception ("Por favor, digite um numero correto!!!")
    
    if not isinstance(nota_dois, (float, int)):
        raise Exception ("Por favor, digite um numero correto!!!")
    
    elif nota_um < 0 or nota_dois < 0:
        raise Exception ("Não pode haver notas menores que zero")
    
    nota_media = (nota_um + nota_dois) / 2

    return nota_media

def valida_conceito_nota(nota_media):
    conceitos =        [((0, 5), "E"),
                       ((5, 6), "D"),
                       ((6, 7.5), "C"),
                       ((7.5, 9), "B"),
                       ((9, 10), "A")]
    
    for intervalo, conceito in conceitos:
        inicio, fim = intervalo
        if inicio <= nota_media < fim:
            return conceito
        
def valida_status_aluno(nota_media):
    if nota_media > 6:
        status = " foi Aprovado(a), parabéns por sua dedicação, continue assim!!!"
        return status
    else:
        status = " infelizmente você foi Reprovado(a), se esforce um pouco mais nos estudos"
        return status
        
def retorno_mensagem_status_aluno(nome_aluno, nota_media, valida_conceito, status):
    return (f"Ola caro aluno {nome_aluno}, sua nota média foi de {nota_media:.2f}, seu conceito ficou classificado como {valida_conceito}, e você{status}")

#main()