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

    valida_execptions = exeptions_validations(primeiro_lado, segundo_lado, terceiro_lado)

    valida_formacao = is_triangle_validations(primeiro_lado, segundo_lado, terceiro_lado)

    triangulo_equilatero = is_equilatero_triangle(primeiro_lado, segundo_lado, terceiro_lado)
    triangulo_isoceles = is_isoceles_triangle(primeiro_lado, segundo_lado, terceiro_lado)
    triangulo_escaleno = is_escaleno_triangle(primeiro_lado, segundo_lado, terceiro_lado)

    triangle_ytpe = return_triangle_type

    print(valida_execptions)
    print(valida_formacao)

    print(triangulo_equilatero)
    print(triangulo_isoceles)
    print(triangulo_escaleno)

    print(triangle_ytpe)

def exeptions_validations(primeiro_lado, segundo_lado, terceiro_lado):
    if not isinstance(primeiro_lado, (float, int)):
        raise Exception ("Por favor, digite um numero correto!!!")
    
    elif not isinstance(segundo_lado, (float, int)):
        raise Exception ("Por favor, digite um numero correto!!!")
    
    elif not isinstance(terceiro_lado, (float, int)):
        raise Exception ("Por favor, digite um numero correto!!!")
    
    else:
        return "\nTodas as medidas estão OK!!!"

def is_triangle_validations(primeiro_lado, segundo_lado, terceiro_lado):
        if primeiro_lado + segundo_lado > terceiro_lado or \
            segundo_lado + terceiro_lado > primeiro_lado or \
            primeiro_lado + terceiro_lado > segundo_lado:
            return "\nE possível a formação de um triangulo!!!\n"
        
        elif primeiro_lado == segundo_lado or \
                segundo_lado == terceiro_lado or \
                primeiro_lado == terceiro_lado:
            return "\nE possível a formação de um triangulo!!!\n"
        
        else:
            return "\nNão e possivel a formação do triangulo!!!\n"

def is_equilatero_triangle(primeiro_lado, segundo_lado, terceiro_lado):
    return primeiro_lado == segundo_lado == terceiro_lado

def is_isoceles_triangle(primeiro_lado, segundo_lado, terceiro_lado):
    return  primeiro_lado == segundo_lado != terceiro_lado or \
            segundo_lado == terceiro_lado != primeiro_lado or \
            terceiro_lado == primeiro_lado != segundo_lado
       
def is_escaleno_triangle(primeiro_lado, segundo_lado, terceiro_lado):
    return primeiro_lado != segundo_lado != terceiro_lado != primeiro_lado

def return_triangle_type(primeiro_lado, segundo_lado, terceiro_lado):

    return_triangle_equilatero = is_equilatero_triangle(primeiro_lado, segundo_lado, terceiro_lado)
    if return_triangle_equilatero:
        return "As medidas formam um triangulo equilatero!!!"
    
    elif return_triangle_equilatero:
        return "As medidas NÃO formam um triangulo equilatero!!!"

    return_triangle_isoceles = is_isoceles_triangle(primeiro_lado, segundo_lado, terceiro_lado)
    if return_triangle_isoceles:
        return "As medidas formam um triangulo Isoceles!!!"
    
    elif return_triangle_isoceles:
        return "As medidas NÃO formam um triangulo equilatero!!!"
    
    return_triangle_escaleno = is_escaleno_triangle(primeiro_lado, segundo_lado, terceiro_lado)
    if return_triangle_escaleno:
        return"As medidas formam um triangulo equilatero!!!"
    
    elif return_triangle_escaleno:
        return "As medidas NÃO formam um triangulo equilatero!!!"

main()
