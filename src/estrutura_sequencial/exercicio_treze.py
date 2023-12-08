"""
Faça um Programa que calcule o excesso de peixes#13

João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior
que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve
pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa
que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso
a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá
pagar. Imprima os dados do programa com as mensagens adequadas.
"""

def calcula_excesso_peixes(peso_peixe):
     
    if not isinstance(peso_peixe, (float, int)):
          raise Exception("Informe o numero correto de quilos de peixes.")
     
    elif peso_peixe < 0:
          raise Exception("O peso dos peixes não pode ser negativo!!!")
     
    excesso = peso_peixe - 50
    return max(0, excesso)

def calcula_valor_multa(excesso):
    return excesso * 4 if excesso > 0 else 0

def mensagem_retorno_excesso(excesso):
    return (f"A quantidade de peixes em excesso e de {excesso} quilos")

def mensagem_retorno_multa(multa):
     return (f"O valor da multa a ser paga pelo excesso de peixes e de R$ {multa}")

def main():
    peso_peixe = float(input("Quantos quilos de peixe você trouxe? "))
    excesso = calcula_excesso_peixes(peso_peixe)
    multa = calcula_valor_multa(excesso)
    retorno_mensagem_excesso = mensagem_retorno_excesso(excesso)
    retorno_mensagem_multa = mensagem_retorno_multa(multa)
    print(retorno_mensagem_excesso)
    print(retorno_mensagem_multa)

#main()
