import random

# Gerar lista com 20 números aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]
print("Lista original:")
print(lista)

# Encontrar o intervalo com a maior quantidade de negativos

tamanho_max_intervalo = 6
melhor_inicio = 0
melhor_fim = 0
max_negativos = 0

for inicio in range(len(lista)):
    for fim in range(inicio + 1, min(inicio + tamanho_max_intervalo + 1, len(lista) + 1)):
        sublista = lista[inicio:fim]
        negativos = sum(1 for n in sublista if n < 0)
        if negativos > max_negativos:
            max_negativos = negativos
            melhor_inicio = inicio
            melhor_fim = fim

# Deletar intervalo da lista
del lista[melhor_inicio:melhor_fim]

# Mostrar resultado
print("Lista após deleção do intervalo com mais números negativos:")
print(lista)