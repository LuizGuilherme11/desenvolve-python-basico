import datetime
agora = datetime.datetime.now()

# Formatar e imprimir a data e hora no formato desejado
data = f"{agora.day:02d}/{agora.month:02d}/{agora.year}"
hora = f"{agora.hour:02d}:{agora.minute:02d}"

print(f"Data: {data}")
print(f"Hora: {hora}")