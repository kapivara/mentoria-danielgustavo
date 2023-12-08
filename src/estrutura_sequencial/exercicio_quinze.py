"""
Faça um programa para uma loja de tintas.#17

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao
usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
import math

def calculo_uso_litros_tinta(area_para_pintura):
    if not isinstance(area_para_pintura, (float, int)):
        raise Exception ("Informe corretamente a metragem que precisas pintar")
    
    elif area_para_pintura < 0:
        raise Exception("Metragens menores que zero, não podem ser pintadas")
    
    return area_para_pintura / 3

def qtd_latas_tintas(qtd_litros_tinta):
    litros_por_lata = 18
    return math.ceil(qtd_litros_tinta / litros_por_lata)

def valor_total_tintas(qtd_latas_tinta):
    preco_lata_tinta = 80
    return qtd_latas_tinta * preco_lata_tinta

def retorno_mensagem_litros_tintas(qtd_litros_tinta):
    return (f"A quantidade de litros a serem gastos e de {qtd_litros_tinta}")

def retorno_mensagem_qtds_latas(qtd_latas_tinta):
    return (f"A quantidade de latas a serem gastas e de {qtd_latas_tinta}")

def retorno_mensagem_preco_total_tintas(preco_total_tintas):
    return (f"O valor total a ser gasto e de R$ {preco_total_tintas}")


def main():
    area_para_pintura = float(input("Quantos metros quadrados tem a area a ser pintada ? "))
    
    qtd_litros_tinta = calculo_uso_litros_tinta(area_para_pintura)
    qtd_latas_tinta = qtd_latas_tintas(qtd_litros_tinta)
    preco_total_tintas = valor_total_tintas(qtd_latas_tinta)

    retorno_mensagem_litros_tinta = retorno_mensagem_litros_tintas(qtd_litros_tinta)
    retorno_mensagem_qtd_latas = retorno_mensagem_qtds_latas(qtd_latas_tinta)
    retorno_mensagem_preco_total = retorno_mensagem_preco_total_tintas(preco_total_tintas)

    print(retorno_mensagem_litros_tinta)
    print(retorno_mensagem_qtd_latas)
    print(retorno_mensagem_preco_total)

#main()