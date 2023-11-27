import json
import time
import os
from random import randint


with open("classe.json") as json_file:
    stanza = json.load(json_file)
    vincitore = stanza["persone"][randint(0, len(stanza["persone"])-1)]
    print(f'''
    Vincitore:
    nome -> {vincitore["nome"]}
    cognome -> {vincitore["cognome"]}''')