import os
   
os.chdir("./altri_corsi")
os.chdir("./rinomina/")

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    f_serie, f_title = file_name.split("-")
   
    new_name = "{}-{}{}".format(f_title, f_serie, file_ext)
    os.rename(f, new_name )
