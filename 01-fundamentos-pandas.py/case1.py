import pandas as pd

vendas = [
    {'id_venda': 1, 'produto': 'Notebook', 'categoria': 'Eletrônicos', 'preco': 3500, 'quantidade': 1, 'forma_pagamento': 'Cartão', 'cidade': 'São Paulo'},
    {'id_venda': 2, 'produto': 'Mouse', 'categoria': 'Eletrônicos', 'preco': 120, 'quantidade': 2, 'forma_pagamento': 'Pix', 'cidade': 'Rio de Janeiro'},
    {'id_venda': 3, 'produto': 'Cadeira Gamer', 'categoria': 'Móveis', 'preco': 900, 'quantidade': 1, 'forma_pagamento': 'Boleto', 'cidade': 'Belo Horizonte'},
    {'id_venda': 4, 'produto': 'Teclado', 'categoria': 'Eletrônicos', 'preco': 250, 'quantidade': 1, 'forma_pagamento': 'Cartão', 'cidade': 'São Paulo'},
    {'id_venda': 5, 'produto': 'Mesa Escritório', 'categoria': 'Móveis', 'preco': 1100, 'quantidade': 1, 'forma_pagamento': 'Pix', 'cidade': 'Curitiba'},
    {'id_venda': 6, 'produto': 'Monitor', 'categoria': 'Eletrônicos', 'preco': 1300, 'quantidade': 2, 'forma_pagamento': 'Cartão', 'cidade': 'São Paulo'},
    {'id_venda': 7, 'produto': 'Headset', 'categoria': 'Eletrônicos', 'preco': 300, 'quantidade': 3, 'forma_pagamento': 'Pix', 'cidade': 'Rio de Janeiro'}
]

data_frame = pd.DataFrame(vendas) # transforma em tabela
#print(data_frame)


#1 pergunta de negócio - Qual foi o faturamento total da loja?

data_frame['faturamento'] = data_frame['preco'] * data_frame['quantidade'] #aqui eu coloquei o nome da NOVA coluna e especifiquei como deve ser o valor de cada célula da nova coluna
print(data_frame)
faturamento_total = data_frame['faturamento'].sum()
print(f"\nO faturamento total da loja foi {faturamento_total}.")

#2 pergunta de negócio - Qual categoria gerou mais dinheiro?

vendeuMais = data_frame.groupby('categoria')['faturamento'].sum().sort_values(ascending=False) #essa última parte é pra colocar do maior para o menor - um ranking
print('\nSEPARADO POR CATEGORIA\n')
print(vendeuMais)

#3 pergunta de negócio - Qual forma de pagamento é a mais utilizada?

pagamentos = data_frame['forma_pagamento'].value_counts() #contar em quantas linhas o nome se repete
print(pagamentos)