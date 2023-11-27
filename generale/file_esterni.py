import os
print(os.getcwd())
# os.chdir("/Documenti/analisi")
mioFile = open("elenco", "w")
#se il file non esiste la funzione OPEN lo crea!
mioFile.write("ciamo amico mio che ti chiami Bicher")
mioFile.close()

mioFile1 = open("elenco", "a")
mioFile1.write("come ti chiami?")
mioFile1.close()

mioFile = open("elenco", "r").read()
# print(mioFile)

mioFile = open("elenco", "r").readlines()
print(mioFile)