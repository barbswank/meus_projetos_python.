# lista de alunos e notas
alunos = {
    "Ana": 7,
    "Bruno": 5,
    "Carlos": 9,
    "Daniela": 6,
    "Eduardo": 4
}

# pegar todas as notas
notas = list(alunos.values())

# calcular média
media = sum(notas) / len(notas)

print("Média da turma:", media)

# alunos acima da média (list comprehension)
acima_media = [nome for nome, nota in alunos.items() if nota > media]

print("Alunos acima da média:", acima_media)

# alunos reprovados (nota menor que 6)
reprovados = [nome for nome, nota in alunos.items() if nota < 6]

print("Alunos reprovados:", reprovados)

# dobrar as notas (lambda + map)
dobro_notas = list(map(lambda x: x*2, notas))

print("Dobro das notas:", dobro_notas)

# ordenar alunos por nota
ordenados = sorted(alunos.items(), key=lambda x: x[1])

print("Alunos ordenados por nota:", ordenados)