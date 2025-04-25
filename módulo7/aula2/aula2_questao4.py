import string

def validador_senha(senha):
    if len(senha) < 8:
        return False

    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    especiais = "@#$%&*!?"
    tem_especial = any(c in especiais for c in senha)

    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

senha = input("Digite a senha: ")
if validador_senha(senha):
    print("Senha válida!")
else:
    print("Senha inválida! Ela deve ter:\n- 8+ caracteres\n- Letra maiúscula e minúscula\n- Número\n- Caractere especial (@, #, $, etc.)")
