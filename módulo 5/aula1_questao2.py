import math
import random

n = int(input('digite a quantidade de valores: '))
soma = 0
for i in range(n):
    soma += random.randint(0, 100)
print('a raiz quadrada da soma é', math.sqrt(soma))
