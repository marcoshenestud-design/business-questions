# Business-Questions

Este repositório contém exercícios e estudos de análise de dados utilizando Python e a biblioteca Pandas.
O objetivo é praticar manipulação de dados, cálculos de métricas de negócio e análises simples a partir de conjuntos de dados simulados.

## Exemplos de análises realizadas

- Cálculo de faturamento total
- Faturamento por categoria
- Produtos mais vendidos
- Ticket médio de vendas
- Ranking de cidades com maior faturamento
- Forma de pagamento mais utilizada
- Desempenho de vendedores

## Exemplo de código

```python
produtos_zerados = df[df['quantidade'] == 0]['produto'].unique()
if len(produtos_zerados) > 0:
    print(f"Produtos com vendas zeradas: {list(produtos_zerados)}")
else:
    print("Não há produtos com vendas zeradas nos registros de venda.")
```

## Objetivo

Praticar conceitos de análise de dados e desenvolver habilidades com Python - Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn e Plotly.
