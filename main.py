while True:
    meme_dictionary = {
                "CRINGE": "Garip ya da utandırıcı bir şey",
                "cringe": "Garip ya da utandırıcı bir şey",
                "LOL": "Komik bir şeye verilen cevap",
                "lol": "Komik bir şeye verilen cevap",
                "ROFL": "bir şakaya karşılık cevap",
                "rofl": "bir şakaya karşılık cevap",
                "SHEESH": "onaylamak",
                "sheesh": "onaylamak",
                "CREEPY": "korkunç",
                "creepy": "korkunç",
                "AGGRO ": "agresifleşmek/sinirlenmek",
                "aggro ": "agresifleşmek/sinirlenmek",
                }
    
    
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    
    
    if word in meme_dictionary.keys():
        meaning = meme_dictionary[word]
        print("Anlamı:", meaning)
        
        
    
          
    else:
        print("Sözlükte böyle bir kelime yok.")
