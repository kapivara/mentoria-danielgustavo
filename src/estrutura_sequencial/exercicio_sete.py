"""
Faça um Programa que calcule a área de um quadrado,
em seguida mostre o dobro desta área para o usuário.#7
"""

print("\n\n Mensagem importante, o resultado da área do circulo, sera sempre aprensentado em centimetros, por isso, caso sua área seja maior que 100 centimentros, por favor realize a conversão \n\n")

def calcula_area_quadrado(lado_um, lado_dois):

    if not isinstance(lado_um, (float, int)):
        raise Exception("Digite um numero válido")
    
    elif not isinstance(lado_dois, (float, int)):
        raise Exception("Digite um numero válido")
    
    elif(lado_um) < 0 or lado_dois < 0:
        raise Exception("As medidas dos lados devem ter valores positivos!!!")
    
    return (lado_um*lado_dois)*2

def imprime_area_quadrado(dobro_area):
    print ((f"O dobro da area deste quadrado e de {dobro_area} centimentros."))

def main():
    lado_um = float(input("Digite o comprimento do lado do quadrado: "))
    lado_dois = float(input("Digite o comprimento do lado do quadrado: "))
    dobro_area = calcula_area_quadrado(lado_um, lado_dois)
    mensagem = imprime_area_quadrado(dobro_area)
    return mensagem

main()