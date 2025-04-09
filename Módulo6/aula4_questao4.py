
num1 = int(input('digite a quantidade de elementos da lista 1: ')) # número de elementos na lista 1
lista1 = []
print(f'digite os {num1} elementos da lista 1') # entrada de elementos na lista 1 de acordo com a quantidade escolhida pelo usuário
for i in range(num1): # laço para adicionar o número a lista 1
    n = int(input())
    lista1.append(n)

num2 = int(input('digite a quantidade de elementos da lista 2: ')) # número de elementos na lista 2
lista2 = []
print(f'digite os {num2} elementos da lista 2') # entrada de elementos na lista 2 de acordo com a quantidade escolhida pelo usuário
for i in range(num2): # laço para adicionar o número a lista 2
    n2 = int(input())
    lista2.append(n2)

lista_combinada = []  #lista combinada

tamanho_minimo = min(len(lista1), len(lista2))  # Determina o tamanho da menor lista

for i in range(tamanho_minimo):  # Laço para intercalar os elementos
    lista_combinada.append(lista1[i])  # Adiciona o elemento da lista1
    lista_combinada.append(lista2[i])  # Adiciona o elemento da lista2

# Adicionando os elementos restantes da maior lista usando a concatenação "+"
if len(lista1) > len(lista2):
    lista_combinada += lista1[tamanho_minimo:]  # Adiciona os elementos restantes de lista1
else:
    lista_combinada += lista2[tamanho_minimo:]  # Adiciona os elementos restantes de lista2

# saída
print(lista1)
print(lista2)
print(lista_combinada)