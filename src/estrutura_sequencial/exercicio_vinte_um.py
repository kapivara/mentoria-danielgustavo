"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.#23
"""
from unicodedata import normalize

def main():
    letra = input("Digite uma letra para saber se ela e vogal ou consoante: ")

    resultado_analise_letra = identifica_tipo_letra(letra)

    print (resultado_analise_letra)

def identifica_tipo_letra(letra):

    if isinstance(letra, int):
        raise Exception ("Um numero não pode ser uma letra")

    elif len(letra) != 1:
        raise Exception("Você deve digitar apenas uma letra!!!")
    
    elif not isinstance(letra, str):
        raise Exception("Você deve digitar uma letra!!!")
    
    elif letra in ("A", "E", "I", "O", "U"):
        return (f"A letra digitada foi {letra}, e essa letra e uma VOGAL")
    
    elif letra in ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'):
        return(f"A letra digitada foi {letra}, e essa letra e uma CONSOANTE")
    
    else:
        raise Exception ("Não e nenhum das opções")

#main()
