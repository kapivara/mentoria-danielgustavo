"""
[Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero,
isósceles ou escaleno.#34]

Dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

def main():
    primeiro_lado = float(input("Digite a medida a medida do primeiro lado: "))
    segundo_lado = float(input("Digite a medida a medida do segundo lado: "))
    terceiro_lado = float(input("Digite a medida a medida do terceiro lado: "))

    valida_form_triangulo_equilatero = valida_formacao_triangulo_equilatero(primeiro_lado, segundo_lado, terceiro_lado)
    valida_form_triangulo_isosceles = valida_form_triangulo_isosceles

    tipo_triangulo = valida_tipo_triangulo(primeiro_lado, segundo_lado, terceiro_lado)

    print(valida_form_triangulo_equilatero)
    print(valida_form_triangulo_isosceles)
    print()
    print(tipo_triangulo)

def valida_formacao_triangulo(primeiro_lado, segundo_lado, terceiro_lado):
        if primeiro_lado + segundo_lado > terceiro_lado and segundo_lado + terceiro_lado > primeiro_lado and primeiro_lado + terceiro_lado > segundo_lado:
            return "E possível a formação de um triangulo!!!\nEsse triangulo e Equilatero"
        
        elif primeiro_lado == segundo_lado or segundo_lado == terceiro_lado or primeiro_lado == terceiro_lado:
            return "E possível a formação de um triangulo!!!"
        
        else:
            return "Não e possivel a formação do triangulo!!!"

def valida_tipo_triangulo_equilatero(primeiro_lado, segundo_lado, terceiro_lado):
        if primeiro_lado == segundo_lado and primeiro_lado == terceiro_lado:
            return "Triângulo Equilátero!!!"

def valida_formacao_triangulo_isosceles(primeiro_lado, segundo_lado, terceiro_lado):
        if primeiro_lado + segundo_lado > terceiro_lado and segundo_lado + terceiro_lado > primeiro_lado and primeiro_lado + terceiro_lado > segundo_lado:
            return "E possível a formação de um triangulo!!!\nEsse triangulo e Equilatero"
        
        elif primeiro_lado == segundo_lado or segundo_lado == terceiro_lado or primeiro_lado == terceiro_lado:
            return "E possível a formação de um triangulo!!!"
        
        else:
            return "Não e possivel a formação do triangulo!!!"
       
def valida_tipo_triangulo_isoceles(primeiro_lado, segundo_lado, terceiro_lado):
     

main()
