#entrada
##genero, idade e tempo de serviço
genero = input("qual seu gênero? ")
idade = int(input("digite sua idade: "))
tempo = int(input("digite seu tempo de trabalho: "))

#processamento
##caso1- mulheres mais de 60 anos e homens mais de 65
##caso2- ter trabalhado 30 anos
##caso3- ter 60 anos e trabalhado pelo menos 25
caso1 = (genero == 'feminino' and idade >= 60) or (genero == 'masculino' and idade >= 65)
caso2 = idade >= 30
caso3 = idade >= 60 and tempo >= 25

pode_aposentar = caso1 or caso2 or caso3

#saída
print(pode_aposentar)