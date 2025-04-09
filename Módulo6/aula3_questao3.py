import random # importa a função random
lista1 = [random.randint(0,50) for i in range(20)]# gera 20 números aleatórios na lista 1
lista2 = [random.randint(0,50) for i in range(20)]# gera 20 números aleatórios na lista 2
print(sorted(lista1))
print(sorted(lista2))
interseccao = []
for elemento in lista1: # encontra as intersecções entre as 2 listas sem repetição
    if elemento in lista2 and interseccao not in interseccao:
        interseccao.append(elemento)
interseccao.sort() # gera a lista de interseccao ordenada
for num in interseccao: # mostra a quantidade que cada elemento aparece em cada lista
    print(f"{num}: lista 1 = {lista1.count(num)}"" e", f"{num}: lista 2 = {lista2.count(num)}")
