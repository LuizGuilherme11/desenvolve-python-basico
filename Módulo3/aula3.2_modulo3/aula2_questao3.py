#entrada
##perguntar idade, se ja jogou pelo menos 3 jogos de tabuleiro e quantas vezes venceu um jogo
idade = int(input("qual sua idade? "))
n_de_jogos = int(input("quantos jogos você ja jogou? "))
n_de_vitorias = int(input("quantas vezes você venceu um jogo ? "))

#processamento
##verdadeiro se idade estiver entre 16 e 18, pelo menos 3 jogos jogados e 1 vitória
ingresso_permitido = ((idade == 17 and n_de_jogos >= 3) and n_de_vitorias >= 1)
#saída
print(f"ingresso permitido no clube {ingresso_permitido}")