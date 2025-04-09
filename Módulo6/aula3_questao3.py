import random # importa a função random
lista1 = [random.randint(0,50) for i in range(20)] #gera 20 números aleatórios na lista 1
lista2 = [random.randint(0,50) for i in range(20)]# gera 20 números aleatórios na lista 2
interseccao = list(set(lista1) & set(lista2)) # encontra as intersecções entre as 2 listas
print(lista1)
print(lista2)
interseccao_ordenada = interseccao.sort # gera a lista de interseccao ordenada
print(interseccao_ordenada)
for num in interseccao: # mostra a quantidade que cada elemento aparece em cada lista
    print(f"{num}: lista 1 = {lista1.count(num)}", f"{num}: lista 2 = {lista2.count(num)}")