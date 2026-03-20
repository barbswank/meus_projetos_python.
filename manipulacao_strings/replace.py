# Exercícios de REPLACE

# Remover espaços
texto1 = "Python é legal"
texto1_arrumado = texto1.replace(" ", "")
print("Sem espaços:", texto1_arrumado)  # Pythonélegal

# Remover números
nome = "Jo4n4t4h4n"
nome_arrumado = nome.replace("4", "")
print("Sem números:", nome_arrumado)  # Jonathan

# Exemplo adicional
frase = "2023 é o ano!"
frase_arrumada = frase.replace("2023", "Ano atual")
print("Frase arrumada:", frase_arrumada)  # Ano atual é o ano!