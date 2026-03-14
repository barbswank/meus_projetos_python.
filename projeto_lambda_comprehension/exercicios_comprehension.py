# Quadrados de 0 a 9
quadrados = [x**2 for x in range(10)]
print(quadrados)

# Números pares de 0 a 10
pares = [x for x in range(11) if x % 2 == 0]
print(pares)

# Comprimento de palavras
palavras = ["python","java","c"]
tamanho = [len(p) for p in palavras]
print(tamanho)

# Nomes em maiúsculo
nomes = ["ana","bruno","carla"]
maiusculo = [n.upper() for n in nomes]
print(maiusculo)