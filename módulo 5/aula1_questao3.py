import random
numero = random.randint(1, 10)
n = int(input('tente adivinhar número de 1 a 10: '))
while n > numero:
        print('Muito alto, tente novamente')
        n = int(input('tente adivinhar número de 1 a 10: ')) 
while n < numero:
        print('Muito baixo, tente novamente')
        n = int(input('tente adivinhar número de 1 a 10: '))
while n == numero:
        print('Correto')
        break