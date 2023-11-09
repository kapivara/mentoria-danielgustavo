"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.#27
"""

print("\n Para lhe auxiliar nas compras, preciso que me repasse o valor das 3 opções de produtos que tens que comprar!!!\n")

def main():
    primeiro_produto = float(input("Qual o valor do primeiro produto ? "))
    segundo_produto = float(input("Qual o valor do segundo produto ? "))
    terceiro_produto = float(input("Qual o valor do terceiro produto ? "))

    menor_preco = analisa_menor_preco(primeiro_produto, segundo_produto, terceiro_produto)

    mensagem_retorno_menor_preco = mensagem_menor_preco(menor_preco)

    print(mensagem_retorno_menor_preco)

def analisa_menor_preco(primeiro_produto, segundo_produto, terceiro_produto):

    if (type (primeiro_produto) not in (float, int) or type (segundo_produto) not in (float, int) or type (terceiro_produto) not in (float, int)):       
        raise Exception ("Por favor forneça corretamente o valor do produto")
    
    elif primeiro_produto < 0 or segundo_produto < 0 or terceiro_produto < 0:
        raise Exception("O valor do produto não pode ser negativo!!!")
    
    elif primeiro_produto < segundo_produto and primeiro_produto < terceiro_produto:
        return(primeiro_produto)
    
    elif segundo_produto < primeiro_produto and segundo_produto < terceiro_produto:
        return(segundo_produto)
    
    else:
        return(terceiro_produto)
    
def mensagem_menor_preco(menor_numero):
    return(f"O produto com menor valor custa R$ {menor_numero}")

#main()
