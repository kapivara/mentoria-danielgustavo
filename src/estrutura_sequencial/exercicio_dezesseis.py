"""O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões
de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:

comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias."""

import math

def calculo_uso_litros_tinta(area_para_pintura):
    if not isinstance(area_para_pintura, (float, int)):
        raise Exception ("Informe corretamente a metragem que precisas pintar")
    
    elif area_para_pintura < 0:
        raise Exception("Metragens menores que zero, não podem ser pintadas")
    
    extra = 1.10
    
    return (area_para_pintura*extra) / 6

def qtd_tintas_latas(qtd_litros_tinta):
    litros_por_lata = 18
    return math.ceil(qtd_litros_tinta / litros_por_lata)

def qtd_tintas_galoes(qtd_litros_tinta):
    litros_por_galao = 3.6
    return math.ceil(qtd_litros_tinta / litros_por_galao)

def qtd_latas_e_galoes_tinta(qtd_litros_tinta, area_para_pintura):
    qtd_litros_tinta = calculo_uso_litros_tinta(area_para_pintura)
    qtd_latas_necessarias = int(qtd_litros_tinta // 18)
    sobra_litros_tinta = qtd_litros_tinta % 18
    qtd_galoes_necessarios = math.ceil(sobra_litros_tinta / 3.6)
            
    return qtd_latas_necessarias, qtd_galoes_necessarios

def valor_tinta_latas(qtd_latas_tinta):
    preco_lata_tinta = 80
    return qtd_latas_tinta * preco_lata_tinta

def valor_tinta_galoes(qtd_galoes_tinta):
    preco_galao_tinta = 25
    return qtd_galoes_tinta * preco_galao_tinta

def valor_total_galoes_e_latas(area_para_pintura):
    qtd_litros_tinta = calculo_uso_litros_tinta(area_para_pintura)
    qtd_latas_necessarias = int(qtd_litros_tinta // 18)
    sobra_litros_tinta = qtd_litros_tinta % 18
    qtd_galoes_necessarios = math.ceil(sobra_litros_tinta / 3.6)
    preco_lata_tinta = 80
    preco_galao_tinta = 25

    return (qtd_latas_necessarias * preco_lata_tinta) + (qtd_galoes_necessarios * preco_galao_tinta)

def retorno_mensagem_litros_tintas(qtd_litros_tinta):
    return (f"A quantidade de LITROS a serem gastos e de {qtd_litros_tinta}")

def retorno_mensagem_qtds_latas(qtd_latas_tinta):
    return (f"A quantidade de LATAS a serem gastas e de {qtd_latas_tinta}")

def retorno_mensagem_qtds_galoes(qtd_galoes_tinta):
    return (f"A quantidade de LATAS a serem gastas e de {qtd_galoes_tinta}")

def retorno_mensagem_qtd_latas_e_galoes(qtd_latas_e_galoes):
    return (f"A quantidade de LATAS e GALOES a serem gastas e de {qtd_latas_e_galoes}, respectivamente")

def retorno_mensagem_preco_total_latas_tintas(preco_total_latas_tintas):
    return (f"O valor total a ser gasto com LATAS de tinta e de R$ {preco_total_latas_tintas}")

def retorno_mensagem_preco_total_galoes_tintas(preco_total_galoes_tintas):
    return (f"O valor total a ser gasto com GALOES de tinta e de R$ {preco_total_galoes_tintas}")

def retorno_mensagem_preco_total_latas_e_galoes(preco_total_tintas_latas_e_galoes):
    return (f"O valor total a ser gasto comprando LATAS e GALOES e de R$ {preco_total_tintas_latas_e_galoes}")

def main():
    area_para_pintura = float(input("Quantos metros quadrados tem a area a ser pintada ? "))
    
    qtd_litros_tinta = calculo_uso_litros_tinta(area_para_pintura)

    qtd_latas_tinta = qtd_tintas_latas(qtd_litros_tinta)
    qtd_galoes_tinta = qtd_tintas_galoes(qtd_litros_tinta)
    qtd_latas_e_galoes = qtd_latas_e_galoes_tinta(qtd_litros_tinta, area_para_pintura)

    preco_total_tintas_latas = valor_tintas_latas(qtd_latas_tinta)
    preco_total_tintas_galoes = valor_tintas_galoes(qtd_galoes_tinta)
    preco_total_latas_e_galoes = valor_total_galoes_e_latas(area_para_pintura)

    retorno_mensagem_litros_tinta = retorno_mensagem_litros_tintas(qtd_litros_tinta)
    retorno_mensagem_qtd_latas = retorno_mensagem_qtds_latas(qtd_latas_tinta)
    retorno_mensagem_qtd_galoes = retorno_mensagem_qtds_galoes(qtd_galoes_tinta)
    retorno_mensagem_qtd_latas_galoes = retorno_mensagem_qtd_latas_e_galoes(qtd_latas_e_galoes)
    retorno_mensagem_preco_total_latas = retorno_mensagem_preco_total_latas_tintas(preco_total_tintas_latas)
    retorno_mensagem_preco_total_galoes = retorno_mensagem_preco_total_galoes_tintas(preco_total_tintas_galoes)
    retorno_mensagem_valor_total_latas_e_galoes = retorno_mensagem_preco_total_latas_e_galoes(preco_total_latas_e_galoes)

    print(retorno_mensagem_litros_tinta)
    print(retorno_mensagem_qtd_latas)
    print(retorno_mensagem_qtd_galoes)
    print(retorno_mensagem_qtd_latas_galoes)
    print(retorno_mensagem_preco_total_latas)
    print(retorno_mensagem_preco_total_galoes)
    print(retorno_mensagem_valor_total_latas_e_galoes)

#main()