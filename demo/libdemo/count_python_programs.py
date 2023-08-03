import os

entries = os.walk(r"d:\classroom\jun28p\demo")

count = 0
for (dirname, folders, files) in entries:
    for file in files:
        if file.endswith(".py"):
            count += 1

print(count)
