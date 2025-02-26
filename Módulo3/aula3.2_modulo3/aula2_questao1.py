#entrada
##idade juliana e cris
idade_juliana = int(input())
idade_cris = int(input())

#processamento
##true se os 2 puderem entrar
##false se qualquer um dos 2 não puder entrar
permitido = idade_juliana >= 18 and idade_cris >= 18

#saída
print(permitido)