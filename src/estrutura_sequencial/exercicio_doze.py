"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
que calcule seu peso ideal. #12

construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
(72.7*altura) - 58

utilizando as seguintes fórmulas:
Para homens: (72.7h) - 58
Para mulheres: (62.1h) - 44.7
"""

print("Querido usuário, altura deve ser informada em metros, ex: 1.63, informar o sexo colocar 'M'/Masculino ou 'F'/Feminino")

def calcula_peso_ideal(altura, sexo):

    if not isinstance(altura, (float, int)):
            raise Exception ("Informe a altura corretamente")
           
    elif altura < 0:
            raise Exception("Por favor informe uma altura positiva!!!")

    elif sexo != str:
         raise Exception("Por favor informe o sexo corretamente")  

    elif sexo == "M":
        peso_ideal = (72.7*altura) - 58

    elif sexo == "F":
        peso_ideal = (62.1*altura) - 44.7

        return peso_ideal

def imprime_peso_ideal(peso_ideal):
    print(f"Seu peso ideal seria de {peso_ideal}")

def main():
    sexo_pessoa = str(input("Qual seu sexo ? ")).upper()
    altura = float(input("Digite sua altura para saber seu peso ideal: "))
    peso_ideal = calcula_peso_ideal(altura, sexo_pessoa)
    retorno_mensagem = imprime_peso_ideal(peso_ideal)
    return retorno_mensagem

main()
