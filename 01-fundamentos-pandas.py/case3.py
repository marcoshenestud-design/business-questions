import pandas as pd

vendas = {
    "id_venda": [1, 2, 3, 4],
    "produto": ["Notebook", "Mouse", "Teclado", "Monitor"],
    "categoria": ["Eletrônicos", "Acessórios", "Acessórios", "Eletrônicos"],
    "preco": [3500, 80, 150, 1200],
    "quantidade": [1, 3, 2, 1],
    "vendedor": ["Ana", "Carlos", "Ana", "Carlos"]
}

df = pd.DataFrame(vendas)
#print(pd.DataFrame(vendas))

# ===============================
# 💰 VENDAS & RECEITA
# ===============================

# 1. Qual foi o faturamento total?
df['faturamento'] = df['preco'] * df['quantidade']
print(df)
print('-'*75)
print(f'O faturamento total foi {df['faturamento'].sum()}.')
print('-'*60)

# 2. Qual produto gerou mais receita?
receita_produto = df.groupby('produto')['faturamento'].sum()
print(f"Produto com mais receita: {receita_produto.idxmax()}.") #mostra somente o que tem qual dos produtos tem o maior faturamento
print('-'*60)

# 3. Qual produto vendeu mais unidades?
produtoUnidade = (df.groupby('produto')['quantidade'].sum())
print(f'O produto que mais vendeu foi {produtoUnidade.idxmax()}.')
print('-'*60)

# 4. Qual foi o ticket médio das vendas?
ticket_medio = df['faturamento'].sum() / df['id_venda'].count()
print(f"O ticket médio das vendas foi {ticket_medio:.2f}.")
print('-'*60)

# 5. Qual categoria vendeu mais em valor?
catMaisVendeu = (df.groupby('categoria')['faturamento'].sum())
print(f'A categoria que mais vendeu {catMaisVendeu.idxmax()}.')
print('-'*60)

# 6. Qual categoria vendeu mais em quantidade?
catMaisQuantidade = df.groupby('categoria')['quantidade'].sum()
print(f'A categoria que vendeu mais quantidade foi {catMaisQuantidade.idxmax()}.')
print('-'*60)

# ===============================
# 🧑‍💼 VENDEDORES
# ===============================

# 7. Qual vendedor vendeu mais?
print(f'O vendedor que mais vendeu foi {df.groupby('vendedor')['quantidade'].sum().idxmax()}.') #preciso saber se caso dosi vendedores tivessem as mesmas quantidade de vendas. o que eu faria?
print('-'*60)

# 8. Qual vendedor faturou mais?
print(f'Quem faturou mais foi {df.groupby('vendedor')['faturamento'].sum().idxmax()}.')
print('-'*60)

# 9. Quantas vendas cada vendedor realizou?
print(df.groupby('vendedor')['quantidade'].count())
print('-'*60)

# 10. Qual vendedor tem o maior preço médio por venda?
preco_medio_venda = df.groupby('vendedor')['faturamento'].sum() / df.groupby('vendedor')['id_venda'].count()
print(preco_medio_venda)
print('-'*60)
print(f"Vendedor com maior preço médio por venda: {preco_medio_venda.idxmax()}.")
print('-'*60)



# ===============================
# 📦 PRODUTOS
# ===============================

# 11. Quais produtos tiveram vendas acima da média?
media = df['faturamento'].mean()
print(df.groupby('produto')['faturamento'].sum().loc[lambda x: x > media])
print('-'*60)

# 12. Quais produtos tiveram vendas abaixo da média?
print(df.groupby('produto')['faturamento'].sum().loc[lambda x: x < media])
print('-'*60)

# 13. Qual é o top 3 produtos mais vendidos?
print(df.groupby('produto')['quantidade'].sum().nlargest(3))
print('-'*60)

# 14. Existe algum produto com vendas zeradas?
############
############

# 15. Qual produto tem o maior preço unitário?
print(df.groupby('produto')['preco'].sum().nlargest(1))
print('-'*60)

# ===============================
# 📈 ANÁLISES SIMPLES (NEGÓCIO)
# ===============================

# 16. Se aumentarmos o preço em 10%, qual será o novo faturamento?
df['preco'] = df['preco'] * 0,1
print(df)

# 17. Qual produto representa maior percentual do faturamento total?



# 18. Quais produtos representam 80% da receita? (Pareto 80/20)



# 19. Se removermos um vendedor, quanto de faturamento perdemos?



# 20. Qual categoria deveria receber mais investimento?


# ===============================
# 🧠 PERGUNTAS DE ENTREVISTA
# ===============================

# 21. O que você faria para aumentar o faturamento?



# 22. Que métrica é mais importante: quantidade vendida ou receita?



# 23. Como identificar produtos encalhados?



# 24. Como explicar esses dados para alguém não técnico?



# 25. Que tipo de gráfico usaria para mostrar essas informações?