"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a
letra escrever: F - Feminino, M - Masculino, Sexo Inválido.#20
"""

def main():
    letra = input("Digite 'F' ou 'M' para identificar seu sexo: ")
    converte_maiusculo = letra.upper()

    resultado_analise_letra = identifica_letra(converte_maiusculo)

    print (resultado_analise_letra)

def identifica_letra(letra):
    if letra not in ['F', 'M']:
        raise Exception("Sexo invalido, vc deve digitar 'F' ou 'M'!!!!")
    
    elif letra == "F":
        return (f"A letra digitada foi {letra}, e o sexo e FEMININO")
    
    elif letra == "M":
        return(f"A letra digitada foi {letra}, e o sexo e MASCULINO")

#main()
