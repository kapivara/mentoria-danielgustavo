"""
Faça um Programa que converta metros para centímetros
"""

def imprime_conversao(medida_em_metros, conversao):
    return f"{medida_em_metros} metro(s), convertido(s) são {conversao} centimetros."

def calcula_conversao(medida_em_metros):
    if type(medida_em_metros) != int:
        raise Exception("Por favor, digite um numero valido")
    
    elif (medida_em_metros) < 0:
        raise Exception("Por favor, digite um numero positivo")
    
    elif (medida_em_metros) == 0:
        raise Exception("Impossível converter zero, você deve digitar um numero maior que zero")
        
    return medida_em_metros*100
    
def main():
    medida_em_metros = int (input("Digite o valor que desejas converter: "))
    conversao = calcula_conversao(medida_em_metros)
    mensagem = imprime_conversao(medida_em_metros, conversao)
    print(mensagem)

#main()
