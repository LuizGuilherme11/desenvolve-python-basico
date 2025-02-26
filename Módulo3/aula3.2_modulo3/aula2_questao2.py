#entrada
##idade juliana e cris
idade_juliana = int(input())
idade_cris = int(input())

#processamento
##true se um for maior de idade
##false se qualquer os 2 forem menores de idade
permitido = idade_juliana >= 18 or idade_cris >= 18

#saída
print(permitido)