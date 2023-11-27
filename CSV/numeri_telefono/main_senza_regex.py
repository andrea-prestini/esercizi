import csv
import time


def sostituzione_prefisso(fileCSV):
    
    
    """
        fileCSV (): 

    Returns: string + file
        
    """
    sost_1 = "+39+39"
    sost_2 = "+39 "


    ok_number = []

    print("Eseguo le sostituzioni richieste...")
    time.sleep(3)

    with open(fileCSV, "r") as file_csv:
        lettore = csv.reader(file_csv, delimiter="\n")
        for line in lettore:
            new_number = line[0] \
            .replace("+39 ", "+39") \
            .replace("+39+39", "+39") \
            .replace(",", "")
            ok_number.append(new_number)

    time.sleep(1)
    with open("./numeri_corretti.csv", "w") as file:
        for line in ok_number:
            file.write(line)
            file.write("\n")

    time.sleep(3)
    print(f'''
          Ho eseguito le seguenti modifiche sul file csv importato:
          sostituzione 1: {sost_1} in +39
          sostituzione 2: {sost_2}spazio in +39 senza spazio
          Scrivo le informazioni nel file numeri_corretti...
          ''')
    time.sleep(3)
    print("fine procedimento...")
    
    return f'Ho creato il file numeri_corretti...'



sostituzione_prefisso("./elenco.csv")

