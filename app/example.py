#!/home/ubuntupc/develop/NLP-for-querying-data/.venv/bin/env python

import Class_NLP_Query
from Class_NLP_Query import BotAI


botAI = BotAI(db_file="db_esempio.csv")

if botAI.check_model():
    while True:
    
        try:
        
            nuova_frase = input("Chiedi qualcosa:")

            print(bot_reply(nuova_frase))
            
        except KeyboardInterrupt:
            break
