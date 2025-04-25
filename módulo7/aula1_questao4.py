numero = input("Digite o número de celular (sem traço, só os dígitos): ")

# Verifica se tem 8 ou 9 dígitos
if len(numero) == 8:
    numero = '9' + numero
elif len(numero) == 9:
    if numero[0] != '9':
        print("Número inválido: número com 9 dígitos deve começar com 9.")
        exit()
else:
    print("Número inválido: deve conter 8 ou 9 dígitos.")
    exit()

# Formata com traço
formatado = numero[:5] + '-' + numero[5:]
print("Número completo:", formatado)
