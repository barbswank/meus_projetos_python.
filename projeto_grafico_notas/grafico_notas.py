import matplotlib.pyplot as plt

# Lista de alunos e notas
alunos = ["Ana", "Bruno", "Carla", "Daniel"]
notas = [7, 9, 6, 8]

# Criar gráfico de barras
plt.bar(alunos, notas)
plt.title("Notas dos Alunos")
plt.xlabel("Alunos")
plt.ylabel("Notas")
plt.show()