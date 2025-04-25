import random

def encrypt(lista_de_nomes):
    chave = random.randint(1, 10)
    criptografados = []

    for nome in lista_de_nomes:
        nome_cripto = ""
        for c in nome:
            novo_char = chr((ord(c) + chave - 33) % 94 + 33)
            nome_cripto += novo_char
        criptografados.append(nome_cripto)

    return criptografados, chave

nomes = []
print("Digite os nomes para criptografar (digite ENTER para parar):")

while True:
    nome = input("Nome: ")
    if nome == "":
        break
    nomes.append(nome)
resultado, chave = encrypt(nomes)

print("Nomes criptografados:", resultado)
print("Chave de criptografia:", chave)