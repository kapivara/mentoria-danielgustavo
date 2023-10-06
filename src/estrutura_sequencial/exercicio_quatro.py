"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média. #4
"""

def imprime_nota_media(media):
    return f"A média da nota desse aluno e de {media} pontos."

def calcula_media(nota_um, nota_dois, nota_tres, nota_quatro):
    if type(nota_um) != int:
        raise Exception("Por favor, digite um numero valido")
    
    elif type(nota_dois) != int:
        raise Exception("Por favor, digite um numero valido")
    
    elif type(nota_tres) != int:
        raise Exception("Por favor, digite um numero valido")
    
    elif type(nota_quatro) != int:
        raise Exception("Por favor, digite um numero valido")
    
    return (nota_um + nota_dois + nota_tres + nota_quatro)/4
    
def main():
    nota_um = int (input("Digite o valor da primeira nota do aluno: "))
    nota_dois = int (input("Digite o valor da segunda nota do aluno: "))
    nota_tres = int (input("Digite o valor da terceira nota do aluno: "))
    nota_quatro = int (input("Digite o valor da quarta nota do aluno: "))
    media = calcula_media(nota_um, nota_dois, nota_tres, nota_quatro)
    mensagem = imprime_nota_media(media)
    print(mensagem)

#main()

