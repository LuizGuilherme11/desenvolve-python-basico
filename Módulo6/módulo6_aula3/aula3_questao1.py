lista = []
while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
    
    if entrada.lower() == 'fim':
        break
    else:
        num = int(entrada)
        lista.append(num)
if len(lista) < 4:
    print("Você precisa digitar pelo menos 4 números.") # solicita pelo menos 4 números de entrada
else:
    # Imprimir a lista original
    print("Lista original: ")
    print(lista)

    # imprimir os 3 primeiros números da lista
    print("os 3 primeiros números da lista: ")
    print(lista[:3])

    # Imprimir os 2 últimos elementos
    print("Os 2 últimos elementos: ")
    print(lista[-2:])

    # Imprimir a lista invertida
    print("Lista invertida: ")
    print(lista[::-1])

    # Imprimir os elementos de índice par
    print("Elementos de índice par: ")
    print(lista[::2])

    # Imprimir os elementos de índice ímpar
    print("Elementos de índice ímpar: ")
    print(lista[1::2])