import random #importar a função random
lista = [] #criação da lista
valores = [random.randint(-100, 100) for i in range(20)]  #gerador de 20 números aleatórios entre -100 e 100
lista.append(valores) #adiciona os valores a lista
ordenados = sorted(valores) #ordena sem alterar a lista original
print(ordenados)
print(lista) #lista original
print(max(valores)) #maior valor da lista
print(min(valores)) #menor valor da lista