import random #impportar função random
num_elementos = random.randint (5, 20) #entrada de um número aleatório
valores = [random.randint (1, 10) for i in range (num_elementos)] #quantidade de valores igual ao valor de "num_elementos"
elementos = valores
print(elementos) #saída de dados da lista
print(sum(elementos)) #soma de todos os elementos da lista
print(sum(elementos)/len(elementos)) #média dos elementos da lista