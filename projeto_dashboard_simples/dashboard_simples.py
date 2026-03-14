import matplotlib.pyplot as plt

# Dicionário de vendas
vendas = {"Produto A": 30, "Produto B": 45, "Produto C": 25}

produtos = list(vendas.keys())
valores = list(vendas.values())

plt.bar(produtos, valores)
plt.title("Vendas de Produtos")
plt.ylabel("Quantidade vendida")
plt.show()