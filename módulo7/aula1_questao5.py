frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"

indices_vogais = []

for i in range(len(frase)):
    if frase[i] in vogais:
        indices_vogais.append(i)

print("Total de vogais:", len(indices_vogais))
print("Índices das vogais:", indices_vogais)