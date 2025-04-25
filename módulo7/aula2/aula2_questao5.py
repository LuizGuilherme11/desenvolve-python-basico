import random

def embaralhar_palavra(palavra):
    if len(palavra) <= 3:
        return palavra  # Não embaralha palavras muito curtas
    
    meio = list(palavra[1:-1])
    random.shuffle(meio)
    return palavra[0] + "".join(meio) + palavra[-1]

def embaralhar_palavras(frase):
    palavras = frase.split()
    embaralhadas = [embaralhar_palavra(palavra) for palavra in palavras]
    return " ".join(embaralhadas)

frase = input("Digite uma frase: ")
nova_frase = embaralhar_palavras(frase)
print("Frase embaralhada:", nova_frase)