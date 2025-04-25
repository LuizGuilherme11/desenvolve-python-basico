def encontrar_anagramas(texto, palavra):
    from collections import Counter

    tam = len(palavra)
    contador_palavra = Counter(palavra)
    resultado = []

    for i in range(len(texto) - tam + 1):
        janela = texto[i:i+tam]
        if Counter(janela) == contador_palavra:
            resultado.append(i)

    return resultado

# Entrada do usuário
texto = input("Digite a frase: ")
palavra = input("Digite a palavra objetivo: ")

indices = encontrar_anagramas(texto, palavra)

print("Anagramas encontrados nas posições:", indices)
