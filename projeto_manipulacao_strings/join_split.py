# Exercícios de JOIN e SPLIT

# JOIN
lista1 = ["Sol", "Lua", "Terra"]
resultado1 = "-".join(lista1)
print("JOIN com '-':", resultado1)  # Sol-Lua-Terra

lista2 = ["maçã", "banana", "uva"]
resultado2 = ",".join(lista2)
print("JOIN com ',':", resultado2)  # maçã,banana,uva

# SPLIT
texto1 = "maçã,banana,uva"
lista = texto1.split(",")
print("SPLIT com ',':", lista)  # ['maçã','banana','uva']

texto2 = "Python+é+legal"
lista2 = texto2.split("+")
print("SPLIT com '+':", lista2)  # ['Python','é','legal']