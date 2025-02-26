#entrada de dados
comprimento = int(input("digite o comprimento do terreno: "))
largura     = int(input("digite a largura do terreno: "))
preço_m2    = float(input("o valor do m2 é: ")) 
#processamento
area_m2     = comprimento * largura
preco_total = preço_m2 * area_m2
#saída
print(f"o terreno tem {area_m2}m2 e custa {preco_total:,.2f}")