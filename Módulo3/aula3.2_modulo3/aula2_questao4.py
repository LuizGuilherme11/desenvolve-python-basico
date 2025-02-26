#entrada
classe = input("Escolha a classe do personagem (guerreiro, mago ou arqueiro): ").strip().lower()
forca = int(input("Digite os pontos de Força: "))
magia = int(input("Digite os pontos de Magia: "))
#processamento e saída
print((classe == "guerreiro" and forca >= 15 and magia <= 10) or
      (classe == "mago" and forca <= 10 and magia >= 15) or
      (classe == "arqueiro" and 5 < forca <= 15 and 5 < magia <= 15))