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

    triangle_ytpe = return_triangle_type(primeiro_lado, segundo_lado, terceiro_lado)

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
    
    elif primeiro_lado < 0 or segundo_lado < 0 or terceiro_lado < 0:
        raise Exception ("Por favor, digite um numero positivo!")
 
    else:
        return "\nExeptions: Todas as medidas estão OK!!!\n"

def is_triangle_validations(primeiro_lado, segundo_lado, terceiro_lado):
        if primeiro_lado + segundo_lado > terceiro_lado and \
            segundo_lado + terceiro_lado > primeiro_lado and \
            terceiro_lado + primeiro_lado > segundo_lado:
            print ("\nE possível a formação de um triangulo!!!\n")
            return True
     
        elif primeiro_lado == segundo_lado and \
            segundo_lado == terceiro_lado and \
            primeiro_lado == terceiro_lado:
            print ("\nE possível a formação de um triangulo!!!\n")
            return True
        
        else:
            print("\nNão e possível a formação de um triangulo!!!\n")
            return False

def is_equilatero_triangle(primeiro_lado, segundo_lado, terceiro_lado):
    if is_triangle_validations(primeiro_lado, segundo_lado, terceiro_lado):
        return primeiro_lado == segundo_lado == terceiro_lado
    else:
        return False

def is_isoceles_triangle(primeiro_lado, segundo_lado, terceiro_lado):
    if is_triangle_validations(primeiro_lado, segundo_lado, terceiro_lado):
        return  primeiro_lado == segundo_lado != terceiro_lado or \
            segundo_lado == terceiro_lado != primeiro_lado or \
            terceiro_lado == primeiro_lado != segundo_lado
    else:
        return False
       
def is_escaleno_triangle(primeiro_lado, segundo_lado, terceiro_lado):
    if is_triangle_validations(primeiro_lado, segundo_lado, terceiro_lado):
        return primeiro_lado != segundo_lado != terceiro_lado != primeiro_lado
    else:
        return False

def return_triangle_type(primeiro_lado, segundo_lado, terceiro_lado):
    return_triangle_equilatero = is_equilatero_triangle(primeiro_lado, segundo_lado, terceiro_lado)
    if return_triangle_equilatero:
        return "\nAs medidas formam um triangulo equilatero!!!\n"
    
    else:
        print(" ")
    
    return_triangle_isoceles = is_isoceles_triangle(primeiro_lado, segundo_lado, terceiro_lado)
    if return_triangle_isoceles:
        return "\nAs medidas formam um triangulo Isoceles!!!\n"
    
    else:
        print(" ")
    
    return_triangle_escaleno = is_escaleno_triangle(primeiro_lado, segundo_lado, terceiro_lado)
    if return_triangle_escaleno:
        return"\nAs medidas formam um triangulo escaleno!!!\n"
    
    else:
        print(" ")

#main()
