import os

entries = os.walk(r"d:\classroom\jun28p\demo")
search = input("Enter search string :")


def containsString(filename, search) -> bool:
    try:
        with open(filename, "rt") as f:
            return search in f.read()
    except:
        pass


for (dirname, folders, files) in entries:
    for file in files:
        filename = dirname + "\\" + file
        if filename.endswith(".py"):
            if containsString(filename, search):
                print(filename)
