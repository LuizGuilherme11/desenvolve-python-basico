def formatar_data(data):
    # Lista com os meses por extenso
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    
    # Separando o dia, mês e ano
    dia, mes, ano = data.split('/')
    
    # Convertendo o mês para o nome correspondente
    mes_extenso = meses[int(mes) - 1]
    
    # Retornando a data formatada
    return f"{dia} de {mes_extenso} de {ano}"

# Solicita a data de nascimento
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Exibe a data com o mês por extenso
print("Sua data de nascimento é:", formatar_data(data_nascimento))