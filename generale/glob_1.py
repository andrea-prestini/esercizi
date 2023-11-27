import glob
import time

glob_csv = glob.iglob("**/*.ipynb")

for i, file in enumerate(glob_csv, 1):
    if file.startswith(("D", "F")):
        print(i, file, sep=": ")
    else:
        continue
    time.sleep(0.2)