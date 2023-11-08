"""
O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.

Faça um programa para a leitura de duas notas parciais de um aluno.#24
"""

def main():
    nota_um = float(input("Digite o valor da primeira nota: "))
    nota_dois = float(input("Digite o valor da segunda nota: "))

    nota_media = calcula_nota_media(nota_um, nota_dois)

    resultado_media_aprovado_reprovado = mensagem_aprovado_reprovado(nota_media)

    print(f"Sua nota médio foi de {nota_media}")
    print (resultado_media_aprovado_reprovado)

def calcula_nota_media(nota_um, nota_dois):

    if not isinstance(nota_um, (float, int)):
        raise Exception ("As notas devem ser numeros!!!")
    
    elif not isinstance(nota_dois, (float, int)):
        raise Exception ("As notas devem ser numeros!!!")

    elif nota_um < 0 or nota_dois < 0:
        raise Exception ("A nota não pode ser negativa!!!")
    
    return (nota_um + nota_dois) / 2
    
def mensagem_aprovado_reprovado(nota_media):
    if nota_media == 10:
        return("Aluno APROVADO COM DISTINÇÃO!!!")

    elif nota_media > 7:
        return ("Aluno APROVADO!!!")
    
    elif nota_media < 7:
        return ("Aluno Reprovado!!!")

#main()
