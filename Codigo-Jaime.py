meme_dict = {"CRINGE": "Algo excepcionalmente raro o vergonzoso","LOL": "Una respuesta común a algo gracioso",
"XD": "Otra forma de responder a algo gracioso, como una risa contagiosa.","ROFL":"Rodando en el piso riendo.","IKR":"Traducido a I know, right?, que sería Lo sé, ¿verdad?"
,"CREEPY":"Algo tenebroso.","NOOB":"Persona mala o novato."}

for i in range(7):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        # ¿Qué debemos hacer si se encuentra la palabra?
        print(meme_dict[word])
    else:
        # ¿Qué hacer si no se encuentra la palabra?
        print("Esta palabra no la conozco.")
