#entrada
valor = int(input("digite o valor: "))

#processamento
##divisao das notas de 100
valor1 = valor // 100
print(f"{valor1} nota(s) de R$100")
##atualização
valor1 = valor % 100 

##divisao das notas de 50
valor2 = valor1 // 50
print(f"{valor2} nota(s) de R$50")
##atualização
valor2 = valor1 % 50

##divisao das notas de 20
valor3 = valor2 // 20
print(f"{valor3} nota(s) de R$20")
##atualizção
valor3 = valor2 % 20

##divisao das notas de 10
valor4 = valor3 // 10
print(f"{valor4} nota(s) de R$10")
##atualização
valor4 = valor3 % 10

##divisao das notas de 5
valor5 = valor4 // 5
print(f"{valor5} nota(s) de R$5")
##atualização
valor5 = valor4 % valor3

##divisao das notas de 2
valor6 = valor5 // 2
print(f"{valor6} nota(s) de R$2")
##atualização
valor6 = valor5 % valor4

##divisao das notas de 1
valor7 = valor6 // 1
print(f"{valor7} nota(s) de R$1")
