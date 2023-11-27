class impiegato():

    

    def __init__(self, nome, cognome, cittadinanza, reparto, azienda=""):
        self.nome = nome
        self.cognome = cognome
        self.cittadinanza = cittadinanza
        self.reparto = reparto
        self.azienda = azienda
        if reparto == "amministratore":
            self.azienda = "ALFA BETA GAMMA"
        else:
            self.azienda = "CENTRO camuno BICHER"
        

        
    def nome_completo(self):
        return(f'''
                Azienda di riferimento -- {self.azienda}
                Elenco operatori inseriti nell'organico aziendale
                nome: {self.nome}
                cognome: {self.cognome}
                cittadinanza: {self.cittadinanza}''')
        
    
amministratore = impiegato("andrea", "prestini", "italiana", "amministratore")    
contabilità = impiegato("giovanna", "bianchi", "rumena", "contabilità")    
centralino = impiegato("patrizia", "pellegrini", "albanese", "centralino")    
operaio = impiegato("giovanni", "ligasacchi", "inglese", "operaio") 
magazzino = impiegato("pietro", "maso", "italiana", "magazzino")
forno = impiegato("joe", "habed", "marocco", "forno")


print(operaio.nome_completo())#versione con metodo di classe
print(centralino.nome_completo())#versione con metodo di classe
print(forno.nome_completo())
print(amministratore.nome_completo())


#%%
lista = ["uno", "due", "tre", "quattro", "cinque"]
for i in lista:
    print(i)
# %%
