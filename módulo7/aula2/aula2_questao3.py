import string

def verificar_palindromo(frase):
    # Remove espaços, pontuação e transforma tudo em minúsculas
    frase_limpa = "".join(char.lower() for char in frase if char.isalnum())
    
    # Verifica se a frase é igual a sua versão invertida
    return frase_limpa == frase_limpa[::-1]

# Loop para continuar até o usuário digitar "Fim"
while True:
    frase_usuario = input("Digite uma frase (ou 'Fim' para sair): ")
    
    if frase_usuario.strip().lower() == "fim":
        print("Programa encerrado.")
        break
    
    if verificar_palindromo(frase_usuario):
        print("A frase é um palíndromo!")
    else:
        print("A frase não é um palíndromo.")