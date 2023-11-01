"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade
de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do
arquivo usando este link (em minutos).#15
"""

print("Nota Importante: O tamanho do arquivo deverá ser sempre em Mbps(megabytes)\n")
print("A velocidade de sua net, deve ser repassada em Mbps(megabytes), 1GB = 1024mbps\n")

def calcula_tempo_dowload(velocidade_net, tamanho_arquivo):
    if not isinstance(tamanho_arquivo, (float, int)):
        raise Exception("Informe o tamanho correto do arquivo!!!")

    elif tamanho_arquivo < 0:
        raise Exception ("O tamanho do arquivo não pode ser negativo")
    
    elif not isinstance(velocidade_net, (float, int)):
        raise Exception("Informe a velocidade correta da sua net!!!")
    
    elif velocidade_net < 0:
        raise Exception ("A velocidade da sua net não pode ser negativa")

    return tamanho_arquivo / velocidade_net

def transformar_tempo_em_minutos(tempo_dowload):
    return tempo_dowload / 60

def retorno_tempo_para_dowload(tempo_dowload):
    return (f"O tempo aproximado para se findar seu dowload, será de {tempo_dowload} minutos")

def main():
    tamanho_arquivo = float(input("Digite aqui o tamanho do arquivo que desejas prever o tempo de download: "))
    velocidade_net = float(input("Qual a velocidade de sua net ? "))

    tempo_dowload_segundos = calcula_tempo_dowload(velocidade_net, tamanho_arquivo)
    tempo_dowload_minutos = transformar_tempo_em_minutos(tempo_dowload_segundos)

    mensagem_retorno_tempo_dowload = retorno_tempo_para_dowload(tempo_dowload_minutos)

    print(mensagem_retorno_tempo_dowload)

#main()
