# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Lista de vogais ordenada
vogais = sorted([letra for letra in frase if letra in 'aeiou'])

# Lista de consoantes, excluindo espaços e vogais
consoantes = [letra for letra in frase if letra.isalpha() and letra not in 'aeiou']

# Exibe os resultados
print("Vogais ordenadas:", vogais)
print("Consoantes (sem espaços):", consoantes)
