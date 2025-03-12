#entrada
n = int(input('quantidade de experimentos: '))
cont = 0
soma_s, soma_c, soma_r = 0, 0, 0
#processamento
while cont < n:
    cont += 1
    tipo = input('tipo: ')
    quantidade = int(input('quantidade: '))
if tipo == 'coelho':
    soma_c += quantidade
elif tipo == 'rato':
    soma_r += quantidade
elif tipo == 'sapo':
    soma_s += quantidade

#saída
print(f"total de coelhos: {soma_c}")
print(f"total de sapos: {soma_s}")
print(f"total de ratos: {soma_r}")
print(f"total de cobaias: {soma_s + soma_r + soma_c}")
