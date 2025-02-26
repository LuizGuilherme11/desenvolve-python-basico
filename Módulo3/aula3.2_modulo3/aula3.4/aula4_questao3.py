#entrada
##solicita ao usuário para inserir um ano
ano = int(input("insira um ano: "))

#processamento
#saída
##mprimir "Bissexto" se o ano for divisível por 4 e não for divisível por 100
##ou se for divisível por 400. Caso contrário, imprima "Não Bissexto
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Bissexto")
else:
    print("Não bissexto")