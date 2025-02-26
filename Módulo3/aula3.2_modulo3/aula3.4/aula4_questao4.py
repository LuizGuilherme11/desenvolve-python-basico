# entrada
## solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas
distancia_em_quilometros, peso_em_quilogramas = float(input("digite a distancia em quilometros: ")), float(input("digite o peso em quilogramas: "))

# processamento
## Solicita os dados do usuário
distancia = float(input("Digite a distância da entrega em km: "))
peso = float(input("Digite o peso do pacote em kg: "))

## Determina o preço por kg baseado na distância
if distancia <= 100:
    preco_por_kg = 1.00
elif distancia <= 300:
    preco_por_kg = 1.50
else:
    preco_por_kg = 2.00

## Calcula o valor do frete
frete = peso * preco_por_kg

## Aplica a taxa extra se o peso for maior que 10 kg
if peso > 10:
    frete += 10

## Exibe o valor do frete
print(f"Valor do frete: R${frete:.2f}")