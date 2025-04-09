# Todos os números pares entre 20 e 50
pares_20_50 = [x for x in range(20, 51) if x % 2 == 0]
print("Pares entre 20 e 50:", pares_20_50)

# Os quadrados de todos os valores da lista
lista = [1,2,3,4,5,6,7,8,9]
quadrados = [x**2 for x in lista]
print("Quadrados:", quadrados)

# Todos os números entre 1 e 100 que sejam divisíveis por 7
divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]
print("Divisíveis por 7:", divisiveis_por_7)

# descobrir de os valores em "range" são par ou ímpar
par_ou_impar = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]
print("Par ou ímpar:", par_ou_impar)
