from tkinter import filedialog as fd


path: str = fd.askopenfilename(title="Select a file:",
                               initialdir="/home/andrea/Scaricati/",
                               filetypes=(("PDF", "*.pdf"), ("MP3", "*.mp3")),
                               )

print("Hai scelto il file: " + path.split("/")[-1])
