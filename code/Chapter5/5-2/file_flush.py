import os

file = open(file="data.txt", mode="w", encoding="utf-8", buffering=1)
file.write("This is a test.")
os.system("pause")
file.flush()
os.system("pause")
file.close()