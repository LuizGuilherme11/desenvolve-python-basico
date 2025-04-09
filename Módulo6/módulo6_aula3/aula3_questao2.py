urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
# Usando fatiamento para extrair os nomes principais dos domínios
dominios = [url[4:-4] for url in urls]
print('urls:') #imprime a url completa
print(urls)
print("Domínios extraídos:") #imprime apenas o domínio
print(dominios)
