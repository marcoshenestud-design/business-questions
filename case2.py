import pandas as pd

vendas = [
    {'id_venda': 1, 'data': '2025-01-01', 'produto': 'Notebook', 'categoria': 'Eletrônicos', 'preco': 3500, 'quantidade': 1, 'forma_pagamento': 'Cartão', 'cidade': 'São Paulo'},
    {'id_venda': 2, 'data': '2025-01-01', 'produto': 'Mouse', 'categoria': 'Eletrônicos', 'preco': 120, 'quantidade': 2, 'forma_pagamento': 'Pix', 'cidade': 'Rio de Janeiro'},
    {'id_venda': 3, 'data': '2025-01-02', 'produto': 'Cadeira Gamer', 'categoria': 'Móveis', 'preco': 900, 'quantidade': 1, 'forma_pagamento': 'Boleto', 'cidade': 'Belo Horizonte'},
    {'id_venda': 4, 'data': '2025-01-02', 'produto': 'Teclado', 'categoria': 'Eletrônicos', 'preco': 250, 'quantidade': 1, 'forma_pagamento': 'Cartão', 'cidade': 'São Paulo'},
    {'id_venda': 5, 'data': '2025-01-03', 'produto': 'Mesa Escritório', 'categoria': 'Móveis', 'preco': 1100, 'quantidade': 1, 'forma_pagamento': 'Pix', 'cidade': 'Curitiba'},
    {'id_venda': 6, 'data': '2025-01-03', 'produto': 'Monitor', 'categoria': 'Eletrônicos', 'preco': 1300, 'quantidade': 2, 'forma_pagamento': 'Cartão', 'cidade': 'São Paulo'},
    {'id_venda': 7, 'data': '2025-01-04', 'produto': 'Headset', 'categoria': 'Eletrônicos', 'preco': 300, 'quantidade': 3, 'forma_pagamento': 'Pix', 'cidade': 'Rio de Janeiro'},
    {'id_venda': 8, 'data': '2025-01-04', 'produto': 'Luminária', 'categoria': 'Decoração', 'preco': 180, 'quantidade': 2, 'forma_pagamento': 'Pix', 'cidade': 'Curitiba'},
    {'id_venda': 9, 'data': '2025-01-05', 'produto': 'Sofá', 'categoria': 'Móveis', 'preco': 2800, 'quantidade': 1, 'forma_pagamento': 'Cartão', 'cidade': 'São Paulo'},
    {'id_venda': 10, 'data': '2025-01-05', 'produto': 'Webcam', 'categoria': 'Eletrônicos', 'preco': 450, 'quantidade': 1, 'forma_pagamento': 'Pix', 'cidade': 'Belo Horizonte'},
    {'id_venda': 11, 'data': '2025-01-06', 'produto': 'Microfone', 'categoria': 'Eletrônicos', 'preco': 600, 'quantidade': 1, 'forma_pagamento': 'Cartão', 'cidade': 'Rio de Janeiro'},
    {'id_venda': 12, 'data': '2025-01-06', 'produto': 'Estante', 'categoria': 'Móveis', 'preco': 750, 'quantidade': 2, 'forma_pagamento': 'Boleto', 'cidade': 'Curitiba'},
    {'id_venda': 13, 'data': '2025-01-07', 'produto': 'Tapete', 'categoria': 'Decoração', 'preco': 400, 'quantidade': 1, 'forma_pagamento': 'Pix', 'cidade': 'São Paulo'},
    {'id_venda': 14, 'data': '2025-01-07', 'produto': 'Mousepad', 'categoria': 'Eletrônicos', 'preco': 80, 'quantidade': 3, 'forma_pagamento': 'Pix', 'cidade': 'Belo Horizonte'},
    {'id_venda': 15, 'data': '2025-01-08', 'produto': 'Câmera', 'categoria': 'Eletrônicos', 'preco': 2200, 'quantidade': 1, 'forma_pagamento': 'Cartão', 'cidade': 'São Paulo'}
]

df = pd.DataFrame(vendas)
#print(df)

#=-=-=-=-=-=-=-=-=-=-=-=-
# PERGUNTAS DE NEGÓCIOS
#=-=-=-=-=-=-=-=-=-=-=-=-

# 1) Qual foi o faturamento total da loja? 
df['faturamentoTotal'] = df['preco'] * df['quantidade']
faturamentoTotal = df['preco'] * df['quantidade']
print(df)
print(f"\n O faturamento total foi: {faturamentoTotal.sum()}.")

# 2) Qual categoria gerou mais faturamento?
catFaturamento = df.groupby('categoria')['faturamentoTotal'].sum().sort_values(ascending=False)
print("\n",catFaturamento)

# 3) Quais são as 3 cidades que mais faturaram?
cidFaturamento = df.groupby('cidade')['faturamentoTotal'].sum().sort_values(ascending=False).head(3)
print(cidFaturamento)

# 4) Qual forma de pagamento é a mais utilizada?
formPagamento = df['forma_pagamento'].value_counts().sort_values(ascending=False)
print(formPagamento)

# 5) Qual foi o faturamento total por dia?
print((df.groupby('data')['faturamentoTotal'].sum().sort_values(ascending=False)))

# 6) Qual produto teve o maior faturamento total?
print(df.groupby('produto')['faturamentoTotal'].sum().sort_values(ascending=False))

# 7) Qual categoria vendeu mais unidades (quantidade total)?
print(df.groupby('categoria')['quantidade'].sum().sort_values(ascending=False))

# 8) Qual cidade realizou mais vendas (quantidade de registros)?
print(df.groupby('cidade')['quantidade'].sum().sort_values(ascending=False))

# 9) Qual foi o ticket médio (faturamento médio por venda)?
quantidade = df['quantidade'].sum()
ticketMedio = faturamentoTotal.sum()/quantidade
print(ticketMedio)

# 10) Em qual dia ocorreu o maior faturamento?
print(df.groupby('data')['faturamentoTotal'].sum().sort_values(ascending=False))

