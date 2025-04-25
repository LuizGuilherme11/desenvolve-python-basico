def substituir_vogais(frase):
    # Definir as vogais (tanto minúsculas quanto maiúsculas)
    vogais = "aeiouAEIOU"
    
    # Substituir todas as ocorrências de vogais por "*"
    frase_modificada = "".join("*" if char in vogais else char for char in frase)
    
    return frase_modificada

# Solicita a frase ao usuário
frase_usuario = input("Digite uma frase: ")

# Exibe a frase com as vogais substituídas
print("Frase com vogais substituídas:", substituir_vogais(frase_usuario))