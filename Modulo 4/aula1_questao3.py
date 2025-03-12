#entrada
## atribuição de valores a n1, n2, n3
n1 = int(input("valor 1: "))
n2 = int(input("valor 2: "))
n3 = int(input("valor 3: "))
## atribuição do valor de "m" que é (n1 + n1 + n3) / 3
m = (n1 + n2 + n3) / 3

#processamento
while m >= 60: # condição 1
        print("Aprovado")
if m  >= 40:
        print("Recuperação")
else:
        print("Reprovado")
print("Fim")
