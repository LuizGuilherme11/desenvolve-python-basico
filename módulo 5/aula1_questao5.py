import emoji #importando o módulo de emojis

emojis_disponiveis = {    #listando os emojis disponiveis
    "❤️": ":red_heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:",
    "😁": "beaming_face_with_smiling_eyes"
}
print("Emojis disponíveis:")
for emoj, codigo in emojis_disponiveis.items():
    print(f'{emoj} - {codigo}')

frase = input("escreva a frase a ser emojizada: ") #entrada de dados (frase escolhida pelo usuário)
frase_emojizada = emoji.emojize(frase) #Para emojizar a frase codificada (frase)
print("frase emojizada:")
print(frase_emojizada)