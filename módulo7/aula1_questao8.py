def calcular_digito(cpf, peso_inicial):
    soma = 0
    for i in range(len(cpf)):
        soma += int(cpf[i]) * (peso_inicial - i)
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)

def validar_cpf(cpf_str):
    # Remove pontos e traço
    cpf_limpo = cpf_str.replace(".", "").replace("-", "")

    # Verifica se tem 11 dígitos numéricos
    if not cpf_limpo.isdigit() or len(cpf_limpo) != 11:
        return False

    # Extrai os 9 primeiros dígitos e os 2 verificadores
    corpo = cpf_limpo[:9]
    digitos_verificadores = cpf_limpo[9:]

    # Calcula os dois dígitos
    primeiro_digito = calcular_digito(corpo, 10)
    segundo_digito = calcular_digito(corpo + primeiro_digito, 11)

    return digitos_verificadores == primeiro_digito + segundo_digito

# Solicita o CPF do usuário
cpf = input("Digite o CPF (formato XXX.XXX.XXX-XX): ")

# Verifica e imprime o resultado
if validar_cpf(cpf):
    print("CPF Válido")
else:
    print("CPF Inválido")
