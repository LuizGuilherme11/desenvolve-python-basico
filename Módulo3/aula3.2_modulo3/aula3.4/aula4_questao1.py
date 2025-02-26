#entrada
##leitura de dois numeros 
n1 = int(input("digite o primeiro número: "))
n2 = int(input("digite o segundo número: "))

#processamento
##somar os dois numeros
soma = n1 + n2

#saída
##se a divisao da soma por 2 for 0 é par, caso contrario impar
if soma % 2 == 0:
        print("é par")
else:
        print("é ímpar")