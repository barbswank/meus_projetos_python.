# Dicionário
produto = {"nome":"Detergente","preco":7.0,"quantidade":10}
print(produto["preco"])

# Lista de nomes
nomes = ["ana","bruno","carla"]
nomes_maiusculo = [n.upper() for n in nomes]
print(nomes_maiusculo)

# Startswith
palavras = ["casa","carro","bicicleta"]
inicio_c = [p for p in palavras if p.startswith("c")]
print(inicio_c)