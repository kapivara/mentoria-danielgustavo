"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.#32
"""

print("\nEsse programa irá lhe apresentar os dias da semana, senhor(a) usuario(a), por favor digite um valor entre 1 e 7!!!!\n")

def main():
    numero_semana = int(input("Digite o numero referente ao dia da semana que queiras: "))

    analisa_numero = analisa_numero_semana(numero_semana)

    mensagem_retorno_dia_semana = retorna_dia_semana(analisa_numero)

    print(mensagem_retorno_dia_semana)
    
def analisa_numero_semana(numero_semana):
    if type(numero_semana) != int:
        raise Exception("Por favor, digite um numero valido")

    elif numero_semana not in [1,2,3,4,5,6,7]:
        raise ValueError ("Numero Invalido!!!")

    return numero_semana

def retorna_dia_semana(numero_semana):
    lista_dias_da_semana = ["Domingo", "Segunda Feira", "Terça Feira", "Quarta Feira", "Quinta Feira", "Sexta Feira", "Sabado"]

    if numero_semana >= 1 and numero_semana <=7 :
            return lista_dias_da_semana[numero_semana-1]
   
#main()
