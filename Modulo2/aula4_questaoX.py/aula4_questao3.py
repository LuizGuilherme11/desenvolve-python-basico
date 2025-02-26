#entrada
nome_do_produto1 = input("Digite o nome do produto 1: ")
preço_unilitario1 = int(input("Digite o preço unitário do produto 1: "))
quantidade1 = int(input("Digite a quantidade do produto 1: "))

nome_do_produto2 = input("Digite o nome do produto 2: ")
preço_unilitario2 = int(input("Digite o preço unitário do produto 2: "))
quantidade2 = int(input("Digite a quantidade do produto 2: "))

nome_do_produto3 = input("Digite o nome do produto 3: ")
preço_unilitario3 = int(input("Digite o preço unitário do produto 3: "))
quantidade3 = int(input("Digite a quantidade do produto 3: "))

#processamento
preço1 = quantidade1 * preço_unilitario1
preço2 = quantidade2 * preço_unilitario2
preço3 = quantidade3 * preço_unilitario3
preço_total = preço1 + preço2 + preço3
 #saída
print(f"Total: {preço_total:,.2f}R$")