
# entrada
N = int(input("digite o número de idades: "))
soma = 0 # resultado
cont = 0 # controle de repetição
while cont < N: # condicional
    idade = int(input())
    soma += idade
    cont += 1
#saída
print(f"a média dessas idade é {soma / N}")