# Lambda simples
quadrado = lambda x: x**2
print(quadrado(5))  # 25

# Lambda com map
numeros = [1,2,3,4,5]
quadrados = list(map(lambda x: x**2, numeros))
print(quadrados)  # [1,4,9,16,25]