"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino
ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou
"Boa Noite!" ou "Valor Inválido!", conforme o caso.#29
"""

print("\nCaro aluno, você deve digitar M = Matutino, V = Vespertino ou N = Noturno!!!\n")

def main():
    turno_aluno = input("Digite qual turno você estuda: ")
    turno_aluno_maiusculo = turno_aluno.upper()

    cumprimentar = analisa_turno(turno_aluno_maiusculo)

    print(cumprimentar)

def analisa_turno(turno_aluno_maiusculo):

    if turno_aluno_maiusculo not in ["M", "V", "N"]:  
       raise Exception ("Digite uma opção válida!!!")
    
    if turno_aluno_maiusculo == "M":
        return (f"A letra digitada foi {turno_aluno_maiusculo}, seu turno e o MATUTINO!!!, Bom dia")
    
    elif turno_aluno_maiusculo == "V":
        return (f"A letra digitada foi {turno_aluno_maiusculo}, seu turno e o VESPERTINO!!!, Boa Tarde")
    
    elif turno_aluno_maiusculo == "N":
       return (f"A letra digitada foi {turno_aluno_maiusculo}, seu turno e o NOTURNO!!!, Boa noite")

#main()
