#entrada
n = int(input("digite um valor: "))
maior = 0
#processamento
while n > 0: # condição do valor "n"
    x = int(input("digite um valor: "))
    while x > maior: # condição do valor "maior"
        maior = x
    n = n - 1
print(maior) # saída