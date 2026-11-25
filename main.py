meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            "MOFIA": "Burla, relajo o tomadura de pelo, Apariencia física o actitud barrial",
            "GUAREMATE": "término coloquial que describe a una persona que hace favores o tareas menores para otra con mayor estatus o influencia, a menudo con actitud servil o lambona",
            }

for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    # ¿Qué debemos hacer si se encuentra la palabra?
    else:
        Print("Sabias que esta palabra significa")
    # ¿Qué hacer si no se encuentra la palabra?
